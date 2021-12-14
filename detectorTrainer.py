from imageai.Classification.Custom import ClassificationModelTrainer
import os

execution_path = os.getcwd()

model_trainer = ClassificationModelTrainer()
model_trainer.setModelTypeAsResNet50()
model_trainer.setDataDirectory(execution_path + '/custom_model')
model_trainer.trainModel(num_objects=10, num_experiments=100, enhance_data=True, batch_size=32, show_network_summary=True)