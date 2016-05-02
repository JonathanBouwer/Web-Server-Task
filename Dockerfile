FROM python:2.7-slim
ADD src /webserver/
WORKDIR /webserver/
RUN pip install -r /webserver/requirements.txt
CMD ["python","/webserver/flaskwebserver.py"]
