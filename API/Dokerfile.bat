@REM Run the docker image
docker build -t gun-detection-api:latest .
docker run -p 5000:5000 gun-detection-api:latest