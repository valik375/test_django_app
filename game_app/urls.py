from django.urls import path
from . import views

app_name = 'game_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('<int:game_id>/', views.play, name='play'),
    path('games_list/', views.games_list, name='games_list'),
    path('delete_game/<int:game_id>/', views.delete_game, name='delete_game'),
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
    path('shop/<int:game_id>/', views.shop_page, name='shop'),
]
