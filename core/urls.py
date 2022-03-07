from django.urls import path
from . import views

app_name = 'core'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetalharServicoView.as_view(), name='detalhe_servico')
]