from flask import Flask, request
from flask import render_template
from flask_cors import CORS

# from flask import send_file

import json
import cv2
import os

from GunDetector import GunDetector
import ImageProcessor as processor


app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "*"]}})

# Load the model
model_path = './model/model.pt'
model = GunDetector()
model.load(path=model_path)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the file from the request
    file = request.files['file']

    # Read the image and preprocess it
    image = processor.process_image(file)
    cv2.imwrite('img.png', image)

    # Make a prediction
    predicted_image = model.predict_image(image)

    # Convert predicted image to Base64
    encoded_image_data = processor.image_to_base64(predicted_image)

    # Return the image as a JSON object
    response_dict = {'image_data': encoded_image_data}
    # return json.dumps(response_dict)

    return str(encoded_image_data)

    # Pass the encoded image data to the template
    # return render_template('results.html', image_data=encoded_image_data)


if __name__ == '__main__':
    app.run()
