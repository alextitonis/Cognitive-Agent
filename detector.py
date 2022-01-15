from imageai.Detection import ObjectDetection
import os

class detector:
    def __init__(self, modelPath="resnet50_coco_best_v2.1.0.h5"):
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(modelPath)
        self.detector.loadModel()
        
    def detect(self, image_data, input_type="array", output_image_path="imagenew.jpg", minPerc=50):
        detections = self.detector.detectObjectsFromImage(input_image=image_data, input_type=input_type, output_image_path=output_image_path, minimum_percentage_probability=minPerc)
        res = []
        print('detected:', len(detections), 'objects!');
        for eachObject in detections:
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
            x1, y1, x2, y2 = eachObject["box_points"]
            center = (x1 + x2) / 2, (y1 + y2) / 2
            res.append(detectedObject(eachObject["name"], center))
            print("--------------------------------")
        return res
    
class detectedObject:
    def __init__(self, name, center):
        self.name = name
        self.center = center