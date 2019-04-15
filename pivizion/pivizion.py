import os
import io

from google.cloud import vision, texttospeech
from google.cloud.vision import types

global is_pi

print(os.uname().sysname)
if os.uname().sysname == 'raspberrypi':
    import picamera
    is_pi = True
else:
    from cv2 import *
    is_pi = False


class PiVizion(object):
    def get_image(self):
        if is_pi:
            print("Pi cam")
        else:
            cam = VideoCapture(0)
            s, img = cam.read()

            if s:
                # namedWindow("cam-test")
                # imshow("cam-test", img)
                # waitKey(0)
                # destroyWindow("cam-test")
                imwrite("filename.jpg", img)


    def detect_labels(self):
        client = vision.ImageAnnotatorClient()

        file_name = "filename.jpg"

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        labels_response = client.label_detection(image=image)
        labels = labels_response.label_annotations

        text_response = client.text_detection(image=image)
        texts = text_response.text_annotations

        print('Labels: ')
        print(labels[0].description)

        print('Text: ')
        print(texts[0].description)


test = PiVizion()
#test.get_image()
test.detect_labels()
