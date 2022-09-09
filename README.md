# Expenses List Service
This project was created to save time and money with features that make your shopping that much better.

Its purpose is to make possible to TODO.

Base URL: [https://expenses-list.com/](https://expenses-list.com/)

### Tools

This project is developed using the following technologies:
- **Python**.
- **Django REST framework**.
- **PostgreSQL** as database.
- **PyTest**, **APITestCase** and **Faker** for tests.
- **Swagger**, **Redoc** for API Documentation.

## Package Structure

```
Project
├── api_auth
│   ├── __init__.py
│   ├── receivers.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── base
│   ├── __init__.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── receivers.py
│   ├── settings.py
│   └── urls.py
├── expenses
│   ├── migrations
│   ├── __init__.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── products
│   ├── fixtures
│   ├── migrations
│   ├── views
│   │   ├── products.py
│   │   ├── products_category.py
│   │   └── products_type.py
│   ├── __init__.py
│   ├── models.py
│   ├── receivers.py
│   ├── serializers.py
│   ├── urls.py
├── shopping
│   ├── migrations
│   ├── views
│   │   ├── purchases.py
│   │   └── shopping.py
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
├── .env
├── .flake8
├── .gitignore
├── docker-compose.staging.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

# Requirements / Dependencies
- [Python = 3.10](https://www.python.org/downloads/release/python-3100/) a high-level, interpreted, general-purpose programming language.
- [Django Rest Framework = 3.13.1](https://www.django-rest-framework.org/) a powerful and flexible toolkit for building Web APIs.
- [PostgreSQL >= 10.22](https://www.postgresql.org/) a powerful, open source object-relational database system.
- [Swagger](https://swagger.io/) for really useful and simple API documentation.

# Running the application locally

  ### With PIP  

- Run the command below to compile the project  

```
$ pip clean install
```

TODO

## Tests

The project is 90% covered with tests.

To run the tests please use

```$ TODO test ``` or ```$ TODO test```

## Swagger 
- Swagger is already configured in this project in SwaggerConfig.py. TODO
- The API can be seen at https://.../swagger-ui.
- You can also try the entire REST API directly from the Swagger interface!

## Postman Documentation

Alternatively to swagger, I have prepared a postman documentation, in which you will be able to check in details each endpoint and possible Requests and responses.

Please access it by link below:

```
https://documenter.getpostman.com/TODO
```

### Contributors

- Frank Ricardo Ramirez <frankjony17@gmail.com>

---


## Support

* If you have any query or doubt, please, feel free to contact me by e-mail.
