# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any necessary dependencies
RUN pip freeze > requirements.txt


# Expose the port the app runs on
EXPOSE 5001

# Define environment variable for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Run the Flask app
CMD ["Flask", "run", "--host=0.0.0.0", "--port=5000"]
