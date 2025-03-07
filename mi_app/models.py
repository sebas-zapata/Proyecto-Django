from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Evita que Django haga migraciones en esta tabla
        db_table = "clientes"  # Nombre exacto de la tabla en MySQL
