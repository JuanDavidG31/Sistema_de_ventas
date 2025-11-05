
from rest_framework.response import Response
from rest_framework import status,  viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import (
    UserSerializer, CategoriaSerializer, UsuarioSerializer
)
from .models import Categoria,  Usuario
from rest_framework import generics
from .models import Producto, Cliente, Venta
from .serializers import ProductoSerializer, ClienteSerializer, VentaSerializer

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VentaListCreate(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


# Vista para registrar nuevos usuarios (autenticación)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'Usuario y contraseña requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# CRUD generales
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
