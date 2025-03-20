from django.shortcuts import render

from about.models import About
from doctors.models import Directions, Doctor
from website.models import Website, Slider


# Create your views here.
def Home(request):
    website = Website.objects.first()
    slides = Slider.objects.all()
    about = About.objects.first()
    directions = Directions.objects.all().order_by('title')
    doctors = Doctor.objects.all().order_by('id')
    context = {
        'website': website,
        'slides': slides,
        'about': about,
        'directions': directions,
        'doctors': doctors,
    }
    return render(request, 'home.html', context)

def AboutPage(request):
    website = Website.objects.first()
    about = About.objects.first()
    context = {
        'website': website,
        'about': about,
    }
    return render(request, 'about.html', context)