

# ---------------------------------------------------------------------------------------------------

# Makefile commands for dev env


# -----------------------------------------------------------------------------------------------------

.PHONY: runserver
runserver:
	 gunicorn config.dev.wsgi:application \
    --name v-templates \
    --bind 0.0.0.0:${port} \
    --workers 3

# Docker commands

.PHONY: build
build:
	docker build -t ${img} -f config/production/docker/Dockerfile .

.PHONY: run
run:
	docker run -it --publish=${port}:8000 $(id)

