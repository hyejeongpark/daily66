# Daily66

## Requirements

- Python 3.4.2
- django 1.9.5

## Dev config

- editorconfig

## Local setting

``` shell
$ git clone git@github.com:hyejeongpark/daily66.git
$ cd daily66
$ pyvenv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
(env) $ python manage.py runserver
```
