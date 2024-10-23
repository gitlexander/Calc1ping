# Use the official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the script
COPY ping_service.py /app/ping_service.py

# Expose port 8000 to satisfy Render's port requirement
EXPOSE 8000

# Run the pinging service
CMD ["python", "ping_service.py"]
