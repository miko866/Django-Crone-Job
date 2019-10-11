# Django Cron-Job - Michal Durik

This web-application and database are for Modul 307

---

## Requirements

- dj-database-url==0.5.0
- Django==2.2.6
- django-heroku==0.3.1
- gunicorn==19.9.0
- passlib==1.7.1
- psycopg2==2.7.5
- pytz==2019.3
- sqlparse==0.3.0
- whitenoise==4.1.4

### Structure

Below, you see the application structure for Awesome Blog.

```
├── Procfile
├── README.md
├── crone_job
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── test
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── test_forms.py
│   │   ├── test_models.py
│   │   ├── test_urls.py
│   │   └── test_views.py
│   └── views.py
├── db.sqlite3
├── django_crone_job
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── static
│   └── crone_job
│       ├── css
│       ├── img
│       └── js
├── staticfiles
├── templates
│   └── crone_job
│       ├── 404.html
│       ├── base.html
│       ├── crone.html
│       ├── entries.html
│       ├── home.html
│       ├── login_user.html
│       └── register_user.html
```
---

## Installation - Terminal
### In app root folder.

Start python virtual environment:

```
source venv/bin/activate
```

Start Django server:

- cd django_crone_job

```
python manage.py runserver
```

And copy address from:

```
Starting development server at ...
```

In to your browser.

## Test URL
```
python manage.py test crone_job
```


## Copyright

&copy; miko866 <br />
[mdurik2@gmail.com](mailto:mdurik2@gmail.com)<br />

