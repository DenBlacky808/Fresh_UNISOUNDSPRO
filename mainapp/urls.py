from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:pk>/', views.download_count, name='download'),
    path('category/<int:pk>/', views.blog, name='category'),
    path('category/<int:pk>/page/<int:page>/', views.blog, name='page'),
]
