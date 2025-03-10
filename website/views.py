from django.shortcuts import render

from website.models import Website, Slider


# Create your views here.
def Home(request):
    website = Website.objects.first()
    slides = Slider.objects.all()
    context = {
        'website': website,
        'slides': slides
    }
    return render(request, 'home.html', context)