import cv2
import os
from detector import PlayerDetector
from tracker import PlayerTracker

# File paths
MODEL_PATH = r'C:\Users\pente\OneDrive\Desktop\New folder\models\best.pt'
VIDEO_PATH = r'C:\Users\pente\OneDrive\Desktop\New folder\videos\input.mp4'
OUTPUT_PATH =r'C:\Users\pente\OneDrive\Desktop\New folder\videos\output.mp4' 


# Check if files exist
if not os.path.exists(VIDEO_PATH):
    print(f"Video file not found: {VIDEO_PATH}")
    exit()

if not os.path.exists(MODEL_PATH):
    print(f"Model file not found: {MODEL_PATH}")
    exit()


# Initialize
player_detector = PlayerDetector(MODEL_PATH)
player_tracker = PlayerTracker()

# Open video
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Cannot open video file")
    exit()


# Get video info
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Video: {width}x{height}, {fps} FPS")

# Setup output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

# Process video
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    print(f"Frame {frame_count}")
    
    # Detect and track players
    bboxes, confs, classes = player_detector.detect(frame)
    player_bboxes = [bboxes[i] for i, c in enumerate(classes) if c == 0]
    tracked = player_tracker.update(player_bboxes)
    
    # Draw boxes and IDs
    for pid, bbox in tracked:
        x1, y1, x2, y2 = map(int, bbox)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {pid}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    out.write(frame)

# Clean up
cap.release()
out.release()
print(f'Done! Output saved as {OUTPUT_PATH}')