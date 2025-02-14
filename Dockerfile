# Use the official Python image based on Alpine
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Install system dependencies (Alpine uses apk package manager)
RUN apk update && apk add --no-cache \
    build-base \
    libpq-dev \
    && rm -rf /var/cache/apk/*

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install pip dependencies (including upgrading pip itself)
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


# Download the punkt, wordnet, and averaged_perceptron_tagger resources during the image build
RUN python -m nltk.downloader punkt wordnet averaged_perceptron_tagger

# Copy the Django project files to the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Run the Django development server using CMD in JSON format
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

##########################################
# Build the Docker image
# docker build -t my-django-app .

# Run the Docker container
# docker run -p 8000:8000 my-django-app
###########################################
