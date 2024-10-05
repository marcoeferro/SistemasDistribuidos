# Use the official Python image as the base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your ETL scripts and other necessary files to the working directory
COPY src/ /app/src/
COPY main.py /app/

# Ensure the data directory exists
RUN mkdir -p /app/data/raw

# Set the working directory
WORKDIR /app

# Set the entrypoint to the main ETL script
ENTRYPOINT ["python", "main.py"]
