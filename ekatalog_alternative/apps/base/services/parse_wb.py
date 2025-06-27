from ekatalog_alternative.apps.base.coreutils.parser import WildberriesScraper
from ekatalog_alternative.apps.base.models.general import General
from decimal import Decimal


class ParseWb:
    def __init__(self, products_quantity, category):
        self.url = "https://www.wildberries.ru"
        self.laptops_url = "catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki"
        self.phones_url = "catalog/elektronika/smartfony-i-telefony/vse-smartfony"
        self.scraper = WildberriesScraper()
        self.products_quantity = products_quantity
        self.category = category

    def start_service(self):
        """Запуск скрапера"""
        category_url = ""
        category_type = ""

        match self.category:
            case "laptops":
                category_type = "laptops"
                category_url = self.laptops_url
            case "phones":
                category_type = "phones"
                category_url = self.phones_url
            case _:
                raise ValueError("Неправильная категория в сервисе!")

        try:
            success = self.scraper.run(
                category_url=f"{self.url}/{category_url}",
                max_products=self.products_quantity
            )

            if success:
                for item in success:
                    General.objects.create(
                        wb_id=int(item.get("wb_id", 0)),
                        title=item.get("title", ""),
                        category=category_type,
                        price_discount=Decimal(item.get("price_discount") or 0),
                        price_original=Decimal(item.get("price_original") or 0),
                        rating=Decimal(item.get("rating") or 0),
                        review=int(item.get("reviews") or 0),
                        link=item.get("link", ""),
                        photo=item.get("photo", "")
                    )

                print("\n🎉 Скрапинг завершен успешно!")
            else:
                print("\n❌ Скрапинг завершился с ошибками")
        except Exception as e:
            print(f"\n💥 Критическая ошибка: {e}")
            self.scraper.cleanup()
