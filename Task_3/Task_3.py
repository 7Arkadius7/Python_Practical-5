# Создайте программу для игры в ""Крестики-нолики"".

table = list(range(1,10))
end = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]


def board():
    print('- - - - - -')
    for i in range(3):
        print('',table[0 + i*3], '|', table[1 + i*3],'|', table[2 + i*3])
        print('- - - - - -')

def position(player):
    while True:
        value = input(f'Ходят {player} - ')
        if value not in '123456789':
            print('Некорректный выбор. Введите верную позицию:')
            continue
        value = int(value)
        if str(table[value-1])=='Х' or str(table[value-1])=='О':
            print('Позиция занята. Выберите свободную позицию')
            continue
        table[value-1] = player
        break

def check_winner():
    for i in end:
        if table[i[0]-1] == table[i[1]-1] == table[i[2]-1]:
            return table[i[1]-1]
    else:
        return False

def main():
    counter = 0
    while True:
        board()
        if counter%2==0:
            position('Х')
        else:
            position('О')
        if counter > 3:
            winner = check_winner()
            if winner:
                board()
                print('Ура!!! Победили', winner)
                break
        counter+=1
        if counter > 8:
            board()
            print('Победила дружба!!!')
            break

main()