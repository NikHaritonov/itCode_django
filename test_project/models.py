from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()


class Buyer(models.Model):
    name = models.CharField(max_length=15)
    wallet = models.FloatField()


class Potion(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredients, through="Structure")
    property_potion = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.FloatField()


class Structure(models.Model):
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    potion = models.ForeignKey(Potion, on_delete=models.CASCADE)
    countOfIngredient = models.IntegerField()

'''Ingredients.objects.all().delete()
Buyer.objects.all().delete()
Potion.objects.all().delete()
Structure.objects.all().delete()'''
'''
mandrake_root = Ingredients.objects.create(name="Корень Мандрагоры", quantity=10, price=20)
chamomile = Ingredients.objects.create(name="Ромашка", quantity=25, price=5)
bluegill = Ingredients.objects.create(name="Синежелчник", quantity=12, price=30)
dragon_tongue = Ingredients.objects.create(name="Драконий язык", quantity=3, price=150)
red_tenecvet = Ingredients.objects.create(name="Красный тенецвет", quantity=30, price=3)
blue_tenecvet = Ingredients.objects.create(name="Голубой тенецвет", quantity=30, price=3)
yellow_tenecvet = Ingredients.objects.create(name="Желтый тенецвет", quantity=30, price=3)
bronze_root = Ingredients.objects.create(name="Бронзовый корень", quantity=12, price=7)
latenna = Ingredients.objects.create(name="Латенна", quantity=14, price=6)

igor = Buyer.objects.create(name="Игорь", wallet=320)
ragnar = Buyer.objects.create(name="Рагнар", wallet=150)
poocker = Buyer.objects.create(name="Пукер", wallet=400)
zlata = Buyer.objects.create(name="Злата", wallet=1000)
artur = Buyer.objects.create(name="Артур", wallet=550)
ciceron = Buyer.objects.create(name="Цицерон", wallet=1)
my_shop = Buyer.objects.create(name="Магазин", wallet=100000)


immortality_potion = Potion.objects.create(name="Зелье бессмертия", property_potion="Временная неуязвимось на 30 секунд",  quantity=5, price = 500)
health_potion = Potion.objects.create(name="Зелье здоровья", property_potion="+30% hp",  quantity=5, price = 50)
mana_potion = Potion.objects.create(name="Зелье маны", property_potion="+30% mp",  quantity=5, price = 50)
stamina_potion = Potion.objects.create(name="Зелье выносливости", property_potion="+30% sp",  quantity=5, price = 50)
invisibility_potion = Potion.objects.create(name="Зелье невидимости", property_potion="Невидимость на 30 секунд",  quantity=10, price = 300)
transformation_potion = Potion.objects.create(name="Зелье превращения в волка", property_potion="Превращает в волка на 10 мин.",  quantity=15, price = 150)

dt_ip = Structure(potion = immortality_potion, ingredients = dragon_tongue, countOfIngredient = 1)
dt_ip.save()
mr_ip = Structure(potion = immortality_potion, ingredients = mandrake_root, countOfIngredient = 2)
mr_ip.save()
l_ip = Structure(potion = immortality_potion, ingredients = latenna, countOfIngredient = 2)
l_ip.save()
rt_hp = Structure(potion = health_potion, ingredients = red_tenecvet, countOfIngredient = 1)
rt_hp.save()
ch_hp = Structure(potion = health_potion, ingredients = chamomile, countOfIngredient = 1)
ch_hp.save()
bt_mp = Structure(potion = mana_potion, ingredients = blue_tenecvet, countOfIngredient = 1)
bt_mp.save()
ch_mp = Structure(potion = mana_potion, ingredients = chamomile, countOfIngredient = 1)
ch_mp.save()
ch_sp = Structure(potion = stamina_potion, ingredients = chamomile, countOfIngredient = 1)
ch_sp.save()
yt_sp = Structure(potion = stamina_potion, ingredients = yellow_tenecvet, countOfIngredient = 1)
yt_sp.save()
blue_inp = Structure(potion = invisibility_potion, ingredients = bluegill, countOfIngredient = 2)
blue_inp.save()
dt_inp = Structure(potion = invisibility_potion, ingredients = dragon_tongue, countOfIngredient = 1)
dt_inp.save()
dt_trp = Structure(potion = transformation_potion, ingredients = dragon_tongue, countOfIngredient = 1)
dt_trp.save()
br_trp = Structure(potion = transformation_potion, ingredients = bronze_root, countOfIngredient = 2)
br_trp.save()
mr_trp = Structure(potion = transformation_potion, ingredients = mandrake_root, countOfIngredient = 1)
mr_trp.save()'''
