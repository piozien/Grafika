from PIL import Image
import numpy as np

#zad1
def rysuj_ramke_w_obrazie(obraz, grub):
    # zamiana na tablice numpy
    tab_obraz = np.asarray(obraz).astype(np.uint8)

    # wymiary
    h, w = tab_obraz.shape

    # czarna ramka grubosci grub
    tab_obraz[:grub, :] = 0  # góra
    tab_obraz[h - grub:, :] = 0  # dol
    tab_obraz[:, :grub] = 0  # lewo
    tab_obraz[:, w - grub:] = 0  # prawo


    return Image.fromarray(tab_obraz)

#zad 2.1
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

#zad 2.2
def rysuj_pasy_pionowe(w, h, grub):

    tab = np.ones((h, w), dtype=np.uint8)

    # pionowe pasy
    ile_paskow = w // grub
    for k in range(ile_paskow):
        tab[:, k * grub:(k + 1) * grub] = k % 2  # na zmiane czarne i białe tło

    # Zamiana wartości
    tab = tab * 255
    return Image.fromarray(tab)

#zad2.3
def rysuj_wlasne(w, h, grub):
    # Stwórz tablicę z samymi 1 (białe tło)
    tab = np.ones((h, w), dtype=np.uint8)

    # szachwonica
    for i in range(0, h, grub):  # iterujemy wiersze co grub
        for j in range(0, w, grub):  # iterujemy kolumny grub
            if (i // grub + j // grub) % 2 == 0:
                tab[i:i + grub, j:j + grub] = 0  # rysujemy czarne pola


    tab = tab * 255
    return Image.fromarray(tab)

#zad 3
def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    # oba obrazy na tablice NumPy
    tab_bazowy = np.asarray(obraz_bazowy).astype(np.uint8)
    tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)

    # wymiary obu obrazów
    h_bazowy, w_bazowy = tab_bazowy.shape
    h_wstawiany, w_wstawiany = tab_wstawiany.shape

    # ustawienie granicy gdy jeden obraz jest wiekszy od drugiego
    n_k = min(h_bazowy, n + h_wstawiany)
    m_k = min(w_bazowy, m + w_wstawiany)
    n_p = max(0, n)
    m_p = max(0, m)

    # kod który wstawia jeden obraz do drugiego
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_bazowy[i][j] = tab_wstawiany[i - n][j - m]


    tab_bazowy = tab_bazowy.astype(bool)
    return Image.fromarray(tab_bazowy)



if __name__ == '__main__':

    zad1_1 = np.ones((50, 100), dtype=np.uint8) * 255
    zad1_2 = Image.fromarray(zad1_1)


    zad1 = rysuj_ramke_w_obrazie(zad1_2, 2)
    zad2_1 = rysuj_ramki(100,50, 3)
    zad2_1.show()
    zad2_2 = rysuj_pasy_pionowe(100,50, 3)
    zad2_2.show()
    zad2_3 = rysuj_wlasne(210,150,10)
    zad2_3.show()
    zad3 = wstaw_obraz_w_obraz(zad2_2,zad2_3,30,30)
    zad3.show()