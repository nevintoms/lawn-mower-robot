# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
# We'll directly install matplotlib here
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run plot_graph.py when the container launches
CMD ["python", "src/main.py"]
