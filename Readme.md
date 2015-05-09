Blog
====

A small personal blog created on Python Django. Hosted on http://lohitaksh.me

It can be used as a a blog by anyone. For that, only the front page needs to be changed.

Access the admin panel by visiting http://blogURL/blog/admin/
Username and Password is the django super user

INSTALLATION
===
Assuming you arleady have Django 1.7 and git-core installed

-sudo apt-get install python-pip
-sudo pip install --upgrade -r ./requirements.txt
-python manage.py makemigrations
-python manage.py syncdb
-Make a user when promtped during the previous command. These are you login credential for the admin panel
-python manage.py runserver





