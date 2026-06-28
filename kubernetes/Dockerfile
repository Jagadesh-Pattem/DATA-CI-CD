FROM python:latest

WORKDIR /project

COPY . /project

RUN pip install flask

CMD ["python", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

