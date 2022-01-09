1. git clone https://github.com/arkid15r/django-project-boilerplate.git
2. virtualenv venv; source venv/bin/activate
3. pip install -r requirements/dev.txt -r requirements/prod.txt
4. python manage.py migrate
5. Run `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` and place the output into .config SECRET_KEY variable
6. python runserver
