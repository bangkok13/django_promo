from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Promo

def index(request):
    latest_promo_list = Promo.objects.order_by('-date')[:5]
    return render(request, 'promos/list.html', {'latest_promo_list':latest_promo_list})

def detail(request, promo_id):
    try:
        a= Promo.objects.get( id = promo_id)
    except:
        raise Http404('no find')
    return render(request, 'promos/detail.html', {'promo': a})