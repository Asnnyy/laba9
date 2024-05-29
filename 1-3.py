import os
from PIL import Image
from PIL import ImageFilter
import csv
def z1():
    k = "kartinki"
    k2 = "kartinki2"
    if not os.path.exists(k2):
        os.mkdir(k2)
    for i in os.listdir(k):
        photo = os.path.join(k, i)
        im = Image.open(photo)
        im = im.filter(ImageFilter.SHARPEN)
        im.save(f'kartinki2/{i}')
z1()
def z2():
    k = "kartinki"
    k2 = "kartinki2"
    if not os.path.exists(k2):
        os.mkdir(k2)
    for i in os.listdir(k):
        if i.endswith("png") or i.endswith("jpg"):
            photo = os.path.join(k, i)
            im = Image.open(photo)
            im = im.filter(ImageFilter.BLUR)
            im.save(f'kartinki2/{i}')
z2()
def z3():
    with open('data.csv', encoding='utf-16') as f:
        f = csv.reader(f)
        itog = 0
        print('Наши покупки:')
        for i in f:
            print(f'{i[0]} - {i[1]} шт. за {i[2]} руб.')
            itog += int(i[2]) * int(i[1])
    print(f'Итоговая сумма:', itog, 'руб.')
z3()




