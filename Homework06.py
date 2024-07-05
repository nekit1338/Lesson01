print("\n", "Словари\n")
my_dict = {"Имя": "Артур", "Возраст": 34}
print("Dict:", my_dict)
print("Existing value:", my_dict["Имя"])
print("Existing value:", my_dict.get("Имя"))
print("Non existing value:", my_dict.get("Фамилия", "Такого ключа нет"))
my_dict["Грейд"] = "Синьор"
my_dict.update({"Стаж работы(годы)": 9})
print("Modified dictionary:", my_dict)
a = my_dict.pop("Имя")
print("Deleted value:", a)
print("\n", "Множества\n")
my_set = {1, 2, 3, False, True, "String", 4.5, a, 1, 2, 3}
print("Set:", my_set)
my_set.add("Ford")
my_set.add((1, 2, 3.7))
my_set.discard(False)
print("Modified set:", my_set)