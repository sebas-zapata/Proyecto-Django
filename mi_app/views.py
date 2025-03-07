from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
            messages.success(request, "Cliente agregado correctamente.")  # Mensaje de éxito
            return redirect('lista_clientes')  # Redirige a la página de clientes
    else:
        form = ClienteForm()
    
    return render(request, 'formulario.html', {'form': form})

# Vista para mostrar los clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    return render(request, 'clientes.html', {'clientes': clientes})


# Vista para editar Clientes
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)  # Obtener el cliente por ID
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)  # Cargar datos en el formulario
        if form.is_valid():
            form.save()  # Guardar cambios
            messages.success(request, "Cliente actualizado correctamente.")  # Mensaje de éxito
            return redirect('lista_clientes')  # Redirigir a la lista de clientes
    else:
        form = ClienteForm(instance=cliente)  # Cargar formulario con datos existentes
    return render(request, 'editar_clientes.html', {'form': form, 'cliente': cliente})


# Vista para eliminar clientes
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)  # Buscar el cliente por ID
    cliente.delete()  # Eliminar el cliente
    messages.success(request, "Cliente eliminado correctamente.")  # Mensaje de éxito
    return redirect('lista_clientes')  # Redirigir a la lista de clientes
