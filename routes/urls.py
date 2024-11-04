from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('load/', views.load_graph, name='load_graph'),
    path('shortest-route/', views.shortest_route, name='shortest_route'),
    path('city/<int:id>/', views.city_detail, name='city_detail'),
]
