from django.shortcuts import render
from .models import Lane, LaneData
from .process_images import detectVehicles
import os
import json

def process_images(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')

        filenames = []
        for image in images:
            # Save the image temporarily with the label name
            filename = f"{image.name.split('.')[0]}.jpg"
            with open(filename, 'wb') as f:
                f.write(image.read())

            filenames.append(filename)

        # Process the images and get the results
        results = detectVehicles(filenames)

        # Delete the temporary images
        for filename in filenames:
            os.remove(filename)

        # Convert JSON string to Python list of dictionaries
        lane_data = json.loads(results)

        # Update lane data
        for lane_entry in lane_data:
            lane_name = lane_entry['lane']
            vehicle_count = lane_entry['vehicle_count']
            car_count = lane_entry['car_count']
            bike_count = lane_entry['bike_count']
            truck_count = lane_entry['truck_count']
            bus_count = lane_entry['bus_count']
            rickshaw_count = lane_entry['rickshaw_count']
            red_duration = lane_entry['red_duration']
            yellow_duration = lane_entry['yellow_duration']
            green_duration = lane_entry['green_duration']

            lane, _ = Lane.objects.get_or_create(name=lane_name)
            lane_data_entry = LaneData.objects.create(
                lane=lane,
                vehicle_count=vehicle_count,
                car_count=car_count,
                bike_count=bike_count,
                truck_count=truck_count,
                bus_count = bus_count,
                rickshaw_count = rickshaw_count,
                red_duration=red_duration,
                yellow_duration=yellow_duration,
                green_duration=green_duration
            )
            lane_data_entry.save()

        print(lane_data)

        # Get the updated lane data
        # lanes = Lane.objects.all()
        lanes_data = LaneData.objects.all()

        return render(request, 'ui_results.html', {'lanes': lanes_data, 'session_data': lane_data})

    return render(request, 'ui-components.html')


def lane_data_view(request):
    lane_data = LaneData.objects.all()  # Retrieve all LaneData objects
    context = {'lane_data': lane_data}  
    return render(request, 'ui-tables.html', context)