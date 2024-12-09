from django.contrib import admin
from .models import Airports, Planes, Travels, Fligth

# Register your models here.
admin.register( [Airports, Planes,
                 Travels, Fligth] )

