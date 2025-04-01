# 🚦 Adaptive Traffic Signal Management System

This project implements an adaptive traffic signal management system using YOLOv8 for vehicle detection. The system calculates dynamic green light durations based on vehicle counts and prioritizes emergency vehicles.

## Features

- **Vehicle Detection**: Uses the YOLOv8 object detection model to detect vehicles from images uploaded for each direction of a traffic signal.
- **Adaptive Green Time**: The green light duration is dynamically adjusted based on the detected vehicle count. The system uses a custom formula to calculate the optimal green light time for each direction.
- **Emergency Vehicle Priority**: If an emergency vehicle (e.g., ambulance) is detected, the system ensures it gets priority, providing a minimum green time of 40 seconds.
- **Side-by-Side Image Display**: The system displays uploaded images side by side and shows the calculated green light duration for each direction.
- **Traffic Analysis Summary**: A table displays the number of vehicles detected and the corresponding green light time for each uploaded image.
- **Maximum Green Light Duration**: Displays the maximum green light duration among all directions.

## Formula for Green Light Calculation

The green light duration for each direction is calculated using the following formula:

### Formula:
\[
\text{Green Time} = \frac{\text{Weighted Vehicle Count}}{\text{Dynamic Flow Rate}}
\]

Where:

- **Weighted Vehicle Count** is the sum of vehicle counts multiplied by their respective weights based on their type (e.g., car, truck, bike).
- **Dynamic Flow Rate** is adjusted based on the vehicle count to dynamically optimize traffic flow.
  
The flow rate is adjusted using the formula:

\[
\text{Dynamic Flow Rate} = \max(2.0, \text{Flow Rate} - \frac{\text{Weighted Vehicle Count}}{80})
\]

- The **min_time** (minimum green light time) is set to 10 seconds.
- The **max_time** (maximum green light time) is capped at 90 seconds.

### Weights for Vehicle Types:
- **Car (2)**: 1.5
- **Truck/Bus (3)**: 3
- **Bike (5)**: 1
- **Motorbike (7)**: 1

If an emergency vehicle (e.g., an ambulance) is detected, the green light time is increased to at least 40 seconds, regardless of the calculated green time.

## Requirements

- Python 3.7+
- Streamlit
- OpenCV
- YOLOv8 (Ultralytics)

### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install streamlit opencv-python ultralytics numpy
