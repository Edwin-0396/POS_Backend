# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 5000 to allow connections
EXPOSE 5000

# Set environment variables
ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
