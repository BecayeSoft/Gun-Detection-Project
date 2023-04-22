import numpy as np
import cv2
import base64


def process_image(file):
    """
    Reads the file sent in the request and convert it to CV2 image.

    :param file: an uploaded file that is present in the request
    :return: a converted image read to be fed to the model.
    """
    image_numpy = np.frombuffer(file.read(), dtype=np.uint8)
    image = cv2.imdecode(image_numpy, cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image, (224, 224))

    return image

def image_to_base64(image):
    """
    Convert the image to a Base64 string. This way we can send it via HTTP.

    :return: an image encoded in base64 format.
    """
    cv2.imwrite('predicted_image.png', image)
    _, encoded_image = cv2.imencode('.png', image)
    encoded_image_data = base64.b64encode(encoded_image).decode('utf-8')

    return encoded_image_data
