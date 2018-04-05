from django.urls import path
from basic_app import views

app_name = 'basic_app'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
]
