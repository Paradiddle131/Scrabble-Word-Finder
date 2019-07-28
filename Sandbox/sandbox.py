# sample = "g__z_"
# print(list(enumerate(sample)))
# print(list(enumerate(sample))[0][1])
# print(sample[0])

kelimeler = ["ornek", "kelimeler", "yaziyorum", "extreme", "before", "kelime", "eklem", "melek"]
# print(kelimeler[0].replace())

def dogrula(harfler):
    # harfler = ['e', 'e', 'l', 'k', 'm', 'i']
    harf_listesi = list(harfler)
    harf_sayisi = 5
    alfabe = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'i', 'ı', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    result = all(kelime in harf_listesi for kelime in kelimeler)
    for kelime in kelimeler:
        harf_listesi2 = harf_listesi.copy()
        # result = all(harf in kelime for harf in harf_listesi)
        for harf in harf_listesi:
            if(harf in kelime):
                del harf_listesi2[harf_listesi2.index(harf)]
        if len(harf_listesi2) == 0 or len(harf_listesi) - len(harf_listesi2) == len(kelime):
            result = True
        print(kelime, " : ", result)
        result = False

def ayikla(aranan_kelime, harfler):
    # dosya = open("sozluk_100.txt", "r", encoding="utf-8")
    dosya = open("sozluk.txt", "r", encoding="utf-8")
    kelimeler = dosya.read()
    aranan_uzunluk = len(aranan_kelime)
    harf_listesi = list(harfler)
    harf_sayisi = len(harfler)
    ayiklanmis_kelimeler = []
    sonuc = []
    sayac = 0
    for kelime in kelimeler.split("\n"):
        kelime2 = kelime
        harf_listesi2 = harf_listesi.copy()
        for harf in harf_listesi:
            if(harf in kelime2):
                del harf_listesi2[harf_listesi2.index(harf)]
                kelime2 = kelime2.replace(harf, '', 1)
        if (len(harf_listesi) - len(harf_listesi2) == len(kelime) and (len(kelime) <= harf_sayisi) and len(kelime) == aranan_uzunluk):
            ayiklanmis_kelimeler.append(kelime)
    for ayiklanmis_kelime in ayiklanmis_kelimeler:
        for i in range(0, len(ayiklanmis_kelime)):
            try:
                if ayiklanmis_kelime[i] == aranan_kelime[i] or aranan_kelime[i] == '_':
                    sayac += 1
            except:
                pass
            if harf_sayisi == i+1:
                break
        if (sayac == aranan_uzunluk):
            sonuc.append(ayiklanmis_kelime)
        sayac = 0
    return sonuc

def kelime_bul(aranan_kelime, harfler):
    kelimeler = ayikla(aranan_kelime, harfler)
    harf_sayisi = len(harfler)
    harfler = list(harfler)
    aranan_harfler = []
    sayac = 0
    bilinen_harf_sayisi = 0
    for harf in list(enumerate(aranan_kelime)):
        aranan_harfler.append(harf[1])
        if harf[1] != '_':
            bilinen_harf_sayisi += 1
    sonuc = []
    for kelime in kelimeler:
        for i in range(0, len(aranan_kelime)):
            try:
                if kelime[i] == aranan_harfler[i]:
                    sayac += 1
            except:
                pass
            if harf_sayisi == i+1:
                break
        if (sayac == bilinen_harf_sayisi):
            sonuc.append(kelime)
        sayac = 0
    return sonuc

# print(dogrula("eelkmi"))

sample4 = "abcabc"
print(sample4.replace('a', '', 1))
