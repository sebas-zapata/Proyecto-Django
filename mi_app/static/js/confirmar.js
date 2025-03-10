
function confirmarEliminacion(event, clienteId) {
    event.preventDefault(); // Evita la navegación directa

    Swal.fire({
        title: "¿Estás seguro?",
        text: "Deseas eliminar este cliente realmente.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#000000",
        cancelButtonColor: "#616161",
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            // Redirige a la URL de eliminación en Django
            window.location.href = `/eliminar/${clienteId}/`;
        }
    });
}
