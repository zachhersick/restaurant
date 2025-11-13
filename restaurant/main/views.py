from django.shortcuts import render
from .models import Course, Dish

# Create your views here.
def home(request):
    return render('', 'index.html')

def menu(request):
    dish_list = Dish.objects.order_by('id')
    course_list = Course.objects.order_by('id')
    context = {
        'dishes' : dish_list,
        'courses' : course_list,
    }
    return render(request, 'menu.html', context)

def aboutpage(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')