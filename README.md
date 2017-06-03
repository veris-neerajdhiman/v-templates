# v-templates
Template service


## SET UP INSTRUCTIONS
 
### Local env

- clone this repo

- make venv  # set up virtual env
- activate virtual env
- make install # install requirements

- Database : 
	- CREATE USER v_admin WITH PASSWORD 'admin@123';
	-  CREATE DATABASE template_service;
	- GRANT ALL PRIVILEGES ON DATABASE template_service to v_admin;

- make makemigrations # migrations
- make migrate # migrate models to postgres
- make dbshell # for db shell
- make shell # shell_plus
- make runserver port={port_no_here} # ryun dev server
- make superuser # create superuser