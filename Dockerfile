FROM python:3.10-slim

WORKDIR /PAIDITAPPWEB
COPY logica ./logica
copy servicios ./servicios
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r ./servicios/requirements.txt
ENV PYTHONPATH="$PYTHONPATH:/PAIDITAPPWEB"
EXPOSE 8000
CMD ["python", "./servicios/manage.py", "runserver", "0.0.0.0:8000"]

