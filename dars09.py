# 04.03.2021
# 9-dars FOR takrorlash operatori
# Muallif: Islamic

# mehmonlar = ["Abbos", "Doniyor", "Sardor", "Izzatilla", "Umid"]
# for mehmon in mehmonlar:
#    print("Salom", mehmon)
#    print("Xayr", mehmon)

# mehmonlar = ["Xasan", "Xusan", "Bobur", "Rustam", "Axror"]
# for mehmon in mehmonlar:
#   print(f"Hurmatli {mehmon}, sizni 12 Avgust kuni nahor oshiga...")
#   print("Hurmat bilan, Islamic\n")

# sonlar = list(range(1,11))  
# for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))  ## 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati = []  ## bo'sh ro'yxat yaratamiz
# for son in sonlar:  ## sonlardagi har bir son uchun
#    sonlar_kvadrati.append(son**2)  ## uning kv.ni hisoblab sonlar_kvadrati\
    ##ga yuklaymiz
    
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []  ## bo'sh ro'yxat
# print("5 ta eng yaqin do'stingizni kiriting")
# for n in range(5):  ## n bu yerda 0 dan 4 gacha qiymatlar oladi
#    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:\n>>>"))
# print(dostlar)

### AMALIYOT: 
    
## Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing va ro'yxatdagi \
    ##har bir ismga takrorlanuvchi xabar yozing
# ismlar = ["Axror", "Azim", "Nizom", "Olim", "Dilshod"]
# for ism in ismlar:
#    print(ism, "aka")
#    print(f"Assalom aleykum, {ism} aka. Xush kelibsiz!")

## Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" \
    ##degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini 
    ##yozing)
# print(f"Kod {len(ismlar)} marta takrorlandi")

## 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar \
    ##bir elementining kubini yangi qatordan konsolga chiqaring.
# toq_sonlar = list(range(11,100,2))
# for son in toq_sonlar:
#    print(f"{son} ning kubi {son**3} ga teng")

## Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang\
    ##va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#print("5 ta eng sevimli kinolaringiz qaysilar?")
#for k in range(5):
#    kinolar.append(input(f"Iltimos {k+1}-kino nomini yozing:\n>>>"))
#print(kinolar)

## Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini)\
    ##so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab\
        ##ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# insonlar = int(input("Bugun necha kishi bilan suhbat qildingiz? >>> "))
# ismlar = []
# for i in range(insonlar):
#     ismlar.append(input(f"{i+1}-suhbatlashgan insoningiz kim?\n>>> "))
# print("\n")
# print(ismlar)
