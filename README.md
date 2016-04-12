# Daily66

## Requirements

- Python 3.4.2
- django 1.9.5

## Dev config

- editorconfig

## Local setting

```
$ git clone git@github.com:hyejeongpark/daily66.git
$ cd daily66
$ pyvenv env
$ . env/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
