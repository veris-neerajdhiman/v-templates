

#local: ./config/local/Makefile.local
#	./config/local/Makefile.local $(ARGS)

#.PHONY: run
#run : /config/local/Makefile.local
#	@echo /config/local/Makefile.local $(RUN_ARGS)

# Makefile commands for Local env

.PHONY: venv
venv:
	virtualenv -p /usr/bin/python3 env

.PHONY: install
install:
	pip install -r requirements/local.txt

.PHONY: runserver
runserver:
	python manage.py runserver 0.0.0.0:${port} --settings=config.local.settings

.PHONY: migrations
migrations:
	python manage.py makemigrations  --settings=config.local.settings

.PHONY: migrate
migrate:
	python manage.py migrate  --settings=config.local.settings

.PHONY: dbshell
dbshell:
	python manage.py dbshell  --settings=config.local.settings

.PHONY: shell
shell:
	python manage.py shell_plus  --settings=config.local.settings

.PHONY: superuser
superuser:
	python manage.py createsuperuser  --settings=config.local.settings
