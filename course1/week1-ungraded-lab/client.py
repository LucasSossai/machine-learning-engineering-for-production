import io
import os

import cv2
import numpy as np
import requests

MODEL = "yolov3-tiny"
FULL_URL = f"http://localhost:8000/predict?model={MODEL}"


dir_name = "images_predicted"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)


def response_from_server(url, image_file, verbose=True):
    """Makes a POST request to the server and returns the response.

    Args:
        url (str): URL that the request is sent to.
        image_file (_io.BufferedReader): File to upload, should be an image.
        verbose (bool): True if the status of the response should be printed. False otherwise.

    Returns:
        requests.models.Response: Response from the server.
    """

    files = {"file": image_file}
    print(f"Sending POST request to {url}")
    response = requests.post(url, files=files)
    status_code = response.status_code
    if verbose:
        msg = (
            "Everything went well!"
            if status_code == 200
            else "There was an error when handling the request."
        )
        print(msg)
    return response


def save_image_from_response(response, filename):
    """Save image within server's response.

    Args:
        response (requests.models.Response): The response from the server after object detection.
    """

    image_stream = io.BytesIO(response.content)
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    print(f"Saving image in images_predicted/{filename}")
    cv2.imwrite(f"images_predicted/{filename}", image)


image_files = ["car2.jpg", "clock3.jpg", "apples.jpg"]

for image_file in image_files:
    print(f"Currently testing: {image_file}")
    with open(f"images/{image_file}", "rb") as img:
        prediction = response_from_server(FULL_URL, img, verbose=True)

    save_image_from_response(prediction, image_file)
