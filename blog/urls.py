from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('article/<str:name>/', views.article, name='article'),
    path('new-route/', views.new_view, name='new_view_name'),
    path('blog/resultats/', views.resultats, name='resultats'),
    path('choix/', views.my_view, name='vue'),
]