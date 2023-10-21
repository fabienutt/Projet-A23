from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('article/<str:name>/', views.article, name='article'),
    path('new-route/', views.new_view, name='new_view_name'),
     path('blog/resultats.html/', views.resultats, name='resultats'),
]