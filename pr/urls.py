from django.urls import path

from . import views

app_name = 'pr'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:promo_id>/', views.detail, name = 'detail'),
]
