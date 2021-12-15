from imageai.Classification.Custom import ClassificationModelTrainer
import os

class detectorTrainer:
    def __init__(self, modelPath, num_objects=10, num_experiments=100, enhance_data=True, batch_size=32, show_network_summary=True):
        self.model_trainer = ClassificationModelTrainer()
        self.model_trainer.setModelTypeAsResNet50()
        self.model_trainer.setDataDirectory(modelPath)
        self.model_trainer.trainModel(num_objects=num_objects, 
                                      num_experiments=num_experiments, 
                                      enhance_data=enhance_data, 
                                      batch_size=batch_size, 
                                      show_network_summary=show_network_summary)