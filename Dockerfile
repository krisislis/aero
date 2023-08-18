FROM python:3.9
WORKDIR /opt/aero/

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' airflow

USER airflow
ENV PYTHONPATH "${PYTHONPATH}:/opt/aero"
