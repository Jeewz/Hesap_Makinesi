print("""*****************Hesap Makinesi********************
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Yüzde
6. Faktöriyel
***************************************************
""")

işlem = int(input("İşlem sayısını giriniz:"))

if (işlem == 6):
    sayı = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
    faktöriyel = 1
    i = 1
    if sayı >= 0:
        while i <= sayı:
            faktöriyel *= i
            i += 1
        print("Girdiğiniz sayının faktöriyeli:", faktöriyel)
    exit()

a = int(input("birinci sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))


if (işlem == 1):
    print("{} ile {} sayısının toplamı {}.".format(a,b,a+b))
elif (işlem == 2):
    print("{} ile {} sayısının farkı {}.".format(a,b,a-b))
elif (işlem == 3):
    print("{} ile {} sayısının çarpımı {}.".format(a,b,a*b))
elif (işlem == 4):
    print("{} ile {} sayısının bölümü {}.".format(a,b,a/b))
elif (işlem == 5):
    print("{} yüzde {}'si  {}.".format(a,b,(a*b)/100))
else:
    print("Geçersiz işlem sayısı girildi.")

