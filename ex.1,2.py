
a=int(input("Найдём периметр квадрата,введите одну из сторон: "))

while True:
    try:
        if a <=0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError
P = 4*a
print(f'\nВаш периметр: {P}')

a1=int(input("\nТеперь найдём площадь квадрата\n\nВведите значение а: "))
b=int(input("\nВведите значение b: "))

while True:
    try:
        if a1 <= 0 :
            print("Введите число больше нуля")
            exit()
        elif b <= 0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError
S = a1*b
print(f'\nВаша площадь: {S}')