# Django-app

Para iniciar el entorno virtual

```sh
.\env\Scripts\activate
```

Iniciar aplicación en django

```sh
cd prometeocoleccionablesapp
py manage.py startapp {app_name}
```

Para agregar la aplicación, hay que modificar el archivo settings.py

```python
INSTALLED_APPS = [
    'products.apps.ProductsConfig', # Se agregó acá la app 'Products'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

o, mejor práctica:

```python
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_APPS = (
    'jazzmin',
)

LOCAL_APPS = (
    'products',
)


INSTALLED_APPS = THIRD_APPS + DJANGO_APPS  + LOCAL_APPS
```

Correr migraciones de una aplicación en django

```sh
cd prometeocoleccionablesapp
py manage.py makemigrations {app_name}
```

Correr migraciones del proyecto

```sh
cd prometeocoleccionablesapp
py manage.py migrate
```

Correr proyecto en django

```sh
cd prometeocoleccionablesapp
py manage.py runserver
```

Consola interactiva

```sh
cd prometeocoleccionablesapp
py manage.py shell
```

Correr test

```sh
cd prometeocoleccionablesapp
py manage.py test {app_name}
```
