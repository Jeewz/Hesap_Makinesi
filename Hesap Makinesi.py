print("""
*****************Hesap Makinesi********************
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Yüzde
6. Faktöriyel
7. Çıkış
***************************************************
""")

while(True):
    işlem = int(input("Yapılacak işlem numarasını seçiniz.(Çıkmak için '7' yazınız):"))
    if işlem == 7:
        print("Çıkılıyor...")
        exit()
    if (işlem == 1):
        try:
            sayı1 = int(input("İlk sayıyı giriniz:"))
            sayı2 = int(input("İkinci sayıyı giriniz:"))
            print("{} ile {}'nin toplamı = {}".format(sayı1 , sayı2 , sayı1 + sayı2))
        except ValueError:
            print("Lütfen sadece sayı girin!")
    elif (işlem == 2):
        try:
            sayı1 = int(input("İlk sayıyı giriniz:"))
            sayı2 = int(input("İkinci sayıyı giriniz:"))
            print("{} ile {}'nin farkı = {}".format(sayı1 , sayı2 , sayı1 - sayı2))
        except ValueError:
            print("Lütfen sadece sayı girin!")
    elif (işlem == 3):
        try:
            sayı1 = int(input("İlk sayıyı giriniz:"))
            sayı2 = int(input("İkinci sayıyı giriniz:"))
            print("{} ile {}'nin çarpımı = {}".format(sayı1 , sayı2 , sayı1 * sayı2))
        except ValueError:
            print("Lütfen sadece sayı girin!")
    elif (işlem == 4):
        try:
            sayı1 = int(input("İlk sayıyı giriniz:"))
            sayı2 = int(input("İkinci sayıyı giriniz:"))
            print("{} ile {}'nin bölümü = {}".format(sayı1 , sayı2 , sayı1 / sayı2))
        except ZeroDivisionError:
            print("Bir sayıyı 0'a bölemezsiniz!")
        except ValueError:
            print("Lütfen sadece sayı girin!")
    elif (işlem == 5):
        try:
            sayı1 = int(input("Sayıyı giriniz:"))
            sayı2 = int(input("Yüzdesi:"))
            print("{}'nin yüzde {}'si = {}.".format(sayı1,sayı2,(sayı1*sayı2)/100))
        except ValueError:
            print("Lütfen sadece sayı girin!")
    elif (işlem == 6):
        try:
            sayı = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
            faktöriyel = 1
            i = 1
            if sayı >= 0:
                while i <= sayı:
                    faktöriyel *= i
                    i += 1
                print("Girdiğiniz sayının faktöriyeli:", faktöriyel)
            else:
                print("Negatif sayıların faktöriyeli olmaz")
        except ValueError:
            print("Lütfen sadece sayı girin!")

    else:
        print("Yanlış Kodlama")
