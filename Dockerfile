# Use an official Ubuntu base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Install Python and other necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the application
CMD ["python3", "main.py"]
