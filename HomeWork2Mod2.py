# Сравнение числе при вводе
My_age = 55
print("Введите Ваш возраст: ")
Your_age = int(input())
if My_age == Your_age:
    print("Ровесники!))")

# Различные варианты условий
a, b = 2, 15
if a > b:
    print ("a > b")
if 3 < b < 16:
    print ("b в указанном диапазоне")
if (a > b) or (a == 2):
    print("a равно двум")

# сравнение строк
if("2024" > "12"):
    print("ОК")
if("35" > "41"):
    print("ОК")
if([5,6] > [5,5]):
    print("Все правильно")

# сравниваем
if "Я" != 55:
    print("Можно 55")
# нельзя сравнивать!
if [1, 2] < 2:
    print("Можно 2")
if "9" == 9:
    print("Можно 9")
