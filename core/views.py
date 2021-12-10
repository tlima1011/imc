from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def imc(request):
    return render(request, 'imc.html')


def submit_imc(request):
    if request.POST:
        massa = float(input(request.POST.get('massa')))
        altura = float(input(request.POST.get('altura')))
        imc = massa / altura * altura
        messages.success(request, imc)

