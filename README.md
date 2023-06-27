# git bash

1. mkdir /c/dcrm
2. cd dcrm/
3. python -m venv virt
4. source virt/Scripts/activate
5. pip install django
6. pip install mysql
7. pip install mysql-connector
8. pip install mysql-connector-python
9. django-admin startproject dcrm
10. cd dcrm
11. python manage.py startapp website
12. Open with visual studio code final dcrm project

=================================================

1. python manage.py migrate(Need to run after create model)
2. winpty python manage.py createsuperuser
3. python manage.py runserver
4. python manage.py makemigrations(Need to run after create model)

=================================================
# Reference resource
https://getbootstrap.com/docs/5.3/forms/overview/
https://github.com/flatplanet/Django-CRM/blob/main/website/forms.py