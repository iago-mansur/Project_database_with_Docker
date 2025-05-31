# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY app/ .

# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose the port Jupyter uses
EXPOSE 8888