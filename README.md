## About

- v-templates is `Templates` micro-service.
- It uses `json` to store a template structure and render that json to an app
on runtime. App can use json to display app UI.

## Prerequisites

#### Environment Variables : 

 - DATABASE_NAME_TEMPLATE
 - DATABASE_USER
 - DATABASE_PASSWORD
 - DATABASE_HOST
 - DATABASE_PORT
 - SECRET_KEY
 
## Installation :

1 ) Clone this repo

2 ) Setup virtual environment
```
cd <path-to-repo>/v-templates/

virtualenv -p /usr/bin/python3 env

```

3 ) Activate Virtual environment
```
source env/bin/activate
```
4 ) Install requirements

- Base Requirements

```
pip install -r requirements/base.txt

```
- Testing Requirements
```
pip install -r requirements/test.txt

```
- Local requirements
```
pip install -r requirements/local.txt

```
- Production requirements

```
pip install -r requirements/production.txt

```
5 ) Prerequisites
- Makes sure above `Prerequisites` we mentioned above must be defined and fulfilled.

6 ) Run Server 
```
python manage.py runserver
```

## API Reference : 

- API documentation is hosted on [Swagger hub](https://swaggerhub.com/apis/verisadmin/template-service_api/0.1) 
and is public.

 
## Tests : 

- Run tests using 
```
make test
```
 
 