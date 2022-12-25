# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'абв сидели на трубе, а упала б пропала, кто остался на трубе из абв?'


def abv_del(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)


result = abv_del(my_text)
print(result)
