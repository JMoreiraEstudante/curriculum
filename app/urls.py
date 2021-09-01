from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProjetoListView.as_view(), name='homepage'),
    path('projeto/<int:pk>/', views.ProjetoDetailView.as_view(), name='projeto-detail'),
]