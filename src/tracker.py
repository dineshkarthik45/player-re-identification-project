import numpy as np

class PlayerTracker:
    def __init__(self):
        self.next_id = 0
        self.tracks = []  # List of dicts: {id, bbox, features, last_seen}

    def update(self, detections, features=None):
        """
        Update tracks with new detections.
        detections: list of bounding boxes (xyxy)
        features: optional list of appearance features
        Returns: list of (id, bbox)
        """
        # TODO: Implement matching logic
        results = []
        for det in detections:
            self.tracks.append({'id': self.next_id, 'bbox': det, 'last_seen': 0})
            results.append((self.next_id, det))
            self.next_id += 1
        return results 