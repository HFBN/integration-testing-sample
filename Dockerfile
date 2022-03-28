# Import a python enabled base image
FROM python:3.8.5

# Set the working directory
WORKDIR /opt/

# Install required dependencies
COPY requirements.txt .
# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Lets copy all the stuff we need
# The directory tree inside the container will have the following structure:
# opt/
# --run.sh
# --run.py
# --api/
# ----_init_.py
# ----app.py
# ----config.py
# ----controller.py
# --models/
# ----pipeline.pkl
# --requirements.txt
COPY app .

# Set the port we'd like to use.
EXPOSE 5000

# Notice that we are using our new bash script here.
# This enables us to use a gunicorn web server.
# Explaining gunicorn is out of scope for this tutorial.
# For now, just know that this is a good thing.
CMD ["bash", "./run.sh"]