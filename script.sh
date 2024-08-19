#!/bin/sh

echo "Aplicando migrações do banco de dados..."
python manage.py makemigrations
python manage.py migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando o Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 demoday.wsgi:application
