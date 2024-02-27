import os
import yaml
from roboflow import Roboflow
from ultralytics import YOLO

os.chdir("C:/Users/HarmerA/Dropbox/data/label_ocr")

#Project set up from roboflow
rf = Roboflow(api_key="uHJ90XV1rwOgb1Sg4PdA")
project = rf.workspace("labelreader").project("detect_pin_labels")


# Train OBB model
# dataset = project.version(2).download("yolov8-obb")

# with open(f'{dataset.location}/data.yaml', 'r') as file:
#     data = yaml.safe_load(file)
# data['path'] = dataset.location
# with open(f'{dataset.location}/data.yaml', 'w') as file:
#     yaml.dump(data, file, sort_keys=False)

# model = YOLO("yolov8n-obb.pt")
# results = model.train(data='C:/Users/HarmerA/OneDrive - MWLR/repos/label_ocr/yolov8n-obb.pt', epochs=100, imgsz=640)


# Train standard YOLOv8 PyTorch object detector
dataset = project.version(2).download("yolov8")

# with open(f'{dataset.location}/data.yaml', 'r') as file:
#     data = yaml.safe_load(file)
# data['path'] = dataset.location
# with open(f'{dataset.location}/data.yaml', 'w') as file:
#     yaml.dump(data, file, sort_keys=False)

model = YOLO("yolov8n.pt")
results = model.train(data='C:/Users/HarmerA/OneDrive - MWLR/repos/label_ocr/yolov8m.pt', epochs=100, imgsz=640)









yolo task=detect
mode=predict
model=yolov8n.pt
conf=0.25
source='https://media.roboflow.com/notebooks/examples/dog.jpeg'
