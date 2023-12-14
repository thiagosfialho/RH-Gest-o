from django.urls import path
from .views import DocumentosCreate

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentosCreate.as_view(), name='create_documento'),
    #path('editar/<int:pk>', EmpresaEdit.as_view(), name= 'edit_empresa'),
]
