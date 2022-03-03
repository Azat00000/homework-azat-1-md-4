name = "Азат"
print(name)

age = 19
info_about_me = "Меня зовут " + name + ", мне " + str(age) + " лет!"
print(info_about_me)

print("Азат " * 5)
print("Азат " + "Азат " + "Азат " + "Азат " + "Азат ")

name2 = input("Привет, как звать?")
age2 = input("Сколько тебя юных годиков?")

if int(age2) > 100:
     print("тебе точно не больше 100")
elif int(age2) < 0:
     print("Введи возраст пореалистичней")
else:
     print(" ")

print("Привет ещё раз " + name2 + ", тебе " + age2 + " годиков)")


if int(age2) < 30:
     print("В " + str(age2) + ", особо не гуляй без взрослых:)")
elif int(age2) > 30:
     print("Ого, тебе " + str(age2) + ", как суставы, не болят?")
elif int(age2) >100:
     print('тебе не больше 100')
else:
     print(" ")

print(" ")
name_change=name2[2::]
name_change2=name2[:-1]
name_change3=name2[3:]
print(name_change + ", это твое имея без 2ух первых букв :)\n" + name_change2 +
       ", а это задом наперёд\n" + name_change3 + ", это последние 3 буквы твоего имени\n")

name_simvol = name2
print("В твоём имени " + str(len(name_simvol)) + " символов")


print("Хочешь фокус? Введи-ка свой возраст ещё раз:")
age_summa=int(input())
a = age_summa//10
b = age_summa - a * 10
c = a+b
print(str(c) + ", это сумма символов в твоём имени")
d = a*b
print(str(d) + ", а это произведение")
print(" ")


print("Твоё имя в верхнем регистре: ", name2.upper())
print("Твоё имя в нижнем регистре:", name2.lower())


task = int(input("Реши-ка задачку: 3+3*3="))
if task <= 11:
     print("Неверно\nПрвильный ответ: 12")
elif task >=13:
     print("Неверно\nПрвильный ответ: 12")
else:
    print("Ниче се, с первого раза)")




