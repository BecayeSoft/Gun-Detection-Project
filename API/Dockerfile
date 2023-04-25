# Choose a lightweight version of Python
FROM python:3.11.3-slim-buster

# Set Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/

# OpenCV Dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# No caching to keep docker image small
 RUN pip3 install --no-cache-dir -r requirements.txt

# Copy files into the app folder
COPY . /app

# Expose the port where the Flask app will run
EXPOSE 5000

# Run the appdoc
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# Alternative
# RUN pip3 install gunicorn
# CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4"]
