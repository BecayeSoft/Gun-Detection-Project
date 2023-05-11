# Gun-detection Desktop Application
A very simple Desktop interface for testing the model on images ans videos.

This is a standalone desktop app to test the model locally.
You can test it on your own machine.

## Setup
Instructions to test the project.

Since it is not necessary to clone the whole project, you can follow these steps:

1. Clone the `desktop-app` folder
```
git clone --depth=1 --filter=tree:0 "https://github.com/BecayeSoft/Guns-Detections-Project" desktop-app
```

2. Navigate to desktop-app
```
cd desktop-app
```

2. Install the dependencies
```
pip install -r requirements.txt
```

4. Launch the app
```
python main.py
```

## Understanding the code

`GunDetector`
A YOLOv8 model to make inferences on images and videos.

`main.py`
A Tkinter GUI to select image and videos to test the model.
