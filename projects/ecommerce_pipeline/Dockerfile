FROM python:3.9
WORKDIR /ecommerce_app
COPY . /ecommerce_app
RUN pip install streamlit pandas
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]