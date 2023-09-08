# Описание api_final
Проект представляет собой api для управления публикациями. Публикации могут содержать комментарии. 
Пользователи могут объединяться в группы и подписываться друг на друга.
Авторизация реализована на jwt-токене.

# Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:meteopavel/api_final_yatube.git
cd yatube_api
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
linux: source env/bin/activate
windows: source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
# Примеры
Получение публикаций: 
```
GET /api/v1/posts/
```

Создание публикации:
```
POST /api/v1/posts/
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Получение комментариев:
```
GET /api/v1/posts/{post_id}/comments/
```

Добавление комментария:
```
POST /api/v1/posts/{post_id}/comments/
{
    "text": "string"
}
```

Подписки:
```
GET /api/v1/follow/
```

Подписка:
```
POST /api/v1/follow/
{
    "following": "string"
}
```
# Основные используемые инструменты
*Python 3.9.10
*Django 3.2.16
*djangorestframework 3.12.4
*pytest 6.2.4
*PyJWT 2.1.0
*requests 2.26.0