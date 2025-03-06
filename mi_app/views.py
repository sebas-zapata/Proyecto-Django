from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Vista para el inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista para el formulario
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redirige a la página de clientes
    else:
        form = ClienteForm()
    
    return render(request, 'formulario.html', {'form': form})

# Vista para mostrar los clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    return render(request, 'clientes.html', {'clientes': clientes})
