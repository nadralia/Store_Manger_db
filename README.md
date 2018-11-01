[![Build Status](https://travis-ci.org/nadralia/Store_Manger_db.svg?branch=develop)](https://travis-ci.org/nadralia/Store_Manger_db)
[![Coverage Status](https://coveralls.io/repos/github/nadralia/Store_Manger_db/badge.svg?branch=develop)](https://coveralls.io/github/nadralia/Store_Manger_db?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/2b070754c151d29cfc6a/maintainability)](https://codeclimate.com/github/nadralia/Store_Manger_db/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/2b070754c151d29cfc6a/test_coverage)](https://codeclimate.com/github/nadralia/Store_Manger_db/test_coverage)

# Store_Manger_db
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

## Getting Started
- To start get started;
## Features 
- Admin can add a product
- Admin or store attendant can get all products
- Admin or store attendant can get a specific product.
- Store attendant can add a sale order.
- Admin can get all sale order details.


## Project Links

``` Use this link to access the api endpoints https://github.com/nadralia/Store_Manger_db ```

## API Endpoints

| End Point	                        | Description
|-------------------------------:   |-----------------------------------: | 
| POST /api/v1/auth/signup	        | User creates an account |
| POST /api/v1/auth/login	        | User with an account can sign in with the correct credentials |
| POST /api/v1/products             | Add a product |
| GET /api/v1/products              | Get history of all products |
| GET /api/v1/sales                 | Admin gets all sales |
| GET /api/v1/sales/int:sale_id 	| Admin fetchs a single sale |
| PUT /api/v1/sales/int:sales_id	| Admin Updates the status of an sales |


**Technologies used to build the application**

* [Python 3.7](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)


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


### Link to Store Manager on Heroku

# Running the tests

- To run the test run ```nosetests --with-cov --cov  tests/``` in a command line interface

# Built with:

- Python 3
- Flask
- PostgreSQL

# Authors

- Adralia Nelson
