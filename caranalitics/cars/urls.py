# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_car, name = 'create_car'),
    path('update/<int:id>/', views.update_car, name='update'),
    path('list/', views.car_list, name='list'),
    path('delete/<int:id>/', views.delete_car, name='delete'),
    path('detail/<int:id>/', views.detail_car, name='detail'),
]