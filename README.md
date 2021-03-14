# Marketplace
 In this Python project it is possible to have an e-commerce structure, where it is possible to add values in
  the tables and the seller, address, category, marketplace and product, each with its characteristics and particularities.

### Requirements

* ***If Windows is used to run, windows 10 64 bits are required, this project is compatible with linux distributions.***

* python_version = 3.8 - download link for windows: https://www.python.org/downloads/windows/ 

* Docker preferably latest version - download link for windows: https://www.docker.com/products/docker-desktop

* Pipenv

* Integrated Development Environment of your preference - Pycharm was used in the creation of this project.
download link for windows: https://www.jetbrains.com/pt-br/pycharm/download/#section=windows

* git 2.0 - download link for windows https://git-scm.com/

* Postman - Allows you to test the functionality of the API - download link for windows: https://www.postman.com/downloads/

* DBeaver version 7.2 - for data persistence and and PostgreSQL database modeling - 
 download link for windows https://dbeaver.io/download/

### Packages:
* flask 
* flask-migrate
* flask-marshmallow
* flask-sqlalchemy
* pytest
* pytest-cov
* pytest-mock
* marshmallow
* marshmallow-sqlalchemy
* python-dotenv
* psycopg2
* validate-docbr
* email-validator
* requests


## Instalation

1º - 
Clone project on Github

2º - 
run on the IDE terminal: ****"pip install --user pipenv"**** or ****"pip install pipenv"****
 *(if necessary you must activate the pipenv environment)*  
Refer to support documents: https://python-guide-pt-br.readthedocs.io/pt_BR/latest/dev/virtualenvs.html

3º - 
run on the IDE terminal: ****"pipenv install"****

4º - 
run on IDE terminal: ****"docker-compose up -d"****

5º - 
create connection with PostgreSQL - Using DBeaver

```
Host = localhost

Database = python-flask 

password = senha

Username = create connection with PostgreSQL
```
 ![](app/utils/images/dbeaver.PNG?raw=true)

6º - 
run on IDE terminal: ****"export FLASK_ENV=development"**** 

7º - 
run on IDE terminal: ****"FLASK_ENV=development flask db migrate"****           

8º - 
run on IDE terminal: ****"FLASK_ENV=development flask db upgrade"****     

9º -  run on the IDE terminal: ****"pipenv run flask run"****

## Run API

Documentation Postman:
https://documenter.getpostman.com/view/10706208/Tz5qaHJx

**Method:**
`GET` | `POST` | `DELETE` | `PATCH`

**URL:** 

``` 
http://127.0.0.1:5000/category

http://127.0.0.1:5000/seller

http://127.0.0.1:5000/marketplace

http://127.0.0.1:5000/product

http://127.0.0.1:5000/address
``` 

***Database Modeling***

 ![](app/utils/images/databaseModeling.PNG?raw=true)