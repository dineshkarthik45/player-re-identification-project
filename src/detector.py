import os
from ultralytics import YOLO

class PlayerDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image):
        """
        Run detection on an image (numpy array).
        Returns: list of detections (xyxy, confidence, class)
        """
        results = self.model(image)
        return results[0].boxes.xyxy.cpu().numpy(), results[0].boxes.conf.cpu().numpy(), results[0].boxes.cls.cpu().numpy() 