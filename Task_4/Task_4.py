# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


with open('File1.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст который нужно сжать: '))
with open('File1.txt', 'r') as file:
    text = file.readline()
    rle_text = text.split()

print(text)

def encoding(text):
    encod = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                encod += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encod += str(count) + prev_char
        return encod


rle_text = encoding(text)

with open('File2.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{rle_text}')
print(rle_text)


