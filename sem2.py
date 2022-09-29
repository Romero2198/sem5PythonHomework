import random
# Вариант с 2 игроками:
# candy_count = 2021
# gamer_1 = input('Введите имя первого игрока: ')
# gamer_2 = input('Введите имя второго игрока: ')
# current_gamer = gamer_1
# while candy_count > 0:
#     print(f'Количество оставшихся конфет: {candy_count}')
#     while True:
#         number_to_delete = int(input(f'Ход игрока {current_gamer} 1 - 28: '))
#         if (number_to_delete >= 1) and (number_to_delete <= 28):
#             break
#     candy_count -= number_to_delete
#     current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
# print(f'Победил {current_gamer}')

#Вариант с обычным ботом:
candy_count = 2021
gamer_1 = 'Игрок'
gamer_2 = 'Бот'
current_gamer = random.choice([gamer_1, gamer_2])
print(f'Первым ходит {current_gamer}')
while candy_count > 0:
    print(f'Количество оставшихся конфет: {candy_count}')
    if current_gamer == gamer_1:
        number_to_delete = int(input('Ход игрока 1 - 28: '))
        if (number_to_delete >= 1) and (number_to_delete <= 28):
            candy_count -= number_to_delete
            if candy_count <= 0:
                print(f'Победил {current_gamer}')
            current_gamer = gamer_2
    elif current_gamer == gamer_2:
        number_to_delete = random.randint(1, 28)
        print(f'Ход бота 1 - 28: {number_to_delete}')
        candy_count -= number_to_delete
        if candy_count <= 0:
            print(f'Победил {current_gamer}')
        current_gamer = gamer_1