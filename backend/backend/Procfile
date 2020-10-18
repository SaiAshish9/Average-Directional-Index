release: python manage.py makemigrations --no-intput
release: python manage.py migrate --no-input

web: gunicorn backend.wsgi