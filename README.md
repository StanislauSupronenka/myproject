Marketplace
A small functional market place for to buy currency.

Database
I'm using a simple PostgreSQL setup. 


Run
1.Create and activate a virtualenv (Python 3)
2.virtualenv -p python3 venv
3.source venv/bin/activate
4.Install requirements
5.pip install -r requirements.txt
6.Create a PostgreSQL database
7.CREATE DATABASE myproject CHARACTER SET utf8;
8.Init database
9../manage.py migrate
10../manage.py runserver
To override default settings, create a local_settings.py file in the myproject folder.


