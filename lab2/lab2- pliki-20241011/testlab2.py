import numpy as np
from PIL import Image

def rysuj_ramke_w_obrazie(tab_obraz, grub):
    h, w = tab_obraz.shape

    tab_obraz[:grub, :] = 0
    tab_obraz[h - grub:, :] = 0
    tab_obraz[:, :grub] = 0
    tab_obraz[:, w - grub:] = 0

    return Image.fromarray(tab_obraz)

def rysuj_pasy_pionowe(w, h, grub):

    tab = np.ones((h, w), dtype=np.uint8)

    # pionowe pasy
    ile_paskow = w // grub
    for k in range(ile_paskow):
        tab[:, k * grub:(k + 1) * grub] = k % 2  # na zmiane czarne i białe tło

    # Zamiana wartości
    tab = tab * 255
    return Image.fromarray(tab)

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    # oba obrazy na tablice NumPy
    tab_bazowy = np.asarray(obraz_bazowy).astype(np.uint8)
    tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)

    # wymiary obu obrazów
    h_bazowy, w_bazowy = tab_bazowy.shape
    h_wstawiany, w_wstawiany = tab_wstawiany.shape

    # ustawienie granicy jezeli jeden obraz jest wiekszy od drugiego
    n_k = min(h_bazowy, n + h_wstawiany)
    m_k = min(w_bazowy, m + w_wstawiany)
    n_p = max(0, n)
    m_p = max(0, m)

    # kod który wstawia jeden obraz do drugiego
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_bazowy[i][j] = tab_wstawiany[i - n][j - m]

    # Konwersja tablicy na bool tworzenie obrazu-czarnobiałego
    tab_bazowy = tab_bazowy.astype(bool)
    return Image.fromarray(tab_bazowy)


def rysuj_ramki(w, h, grub):
    # tworzy białe tło
    tab = np.ones((h, w), dtype=np.uint8)

    # rysowanie ramek na zmianę
    ile_ramek = min(w, h) // (2 * grub)
    for i in range(ile_ramek):
        tab[i * grub:(i + 1) * grub, i * grub:w - i * grub] = i % 2  # góra i dół
        tab[h - (i + 1) * grub:h - i * grub, i * grub:w - i * grub] = i % 2  # dolna ramka
        tab[i * grub:h - i * grub, i * grub:(i + 1) * grub] = i % 2  # lewa
        tab[i * grub:h - i * grub, w - (i + 1) * grub:w - i * grub] = i % 2  # prawa

    tab = tab * 255
    return Image.fromarray(tab)

if __name__ == '__main__':

    # zad5_2 = rysuj_ramki(80,130,5)
    # zad5_2.save("zad5_2.bmp")
    obraz_jpeg = Image.open("zad5_2.bmp")
    obraz_jpeg.save("ramki.jpg", format="JPEG")
    mode = obraz_jpeg.mode  # Tryb obrazu
    size = obraz_jpeg.size  # Rozmiar obrazu (szerokość, wysokość)
    tablica = np.asarray(obraz_jpeg)  # Konwersja na tablicę NumPy
    wymiar_tablicy = tablica.shape  # Wymiary tablicy
    liczba_elementow = tablica.size  # Liczba elementów tablicy

    # Drukowanie wyników
    print(f"{mode}; {size}; {wymiar_tablicy}; {liczba_elementow}")











    # zad6 = rysuj_ramki(80,130,5)
    # zad6.save("zad6.bmp")

    # zad6paint = Image.open("zad6paint.bmp")
    # mode = zad6paint.mode  # Tryb obrazu
    # size = zad6paint.size  # Rozmiar obrazu (szerokość, wysokość)
    # tablica = np.asarray(zad6paint)  # Konwersja na tablicę NumPy
    # shape = tablica.shape  # Wymiary tablicy
    # num_elements = tablica.size  # Liczba elementów w tablicy
    #
    # # Drukowanie wyników
    # print(f"{mode}; {size}; {shape}; {num_elements}")

    #zad3 = rysuj_pasy_pionowe(200,100,10)
    #zad3.save('zad3.bmp')
    # obraz_jpeg = Image.open('zad3_2.bmp')  # Otwórz zapisany obraz JPEG
    #
    # # Informacje o obrazie
    # mode = obraz_jpeg.mode
    # pixel_value = obraz_jpeg.getpixel((66, 13))  # Wartość piksela na pozycji (66, 13)
    # tablica = np.asarray(obraz_jpeg)
    # element_tablicy = tablica[97, 20]
    # print(f"{mode}; {pixel_value}; {element_tablicy}")

    # obraz_bazowy = rysuj_pasy_pionowe(300,200,15)
    # obraz_wstawiany = np.asarray(Image.open("inicjaly.bmp"))
    #
    # zad3pkt1 = wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, 250, 100)
    # zad3pkt2 = wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, 0, 50)

    #zad3pkt1.show()
    #zad3pkt2.show()






    #pierwsza część zadania tworzenie obrazu w trybie 1
    tablica = np.loadtxt('tablica.txt', dtype=np.uint8)
    tablica_bin = tablica * 255
    obraz = Image.fromarray(tablica_bin, mode='L')

 # rysowanie ramki
    obraz_z_ramka = rysuj_ramke_w_obrazie(np.array(obraz), 40)
    obraz_z_ramka.save('zad6.jpg')
    obraz_z_ramka.show()
