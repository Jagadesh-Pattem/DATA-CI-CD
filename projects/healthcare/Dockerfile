FROM python:3.9

WORKDIR /healthcare-app

COPY . /healthcare-app

RUN pip install pandas streamlit requests

EXPOSE 3000

CMD ["streamlit", "run", "app.py", "--server.port=3000", "--server.address=0.0.0.0"]