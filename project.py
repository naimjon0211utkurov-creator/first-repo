
print("Добро пожаловать в электронный журнал!")

journal = {
    "Али": [5, 4, 5],
    "Мадина": [3, 4],
    "Тимур": [2, 3, 3]
}


def average(grades):
    return round(sum(grades) / len(grades), 2)


while True:
    print("\n===== ЖУРНАЛ ОЦЕНОК =====")
    print("1 — Показать всех учеников")
    print("2 — Добавить ученика")
    print("3 — Поставить оценку")
    print("4 — Средний балл ученика")
    print("5 — Лучший ученик")
    print("6 — Список отстающих")
    print("7 — Удалить ученика")
    print("8 — Статистика группы")
    print("9 — Рейтинг учеников")
    print("10 — График оценок")
    print("0 — Выход")

    choice = input("\nВыберите пункт меню: ")

    # 1. Показать всех учеников
    if choice == "1":
        if not journal:
            print("Учеников пока нет.")
        else:
            print("\nСписок учеников:")
            for name, grades in journal.items():
                print(f"{name}: {grades}")

    # 2. Добавить ученика
    elif choice == "2":
        name = input("Введите имя ученика: ")

        if name in journal:
            print("Такой ученик уже существует!")
        else:
            journal[name] = []
            print(f"Ученик {name} успешно добавлен!")

    # 3. Поставить оценку
    elif choice == "3":
        name = input("Имя ученика: ")

        if name not in journal:
            print("Такого ученика нет!")
        else:
            grade = input("Оценка (1-5): ")

            if grade in ["1", "2", "3", "4", "5"]:
                journal[name].append(int(grade))
                print("Оценка успешно добавлена!")
                print(f"{name}: {journal[name]}")
            else:
                print("Неверная оценка!")

    # 4. Средний балл ученика
    elif choice == "4":
        name = input("Имя ученика: ")

        if name not in journal:
            print("Такого ученика нет!")
        elif not journal[name]:
            print("У этого ученика пока нет оценок.")
        else:
            result = average(journal[name])
            print(f"Средний балл {name}: {result}")

    # 5. Лучший ученик
    elif choice == "5":
        best_name = ""
        best_average = -1

        for name, grades in journal.items():
            if not grades:
                continue

            result = average(grades)

            if result > best_average:
                best_average = result
                best_name = name

        if best_name == "":
            print("Пока нет учеников с оценками.")
        else:
            print(f"Лучший ученик: {best_name}")
            print(f"Средний балл: {best_average}")

    # 6. Список отстающих
    elif choice == "6":
        print("\nОтстающие (средний балл ниже 3.5):")

        found = False

        for name, grades in journal.items():
            if not grades:
                continue

            result = average(grades)

            if result < 3.5:
                print(f"{name} — {result}")
                found = True

        if not found:
            print("Отстающих нет!")

    # 7. Удалить ученика
    elif choice == "7":
        name = input("Введите имя ученика для удаления: ")

        if name in journal:
            del journal[name]
            print(f"Ученик {name} удалён!")
        else:
            print("Такого ученика нет!")

    # 8. Статистика группы
    elif choice == "8":
        if not journal:
            print("Журнал пустой!")
        else:
            total_grades = 0
            total_sum = 0
            all_grades = set()
            bad_students = set()

            for name, grades in journal.items():
                total_grades += len(grades)
                total_sum += sum(grades)

                for grade in grades:
                    all_grades.add(grade)

                if 2 in grades:
                    bad_students.add(name)

            print("\n===== СТАТИСТИКА ГРУППЫ =====")
            print(f"Учеников: {len(journal)}")
            print(f"Всего оценок: {total_grades}")

            if total_grades > 0:
                result = round(total_sum / total_grades, 2)
                print(f"Общий средний балл: {result}")
            else:
                print("Общий средний балл: нет оценок")

            print(f"Встречаются оценки: {all_grades}")
            print(f"Ученики с двойками: {bad_students}")

    # 9. Рейтинг учеников
    elif choice == "9":
        rating = []

        for name, grades in journal.items():
            if not grades:
                continue

            result = average(grades)
            rating.append((result, name))

        rating.sort(reverse=True)

        if not rating:
            print("Нет учеников с оценками.")
        else:
            print("\n===== РЕЙТИНГ УЧЕНИКОВ =====")

            for i, (result, name) in enumerate(rating, start=1):
                print(f"{i}. {name} — {result}")

    # 10. График оценок
    elif choice == "10":
        grade_count = {}

        for grades in journal.values():
            for grade in grades:
                if grade in grade_count:
                    grade_count[grade] += 1
                else:
                    grade_count[grade] = 1

        print("\n===== ГРАФИК ОЦЕНОК =====")

        for grade in range(5, 0, -1):
            count = grade_count.get(grade, 0)
            stars = "*" * count
            print(f"{grade}: {stars}")

    # 0. Выход
    elif choice == "0":
        print("До свидания!")
        break

    # Неверный пункт меню
    else:
        print("Нет такого пункта меню!")
