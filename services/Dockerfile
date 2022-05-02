FROM python:3.9.6-slim-buster

RUN apt-get update \
	&& apt-get -y install netcat gcc \
	&& apt-get clean

RUN  pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./api /api/api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]
