from django.urls import path
from .views import EnderecoListView, EnderecoFormView, EnderecoDeleteView, EnderecoDetailView
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('listar/', EnderecoListView.as_view(), name='listar_endereco'),
    path('form/', EnderecoFormView.as_view(), name='form_endereco'),
    path('delete/<int:pk>', EnderecoDeleteView.as_view(), name='delete_endereco'),
    path('detail/', EnderecoDetailView.as_view(), name='detail_endereco')
]