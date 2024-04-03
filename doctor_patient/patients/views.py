from django.contrib.auth.decorators import login_required
from .models import Doctor
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('doctor_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def patient_logout(request):
    logout(request)
    return redirect('doctor_list')


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


@login_required
def doctor_detail(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})
