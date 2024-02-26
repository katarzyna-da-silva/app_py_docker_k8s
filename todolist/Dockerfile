# Choose a base image with Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /todolist

# Copy the contents of the current directory into the /todolist directory in the container
COPY . /todolist

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r /todolist/requirements.txt

# Update package lists
RUN apt-get update

# Set the default command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001", "--no-debugger"]
