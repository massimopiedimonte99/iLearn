from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Author(models.Model):
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    
    class Meta:
        unique_together=['name', 'surname']

    def get_absolute_url(self):
        return reverse('books:index')

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default='')
    title=models.CharField(max_length=255, unique=True)
    isbn=models.CharField(max_length=13, unique=True)
    cover_image=models.FileField()

    def get_absolute_url(self):
        return reverse('books:detail', kwargs = {'pk':self.id})

    def __str__(self):
        return self.title
