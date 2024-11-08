from PIL import Image  # Python Imaging Library
import numpy as np

# ---------- wczytywanie obrazu zapisanego w różnych formatach .bmp, .jpg, .png oraz pobieranie informacji o obrazie  -------------------
obrazek = Image.open("obrazek.bmp")  # wczytywanie obrazu
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)
