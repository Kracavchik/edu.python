import lesson05.home_work.hw05_easy as easy
import os


def chg_folder():
    while True:
        answer_chg = input("Введите путь к папке.\n")
        try:
            os.chdir(answer_chg)
            print("Успешно перешел!")
            break
        except FileNotFoundError:
            print("Невозможно перейти. Введен неверный путь!")
            continue


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


answer = 0
while True:
    answer_list = [1, 2, 3, 4]
    answer = int(input("""Выберите действие:
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку \n"""))

    if answer in answer_list:
        break
    else:
        print("Выберите допустимый вариант")
        continue

if answer == 1:
    chg_folder()
elif answer == 2:
    easy.cwd()
elif answer == 3:
    folder_name = input("Введите имя папки:\n")
    easy.file_create_delete(2, 2, folder_name)
elif answer == 4:
    folder_name = input("Введите имя папки:\n")
    easy.file_create_delete(1, 2, folder_name)
