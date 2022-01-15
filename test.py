import utils
import detector
import os

data = utils.loadImgToArray(os.getcwd() + '/test.jpg');
d = detector.detector();
d.detect(data, input_type="array", output_image_path="imagenew.jpg", minPerc=50);