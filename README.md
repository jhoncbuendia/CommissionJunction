# Commission Junction Platform
### Version: 1.0

### Tech
* AngularJS
* Twitter Bootstrap
* Django 
* Postgresql

# Installation

### Operative System: Ubuntu Server

### Deployment steps:

* Install Pip
```sh
        $ sudo apt-get install python-pip python-dev build-essential
```
*  Install virtual Env
```sh
        $ sudo pip install virtualenv
```
* Install psycopg2

```sh
        $ sudo pip install psycopg2
```
*  Install Postgresql
```sh
        $ sudo apt-get update
        $ sudo apt-get install postgresql postgresql-contrib
```
*  Install gunicorn
```sh
        $ sudo pip install gunicorn
```
*  Run Postgres scripts found in store procedures file
*  Copy commission proyect to virtual env path
*  Configure postgres conection in settins.py file 
*  Copy static folder to static content server 
*  Configure STATIC_URL value found in settings.py
*  Run proyect with gunicorn 
```sh
        $ cd virualenv_path/
        $ source activate
        $ cd comission
        $ gunicorn wsgi -b 0.0.0.0:port
```

