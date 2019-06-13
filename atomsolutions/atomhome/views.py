from django.shortcuts import render, get_object_or_404
from requests_html import HTMLSession
from django.views.generic.list import ListView
from .models import Post
from django.views.generic import DetailView
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext


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


def recruit(request):
    return render(request, 'atomhome/en/recruitment.html')


def dt1(request):
    return render(request, 'atomhome/en/recruit/detail1.html')


def dt2(request):
    return render(request, 'atomhome/en/recruit/detail2.html')


def dt3(request):
    return render(request, 'atomhome/en/recruit/detail3.html')


def dt4(request):
    return render(request, 'atomhome/en/recruit/detail4.html')


def dt5(request):
    return render(request, 'atomhome/en/recruit/detail5.html')


def dt6(request):
    return render(request, 'atomhome/en/recruit/detail6.html')


def contact(request):
    return render(request, 'atomhome/en/contact.html')


def privacy(request):
    return render(request, 'atomhome/en/privacy.html')


def faq(request):
    return render(request, 'atomhome/en/faq.html')


def vr(request):
    return render(request, 'atomhome/en/vr.html')

class NewsView(ListView):
    model = Post
    template_name = 'atomhome/en/news.html'
    paginate_by = 5
    ordering = ['-created']

   
class NewsDetailView(generic.DetailView):
    template_name = 'atomhome/en/details.html'
    model = Post

