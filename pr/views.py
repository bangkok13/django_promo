from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Promo
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PromoListSerializer, CreatePromoListSerializer


class PromoListView(APIView):
    """Вывод списка промо"""
    def get(self, request):
        promos = Promo.objects.filter(date__year=2020)
        serializer = PromoListSerializer(promos, many=True)
        return Response(serializer.data)


class CreatePromoView(APIView):
    """Добавление промо"""
    def post(self, request):
        create = CreatePromoListSerializer(data=request.data)
        if create.is_valid():
            create.save()
        return Response(status=201)


def index(request):
    latest_promo_list = Promo.objects.order_by('-date')[:5]
    return render(request, 'promos/list.html', {'latest_promo_list':latest_promo_list})


def detail(request, promo_id):
    try:
        a= Promo.objects.get( id = promo_id)
    except:
        raise Http404('no find')
    return render(request, 'promos/detail.html', {'promo': a})