print("Добро пожаловать в наше кафе! ")
amount = float(input("Введите сумму заказа: "))
people = int(input("Введите кол-во человек: "))


total = round(amount * 1.1, 2)
person = round(total / people, 2)


print(f"Итого с обслуживанием: {total}")
print(f"С каждого: {person}")


print("=======================")
print("Спасибо за заполнение анкеты!")


