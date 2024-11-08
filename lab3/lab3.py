from PIL import Image
import numpy as np

#zadanie 1
def rysuj_ramki_szare(w, h, grub, kolor_ramki=80, kolor_tla=180):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    tab[grub:h - grub, grub:w - grub] = kolor_tla
    return Image.fromarray(tab)
def rysuj_pasy_pionowe_szare(w, h, grub, kolor_start=100, zmiana_koloru=50):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)

    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            odcien_szary = (kolor_start + k * zmiana_koloru) % 256
            tab[:, j] = odcien_szary
    return Image.fromarray(tab)


#zadanie 2
def negatyw(obraz):
    tryb = obraz.mode

    if tryb == '1':

        tab = np.asarray(obraz)
        tab_neg = 1 - tab
        return Image.fromarray(tab_neg.astype(np.uint8) * 255)


    elif tryb == 'L':
        tab = np.asarray(obraz)
        tab_neg = 255 - tab
        return Image.fromarray(tab_neg)


    elif tryb == 'RGB':
        tab = np.asarray(obraz)
        tab_neg = 255 - tab
        return Image.fromarray(tab_neg)

    else:
        print(f"Nieobsługiwany tryb obrazu: {tryb}")

def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)

def rysuj_po_skosie_szare(h,w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)

#zadanie 3
def koloruj_w_paski(obraz, grub):
    if obraz.mode != '1':
        raise ValueError("Obraz musi być w trybie '1' (czarno-biały).")
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    tab_rgb = np.ones((h, w, 3), dtype=np.uint8) * 255
    kolory = [
        [255, 0, 0],  # Czerwony
        [0, 255, 0],  # Zielony
        [0, 0, 255], # Niebieski
    ]
    ile_kolorow = len(kolory)

    for i in range(h):
        kolor_paska = kolory[(i // grub) % ile_kolorow]
        for j in range(w):
            if t_obraz[i, j] == 0:
                tab_rgb[i, j] = kolor_paska
    return Image.fromarray(tab_rgb, mode='RGB')

if __name__ == '__main__':
    #zadanie 1
    # im_ramka_szara = rysuj_ramki_szare(300, 200, 5)
    # im_pasy_pionowe_szare = rysuj_pasy_pionowe_szare(300, 200, 5)
    #
    #
    # im_ramka_szara.save("zad1_ramka_szara.png")
    # im_pasy_pionowe_szare.save("zad1_pasy_pionowe_szare.png")
    # im_ramka_szara.show()
    # im_pasy_pionowe_szare.show()
    #
    # #zadanie 2
    gwiazdka = Image.open("zad2_gwiazdka.bmp")
    negatyw_gwiazdka = negatyw(gwiazdka)
    negatyw_gwiazdka.show()
    # negatyw_gwiazdka.save("zad2_negatyw_gwiazdka.png")
    # ramki_kolorowe=rysuj_ramki_kolorowe(200, [20, 120, 220], 5, 8, -5)
    # ramki_kolorowe.save("zad2_ramki_kolorwe.png")
    # negatyw_ramki_kolorowe = negatyw(ramki_kolorowe)
    # negatyw_ramki_kolorowe.show()
    # negatyw_ramki_kolorowe.save("zad2_negatyw_ramki_kolorowe.png")
    # pasy_skos = rysuj_po_skosie_szare(100,300,5,8)
    # pasy_skos.show()
    # pasy_skos.save("zad2_pasy_skos.png")
    # negatyw_po_skosie = negatyw(pasy_skos)
    # negatyw_po_skosie.show()
    # negatyw_po_skosie.save("zad2_negatyw_po_skosie_szare.png")

    #zadanie 3
     # inicjaly = Image.open("inicjaly.bmp")
     #inicjaly.show()
     #inicjaly.save("zad3_inicjaly.png")
     # koloruj_inicjaly = koloruj_w_paski(inicjaly,10)
     # koloruj_inicjaly.show()
     #koloruj_inicjaly.save("zad3_inicjaly_kolor.png")
     #koloruj_inicjaly.save("zad3_inicjaly_kolor.jpg")