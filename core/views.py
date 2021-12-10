from django.shortcuts import render

# Create your views here.


def imc(request):
    return render(request, 'imc.html')
