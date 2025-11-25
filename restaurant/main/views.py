from django.shortcuts import render
from .models import Course, Dish

# Create your views here.
def home(request):
    return render('', 'index.html')

def menu(request):
    dish_list = (Dish.objects
                .values('course__name_en', 'name_en', 'price', 'ingredients_en')
                .order_by('course__name_en', 'name_en')
            )
    context = {'dishes' : dish_list}
    return render(request, 'menu.html', context)

def aboutpage(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')