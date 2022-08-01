from django.urls import path
from . import views

app_name = 'game_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('<int:game_id>/', views.play, name='play'),
]
