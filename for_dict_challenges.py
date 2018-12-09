from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'}
]
# ???
name1 = []
for student1 in students:
    name1.append(student1['first_name'])
for name in sorted(set(name1)):
    print(f'{name}: {name1.count(name)}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???
name2 = []
for student2 in students:
    name2.append(student2['first_name'])
print(f'Самое частое имя среди учеников: {Counter(name2).most_common(1)[0][0]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
name3 = []
school_class = 1
for class3 in school_students:
    for student3 in class3:
        name3.append(student3['first_name'])
    print(f'Самое частое имя в классе {school_class}: {Counter(name3).most_common(1)[0][0]}')
    school_class += 1
    name3 = []
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class4 in school:
    count_male = 0
    count_female = 0
    for student4 in class4['students']:
        if is_male[student4['first_name']]:
            count_male += 1
        else:
            count_female += 1
    class_name = class4['class']
    print(f'В классе {class_name} девочек: {count_female}, мальчиков: {count_male}')

# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
max_male = 0
max_female = 0
max_male_class = ''
max_female_class = ''
for class5 in school:
    count_male5 = 0
    count_female5 = 0
    for student5 in class5['students']:
        if is_male[student5['first_name']]:
            count_male5 += 1
        else:
            count_female5 += 1
    if count_male5 > max_male:
        max_male = count_male5
        max_male_class = class5['class']
    elif count_female5 > max_female:
        max_female = count_male5
        max_female_class = class5['class']
print('Больше всего мальчиков в классе', max_male_class)
print('Больше всего девочек в классе', max_female_class)
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

