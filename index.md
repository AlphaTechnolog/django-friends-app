In the `django-friends-app` you must register your friends in a sqlite3 database and:

- **C**reate
- **R**ead
- **U**pdate
- **D**elete

Your friends!

# Requirements

To run `django-friends-app`, require:

- Python 3
- Django
- Git

# Installing and running

To download it execute in your shell:

```sh
cd ~
mkdir repo
cd repo
git clone https://github.com/AlphaTechnolog/django-friends-app.git friends-app
cd friends-app
python3 manage.py migrate
python3 manage.py makemigrations main
python3 manage.py migrate
python3 manage.py createsuperuser # Creation of super user
# -- Output --
# Username: testuser
# Email address: 324823@4w84.3284
# Password: ***
# Password (again): ***
python3 manage.py runserver
```

Now go to http://localhost:8000
