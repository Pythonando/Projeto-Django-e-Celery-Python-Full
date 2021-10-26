from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscricao, name='inscricao'),
    path('processa_inscricao', views.processa_inscricao, name='processa_inscricao')
]
