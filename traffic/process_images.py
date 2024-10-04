import cv2
from darkflow.net.build import TFNet
import json
import os
import time
import numpy as np

options = {
    'model': 'traffic/darkflow/cfg/yolo.cfg',
    'load': 'traffic/darkflow/bin/yolov2.weights',
    'threshold': 0.3
}

# Traffic light timers (in seconds) for each lane
timer = {}

tfnet = TFNet(options)
outputPath = os.getcwd() + "/static/outputSaveFilename/"
relative_outputPath = "/static/outputSaveFilename/"

def detectVehicles(filenames, scaling_factor=0.9):
    lane_data = []
    i= 0

    for filename in filenames:
        img_orig = cv2.imread(filename, cv2.IMREAD_COLOR)
        img = img_orig.copy()
        result = tfnet.return_predict(img)
        for vehicle in result:
            label=vehicle['label']   #extracting label
            if(label=="car" or label=="bus" or label=="bike" or label=="truck" or label=="rickshaw"):    # drawing box and writing label
                top_left=(vehicle['topleft']['x'],vehicle['topleft']['y'])
                bottom_right=(vehicle['bottomright']['x'],vehicle['bottomright']['y'])
                img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)    #green box of width 5
                img=cv2.putText(img,label,top_left,cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)   #image, label, position, font, font scale, colour: black, line width      
        img = cv2.resize(img, (525, 700))
        img_orig = cv2.resize(img_orig, (525, 700))
        # Assuming img_orig and img are your two images
        space_width = 10  # Adjust the value to set the desired space width
        # Create a space array with the same height as the images and the desired width
        space = np.zeros((img_orig.shape[0], space_width, img_orig.shape[2]), dtype=np.uint8)
        # Horizontally stack the images with the space array in between
        img_combined = np.hstack([img_orig, space, img])
        outputSaveFilename = outputPath + "output_" +filename
        outputFilename = relative_outputPath + "output_" +filename
        print(outputSaveFilename)
        cv2.imwrite(outputSaveFilename,img_combined)
        print('Output image stored at:', outputSaveFilename)



        lane_vehicle_count = {
            'lane': filename.split('.')[0],  # Use image name as lane name
            'red_duration': 0,
            'yellow_duration': 3,
            'green_duration': 0,
            'vehicle_count': 0,
            'car_count': 0,
            'truck_count': 0,
            'bike_count': 0,
            'rickshaw_count': 0,
            'bus_count': 0,
        }

        lane_vehicle_count[str(i)] = str(outputFilename)
        i += 1

        for vehicle in result:
            label = vehicle['label']
            if label in ['car', 'bus', 'bike', 'truck', 'rickshaw']:
                lane_vehicle_count['vehicle_count'] += 1

                if label == 'car':
                    lane_vehicle_count['car_count'] += 1
                elif label == 'bike':
                    lane_vehicle_count['bike_count'] += 1
                elif label == 'truck':
                    lane_vehicle_count['truck_count'] += 1
                elif label == 'bus':
                    lane_vehicle_count['bus_count'] += 1
                elif label == 'rickshaw':
                    lane_vehicle_count['rickshaw_count'] += 1

        # Calculate the green light duration based on the vehicle count
        green_time = 5.0 + scaling_factor * lane_vehicle_count['vehicle_count']

        # Get the previous lane's green duration
        previous_lane = lane_data[-1] if lane_data else None
        if previous_lane:
            previous_green_duration = previous_lane['green_duration']
            red_time = 0
        else:
            red_time = 0

        lane_vehicle_count['green_duration'] = int(green_time)
        lane_vehicle_count['red_duration'] = int(red_time)

        lane_data.append(lane_vehicle_count)

    return json.dumps(lane_data)


