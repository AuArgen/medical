from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone

from about.models import About
from doctors.models import Directions, Doctor
from patient.models import Patient, QueuePatient
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


def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Замените 'home' на нужный URL после авторизации
        else:
            error_message = "Неверный email или пароль"

    website = Website.objects.first()
    context = {
        'website': website,
        'error_message': error_message if 'error_message' in locals() else None
    }
    return render(request, 'login.html', context)


def RegisterPage(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        pin = request.POST.get('pin')
        phone = request.POST.get('phone')

        # Проверка на пустые поля
        if not all([email, password, last_name, first_name, pin, phone]):
            error_message = "Все поля обязательны для заполнения."
        elif User.objects.filter(email=email).exists():
            error_message = "Пользователь с таким email уже существует."
        else:
            try:
                user = User.objects.create_user(
                    username=email, email=email, password=password,
                    last_name=last_name, first_name=first_name
                )
                Patient.objects.create(user=user, phone=phone, id_card_number=pin)
                return redirect('login')  # Перенаправление на страницу входа
            except Exception as e:
                error_message = f"Ошибка регистрации: {str(e)}"

    website = Website.objects.first()
    context = {
        'website': website,
        'error_message': error_message
    }
    return render(request, 'register.html', context)


def LogoutPage(request):
    logout(request)
    return redirect('home')


def DcotorPage(request, pk):
    website = Website.objects.first()
    doctor = Doctor.objects.get(id=pk)
    queues = QueuePatient.objects.filter(doctor=doctor,).order_by('-id').order_by('order')
    context = {
        'website': website,
        'doctor': doctor,
        'queues': queues,
    }
    return render(request, 'doctor.html', context)


def DcotorQueuePage(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        description = request.POST.get('description')
        user = request.user
        doctor = Doctor.objects.get(id=pk)
        patient = Patient.objects.get(user=user)
        order = QueuePatient.objects.filter(doctor=doctor).count()
        patient = QueuePatient.objects.create(patient=patient, doctor=doctor,
                                              description=description,
                                              accepted=False,
                                              status=False,
                                              date_start=timezone.now(),
                                              date_end=timezone.now(),
                                              order=order + 1)

        return redirect(f'/doctor/{pk}#list_queue')

    website = Website.objects.first()
    doctor = Doctor.objects.get(id=pk)
    context = {
        'website': website,
        'doctor': doctor,
    }
    return render(request, 'queue.html', context)
