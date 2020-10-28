# imagen base
FROM python:3.8.5-alpine

# nuevo
# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd


# estableciendo directorio de trabajo
WORKDIR /usr/src/app

# agregando e instalando requerimientos
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copiando app
COPY . /usr/src/app

# ejecutando server
CMD ["/usr/src/app/entrypoint.sh"]
#CMD python manage.py run -h 0.0.0.0

