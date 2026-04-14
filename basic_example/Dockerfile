# Use a lightweight Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /basic_example

# Copy requirements and install dependencies
COPY requirements.txt /basic_example
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /basic_example

# Inform Docker that the container listens on port 5000
# !!!Don't use port 5000 on macOS, it will cause a return conflict since port 5000 is used internally by macOS.
EXPOSE 50000

# Command to run the application
CMD ["python", "app.py"]