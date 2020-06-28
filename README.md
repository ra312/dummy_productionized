### Installation

conda create -n <env_name> -f django-production.yml

### Run locally
python manage.py runserver 8000

### Test the service locally
curl -X GET http://127.0.0.1:8000/classify/?sound=meow
