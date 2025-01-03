# Volman

A Django-based, fake volunteer management system

## To Use

Perform the necessary migrations, install TailwindCSS for Django, and
populate the Volunteer, Session, and User databases:

```
python manage.py migrate
python manage.py tailwind install
python manage.py populate
```

In one terminal, start the TailwindCSS server:

```
python manage.py tailwind start
```

In a different terminal, start the Django web server:

```
python manage.py runserver
```