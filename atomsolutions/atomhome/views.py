from django.shortcuts import render
from requests_html import HTMLSession

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
    session = HTMLSession()
    r = session.get('https://coinmarketcap.com/currencies/eternal-token/')
    s = r.html.find('.h2', first=True)
    valueint = s.text

    return render(request, 'atomhome/en/xet.html', {'valueint': valueint})


def media(request):
    return render(request, 'atomhome/en/media.html')


def mediajp(request):
    return render(request, 'atomhome/jp/media.html')


def video(request):
    return render(request, 'atomhome/en/video.html')


def wlabel(request):
    return render(request, 'atomhome/en/whitelabel.html')
