
### run aws ubuntu 18.04
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04

```
python3 -m venv my_env
source my_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### run migrate
##### packaging up your model changes
del all __pycache__ and mydatabase
```
python manage.py makemigrations model
python manage.py migrate
```

##### create supersuer
```
python manage.py createsuperuser
```

### run local
```
python manage.py runserver 0.0.0.0:8083
```



