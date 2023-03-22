echo "Apply database migrations"
python ./Project/manage.py migrate

echo "Create superuser"
python ./Project/manage.py createadminuser

# Start server
echo "Starting server"
python ./myFirstProject/manage.py runserver 0.0.0.0:8000
#gunicorn --reload config.wsgi -c gunicorn.py -b 0.0.0.0:8888
