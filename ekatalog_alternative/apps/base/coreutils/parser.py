from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
import random
import re
from datetime import datetime
import logging
from pathlib import Path


# noinspection PyBroadException
class WildberriesScraper:
    def __init__(self, headless=True, log_level=logging.INFO):
        """
        Инициализация скрапера с улучшенными настройками

        Args:
            headless (bool): Запуск в фоновом режиме
            log_level: Уровень логирования
        """
        self.logger = None
        self.setup_logging(log_level)
        self.driver = None
        self.headless = headless
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
        ]

    def setup_logging(self, level):
        """Настройка логирования"""
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('wildberries_scraper.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def create_driver(self):
        """Создание драйвера с максимальной маскировкой"""
        options = webdriver.ChromeOptions()

        # Базовые настройки маскировки
        if self.headless:
            options.add_argument('--headless')

        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-extensions')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-web-security')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-features=VizDisplayCompositor')

        # Случайный User-Agent
        user_agent = random.choice(self.user_agents)
        options.add_argument(f'--user-agent={user_agent}')

        # Отключение автоматизации
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # Настройки приватности
        prefs = {
            "profile.default_content_setting_values": {
                "notifications": 2,
                "media_stream": 2,
            }
        }
        options.add_experimental_option("prefs", prefs)

        try:
            self.driver = webdriver.Chrome(options=options)

            # Дополнительная маскировка через JavaScript
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})

            # Установка размера окна
            self.driver.set_window_size(1920, 1080)

            self.logger.info("Драйвер успешно создан")
            return True

        except Exception as e:
            self.logger.error(f"Ошибка создания драйвера: {e}")
            return False

    def navigate_to_page(self, url, max_retries=3):
        """Переход на страницу с проверками и повторными попытками"""
        for attempt in range(max_retries):
            try:
                self.logger.info(f"Переход на страницу: {url} (попытка {attempt + 1})")
                self.driver.get(url)

                # Случайная задержка
                sleep(random.uniform(3, 7))

                # Проверка успешной загрузки
                if self.is_page_loaded():
                    self.logger.info("Страница успешно загружена")
                    return True
                else:
                    self.logger.warning(f"Страница не загрузилась полностью, попытка {attempt + 1}")

            except Exception as e:
                self.logger.error(f"Ошибка при переходе на страницу: {e}")

            if attempt < max_retries - 1:
                sleep(random.uniform(5, 10))

        return False

    def is_page_loaded(self):
        """Проверка корректной загрузки страницы"""
        try:
            page_source = self.driver.page_source

            # Проверка на блокировки
            block_indicators = [
                "Access denied", "Доступ ограничен", "403 Forbidden",
                "Captcha", "Robot Check", "Проверка безопасности"
            ]

            for indicator in block_indicators:
                if indicator in page_source:
                    self.logger.error(f"Обнаружена блокировка: {indicator}")
                    return False

            # Проверка минимальной длины
            if len(page_source) < 1000:
                self.logger.error("Слишком короткая страница")
                return False

            return True

        except Exception as e:
            self.logger.error(f"Ошибка проверки загрузки страницы: {e}")
            return False

    @staticmethod
    def cleaner(cleaning_str, option: int):
        """Фильтр полей"""
        if not cleaning_str:
            return ""

        match option:
            case 1:
                """Очистка цены от символа рубля и пробелов"""
                # Удаляем символ рубля, пробелы и оставляем только цифры с возможными разделителями
                cleaned = re.sub(r'[₽\s]', '', cleaning_str)
                # Заменяем пробелы в числах на пустую строку (для больших чисел типа "27 880")
                cleaned = re.sub(r'(\d)\s+(\d)', r'\1\2', cleaned)
                return cleaned.strip()
            case 2:
                """Очистка рейтинга и преобразование в decimal формат"""
                # Ищем число с возможной запятой или точкой
                match = re.search(r'(\d+)[,.](\d+)', cleaning_str)
                if match:
                    # Преобразуем в decimal формат с точкой
                    return f"{match.group(1)}.{match.group(2)}"

                # Ищем целое число
                match = re.search(r'(\d+)', cleaning_str)
                if match:
                    return f"{match.group(1)}.0"

                return ""
            case 3:
                """Очистка количества отзывов от слов 'оценки', 'оценок' и т.д."""
                # Удаляем все кроме цифр
                cleaned = re.sub(r'\D', '', cleaning_str)
                return cleaned
            case _:
                raise ValueError("Неправильная опция для фильтра элементов")

    @staticmethod
    def extractor(element, selector, option: int, attribute=None):
        """Безопасное извлечение текста и значения аттрибута"""
        if not element or not selector:
            return None

        match option:
            case 1:
                """Безопасное извлечение текста"""
                try:
                    elem = element.find_element(By.CSS_SELECTOR, selector)
                    text = elem.text.strip()
                    # Очистка от префиксов
                    if text.startswith("/ "):
                        text = text[2:]
                    return text
                except:
                    return ""
            case 2:
                """Безопасное извлечение атрибута"""
                try:
                    elem = element.find_element(By.CSS_SELECTOR, selector)
                    return elem.get_attribute(attribute) or ""
                except:
                    return ""
            case _:
                raise ValueError("Неправильная опция для извлекатора")

    def extract(self, product_element):
        """Извлечение данных о товаре с улучшенной обработкой ошибок"""
        data = {}

        # Маппинг селекторов
        selectors = {
            'wb_id': lambda: product_element.get_attribute("data-nm-id") or "",
            'title': lambda: self.extractor(product_element, ".product-card__name", 1),
            'price_discount': lambda: self.cleaner(self.extractor(product_element, ".price__lower-price", 1), 1),
            'price_original': lambda: self.cleaner(self.extractor(product_element, ".price__wrap del", 1), 1),
            'rating': lambda: self.cleaner(self.extractor(product_element, ".address-rate-mini", 1), 2),
            'reviews': lambda: self.cleaner(self.extractor(product_element, ".product-card__count", 1), 3),
            'link': lambda: self.extractor(product_element, ".product-card__link", 2, "href"),
            'photo': lambda: self.extractor(product_element, ".j-thumbnail", 2, "src")
        }

        # Извлечение данных с обработкой ошибок
        for key, extractor in selectors.items():
            try:
                data[key] = extractor()
            except Exception as e:
                self.logger.debug(f"Ошибка извлечения {key}: {e}")
                data[key] = ""

        return data

    def scrape(self, max_products):
        """Основной метод парсинга товаров"""
        products_data = []

        try:
            products = self.driver.find_elements(By.CSS_SELECTOR, "article.product-card")
            total_products = min(len(products), max_products)

            self.logger.info(f"Начинаем парсинг {total_products} товаров")

            for i, product in enumerate(products[:max_products]):
                try:
                    data = self.extract(product)
                    products_data.append(data)

                    # Прогресс
                    if (i + 1) % 10 == 0:
                        self.logger.info(f"Обработано товаров: {i + 1}")
                    else:
                        self.logger.debug(f"[{i + 1}] {data['title'][:40]}...")

                    # Небольшая задержка
                    sleep(random.uniform(0.1, 0.5))

                except Exception as e:
                    self.logger.error(f"Ошибка при парсинге товара {i + 1}: {e}")
                    continue

            return products_data
        except Exception as e:
            self.logger.error(f"Критическая ошибка при парсинге: {e}")
            return [], None

    def run(self, category_url, max_products=50):
        """Главный метод запуска скрапера"""
        try:
            # Создание драйвера
            if not self.create_driver():
                return False

            # Переход на страницу
            if not self.navigate_to_page(category_url):
                return False

            # Парсинг товаров
            products_data = self.scrape(max_products)

            self.logger.info(f"Парсинг завершен успешно!")
            self.logger.info(f"Обработано товаров: {len(products_data)}")

            return products_data

        except Exception as e:
            self.logger.error(f"Критическая ошибка: {e}")
            return False

        finally:
            self.cleanup()

    def cleanup(self):
        """Очистка ресурсов"""
        if self.driver:
            try:
                self.driver.quit()
                self.logger.info("Драйвер закрыт")
            except Exception as e:
                self.logger.error(f"Ошибка при закрытии драйвера: {e}")


def main():
    """Пример использования"""
    # Настройки
    laptops_url = "catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki"
    phones_url = "catalog/elektronika/smartfony-i-telefony/vse-smartfony"
    category_url = f"https://www.wildberries.ru/{laptops_url}"
    max_products = 2
    target_load = 2

    # Создание и запуск скрапера
    scraper = WildberriesScraper()

    try:
        success = scraper.run(
            category_url=category_url,
            max_products=max_products
        )

        if success:
            print(f'\n{success}\n')
            print("\n🎉 Скрапинг завершен успешно!")
        else:
            print("\n❌ Скрапинг завершился с ошибками")

    except KeyboardInterrupt:
        print("\n⚠️ Скрапинг прерван пользователем")
        scraper.cleanup()
    except Exception as e:
        print(f"\n💥 Критическая ошибка: {e}")
        scraper.cleanup()


if __name__ == "__main__":
    main()
