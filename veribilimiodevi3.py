# =============================================================================
# Soru 1 – Liste Metotları
# Bir sınıfta öğrencilerin notları şu şekilde tutuluyor:
# notlar = [85, 92, 76, 92, 100, 76, 85, 92]
# • Listedeki tekrar eden notları silip benzersiz bir liste oluşturun.
# • En yüksek ve en düşük notu bulun.
# • Notları küçükten büyüğe sıralayın.
# =============================================================================
notlar = [85, 92, 76, 92, 100, 76, 85, 92]
notlar=set(notlar)
print(notlar)
print(sorted(notlar))
print(min(notlar))
print(max(notlar))
# =============================================================================
# Soru 2 – Sayılar
# Bir sayının Armstrong sayısı olup olmadığını kontrol eden bir Python fonksiyonu yazın.
# Armstrong sayısı: Her basamağının küplerinin toplamı kendisine eşit olan sayılar.
# Örn: 153 → 1³+5³+3³ = 153
# =============================================================================
sayi = int(input("Tam sayı giriniz: "))

def armstrong_mu(sayi):
    basamaklar = [int(x) for x in str(sayi)]
    toplam = sum([b ** 3 for b in basamaklar])
    return toplam == sayi
if armstrong_mu(sayi):
    print(sayi, "bir Armstrong sayısıdır.")
else:
    print(sayi, "bir Armstrong sayısı değildir.")
# =============================================================================
# Soru 3 – Kümeler
# Aşağıdaki iki küme verilmiştir:
# A = {"Python", "R", "SQL", "Java"}
# B = {"C++", "Python", "JavaScript", "SQL"}
# • Ortak dilleri bulun.
# • Sadece A’da olan dilleri listeleyin.
# • İki kümenin birleşimini alfabetik olarak yazdırın
# =============================================================================
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}
ortak = A & B
print("Ortak diller:", ortak)
sadece_A = A - B
print("Sadece A’da olan diller:", sadece_A)
birlesim = sorted(A | B)
print("Birleşim (alfabetik):", birlesim)

# =============================================================================
# Soru 4 – Modüller
# • random modülünü kullanarak 1–100 arasında 10 rastgele sayı üretin.
# • Bu sayıların ortalamasını ve standart sapmasını statistics modülü ile hesaplayın.
# =============================================================================
import random
import statistics

sayilar = [random.randint(1, 100) for _ in range(10)]
print("Rastgele sayılar:", sayilar)

ortalama = statistics.mean(sayilar)
print("Ortalama:", ortalama)

std_sapma = statistics.stdev(sayilar)
print("Standart Sapma:", std_sapma)


# =============================================================================
# Soru 5 – Fonksiyonlar
# kelime_sayacı(metin) adında bir fonksiyon yazın.
# Fonksiyon verilen metindeki:
# • toplam kelime sayısını
# • en uzun kelimeyi
# • en sık geçen kelimeyi döndürsün.
# =============================================================================

def kelime_sayaci(metin):
    for ch in ",.!?;:":
        metin = metin.replace(ch, "")
    kelimeler = metin.lower().split()
    toplam = len(kelimeler)
    en_uzun = max(kelimeler, key=len)
    en_sik = max(set(kelimeler), key=kelimeler.count)
    return toplam, en_uzun, en_sik

metin = "Python öğrenmek çok güzel ve Python ile programlama eğlenceli."
sonuc = kelime_sayaci(metin)
print("Toplam kelime sayısı:", sonuc[0])
print("En uzun kelime:", sonuc[1])
print("En sık geçen kelime:", sonuc[2])

#Soru 6 – Gömülü Fonksiyonlar
sayilar = [5, 12, 7, 18, 24, 3, 16]

ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
kareler = list(map(lambda x: x**2, ciftler))
sirali = sorted(kareler, reverse=True)

print("Çift sayılar:", ciftler)
print("Kareleri:", kareler)
print("Azalan sıralı kareler:", sirali)

# =============================================================================
# Aşağıdaki listeyi, her kelimenin uzunluğuna göre küçükten büyüğe sıralayın.
# kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]
# Bunu sorted + lambda ile yapın.
# =============================================================================
kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]

sirali = sorted(kelimeler, key=lambda x: len(x))

print(sirali)

#Soru 8
def rakam_toplami(metin):
    sayi = ""
    toplam = 0
    for ch in metin:
        if ch.isdigit():
            sayi += ch
        else:
            if sayi != "":
                toplam += int(sayi)
                sayi = ""
    if sayi != "":
        toplam += int(sayi)
    return toplam

print(rakam_toplami("abc12def3"))   # 15
print(rakam_toplami("a5b10c20"))    # 35


#soru 9
import numpy as np


dizi = np.random.randint(0, 51, 10)
print("Dizi:", dizi)


ortalama = np.mean(dizi)
print("Ortalama:", ortalama)


std_sapma = np.std(dizi)
print("Standart Sapma:", std_sapma)


en_buyuk = np.max(dizi)
print("En büyük değer:", en_buyuk)
















































