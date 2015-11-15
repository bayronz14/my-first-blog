from django.db import models
from django.utils import timezone

class Post(models.Model):
        autor = models.ForeignKey('auth.User')
        titulo = models.CharField(max_length=200)
        #foto= models.ImageField(upload_to='photos')
        descripcion = models.TextField()
        precio= models.DecimalField(max_digits=6, decimal_places=2, default=0)
        fecha_creacion = models.DateTimeField(
                default=timezone.now)
        fecha_publicacion = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.fecha_publicacion = timezone.now()
            self.save()

        def __str__(self):
            return self.titulo
