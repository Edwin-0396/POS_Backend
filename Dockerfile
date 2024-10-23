FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev \
    build-essential \
    python3-dev \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Command to run Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
