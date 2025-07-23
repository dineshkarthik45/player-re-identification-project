# Player Re-Identification in a Single Feed

## Overview
This project implements player re-identification in a single video feed. The goal is to assign consistent IDs to players, even if they leave and re-enter the frame, using a YOLOv11-based object detector.

## Project Structure
```
player_reid_project/
├── models/           # YOLOv11 model goes here
├── videos/           # Input videos go here
├── src/              # Source code
│   ├── detector.py
│   ├── tracker.py
│   └── main.py
├── requirements.txt  # Dependencies
├── README.md         # Setup and usage instructions
└── report.md         # Brief report on approach
```

## Setup Instructions
1. Download the YOLOv11 model and the input video from the provided Google Drive link.
2. Place the model in the `models/` folder and the video in the `videos/` folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main script:
   ```bash
   python src/main.py
   ```

## Notes
- See `report.md` for a description of the approach and methodology.
- The code is modular and easy to extend for more advanced tracking or re-identification techniques. 