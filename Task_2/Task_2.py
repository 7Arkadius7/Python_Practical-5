# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота


from random import *

print('*'*100)

win ='Поздравляю!'
import random

random_index = random.randrange(len(win))


def player_vs_bot():
    candies = 100
    take_max = 28
    
    player1 = input('Имя игрока: ')
    player2 = input('Имя игрока(Если хотите играть с компьютером, то напишите имя "Аdroid"): ')
    players = [player1,player2]

    luc = randint(-1, 0)
    print(f'Наши поздравления {players [luc+1]} ты ходишь первым !') 

    while candies > 0:
        luc += 1
        if players [luc%2] == 'Android':
            print(f'\nХодит {players [luc%2]}\nОсталось {candies}.конфет: ')

            if candies > 0:
                step = candies
            
            while step > take_max:
                step = randint(1,28)
            print(step)

        else:
            step = int(input(f'\nХодит,  {players [luc%2]} \nОсталось {candies} конфет: '))
            while step > take_max or step > candies:
                step = int (input(f'\nМожно взять только {take_max} конфет , играй по правилам: '))
        candies = candies - step

    print(f'Осталось {candies} конфет.')
    print(f'{win} Победитель {players [luc%2]} ')

player_vs_bot()


# b) Подумайте как наделить бота ""интеллектом""
