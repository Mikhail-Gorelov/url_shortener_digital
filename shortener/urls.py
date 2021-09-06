from django.urls import path

from shortener import views

app_name = 'shortener'

urlpatterns = [
    path('<str:short_url>/', views.redirect_to_origin, name='redirect_to_origin'),
    path('', views.main, name='main'),
]
