# 🚦 Adaptive Traffic Signal Management System

This project implements an adaptive traffic signal management system using YOLOv8 for vehicle detection. The system calculates dynamic green light durations based on vehicle counts and prioritizes emergency vehicles.

## Features

- **Vehicle Detection**: Uses the YOLOv8 object detection model to detect vehicles from images uploaded for each direction of a traffic signal.
- **Adaptive Green Time**: The green light duration is dynamically adjusted based on the detected vehicle count. The system uses a custom formula to calculate the optimal green light time for each direction.
- **Emergency Vehicle Priority**: If an emergency vehicle (e.g., ambulance) is detected, the system ensures it gets priority, providing a minimum green time of 40 seconds.
- **Side-by-Side Image Display**: The system displays uploaded images side by side and shows the calculated green light duration for each direction.
- **Traffic Analysis Summary**: A table displays the number of vehicles detected and the corresponding green light time for each uploaded image.
- **Maximum Green Light Duration**: Displays the maximum green light duration among all directions.

## Optimized Formula for Green Time Calculation

Instead of a simple scaling formula, the green time is calculated using a weighted vehicle count and a realistic flow rate.

### Formula:

The green light duration (`T_green`) is calculated using the following formula:

T_green = max( (W_total_vehicles / R_flow), T_min )


Where:

- `T_green` = Green signal duration (in seconds)
- `W_total_vehicles` = Weighted vehicle count
- `R_flow` = Flow rate (vehicles per second per lane)
- `T_min` = Minimum green time (e.g., 10 seconds)

### Step-by-Step Calculation:

1. **Determine Weighted Vehicle Count**:

   Assign different weights to each vehicle type:

   - **Bike** = 1
   - **Car** = 1.5
   - **Truck/Bus** = 3
   - **Emergency Vehicle** = Instant Green! 🚨

   The formula for the total weighted vehicle count (`W_total_vehicles`) is:

W_total_vehicles = (1 * bikes) + (1.5 * cars) + (3 * trucks/buses)

2. **Estimate Road Flow Rate**:

The flow rate (`R_flow`) should be estimated dynamically based on road type:

- **Urban Roads**: 2-3 vehicles/sec
- **Highways**: 4-6 vehicles/sec
- **Narrow Lanes**: 1-2 vehicles/sec

The flow rate can be adjusted dynamically based on historical traffic data.

3. **Apply the Formula**:

Example calculation:

Suppose there are:

- **5 bikes**
- **10 cars**
- **3 trucks/buses**

The flow rate is **2.5 vehicles/sec**.

The weighted vehicle count is:

W_total_vehicles = (5 * 1) + (10 * 1.5) + (3 * 3) = 5 + 15 + 9 = 29

The green time is calculated as:
T_green = 29 / 2.5 = 11.6 ≈ 12 seconds


However, the green light time should be between a **minimum of 10 seconds** and a **maximum of 90 seconds**. So in this case, the green time is **12 seconds**.

4. **Emergency Vehicle Override**:

If an emergency vehicle is detected (e.g., ambulance), the system will override the normal green time calculation and give **instant green** to prioritize the emergency vehicle.

### Summary:

- The formula dynamically adjusts the green light duration based on the total weighted vehicle count and the flow rate.
- Emergency vehicles are given priority and instantly receive green light.

## Requirements

- Python 3.7+
- Streamlit
- OpenCV
- YOLOv8 (Ultralytics)

### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install streamlit opencv-python ultralytics numpy




