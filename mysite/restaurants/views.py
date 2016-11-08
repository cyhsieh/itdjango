#coding:utf-8
from django.shortcuts import render, render_to_response
from restaurants.models import Restaurant, Food

# Create your views here.
def menu(request):
    food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
    food2={'name':'蒜尼白肉','price':100,'comment':'人氣推薦','is_spicy':True}
    # food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':false}
    foods=[food1,food2]

    restaurants = Restaurant.objects.all()

    return render_to_response('menu.html',locals())