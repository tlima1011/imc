from urllib import response

from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def imc(request):
    return render(request, 'imc.html')


def submit_imc(request):
    if request.POST:
        massa = request.POST.get('massa')
        altura = request.POST.get('altura')
        m = float(input(massa))
        a = float(input(altura))
        imc = m / a * a
        r = ''
        if ((imc >= 0) and ( imc <= 17 )):
            r = "Muito abaixo do preso"
        elif imc <= 18.5 :
            r = "Abaixo do Peso"
        elif imc <= 25:
            r = "Normal"
        elif imc <= 30:
            r = "Sobrepeso"
        elif imc <= 35:
            r = "Obesidade"
        elif imc <= 40 :
            r = "Obesidade Severa"
        else:
            r = "Obesidade Mórbida"
        f = str(imc + r)
    messages.error(request, f)

