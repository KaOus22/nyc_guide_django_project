from django.shortcuts import render
from .boroughs import boroughs
def city(request):
    if request.method == 'GET':
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})
def borough(request, borough):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough,
                     'activities': boroughs[borough].keys()})
# Create your views here.
def activity(request, activity, borough):
    if request.method == 'GET':
        return render(
            request=request, template_name='activity.html',
            context={'borough': borough,
                     'venues': boroughs[borough][activity],
                     'activity': activity})
# ! need to inplement venues as in the urls.py
# ! first get the venue names to render on the activities page.
# ! create a url that takes each venue to it's own page
def venue(request, activity, borough, venue):
    if request.method == 'GET':
        return render(
            request=request, template_name='venue.html',
            context={'borough': borough,
                     'venues': boroughs[borough][activity][venue]['description'],
                     'activity': activity,
                     'venue': venue})