from flask import Flask, request
from flask import render_template
from flask_cors import CORS

import cv2

from GunDetector import GunDetector
import ImageProcessor as processor


app = Flask(__name__)
# TODO: Specify URLs instead
CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "*"]}})

# Load the model
model_path = './model/model.pt'
model = GunDetector()
model.load(path=model_path)

# -----------------------------------------------
# Routes for the templates: For test purpose
# ----------------------------------------------

@app.route('/')
def home():
    return render_template('index.html')\

@app.route('/predict', methods=['POST'])
def predict():
    """
    Process the uploaded file, return the prediction as a base64 image
    then send it to `results.html`
    """
    # Get the file from the request
    file = request.files['file']

    # Read the image and preprocess it
    image = processor.process_image(file)
    cv2.imwrite('img.png', image)

    # Make a prediction
    predicted_image = model.predict_image(image)

    # Convert predicted image to Base64
    encoded_image_data = processor.image_to_base64(predicted_image)

    # Pass the encoded image data to the template
    return render_template('results.html', image_data=encoded_image_data)


# -----------------------------------------------
# Routes for the API: For Deployment
# ----------------------------------------------
@app.route('/api')
def api_home():
    return 'API is running'

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """
    Process the uploaded file and return the prediction as a base64 image
    """
    # Get the file from the request
    file = request.files['file']

    # Read the image and preprocess it
    image = processor.process_image(file)
    cv2.imwrite('img.png', image)

    # Make a prediction
    predicted_image = model.predict_image(image)

    # Convert predicted image to Base64
    encoded_image_data = processor.image_to_base64(predicted_image)

    return str(encoded_image_data)


if __name__ == '__main__':
    app.run()

