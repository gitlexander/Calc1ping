# Use the official lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the script
COPY ping_service.py /app/ping_service.py

# Run the pinging service
CMD ["python", "ping_service.py"]
