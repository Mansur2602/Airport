from django import forms
from .models import Airports, Travels

class AirportForm(forms.Form):
    name = forms.CharField(max_length=20, label='Название аэропорта', widget=forms.TextInput())
    code = forms.CharField(max_length=3, label='Код аэропорта', widget=forms.TextInput())


class PlaneForm(forms.Form):
    model = forms.CharField(max_length=30, label='Модель самолета', widget=forms.TextInput())
    capacity = forms.IntegerField(label='Вместимость', widget=forms.NumberInput())
    distance = forms.FloatField(label='Дальность полета', widget=forms.NumberInput())
    consumtion = forms.FloatField(label='Расход топлива', widget=forms.NumberInput())


class TravelerForm(forms.Form):
    fio = forms.CharField(max_length=150, label='ФИО пассажира', widget=forms.TextInput())
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    passport = forms.CharField(max_length=12, label='Номер паспорта', widget=forms.TextInput())

class FlightForm(forms.Form):
    source = forms.ModelChoiceField(queryset=Airports.objects.all(), label='Аэропорт вылета', widget=forms.Select())
    destination = forms.ModelChoiceField(queryset=Airports.objects.all(), label='Аэропорт прилета', widget=forms.Select())
    traveler = forms.ModelChoiceField(queryset=Travels.objects.all(), label='Пассажир', widget=forms.Select())
    date_depart = forms.DateTimeField(label='Дата и время вылета', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    date_arrive = forms.DateTimeField(label='Дата и время прилета', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))



