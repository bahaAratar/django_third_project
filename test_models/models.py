import uuid
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products') # если удать 1 категорию то удалятся все продукты с этой категорией
    # category = models.ForeignKey('Category', on_delete=models.RESTRICT, related_name='products') # нельзя удалить категорию пока есть продукт с этой категорией
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='products') # если удать категорию то продукты останутся с категорией None

    def __str__(self) -> str:
        return f'{self.title} --- {self.category}'

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.title

class Passport(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.TextField()

class Person(models.Model):
    name = models.CharField(max_length=50)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE, related_name='person')


class Student(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email

class Teacher(models.Model):
    email = models.EmailField()
    student = models.ManyToManyField(Student)

    def __str__(self) -> str:
        return self.email