# Adaptive Traffic Signal Timer

**Adaptive Traffic Signal Timer** is a smart traffic management system using YOLO for real-time traffic density calculation and Django for backend integration, enhanced by the AppSeed Dashboard for a user-friendly interface. The system dynamically adjusts traffic light timers based on vehicle detection, improving traffic flow and reducing congestion.

## System Overview

The project is divided into three main modules:

1. **Vehicle Detection Module**: 
   - Utilizes YOLO for real-time vehicle detection at traffic junctions.
   - Detects cars, bikes, buses, trucks, and more to calculate traffic density.

2. **Signal Switching Algorithm**:
   - Dynamically adjusts green light duration based on detected traffic density.
   - Ensures lanes receive appropriate green light durations, with minimum and maximum limits to avoid lane starvation.

3. **Simulation Module**:
   - Simulates the system to compare the adaptive signal timer with traditional static systems, showcasing the efficiency of dynamic traffic management.

## How It Works

- The system processes images from CCTV cameras at traffic junctions.
- Using YOLO, the Vehicle Detection Module identifies the number and types of vehicles in each lane.
- The Signal Switching Algorithm adjusts the green light duration based on traffic density, improving the flow of vehicles.
- A simulation visualizes the system's effectiveness compared to a static traffic signal system.

## Requirements

- Python 3.8+
- Django
- YOLO (Darknet or TensorFlow)
- AppSeed Dashboard

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/adaptive-traffic-signal-timer.git

2. Install the required Python packages:
   
   ```bash
   pip install -r requirements.txt

3. Run the Django server:
   
   ```bash
   python manage.py runserver
