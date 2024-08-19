FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./code/ /app/

COPY ./script.sh /

ENTRYPOINT ["sh", "/script.sh"]