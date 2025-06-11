# Specifing the python version
FROM python:3.10-slim

# setting the working directory
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# make port 5000 available to the world outside this container
EXPOSE 5000

# define environment variable
ENV FLASK_APP=main.py

# run the application
CMD ["flask", "run", "--host=0.0.0.0"]