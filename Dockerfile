FROM django
ADD . /v-templates

WORKDIR /v-templates

RUN apt-get update && apt-get install -y git
RUN pip install -r ./v-templates/requirements/base.txt
