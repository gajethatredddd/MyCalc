a = int(input("Введите двузначное число: "))
if  10 <= a  <=99 :
    left = a // 10
    right = a % 10
    s = left + right
    p = left * right
    print(f'Сумма: {s}\nПроизведение: {p}')
else:
    print("Ошибка , введите двузначное число")