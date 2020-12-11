from rest_framework import serializers

from .models import Promo


class PromoListSerializer(serializers.ModelSerializer):
    """Список доступных промо"""
    class Meta:
        model = Promo
        fields = ("name", "promo","date")


class CreatePromoListSerializer(serializers.ModelSerializer):
    """Добавление Промо"""
    class Meta:
        model = Promo
        fields = '__all__'
