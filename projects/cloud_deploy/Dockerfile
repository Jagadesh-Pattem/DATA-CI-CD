FROM python:3.9
WORKDIR /deploy-app
COPY . /deploy-app
RUN pip install streamlit pandas
CMD ["streamlit", "run", "app.py"]