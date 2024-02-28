FROM python:3.8-slim as base

RUN apt-get update && apt-get install --no-install-recommends -y gcc libssl-dev apt-utils python3-dev default-libmysqlclient-dev python3-setuptools git libmemcached-dev libz-dev libmagic1

RUN useradd -ms /bin/bash qustodio

COPY ./src /home/qustodio/clean_architecture
COPY ./requirements.txt /home/qustodio/clean_architecture
COPY ./requirements-dev.txt /home/qustodio/clean_architecture

WORKDIR /home/qustodio/clean_architecture

EXPOSE 80

RUN pip3 install -r ./requirements.txt
RUN rm ./requirements.txt

FROM base AS deploy

CMD ["gunicorn", "-w", "4", "--threads", "4", "--timeout", "120", "-b", ":80", "project.wsgi:application"]

FROM base AS test

RUN pip3 install -r ./requirements-dev.txt
RUN rm ./requirements-dev.txt

CMD ["gunicorn", "-w", "4", "--threads", "4", "--timeout", "120", "-b", ":80", "project.wsgi:application"]