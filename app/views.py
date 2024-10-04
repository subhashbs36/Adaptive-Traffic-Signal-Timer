# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.db.models import Sum
from traffic.models import LaneData
from django import template

@login_required(login_url="/login/")
def index(request):
    sum_vehicle_count = LaneData.objects.aggregate(total_vehicle_count=Sum('vehicle_count')).get('total_vehicle_count', 0)
    sum_car_count = LaneData.objects.aggregate(total_car_count=Sum('car_count')).get('total_car_count', 0)
    sum_truck_count = LaneData.objects.aggregate(total_truck_count=Sum('truck_count')).get('total_truck_count', 0)
    sum_bike_count = LaneData.objects.aggregate(total_bike_count=Sum('bike_count')).get('total_bike_count', 0)
    lane_data = LaneData.objects.all()
    sum_counts = {        
        'sum_vehicle_count': sum_vehicle_count,
        'sum_car_count': sum_car_count,
        'sum_truck_count': sum_truck_count,
        'sum_bike_count': sum_bike_count,}
    context = {'lane_data': lane_data, 'sum_counts': sum_counts}
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
