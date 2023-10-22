import math
#0_Перше_знайомство

print("Hello, world!")

PI = 3.14
print("PI =",PI)

#1_Створення_калькулятора

first_number = int(input('Введіть перше число: ')) ;
second_number = int(input('Введіть друге число: ')) ;
print("Сума чисел: ", first_number + second_number)

first_number = int(input('Введіть перше число: ')) ;
second_number = int(input('Введіть друге число: ')) ;
print("Сума чисел: ", first_number + second_number)
print("Різниця чисел: ", first_number - second_number)
print("Добуток чисел: ", first_number * second_number)
print("Частка чисел: ", first_number / second_number)

distMiles = 305.3 / 1.60934
print(round(distMiles, 1))

#2_Ще_трохи_математики

S = float(input('Введіть площу кола: '))
r = math.sqrt(S/math.pi)
print('Радіус дорівнює %6.3f см' %r)

r = float(input('Введіть радіус сфери: '))
S = 4*math.pi*r**2
V = (4/3)*math.pi*r**3
print('Площа дорівнює %6.3f см^2' %S)
print("Об'єм дорівнює %6.3f см^3" %V)

temp = float(input('Введіть температуру за Фаренгейтом: '))
print("Температура за Цельсієм:", round((temp-32)*0.5556, 1))

temp = float(input('Введіть температуру за Цельсієм: '))
print("Температура за Фаренгейтом:", round(temp*1.8+32, 1))

