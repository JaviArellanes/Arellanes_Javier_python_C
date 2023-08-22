from django.db import models

class Productos(models.Model):

    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'

    nombre = models.CharField("Nombre", max_length=300, default="sin nombrar")
    descripcion = models.CharField("Descripción", max_length=300, default="sin descripción")
    precio = models.DecimalField("Precio", decimal_places=2, max_digits=12)
    fecha_de_registro = models.DateField("Fecha de registro", max_length=300, default="sin fecha")
    estatus = models.CharField("Estatus", max_length=300, default="sin estatus")

    def str(self):
        return self.nombre