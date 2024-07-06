grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


students_list = list(students)  # Set -> List
students_list.sort(key=lambda x: x[0])  # Сортировка списка студентов по первому символу (в алфавитном порядке)


average_grades = []  # Новый список для средних баллов
for i in grades:
    average = sum(i)/len(i)
    average_grades.append(average)  # Заполнение списка результатами расчета average


average_grades_round = []  # Новый список с 2 знакам после запятой
for j in average_grades:
    average_grades_round.append(round(j, 2))
students_dict = dict(zip(students_list, average_grades_round))
print(students_dict)
