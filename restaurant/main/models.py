from django.db import models

# Create your models here.
class Course(models.Model):
    """ A class to describe a section of the meal"""
    name_it = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    
    def __str__(self):
        """ String representation of an instance """
        return self.name_it
    
class Dish(models.Model):
    """  """
    name_it = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    price = models.FloatField(max_length=100, default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ingredients_it = models.CharField(max_length=90, default='')
    ingredients_en = models.CharField(max_length=90, default='')

    def __str__(self):
        """ String representation of an instance """
        return self.name_it
