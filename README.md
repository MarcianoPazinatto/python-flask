# Marketplace
 In this Python project it is possible to have an e-commerce structure, where it is possible to add values in
  the tables and the seller, address, category, marketplace and product, each with its characteristics and particularities.

### Requirements

* python_version = 3.8

* Docker preferably latest version

* Pipenv

* Integrated Development Environment of your preference - Pycharm was used in the creation of this project.

* git 2.0

* Postman - Allows you to test the functionality of the API

* DBeaver version 7.2 - for data persistence and and PostgreSQL database modeling

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
run on the IDE terminal: ****pip install --user pipenv****

3º - 
run on the IDE terminal: ****pipenv install****

4º - 
run on IDE terminal: ****docker-compose up -d****

5º - 
create connection with PostgreSQL

```
Host = localhost

Database = python-flask 

password = senha

Username = create connection with PostgreSQL
```
 ![](app/utils/images/dbeaver.PNG?raw=true)

6º - 
run on IDE terminal: ****export FLASK_ENV=development**** 

7º - 
run on IDE terminal: ****FLASK_ENV=development flask db migrate****           

8º - 
run on IDE terminal: ****FLASK_ENV=development flask db upgrade****     

9º -  run on the IDE terminal: ****pipenv run flask run****

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