print("Кортежи\n\n")
immutable_var = ("String", 5, True, [1, 2, 3])
print(immutable_var)
# immutable_var[0] = 123  # Нельзя поменять и удалить элемент в тапле
print("Добавление другого кортежа (1, 2, 3)")
immutable_var = immutable_var + (1, 2, 3)  # Добавление другого кортежа
print(immutable_var)
print("Можно редактировать изменяемые элементы тапла(листы, словари)")
immutable_var[3].insert(2, False)  # Можно редактировать изменяемые элементы тапла(листы, словари)
print(immutable_var)
print("Очистка внутренного содержимого вложенного листа")
immutable_var[3].clear()  # Очистка внутренного содержимого вложенного листа
print(f"{immutable_var}\n\n")

print(f"Списки\n\n")

mutable_list = ["String", 5, True, [1, 2, 3]]
print(mutable_list)
print("Замена 1 элемента String на 1")
mutable_list[0] = 1  # Замена 1 элемента на 1
print(mutable_list)
print("Добавление элемента в конец списка")
mutable_list.append("5 element")  # Добавление элемента в конец списка
print(mutable_list)
print("Добавление элемента во вложенный список")
mutable_list[3].append(4)  # Добавление элемента во вложенный список
print(mutable_list)
print("Поменять элементы в обратном порядке")
mutable_list.reverse()  # Поменять элементы в обратном порядке
print(mutable_list)
print("Реверс вложенного списка")
mutable_list[1].reverse()
print(mutable_list)
print("Очистка списка")
mutable_list.clear()  # Очистка списка
print(mutable_list)