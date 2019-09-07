#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random


def generate_cards():
    global card_player
    global card_machine
    card_player = random.sample(range(90), 15)
    card_machine = random.sample(range(90), 15)
    row_a = sorted(card_player[:5] + [" "] * 4, key=lambda x: random.random())
    row_b = sorted(card_player[5:10] + [" "] * 4, key=lambda x: random.random())
    row_c = sorted(card_player[10:] + [" "] * 4, key=lambda x: random.random())
    row_m_a = sorted(card_machine[:5] + [" "] * 4, key=lambda x: random.random())
    row_m_b = sorted(card_machine[5:10] + [" "] * 4, key=lambda x: random.random())
    row_m_c = sorted(card_machine[10:] + [" "] * 4, key=lambda x: random.random())
    card_player = row_a + row_b + row_c
    card_machine = row_m_a + row_m_b + row_m_c


def print_cards(card_player, card_machine):
    print("Карточка игрока")
    print("--------------------------")
    print(*card_player[:9])
    print(*card_player[9:18])
    print(*card_player[18:])
    print("--------------------------")
    print()
    print("Карточка компьютера")
    print("--------------------------")
    print(*card_machine[:9])
    print(*card_machine[9:18])
    print(*card_machine[18:])
    print("--------------------------")


def new_barrel(val):
   while len(val) > 0:
       x = random.choice(val)
       y = x
       val.remove(x)
       yield y


def barrel_choice(current_barrel):
    global endgame
    global player_counter
    global machine_counter
    print(f"Бочонок номер {current_barrel}")
    print("Зачеркнуть текущую цифру? Да / Нет / Выход")
    mode = input()
    if mode == 'Да':
        if card_player.count(current_barrel) > 0:
            print(f"Бинго! Цифра {current_barrel} есть в карточке игрока!")
            card_player.insert(card_player.index(current_barrel), "-")
            card_player.remove(current_barrel)
            player_counter += 1
        else:
            print(f"Вы ошиблись. Цифры {current_barrel} нет в карточке игрока!")
            endgame = False
    elif mode == 'Нет':
        if card_player.count(current_barrel) > 0:
            print(f"Вы ошиблись. Цифра {current_barrel} есть в карточке игрока!")
            endgame = False
    if card_machine.count(current_barrel) > 0:
        card_machine.insert(card_machine.index(current_barrel), "-")
        card_machine.remove(current_barrel)
        machine_counter += 1


generate_cards()
barrel_bag = [i for i in range(91)]
barrel_iter = new_barrel(barrel_bag)
print("== Лото ==")
print("Добро пожаловать в Игру!")
endgame = True
player_counter = 0
machine_counter = 0

while machine_counter < 15 and player_counter < 15 and endgame == True:
    print_cards(card_player, card_machine)
    barrel_choice(next(barrel_iter))
    print("\n" * 10)
    if len(barrel_bag) == 0:
        break

if machine_counter == 15 and player_counter == 15:
    print("Ничья!")
elif machine_counter == 15:
    print("Выйграл Компьютер!")
elif player_counter == 15:
    print("Вы победили!!!")
else:
    print("Вы проиграли")
