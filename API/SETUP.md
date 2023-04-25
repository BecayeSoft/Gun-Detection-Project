
# Setup

## Virtual Environment
Create a virtual env
```
python3 -m venv env
```

Activate/Deactivate env (PowerShell)
```
env/Activate.ps1
deactivate
```

For mac users:
```
source env/activate
```

Install dependencies
```
pip install -r requirements.txt
```

## Run the Flask API
````
flask run
````

## Docker Container
```
docker build -t gun-detection-api:latest .
docker image ls
docker run -p 5000:5000 gun-detection-api:latest
```
