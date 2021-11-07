from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
    verbose_name_plural = "Categories"

  def __str__(self) -> str:
    return self.name

class Branch(models.Model):
  city = models.CharField(max_length=100)
  foundation = models.DateField()
  email = models.EmailField()
  employees = models.IntegerField()

  class Meta:
    verbose_name_plural = "Branches"

  def __str__(self) -> str:
    return self.city

  def courses(self):
    return Course.objects.filter(branch=self)

class Person(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  email = models.EmailField()
  position = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.surname

class Course(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateTimeField()
  end = models.DateTimeField()
  description = models.CharField(max_length=1000)
  price = models.IntegerField()
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
  branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self) -> str:
    return self.name

class Application(models.Model):
  email = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  motivation = models.TextField()
  course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)