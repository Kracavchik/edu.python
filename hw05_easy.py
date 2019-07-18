import os
import sys
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def file_create_delete(default=0, count=10, name='dir_'):
    dir_name = name
    answer = default
    while answer == 0:
        answer = int(input("""Выберите действие:
                    1 - Создать директории
                    2 - удалить директории 
                    3 - выход \n"""
                           ))
        if answer == 1 or 2 or 3:
            break
        else:
            print('Введите допустимое значение')
            continue
    try:
        if answer == 1:
            for i in range(1, count):
                if name == 'dir_':
                    os.makedirs(dir_name + (str(i)))
                else:
                    os.makedirs(dir_name)
            print("Успешно создано!")
        elif answer == 2:
            for i in range(1, count):
                if name == 'dir_':
                    os.rmdir(dir_name + (str(i)))
                else:
                    os.rmdir(dir_name)
            print("Успешно удалено!")
        elif answer == 3:
            sys.exit(0)
    except FileNotFoundError:
        print("Невозможно удалить. Файлы еще не созданы!")
    except Exception:
        print("Невозможно создать!")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def cwd():
    print(os.listdir())


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def file_copy():
    file_name = sys.argv[0]
    file_name_new = file_name[:file_name.rfind('.')] + '(copy)' + file_name[file_name.rfind('.'):]
    shutil.copy(file_name, file_name_new)


if __name__ == '__main__':
    file_create_delete()
    cwd()
    file_copy()
