import numpy as np
from PIL import Image

# Wczytywanie obrazka
obrazek = Image.open("inicjaly.bmp")

#zad 2
print("Zadanie 2")
print("Tryb:", obrazek.mode)
print("Format:", obrazek.format)
print("Rozmiar:", obrazek.size)

#zad 3
# print("Zadanie 3")
# # Zamiana obrazu na tablicę numpy
# dane_obrazka = np.asarray(obrazek)
#
# # Zamiana na tablicę zerojedynkową tylko jak mam czarnobiały obraz
# tablica_bin = (dane_obrazka > 0).astype(np.uint8)
#
# # Zapis tablicy do pliku tekstowego  fmt=%d sprawia, że zapisuje to jako liczby całkowite
# np.savetxt("inicjaly.txt", tablica_bin, fmt='%d')
#
# #zad 4
# print("Zadanie 4")
# # Wczytywanie obrazu
# dane_obrazka = np.asarray(Image.open("inicjaly.bmp"))
#
# # Pobieranie wartości pikseli biały kolor to true 1; czarny false 0
# print(f"Wartość piksela (50, 30): {dane_obrazka[30, 50]}")
# print(f"Wartość piksela (90, 40): {dane_obrazka[40, 90]}")
# print(f"Wartość piksela (99, 0): {dane_obrazka[0, 99]}")
#
# #zad 5
# print("Zadanie 5")
# #wczytanie tablicy z txt
# t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
#
# # wczytanie obrazu i zamiana na tablicę
# dane_obrazka = np.asarray(Image.open("inicjaly.bmp"))
#
# #porównanie tablic
# print("Czy tablice są takie same:", np.array_equal(t1, dane_obrazka))
#
# #zad6
# print("Zadanie 6")
# #wczytanie tablicy z pliku txt jako uint8
# t2 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
#
# #porównanie tablic
# print("Czy tablice są takie same:", np.array_equal(t2, dane_obrazka))
#
# #b
# #Stwórz obraz na podstawie otrzymanej tablicy
# obrazek_z_tablicy = Image.fromarray(t2 * 255)  # Mnożymy przez 255, aby uzyskać biel i czerń
# obrazek_z_tablicy.show()
#
# #Zapis obrazu
# obrazek_z_tablicy.save("inicjaly_odtworzone.bmp")
