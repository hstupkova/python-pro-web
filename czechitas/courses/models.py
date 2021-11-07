from django.db import models

class Course(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()

class Branch(models.Model):
  city = models.CharField(max_length=100)
  foundation = models.DateField()
  email = models.EmailField()
  employees = models.IntegerField()

class Person(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  email = models.EmailField()
  position = models.CharField(max_length=100)