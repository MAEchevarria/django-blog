# Django blog
The goal in making this application was to make a backend for mock blog app using Django. A user can create, edit, and delete blogs under different categories.

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
This application is using a postgresql database: `django_blog`.
The database can be changed in `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database_name_here>',
    }
}
```
And for good practice, uses `python-dotenv` for handling Django's secret key. If you run into any errors, within the Django-blog directory, create a `.env` file and insert your django key:
```
DJANGO_SECRET=<secret_key_here>
```

## Technologies used:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
