FROM python:3.6.1-alpine
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir templates
RUN mkdir static
COPY app.py /app.py
COPY templates/*  /templates/
COPY static/*  /static/
CMD ["python","app.py"]
