print("Добро пожаловать в игру 'Викторина ")

gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input("Какого вы пола? муж/жен\n"),
         'pet_name': input("Как зовут вашего питомца?\n"),
         'gamer_or_not': bool(input("Вы любите играть? да/нет\n"))
         }

if gamer['gamer_or_not'] == "да":
    gamer['gamer_or_not'] = True
else:
    gamer['gamer_or_not'] = False


if gamer['age'] < 18:
    if gamer['name'] == 'Вася':
        print(gamer['name'], 'тубу нельзя играть, потому что ты Вася и молодой')
    else:
        print('Тебе нельзя играть')
elif gamer['name'] == 'Петя':
    print('Ты плохой')
elif gamer['age'] > 90:
    answer = input("Эта игра может быть очень утомительной для вас, вы уверены? да/нет\n")
    if answer == "да":
        answer = input("Вы точно уверены? да/нет\n")
        if answer == "да":
            print('Хорошо, тогда добро пожаловать в Игру')
    else:
        print("До свидания", gamer['name'], "!")
else:
    if gamer['age'] > 18 & gamer['age'] < 90:
        print("Здравствуй", gamer['name'], "!")
        print("Я могу назвать буквы алфавита, которых нет в твоем имени и произнести их.")
        name_list = list(str.lower(gamer['name']))
        alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        different_list = list(set(alphabet) - set(name_list))

        for i in different_list:
            print(i)
