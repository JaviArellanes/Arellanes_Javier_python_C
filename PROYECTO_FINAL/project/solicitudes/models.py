from django.db import models
	
class Solicitudes(models.Model):

    class Meta:
        verbose_name = 'Solicitudes'
        verbose_name_plural = 'Solicitudes'

    titulo = models.CharField("Titulo", max_length=300, default="sin nombrar")
    descripcion = models.CharField("Descripción", max_length=300, default="sin descripción")
    fecha_de_registro = models.DateField("Fecha de registro", max_length=300, default="sin fecha")
    estatus = models.CharField("Estatus", max_length=300, default="sin estatus")

    def _str_(self):
        return self.titulo
