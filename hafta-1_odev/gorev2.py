# Kullanıcıdan bir sayı alıyoruz
n = int(input("Bir sayı girin: "))

# Kullanıcıdan alınan sayıyı pozitif bir tam sayı olarak kontrol ediyoruz
if n < 1:
    print("Lütfen pozitif bir tam sayı girin.")
    exit()
toplam = 0

# 1'den n'e kadar olan sayıları topluyoruz
for i in range(1, n + 1):
    toplam += i

# Sonucu ekrana yazdırıyoruz
print(f"1'den {n}'e kadar olan sayıların toplamı: {toplam}")