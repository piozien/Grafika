from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt

def szary(w, h):
    return np.array([[(i + 3 * j) % 256 for i in range(w)] for j in range(h)], dtype=np.uint8)

def zadanie2(image):
    #a
    tablica = np.array(image)

    t_r = tablica[:, :, 0]  # kanał r
    t_g = tablica[:, :, 1]  # kanał g
    t_b = tablica[:, :, 2]  # kanał b

    im_r = Image.fromarray(t_r)
    im_g = Image.fromarray(t_g)
    im_b = Image.fromarray(t_b)
    #b
    im1 = Image.merge("RGB", (im_r, im_g, im_b))
    im1.save("im1.png")
    diff = ImageChops.difference(im, im1)
    #c
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(im)
    plt.title("Oryginalny obraz (im)")
    plt.axis('off')

    #scalony
    plt.subplot(1, 3, 2)
    plt.imshow(im1)
    plt.title("Scalony obraz (im1)")
    plt.axis('off')

    #róznica
    plt.subplot(1, 3, 3)
    plt.imshow(diff)
    plt.title("Różnica (im - im1)")
    plt.axis('off')


    plt.savefig("fig1.png")
    plt.show()

def zadanie_3():
    im = Image.open("pliki_do_testu-20241025/obraz12.jpg")
    _, g, _ = im.split()  #pobieram tylko zielony kanał

    zielony_hist = g.histogram()
    liczba_pikseli_150 = zielony_hist[150]

    plt.figure(figsize=(8, 4))
    plt.bar(range(256), zielony_hist, color='green')  # Histogram kanału zielonego
    plt.title("Histogram kanału zielonego")
    plt.xlabel("Wartość pikseli")
    plt.ylabel("Liczba pikseli")
    plt.savefig("hist.png")
    plt.show()

    print("Liczba pikseli w kolorze 150 w kanale zielonym:", liczba_pikseli_150)


from PIL import Image, ImageChops
import numpy as np


def zadanie4(im1, im2):
    # sprawdzam tryb i rozmiar
    if im1.size != im2.size or im1.mode != im2.mode:
        return False, "Obrazy mają różne rozmiary lub tryby."

    #"obliczanie różnicy"
    diff = ImageChops.difference(im1, im2)
    #suma
    diff_sum = np.sum(np.array(diff))

    if diff_sum == 0:
        print("Obrazy są identyczne.")
    else:
        print("Obrazy są różne.")

    plt.title("Różnice między obrazami ")
    plt.imshow(diff)
    plt.axis('off')
    plt.show()

def zadanie5(im):
    r, g, b = im.split()

    im2 = Image.merge('RGB', (g, r, b))
    im2.save('im2.jpg')
    im2.save('im2.png')
    im2_jpg = Image.open('im2.jpg')
    im2_png = Image.open('im2.png')

    # porównanie
    diff_jpg_png = ImageChops.difference(im2_jpg, im2_png)

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(im2_jpg)
    plt.title("Obraz JPG (im2.jpg)")
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.imshow(im2_png)
    plt.title("Obraz PNG (im2.png)")
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.imshow(diff_jpg_png)
    plt.title("Różnica (JPG - PNG)")
    plt.axis('off')
    plt.savefig('fig2.png')
    plt.show()

def zadanie_6(obraz, mix):
    diff = ImageChops.difference(obraz, mix)
    neg_diff = ImageChops.invert(diff)
    mean_diff = np.mean(np.array(diff))
    mean_neg_diff = np.mean(np.array(neg_diff))

    if mean_diff < 1:
        wynik = "Obrazy są identyczne."

    #sprawdzenie negatywu
    elif mean_neg_diff < 1:
        wynik = "Obraz 'mix' jest negatywem obrazu 'obraz'."

    else:

        r, g, b = obraz.split()
        perm_r_g_b = Image.merge('RGB', (g, r, b))
        perm_r_b_g = Image.merge('RGB', (b, g, r))
        perm_g_r_b = Image.merge('RGB', (r, b, g))


        if ImageChops.difference(perm_r_g_b, mix).getbbox() is None:
            wynik = "Obraz 'mix' powstał przez zamianę kanałów R i G."
        elif ImageChops.difference(perm_r_b_g, mix).getbbox() is None:
            wynik = "Obraz 'mix' powstał przez zamianę kanałów R i B."
        elif ImageChops.difference(perm_g_r_b, mix).getbbox() is None:
            wynik = "Obraz 'mix' powstał przez zamianę kanałów G i B."

        else:
            #sprawdzenie negatywu z zamianą kolorów
            neg_image = ImageChops.invert(obraz)
            if ImageChops.difference(neg_image, mix).getbbox() is None:
                wynik = "Obraz 'mix' jest negatywem z zamienionymi kolorami."
            else:
                wynik = "Transformacja 'mix' względem 'obraz' jest nieznana."

    #wyświetlenie różnicy
    plt.imshow(diff)
    plt.title("Różnica (obraz - mix)")
    plt.axis('off')
    plt.show()


    return wynik

def zadanie7(im):

    # Konwersja obrazu do tablicy numpy
    pixels = np.array(im)

    # Obliczenie odchylenia standardowego dla każdego kanału
    std_dev = np.std(pixels, axis=(0, 1))

    # Zaokrąglenie wyników do jednego miejsca po przecinku
    std_dev_rounded = np.round(std_dev, 1)

    # Wydrukowanie wyników
    print(*std_dev_rounded)

if __name__ == '__main__':
    # Zadanie 1
    # obraz = Image.open("pliki_do_testu-20241025/obraz9.jpg")
    # w, h = obraz.size
    # szary_obraz = Image.fromarray(szary(w, h))
    # r, g, b = obraz.split()
    # mix = Image.merge("RGB", (szary_obraz, g, b))
    # mix.save("mix.png")
    # mix.show()
    #Zadanie 2
    im = Image.open('im.png')
    # zadanie2(im)

    #Zadanie3
    #zadanie_3()

    #Zadanie 4
    # im2_png = Image.open("im2.png")
    # im2_jpg = Image.open("im2.jpg")
    # zadanie4(im2_jpg,im2_png)

    #Zadanie 5
    #zadanie5(im)

    #Zadanie 6
    # mix11 = Image.open("pliki_do_testu-20241025/mix011.png")
    # img11 = Image.open("pliki_do_testu-20241025/obraz11.jpg")
    # wynik = zadanie_6(img11,mix11)
    # print(wynik)

    #Zadanie 7
    zad7 = Image.open("pliki_do_testu-20241025/obraz9.jpg")
    zadanie7(zad7)