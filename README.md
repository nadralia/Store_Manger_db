[![Build Status](https://travis-ci.org/nadralia/Store_Manger_db.svg?branch=develop)](https://travis-ci.org/nadralia/Store_Manger_db)
[![Coverage Status](https://coveralls.io/repos/github/nadralia/Store_Manger_db/badge.svg?branch=develop)](https://coveralls.io/github/nadralia/Store_Manger_db?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/2b070754c151d29cfc6a/maintainability)](https://codeclimate.com/github/nadralia/Store_Manger_db/maintainability)


# Store_Manger_db
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

## Getting Started
- To start get started;

## Features
- Login
- Create an attendant's account
- Fetch all products
- Fetch a single product record
- Fetch all sale records
- Fetch a single sale record
- Create a product
- Create a sale order
- Update a prooduct item
- Delete a product item

#### Endpoints to create an attendants account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/auth/signup | False | Create an attendant's account
POST | /api/v1/auth/login | True | Login a user

#### Endpoints to create, views available products and create sale records
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/products | False | Create a product
POST | /api/v1/sales | False | Create a sale order
GET | /api/v1/products | False | Fetch all available products
GET | /api/v1/products/<product_id> | False | Fetch details of a single product
DELETE | /api/v1/products/<product_id> | False | Delete a single product
PUT | /api/v1/products/<product_id> | False | Edit details of a single product
GET | /api/v1/sales/<sale_id> | False | Fetch details of a single sale record
GET | /api/v1/sales | False | Fetch all sale records created


## Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone https://github.com/nadralia/Store_Manger_db
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate
```
Install the dependencies in the requirements.txt file using pip
```sh
$ pip install -r requirements.txt
```

Start the application by running
```sh
$ python run.py
```
Test your setup using [postman](www.getpostman.com) REST-client


# Running the tests

- To run the test run ```nosetests --with-cov --cov  tests/``` in a command line interface

# Built with:

- Python 3
- Flask
- PostgreSQL

# Authors

- Adralia Nelson

### Link to Store Manager on Heroku
