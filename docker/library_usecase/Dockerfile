FROM python:latest

LABEL name="library docker use case"
LABEL author="Jagadesh"
LABEL email="jagadeshpattem@gmail.com"

WORKDIR /app

COPY . /app

RUN pip install pandas numpy matplotlib

EXPOSE 8080

ENV ENVIRONMENT=production
ENV DEBUG_MODE=true

CMD ["python", "/app/app.py"]