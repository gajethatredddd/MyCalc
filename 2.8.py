a = int(input("Введите двузначное число: "))

if  10 <= a  <=99 :
    left = a // 10
    right = a % 10
    perevertish = right * 10 + left
    print(f'Ваше перевёрнутое число: {perevertish}')
else:
    print("Ошибка , введите двузначное число")