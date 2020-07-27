FROM python:3-slim

RUN pip install gevent flask 

WORKDIR /app

COPY ./ /app

EXPOSE 5000 

CMD ["python", "gevent_server.py"]
