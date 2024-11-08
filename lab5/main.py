from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt
from random import randint


def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] > 0:
                k = randint(0, 2)
                t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)


def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    obraz_bazowy = np.array(obraz_bazowy.convert('RGB'))
    obraz_wstawiany = np.array(obraz_wstawiany.convert('L'))

    obraz_bazowy.setflags(write=True)

    h_wstawiany, w_wstawiany = obraz_wstawiany.shape
    h_bazowy, w_bazowy, _ = obraz_bazowy.shape

    for i in range(h_wstawiany):
        for j in range(w_wstawiany):
            if obraz_wstawiany[i, j] == 0:
                x = m + i
                y = n + j
                if 0 <= x < h_bazowy and 0 <= y < w_bazowy:
                    obraz_bazowy[x, y] = kolor

    return Image.fromarray(obraz_bazowy)


def odkoduj(obraz1, obraz2):
    t_obraz1 = np.asarray(obraz1.convert('L'))
    t_obraz2 = np.asarray(obraz2.convert('L'))

    difference = np.abs(t_obraz1 - t_obraz2)
    difference[difference > 0] = 255
    difference[difference == 0] = 0

    return Image.fromarray(difference.astype(np.uint8))


def zadanie1():
    im = Image.open('obraz_bazowy.png')
    inicjaly = Image.open('obraz_wstawiany.bmp')

    # pkt 1
    m1 = 0
    n1 = im.size[0] - inicjaly.size[0]
    result1 = wstaw_inicjaly(im, inicjaly, m1, n1, [0, 255, 0])

    # pkt 2
    m2 = im.size[1] - inicjaly.size[1]
    n2 = 0
    result2 = wstaw_inicjaly(result1, inicjaly, m2, n2, [255, 0, 0])

    # pkt 3
    m3 = im.size[1] // 2 - inicjaly.size[1] // 2
    n3 = im.size[0] - inicjaly.size[0] // 2  # widoczna pierwsza
    result3 = wstaw_inicjaly(result2, inicjaly, m3, n3, [0, 0, 255])

    # pkt 4
    result3.save('obraz_inicjaly.png')


def zadanie2():
    image_path = 'obraz.png'
    im = Image.open(image_path)

    for i in range(1, 6):
        im.save(f'obraz{i}.jpg')
        im = Image.open(f'obraz{i}.jpg')

    original = Image.open('obraz.png')
    final_image = Image.open('obraz5.jpg')

    difference = ImageChops.difference(original, final_image)


    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(original)
    plt.subplot(1, 3, 2)
    plt.title('Final Image')
    plt.imshow(final_image)
    plt.subplot(1, 3, 3)
    plt.title('Difference')
    plt.imshow(difference)
    plt.show()

def zadanie2_1():
    final_image = Image.open('obraz5.jpg')
    imageno4 = Image.open('obraz4.jpg')
    difference2 = ImageChops.difference(imageno4, final_image)
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    plt.title('obraz4')
    plt.imshow(imageno4)
    plt.subplot(1, 3, 2)
    plt.title('Final Image')
    plt.imshow(final_image)
    plt.subplot(1, 3, 3)
    plt.title('Difference')
    plt.imshow(difference2)
    plt.savefig('porownanie.png')
    plt.show()

def zadanie3():
    im_j = Image.open('jesien.jpg')
    im_kod = Image.open('zakodowany2.bmp')

    result_kod = odkoduj(im_j, im_kod)
    result_kod.save('kod2.bmp')


if __name__ == '__main__':
    zadanie1()
    zadanie2()
    zadanie2_1()
    zadanie3()
