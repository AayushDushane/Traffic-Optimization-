# 🚦 Adaptive Traffic Signal Management System

This project implements an adaptive traffic signal management system using YOLOv8 for vehicle detection. The system calculates dynamic green light durations based on vehicle counts and prioritizes emergency vehicles.

## Features

- **Vehicle Detection**: Uses the YOLOv8 object detection model to detect vehicles from images uploaded for each direction of a traffic signal.
- **Adaptive Green Time**: The green light duration is dynamically adjusted based on the detected vehicle count. The system uses a custom formula to calculate the optimal green light time for each direction.
- **Emergency Vehicle Priority**: If an emergency vehicle (e.g., ambulance) is detected, the system ensures it gets priority, providing a minimum green time of 40 seconds.
- **Side-by-Side Image Display**: The system displays uploaded images side by side and shows the calculated green light duration for each direction.
- **Traffic Analysis Summary**: A table displays the number of vehicles detected and the corresponding green light time for each uploaded image.
- **Maximum Green Light Duration**: Displays the maximum green light duration among all directions.

## Requirements

- Python 3.7+
- Streamlit
- OpenCV
- YOLOv8 (Ultralytics)

### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install streamlit opencv-python ultralytics numpy
