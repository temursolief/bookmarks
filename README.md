# django-social-media

Create your ``` .env ``` file in your root directory and add the following data:
```
    DJANGO_SECRET_KEY = 
    PASSWORD = ADD YOUR POSTGRESQL PASSWORD
```
In fact, the example is already given as ```.env_example```.

Run your server with a fake SSL:
```
    python manage.py runserver_plus --cert-file cert.crt
```
so that you will be able to use social authentications for signing in with Google, Twitter and Facebook as these
platforms support only SSL containing url requests.