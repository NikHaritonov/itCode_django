from django.http import HttpResponse
from django.shortcuts import render
 
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