from django.db import models


class Ciudades(models.Model):
    nombre = models.CharField(max_length=255)


class Categorias(models.Model):
    descripcion = models.CharField(max_length=255)


class Guias(models.Model):
    nombre = models.CharField(max_length=255)
    frase = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    telefono = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    id_categorias = models.ManyToManyField(Categorias)


class Tours(models.Model):
    id_guia = models.ForeignKey(Guias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    precio = models.FloatField(max_length=255)
    url_imagen_mapa = models.CharField(max_length=500)
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
