from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo CRUD
    path('productos/', views.ProductoListCreate.as_view(), name='producto-list-create'),
    path('productos/<str:pk>/', views.ProductoRetrieveUpdateDestroy.as_view(), name='producto-detail'),
    path('clientes/', views.ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<str:pk>/', views.ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'),
    path('ventas/', views.VentaListCreate.as_view(), name='venta-list-create'),
    path('ventas/<str:pk>/', views.VentaRetrieveUpdateDestroy.as_view(), name='venta-detail'),
]
