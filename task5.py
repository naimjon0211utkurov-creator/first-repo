
print("Добро пожаловать в систему результатов контрольной!")

results = [("Али", 5), ("Мадина", 3), ("Тимур", 4), ("Сабина", 2),
           ("Дилшод", 5), ("Камила", 4), ("Бекзод", 2), ("Нигора", 5)]

total = 0
fives = []
retake = 0
grades = set()
grade_count = {}

for name, grade in results:
    total += grade
    grades.add(grade)

    if grade == 5:
        fives.append(name)

    if grade == 2:
        retake += 1

    if grade in grade_count:
        grade_count[grade] += 1
    else:
        grade_count[grade] = 1

average = round(total / len(results), 2)

print("=======================")
print(f"Средний балл группы: {average}")
print(f"Ученики с оценкой 5: {fives}")
print(f"Количество учеников на пересдачу: {retake}")
print(f"Все разные оценки: {grades}")
print(f"Количество каждой оценки: {grade_count}")

print("=======================")
print("Результаты успешно обработаны!")
