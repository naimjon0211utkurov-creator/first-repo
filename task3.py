
print("Добро пожаловать в игру «Угадай число»!")
print("У вас есть 5 попыток, чтобы найти секретное число.")

secret = 37
attempt = 0

while attempt < 5:
    luck = int(input(f"Попытка {attempt + 1}. Введите число: "))
    attempt += 1

    if luck == secret:
        print(f"Поздравляем! Вы угадали число с {attempt}-й попытки!")
        break
    elif luck > secret:
        print("Загаданное число меньше!")
    else:
        print("Загаданное число больше!")

if luck != secret:
    print("Попытки закончились!")
    print(f"Секретное число было: {secret}")

print("=======================")
print("Спасибо за игру!")
