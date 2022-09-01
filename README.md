# Django blog
The goal in making this application was to use Django and PostgreSQL to make a backend for a mock blog app. A user can create, edit, and delete blogs under different categories from the minimal frontend or by making API calls to the backend.

## Installation
```
$ git clone https://github.com/MAEchevarria/django-blog.git
$ cd django-blog
```
Install dependencies and start server
```
$ pip install -r requirements.txt
$ python manage.py runserver
```
Open http://localhost:8000

## Additional notes
This application is using a PostgreSQL database: `django_blog`, that can be changed in `blog_proj/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database_name_here>',
    }
}
```

## Environment Variables
And for good practice, uses `python-dotenv` for handling Django's secret key. If you run into any errors, create a `.env` file and insert your django key. `django-blog/.env`

```
DJANGO_SECRET=<secret_key_here>
```

## Technologies used:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
