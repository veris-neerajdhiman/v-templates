FROM django

WORKDIR /v-templates


ADD ./requirements/base.txt /v-templates/requirements/base.txt
ADD ./requirements/test.txt /v-templates/requirements/test.txt
ADD ./requirements/production.txt /v-templates/requirements/production.txt


RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/production.txt

ADD . /v-templates

EXPOSE 80

COPY ./config/docker/docker-entrypoint.sh /
ENTRYPOINT ["./config/docker/docker-entrypoint.sh"]