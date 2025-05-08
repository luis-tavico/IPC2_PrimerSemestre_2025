from django.urls import path
from .views import lista_productos, crear_producto, actualizar_producto, eliminar_producto

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('crear/', crear_producto, name='crear_producto'),
    path('actualizar/<int:id>/', actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
]