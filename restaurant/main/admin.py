from django.contrib import admin
from .models import Course, Dish

# Register your models here.
admin.site.register((Course, Dish))
