# Ekatalog Alternative

- Клонируем и создаем venv в директории проекта ```python3 -m venv venv```
- Устанавливаем все зависимости в venv ```pip3 install -r requirements.txt```
- Генерируем секретный ключ и ставим в файл .env.local (создать вручную или переименовать файл .env в .env.local. КОПИРУЕМ КЛЮЧ из терминала) ```python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'```
- Делаем миграцию ```python3 manage.py makemigrations``` и ```python3 manage.py migrate```
- Создаем админа ```python3 manage.py createsuperuser``` с почтой ```admin@admin.com``` и паролем ```foo```. ОБЯЗАТЕЛЬНО ТАКИЕ ДАННЫЕ
- Запускаем проект ```python3 manage.py runserver``` и переходим в ```http://localhost:8000``` 
- Авторизуемся под админа которого ранее создали и получаем доступ к админке
- Фронт находится в файле ```index.html```
- Для получения доступа к эндпоинтам нужен JWT токен, можно получить в ```/api/token/```
- Парсинг WB происходить через кнопку ```Спарсить WB```. Она находится в админке
- В целях сокращения времени парсер происходит только в 2 категориях, ```ноутбуки``` и ```телефоны```. В постмане и курлах в категории нужно указать ```phones```, либо ```laptops```
- Пример ```GET http://localhost:8000/api/products/?category=laptops```

# Скриншоты
![alt text](screenshots/Screenshot%202025-06-28%20at%203.59.34%E2%80%AFAM.png)
![alt text](screenshots/Screenshot%202025-06-28%20at%203.59.48%E2%80%AFAM.png)
![alt text](screenshots/Screenshot%202025-06-28%20at%204.00.02%E2%80%AFAM.png)
![alt text](screenshots/Screenshot%202025-06-28%20at%204.00.41%E2%80%AFAM.png)
![alt text](screenshots/Screenshot%202025-06-28%20at%204.00.50%E2%80%AFAM.png)
![alt text](screenshots/Screenshot%202025-06-28%20at%204.03.31%E2%80%AFAM.png)
![alt text](screenshots/Screenshot%202025-06-28%20at%204.05.06%E2%80%AFAM.png)