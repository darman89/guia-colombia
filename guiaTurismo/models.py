import os
import uuid

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


def user_directory_filepath(_, filename):
    _, extension = os.path.splitext(filename)
    filename = str(uuid.uuid4()) + extension
    return 'uploads/{0}'.format(filename)


class Guide(models.Model):
    name = models.CharField(max_length=255)
    phrase = models.CharField(max_length=255)
    photo = models.ImageField(max_length=255, upload_to=user_directory_filepath, default='')
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Tour(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)
    url_map_image = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
