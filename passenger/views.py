from django.shortcuts import render, HttpResponse

# Create your views here.
def passenger_view(request):
    return HttpResponse("<h1>This is our Passenger features page</h1>")
def passengerprofile_view(request):
    return HttpResponse("<h1>This is our Passenger profile page</h1>")
def passengerpurticket_view(request):
    return HttpResponse("<h1>This is our Purchase ticket page</h1>")
def payment_view(request):
    return HttpResponse("<h1>This is our Payment page</h1>")
def busschdule_view(request):
    return HttpResponse("<h1>This is our Bus Schedule page</h1>")
def sunlight_view(request):
    return HttpResponse("<h1>This is our Sunlight direction page</h1>")
def track_view(request):
    return HttpResponse("<h1>This is our Bus tracking page</h1>")
def reserve_view(request):
    return HttpResponse("<h1>This is our Bus Reservation page</h1>")
