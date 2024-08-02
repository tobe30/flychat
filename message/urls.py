from django.urls import path
from . import views


app_name = 'message'

urlpatterns = [
   path('', views.index, name='index'),
   path('message', views.mess, name='message'),
   path('new/<int:user_pk>/', views.new, name='new'),
   path('<int:pk>/', views.detail, name='detail'),


   path('logout', views.logout, name='logout'),

]