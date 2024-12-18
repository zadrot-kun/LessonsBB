FROM python:3.10.13-slim-bullseye

RUN apt update \
 && apt upgrade -y \
 && apt -y install gcc libpcre3 libpcre3-dev

COPY ./lessonsbb_proj /lessonsbb_proj/
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /lessonsbb_proj

EXPOSE 5005
# CMD exec /bin/sh -c "trap : TERM INT; (while true; do sleep 1000; done) & wait"
CMD ["uwsgi", "--ini", "lessonsbb_proj/wsgi.ini"]