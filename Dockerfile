FROM python:3.8.1-slim-buster

COPY httpd.py /usr/src/httpd.py

WORKDIR /usr/src
CMD ["python", "-u", "httpd.py"]