
def listeToStr(liste):
    yazı = ''
    for cumle in liste:
        yazı += cumle + '.'
    
    return yazı

def dosyaOlustur(dosyaNumarası, metin):
    dosyaİsmi = str(dosyaNumarası) # Dosya numarasını stringe çeviriyorum
    dosya = open(dosyaİsmi, 'w') # dosya ismini ve açılış formatını kullanarak dosyamızı açıyoruz
    dosya.write(metin) # Metnimizi dosyaya kaydediyoruz

def main():
    metin = input('LÜTFEN METNİ BURAYA YAPIŞTIRIN = ') # Metni tanımladık
    metinListe = metin.split('.') # Metni noktalarına göre ayırdık
    parca1 = [] # Metnin ilk parçasını temsil eden liste
    kelimeSayisi = 0 # Kelime sayısını kontrol ediyoruz
    sayac = 0 # Dosya numarasını ayarlamak için tuttuğumuz değişken

    for cumle in metinListe: # Metin Listesi içindeki cümlelerde dönüyorum
        cumleler = cumle.split(' ') # Cümleyi boşluklarına göre ayırıp cümledeki kelime sayısını buldum
        cumledekiKelimeSayisi = len(cumleler) # Cümledeki kelime sayısını tutuyorum
        parca1.append(cumle) # Cumleyi metin parçasına ekliyorum
        kelimeSayisi += cumledekiKelimeSayisi # Sınırlanmış kelime sayısını kontrol etmek için ayrı bir değişkende cümledeki kelime sayısını toplayarak sınırı kontrol ediyorum

        if kelimeSayisi >= 5: # Bu sınır aşılmadıysa
            dosyaOlustur(sayac, listeToStr(parca1))
            parca1 = []
            sayac += 1
            kelimeSayisi = 0

    if len(metinListe[-1].split(' ')) < 5:
        parca1.append(metinListe[-1])
    
main()
        