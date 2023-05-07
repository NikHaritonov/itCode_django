from django.http import HttpResponse
from django.shortcuts import render
from .models import Ingredients, Buyer, Potion, Structure
from django.db.models import Avg, Min, Max, Sum

def index(request):
    data = {"header": "Привет Коля", "message": "Твоя тестовая страница"}
    return render(request, "index.html", context=data)

def about(request):
    header = "Данные пользователя"              
    langs = ["Python", "Java", "C#"]            
    user ={"name" : "Игорь", "age" : 20}          
    address = ("Тухвата Янаби", 15, 4)           
  
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "about.html", context=data)
 
def contact(request):
    number_phone = "+79964550505"

    data = {"number_phone": number_phone}
    return render(request, "contact.html", context=data)

def ingredients(request, ingred):
    if ingred:
        elements = Ingredients.objects.all()
        return render(request, "pot_elem.html", {"elements": elements})
    else:
        elements = Potion.objects.all()
        return render(request, "pot_elem.html", {"elements": elements})
    
def buyers_or_structure(request, check):
    if check:
        elements = Buyer.objects.all()
        return render(request, "b_or_s.html", {"elements": elements, "check":check})
    else:
        elements = Structure.objects.all()
        return render(request, "b_or_s.html", {"elements": elements, "check":check})

buyers = Buyer.objects.all()
for buyer in buyers:
    print(buyer.name)

quantity_potions = Potion.objects.aggregate(Sum("quantity"))
print(quantity_potions)

ing_pot = Potion.objects.get(name="Зелье бессмертия").ingredients.all().values_list()
for ing in ing_pot:
    print(ing[1])

ch_pot = Potion.objects.filter(price=50)
for pot in ch_pot:
    print(pot.name)

pr_ing = Ingredients.objects.filter(price__range = (0,20))
for ing in pr_ing:
    print(ing.name)

up_ing = Ingredients.objects.order_by("price")
for ing in up_ing:
    print(f"{ing.name} {ing.price}")

str_id = Structure.objects.values()
print(str_id)

ing_poit_Q = Potion.objects.filter(ingredients__id=68)
for ing in ing_poit_Q:
    print(ing.name)

pot_price_sum = Potion.objects.aggregate(Sum("price"))
print(pot_price_sum)

max_price_ing = Ingredients.objects.aggregate(Max("price"))
print(max_price_ing)


