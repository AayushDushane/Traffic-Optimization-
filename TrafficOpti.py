import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO

# Function to calculate adaptive green signal time
def calculate_green_time(vehicle_counts, flow_rate=2.5, min_time=10, max_time=90):
    weights = {2: 1.5, 3: 3, 5: 1, 7: 1}  # Car, truck/bus, bike, motorbike
    weighted_count = sum(weights.get(cls, 1) for cls in vehicle_counts)  # Default weight 1 if unknown class
    dynamic_flow_rate = max(2.0, flow_rate - (weighted_count / 80))  # Adjust flow rate dynamically
    green_time = max(weighted_count / dynamic_flow_rate, min_time)
    return int(np.clip(green_time, min_time, max_time))  # Clip between min & max

# Streamlit UI Setup
st.set_page_config(page_title="Adaptive Traffic Signal", page_icon="🚦", layout="wide")
st.title("🚦 Adaptive Traffic Signal Management System")

# File uploader for traffic images
uploaded_files = st.file_uploader("Upload images from different sides of the signal", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Load YOLO model
yolo_model = YOLO("yolov8n.pt")

# Process images if uploaded
if uploaded_files:
    total_vehicles = {}
    emergency_detected = False

    col1, col2 = st.columns(2)  # For side-by-side images

    for idx, uploaded_file in enumerate(uploaded_files):
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # YOLO detection
        results = yolo_model(image)

        # Filter detected classes (only vehicles)
        detected_classes = [int(cls) for cls in results[0].boxes.cls]
        vehicle_counts = [cls for cls in detected_classes if cls in [2, 3, 5, 7]]  # Cars, buses, trucks, bikes
        emergency_count = sum(1 for cls in detected_classes if cls == 4)  # Ambulance class (emergency)

        if emergency_count > 0:
            emergency_detected = True  # Flag emergency vehicle presence

        # Calculate green light duration
        green_time = calculate_green_time(vehicle_counts)
        if emergency_detected:
            green_time = max(green_time, 40)  # Ensure at least 40s for emergencies

        # Store results
        total_vehicles[uploaded_file.name] = (len(vehicle_counts), green_time)

        # Display images & results
        with (col1 if idx % 2 == 0 else col2):  # Arrange images in two columns
            st.image(image, caption=f"🚗 Detected Vehicles: {len(vehicle_counts)}", use_container_width=True)
            st.markdown(f"**🟢 Green Light Duration: {green_time} sec**", unsafe_allow_html=True)

    # Display Summary Table
    st.write("### 🚥 Traffic Analysis Summary")
    summary_data = {
        "Lane": list(total_vehicles.keys()),
        "Vehicles Detected": [v[0] for v in total_vehicles.values()],
        "Green Time (s)": [v[1] for v in total_vehicles.values()]
    }
    st.table(summary_data)

    # Show max green time
    max_green_time = max(time for _, time in total_vehicles.values())
    st.write(f"### ⏳ **Maximum Green Light Duration: {max_green_time} sec**")
    if emergency_detected:
        st.write("🚨 **Emergency Vehicle Detected! Priority Given.**")
