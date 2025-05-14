# Kullanıcıdan iki sayı alarak toplama, çıkarma, çarpma, bölme, mod alma ve üs alma işlemlerini yapan Python programı
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlemler
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız (0'a bölme)"
mod = sayi1 % sayi2 if sayi2 != 0 else "Tanımsız (0'a bölme)"
us = sayi1 ** sayi2

# Sonuçların ekrana yazdırılması
print(f"\nToplama: {sayi1} + {sayi2} = {toplam}")
print(f"Çıkarma: {sayi1} - {sayi2} = {fark}")
print(f"Çarpma: {sayi1} * {sayi2} = {carpim}")
print(f"Bölme: {sayi1} / {sayi2} = {bolum}")
print(f"Mod alma: {sayi1} % {sayi2} = {mod}")
print(f"Üs alma: {sayi1} ** {sayi2} = {us}")
# Bu program, kullanıcıdan iki sayı alır ve toplama, çıkarma, çarpma, bölme, mod alma ve üs alma işlemlerini yapar.
# Kullanıcıdan alınan sayılar float türünde olduğu için, kullanıcı tam sayı girse bile float olarak işlenir.      