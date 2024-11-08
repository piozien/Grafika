from PIL import Image, ImageChops, ImageStat as stat
import numpy as np
import matplotlib.pyplot as plt


# Zadanie 2: Operacje na kanale obrazu i porównanie
def zadanie_2(im):
    T = np.array(im)

    # Pobranie kanałów
    t_r = T[:, :, 0]
    t_g = T[:, :, 1]
    t_b = T[:, :, 2]

    im_r = Image.fromarray(t_r)
    im_g = Image.fromarray(t_g)
    im_b = Image.fromarray(t_b)

    im1 = Image.merge('RGB', (im_r, im_g, im_b))
    diff = ImageChops.difference(im, im1)

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(im)
    plt.title("Oryginalny obraz (im)")
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.imshow(im1)
    plt.title("Obraz scalony (im1)")
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.imshow(diff)
    plt.title("Różnica (im - im1)")
    plt.axis('off')
    plt.savefig('fig1.png')
    plt.show()


# Zadanie 3: Kanały split i zapis
def zadanie_3(im):

    r, g, b = im.split()

    im2 = Image.merge('RGB', (g, r, b))
    im2.save('im2.jpg')
    im2.save('im2.png')
    im2_jpg = Image.open('im2.jpg')
    im2_png = Image.open('im2.png')

    #porównanie
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


# Zadanie 4: Identyfikacja operacji na obrazach
def zadanie_4(obraz, mix):
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


# Zadanie 5: Tworzenie obrazów z tablicy
def zadanie_5(im):
    w, h = im.size
    A = np.random.randint(0, 256, (h, w), dtype=np.uint8)
    im3 = Image.fromarray(A)

    #podmiana kanałów z obrazem im3
    img_r = Image.merge("RGB", (im3, im.split()[1], im.split()[2]))
    img_g = Image.merge("RGB", (im.split()[0], im3, im.split()[2]))
    img_b = Image.merge("RGB", (im.split()[0], im.split()[1], im3))

    #rysowanie z podpisami
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(img_r)
    plt.title("Podmiana kanału R")
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.imshow(img_g)
    plt.title("Podmiana kanału G")
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.imshow(img_b)
    plt.title("Podmiana kanału B")
    plt.axis('off')
    plt.savefig('fig4.png')
    plt.show()


#zadanie 6: Histogram i statystyki
def zadanie_6(im):
    statystyki(im)
    r, g, b = im.split()

    #rysowanie histogramu dla każdego kanału z podpisami
    for i, (kanał, nazwa) in enumerate(zip([r, g, b], ["Kanał R", "Kanał G", "Kanał B"])):
        plt.subplot(1, 3, i + 1)
        rysuj_histogram(kanał, nazwa)
    print("Liczba pikseli koloru 1 w kanale G:", g.histogram()[1])


#statystyki
def statystyki(im):
    s = stat.Stat(im)

    print("extrema:", s.extrema, "mean:", s.mean, "median:", s.median)


#rysowanie histogramów
def rysuj_histogram(obraz, tytul):
    histogram = obraz.histogram()
    plt.title(tytul)
    plt.bar(range(256), histogram, color="gray")
    plt.xlim(0, 255)
    plt.ylim(0, max(histogram) * 1.1)
    plt.xlabel("Wartość piksela")
    plt.ylabel("Liczba pikseli")
    plt.show()


# Zadanie 7: Porównanie obrazów
def zadanie_7(im1, im2):
    diff = ImageChops.difference(im1, im2)
    stat_diff = stat.Stat(diff)
    mean_diff = np.mean(stat_diff.mean)
    print("Srednia różnica:", mean_diff)

    plt.title("Różnice między obrazami (im1 - im2)")
    plt.imshow(diff)
    plt.axis('off')
    plt.show()


# Zadanie 8: Wyjaśnienie błędu split na obrazie w trybie L




# Główna funkcja
if __name__ == '__main__':
    # 1. Wczytanie obrazu
    im = Image.open('zad1_obraz.png')

    # # 2. Operacje na kanale obrazu i porównanie
    # zadanie_2(im)
    #
    # # 3. Zamiana kanałów metodą split i zapis do plików
    zadanie_3(im)

    # 4. Identyfikacja operacji na obrazach
    # org = Image.open("pliki_do_testu-20241025/obraz10.jpg")
    # mix = Image.open('pliki_do_testu-20241025/mix310.png')
    # wynik = zadanie_4(org, mix)
    #print(wynik)
    # 5. Tworzenie obrazów z tablicy
    #zadanie_5(im)
    #
    # # 6. Histogram i statystyki
    #zadanie_6(im)
    #
    # # 7. Porównanie obrazów

    zadanie_7(im, im)
    #
    # # 8. Wyjaśnienie błędu split na obrazie w trybie L
    print("Zadanie 8:\nKomenda r, g, b = im.split() nie działa dla obrazu w trybie L, bo obraz w trybie L nie ma trzech kanałów RGB, a jedynie jeden (skalę szarości)")

