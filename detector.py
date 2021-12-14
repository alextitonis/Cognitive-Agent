from imageai.Detection import ObjectDetection
import os
from PIL import Image
from numpy import asarray

img = Image.open('image.jpeg')
data = asarray(img)

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=data, input_type="array", output_image_path="imagenew.jpg", minimum_percentage_probability=50)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    x1, y1, x2, y2 = eachObject["box_points"]
    center = (x1 + x2) / 2, (y1 + y2) / 2
    print("--------------------------------")