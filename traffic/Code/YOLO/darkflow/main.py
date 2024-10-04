import cv2
from darkflow.net.build import TFNet
import os
import time

options = {
    'model': './cfg/yolo.cfg',
    'load': './bin/yolov2.weights',
    'threshold': 0.3
}

tfnet = TFNet(options)
inputPath = os.getcwd() + "/test_images/"
outputPath = os.getcwd() + "/output_images/"

# Traffic light timers (in seconds) for each lane
timer = {}

def detectVehicles(filename):
    global tfnet, inputPath, outputPath, timer
    img = cv2.imread(inputPath + filename, cv2.IMREAD_COLOR)
    result = tfnet.return_predict(img)

    for vehicle in result:
        label = vehicle['label']
        if label in ['car', 'bus', 'bike', 'truck', 'rickshaw']:
            top_left = (vehicle['topleft']['x'], vehicle['topleft']['y'])
            bottom_right = (vehicle['bottomright']['x'], vehicle['bottomright']['y'])
            img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
            img = cv2.putText(img, label, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

    outputFilename = outputPath + "output_" + filename
    cv2.imwrite(outputFilename, img)
    print('Output image stored at:', outputFilename)

    return result

def manageTrafficLights(index, lane, scaling_factor=0.1):
    global timer
    light_times = timer[lane]

    print('Lane:', lane)

    # Red light
    red_time = light_times['previous_green'] if 'previous_green' in light_times else 2  # Use previous green time as red time
    print('Red Light:', red_time, 'seconds')
    time.sleep(red_time)

    # Yellow light
    print('Yellow Light:', light_times['yellow'], 'seconds')
    time.sleep(light_times['yellow'])

    # Calculate green light time based on 5 seconds + density of cars present on the lane
    green_time = 5 + scaling_factor * light_times['vehicle_count']
    print('Green Light:', green_time, 'seconds')
    time.sleep(green_time)

    # Update previous green time for the next lane
    next_lane_index = (index + 1) % len(timer)
    next_lane = list(timer.keys())[next_lane_index]
    timer[next_lane]['previous_green'] = green_time

def processLane(filename, scaling_factor=0.1):
    result = detectVehicles(filename)
    lane_name = os.path.splitext(filename)[0]
    vehicle_count = 0
    for vehicle in result:
        label = vehicle['label']
        if label in ['car', 'bus', 'bike', 'truck', 'rickshaw']:
            vehicle_count += 1

    # Store the vehicle count and red light duration for the lane
    timer[lane_name] = {
        'red': 0,  # Placeholder for red light duration
        'yellow': 3,
        'vehicle_count': vehicle_count
    }

def manageTraffic():
    lanes = list(timer.keys())

    for index, lane in enumerate(lanes):
        manageTrafficLights(index, lane)

# Process input images and calculate timers
for filename in os.listdir(inputPath):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        processLane(filename)

# Manage traffic lights
manageTraffic()

print("Done!")
