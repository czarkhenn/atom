from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'atomhome/en/index.html')


def ofcexchange(request):
    return render(request, 'atomhome/en/official-exchange.html')


def company(request):
    return render(request, 'atomhome/en/company.html')


def xec(request):
    return render(request, 'atomhome/en/xec.html')


def xet(request):
    return render(request, 'atomhome/en/xet.html')
