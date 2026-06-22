# Comment

# FROM - Import a base image
FROM python:3.12

# RUN - To run any command on top of above layer
RUN pip install pandas numpy matplotlib

# Run can also be written as below
RUN ["pip", "install", "pandas", "numpy", "matplotlib"]

# WORKDIR - Create folders in Container and set as working directory
WORKDIR /work_folder/etl

# CMD ["pwd"]

# USER - switch user
# Create user first
RUN useradd -ms /bin/bash jaga
USER jaga

# ENV - To set environmental Variables
ENV app_host=0.0.0.0
ENV app_port=8080

# COPY - To Copy the files from local computer to container
COPY . .

CMD ["ls", "/work_folder/etl"]

# Exposes the port in container. This will be the entrypoint for the users into our containers
EXPOSE 8080 

# ADD - Add files from cloud to local container



