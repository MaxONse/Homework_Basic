my_health = 100
my_armor = 100
spider_health = 50
spider_armor = 75
another_spider_health = 125
another_spider_armor = 30
knife = 50
shield = 30
print("Вы прилетели на планету тилимилитрямдию и попали в яму с 4 путями, куда пойдете,")
way1 = input("Right or Left or Straight Or Back")
if way1 == "Right":
    new_health = my_health+spider_health
    new_armor = my_armor+spider_armor
    print("Вы завалили паука", new_health, " ХП теперь у тебя", new_armor, "армора теперь у тебя")
elif way1 == "Left":
    print("GAME OVER")
elif way1 == "Straight":
    new_health_knife = my_health+knife
    print("Вы нашли нож", new_health_knife, " ХП теперь у тебя")
else:
    new_health_armor = my_armor+shield
    print("Вы нашли щит", new_health_armor,"армора теперь у тебя")

print("Next step: Right or Left or Straight Or Back")
way2 = input("Right or Left or Straight Or Back")
if way2 == "Left":
    new_new_health = my_health+spider_health
    new_new_armor = my_armor+spider_armor
    print("Вы завалили паука", new_new_health, " ХП теперь у тебя", new_new_armor, "армора теперь у тебя")
elif way2 == "Right":
    print("GAME OVER")
elif way2 == "Back":
    new_new_health_knife = my_health+knife
    print("Вы нашли нож", new_new_health_knife, " ХП теперь у тебя")
else:
    new_new_health_armor = my_armor+shield
    print("Вы нашли щит", new_new_health_armor,"армора теперь у тебя")