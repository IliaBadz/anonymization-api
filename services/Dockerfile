FROM python:3.9.6-slim-buster

RUN apt-get update \
	&& apt-get -y install netcat gcc \
	&& apt-get clean


ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv /opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN  pip install --upgrade pip

COPY ./requirements.txt /api/
RUN pip --default-timeout=1000 install -r /api/requirements.txt

COPY ./api api/api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]
