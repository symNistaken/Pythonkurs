
# Kullanıcıdan bir metin alıyoruz
metin = input("Bir metin girin: ")
# Metni tersine çeviriyoruz
ters_metin = ""
for karakter in metin:
    ters_metin = karakter + ters_metin

print("Metnin tersi:", ters_metin)