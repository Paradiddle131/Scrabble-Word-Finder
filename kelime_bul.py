def bul(aranan_kelime, harfler):
    # dosya = open("sozluk_100.txt", "r", encoding="utf-8")
    dosya = open("sozluk.txt", "r", encoding="utf-8")
    kelimeler = dosya.read()
    aranan_uzunluk = len(aranan_kelime)
    harf_listesi = list(harfler)
    harf_sayisi = len(harfler)
    ayiklanmis_kelimeler, sonuc = [], []
    sayac = 0
    for kelime in kelimeler.split("\n"):
        kelime2 = kelime
        harf_listesi2 = harf_listesi.copy()
        for harf in harf_listesi:
            if harf in kelime2:
                del harf_listesi2[harf_listesi2.index(harf)]
                kelime2 = kelime2.replace(harf, '', 1)
        if len(harf_listesi) - len(harf_listesi2) == len(kelime) and (len(kelime) <= harf_sayisi) and len(kelime) == aranan_uzunluk:
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
        if sayac == aranan_uzunluk:
            sonuc.append(ayiklanmis_kelime)
        sayac = 0
    return sonuc


# print(bul("g__z_","mzgae"))
# print(bul("m____", "eeimkl"))
# print(bul("m_____", "eeimkl"))
# print(bul("____k", "eeimkl"))
# print(bul("____k_", "eeimkl"))
# print(bul("____r", "karfit"))
# print(bul("_f___", "karfit"))
# print(bul("_k___", "karfit"))
# print(bul("_f___", "karfit"))
# print(bul("___f_k", "karfit"))
# print(bul("a___", "karfit"))
# print(bul("e__i_", "iamtep"))
print(bul("_____k", "faktri"))
print(bul("__r_f", "faktri"))
print(bul("a_i_", "faktri"))


