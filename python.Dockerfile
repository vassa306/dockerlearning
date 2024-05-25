FROM python:3.8-alpine
#workdir use

WORKDIR /app

RUN pip install flask
#copy html after python script run
RUN apk add curl

COPY app/flask_app.py .

ENTRYPOINT ["/usr/bin/env", "python3", "/app/flask_app.py"] 
