array = []

n = int(input("Сколько чисел будет в массиве?"))

if n < 3:
    print("Вы ввели слишком маленькое количество.")
    exit()

for i in range(n):
    array.append(int(input("Введите число в массив")))

for i in array:
    if i < 1:
        print("Неподходящее число в массиве!")
        exit()

array.sort(reverse=True)

print(array)

flag = 0

for i in range (len(array) - 2):

    El1 = array[i]
    El2 = array[i+1]
    El3 = array[i+2]

    if El1 < El2 + El3 :

        p = (El1 + El2 + El3)*0.5
        s = (p*(p - El1)*(p - El2)*(p - El3))**0.5
        break
    else:
        flag = 1

if flag == 1:
    print("Из данных чисел нельзя составить треугольник")
    exit()

print("Стороны треугольника" , El1 , El2 , El3)
print("Площадь = " , s)