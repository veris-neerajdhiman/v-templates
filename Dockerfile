FROM django

WORKDIR /v-templates


ADD ./requirements/base.txt /v-templates/requirements/base.txt


RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/base.txt

ADD . /v-templates
