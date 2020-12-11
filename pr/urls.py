from django.urls import path

from . import views

app_name = 'pr'
urlpatterns = [
    path('prcreate/', views.CreatePromoView.as_view()),
    path('promo/', views.PromoListView.as_view()),
    path('', views.index, name='index'),
    path('<int:promo_id>/', views.detail, name='detail'),
]
