from django.shortcuts import render, redirect
from .models import Airports, Planes, Travels, Fligth
from .forms import AirportForm, PlaneForm, TravelerForm, FlightForm

def view_data(request):
    airports = Airports.objects.all()
    planes = Planes.objects.all()
    travelers = Travels.objects.all()
    flights = Fligth.objects.all()

    return render(request, 'home.html', {
        'airports': airports,
        'planes': planes,
        'travelers': travelers,
        'flights': flights
    })



def create_airport(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            code = form.cleaned_data['code']
            airport = Airports(name=name, code=code)
            airport.save()
            return redirect('view_data')
    else:
        form = AirportForm()

    return render(request, 'create_airport.html', {'form': form})

def create_plane(request):
    if request.method == 'POST':
        form = PlaneForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data['model']
            capacity = form.cleaned_data['capacity']
            distance = form.cleaned_data['distance']
            consumtion = form.cleaned_data['consumtion']
            plane = Planes(model=model, capacity=capacity, distance=distance, consumtion=consumtion)
            plane.save()
            return redirect('view_data') 
    else:
        form = PlaneForm()

    return render(request, 'create_plane.html', {'form': form})

def create_travel(request):
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        if form.is_valid():
            fio = form.cleaned_data['fio']
            birth_date = form.cleaned_data['birth_date']
            passport = form.cleaned_data['passport']
            traveler = Travels(fio=fio, birth_date=birth_date, passport=passport)
            traveler.save()
            return redirect('view_data')
    else:
        form = TravelerForm()

    return render(request, 'create_travel.html', {'form': form})

def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['source']
            destination = form.cleaned_data['destination']
            traveler = form.cleaned_data['traveler']
            date_depart = form.cleaned_data['date_depart']
            date_arrive = form.cleaned_data['date_arrive']
            flight = Fligth(source=source, destination=destination, traveler=traveler, date_depart=date_depart, date_arrive=date_arrive)
            flight.save()
            return redirect('view_data')
    else:
        form = FlightForm()

    return render(request, 'create_flight.html', {'form': form})

