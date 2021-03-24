# 05.03.2021

# 10-dars TARMOQLANISH (IF - ELSE)

# Mualiif: Islmaic

#avtolar = ["bugatti", "jaguar", "bmw", "tesla", "ford", "toyota"]

#for avto in avtolar:  ## avtolar ichidagi har bir avto uchun ...
#    if avto == "bmw":  ## ... agar avto bmw ga teng bo'lsa ...
#        print(avto.upper())  ## avtoning har bir harfini katta qilib chiqar
#    else:  ## aks holda ...
#        print(avto.title())  ## avtoning faqat birinchi harfini kattada chiqar
        
#ism = 'Ali'

#ism.lower() == 'ali'

#ism = input("Ismingiz nima?\n>>> ")  ## Foydalanuvchi ismini so'raymiz
#if ism.lower() != 'ali':  ## Agar ism Ali ga teng bo'lmasa ...
#    print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
#else:
#   print("Salom, Ali")

#javob = float(input("8x9 nechaga teng? >>> "))
#if javob != 72:
#    print("Javobingiz noto'g'ri.")

#yosh = int(input("Yoshingizni kiriting: >>> "))
#if yosh >= 18:  ## yosh 18 dan katta yoki teng bo'lsa ...
#    print("Xush kelibsiz!")
#else:  ## aks holda ...
#    print("Kirish mumkin emas!")

#login = input("Yangi login kiriting: ")
#if len(login) <= 5:  ## login uzunligini tekshiramiz
#    print("Login kamida 8 belgidan iborat bo'lishi shart!")

#yil = int(input("Tug'ilgan yilingizni kiriting?\n>>> "))
#if 2021-yil < 18:  ## Foydalanuvchining yoshini hisoblaymiz
#    print(f"Yoshingiz {2021-yil}da ekan.")
#    print("Sizga kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")

## IF ni tanasi bn bir qatorda yozilishi:
#yosh = int(input("Yoshingiz nechida?\n>>> "))
#if yosh>60: print("Siz pensiya yoshida ekansiz!")

## IF bn ELSE ning bir qaatorda kelishi:
#x, y = 50, 40  ## x=50 va y=40
#print("x>y") if x>y else print("x<y")

### UY VAZIFALAR:

## Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat \
    ##tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga \
        ##chqaring. GM uchun ikkala harfni katta qiling.
cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
#for car in cars:
#    if car == "gm":
#        print(car.upper())
#    else:
#        print(car.title())

## Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
#for car in cars:
#    if car != "gm":
#        print(car.title())
#    else:
#        print(car.upper())

## Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, \
    ##"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" \
        ##xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, \
            ##{foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
#login = input("Loginingizni yozing:\n>>> ")
#if login.lower() == 'admin':
#    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"Xush kelibsiz, {login.title()}!")

## Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga \
    ##teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
#print("2 ta son kiriting:")
#a = float(input("a = "))
#b = float(input("b = "))
#if a == b:
#    print("Sonlar teng!")
    
## Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa \
    ##konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan \
        ##xabarni chiqaring. 
#son = float(input("Istalgan son kiriting:\n>>> "))
#if son < 0:
#    print("Siz manfiy son kiritdingiz!")
#else:
#    print("Siz musbat son kiritdingiz!")


## Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning \
    ##ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat \
        ##son kiriting" degan xabarni chiqaring. 
#son = float(input("Istalgan sonni kiriting:\n>>> "))
#print(son**(1/2))if son>=0 else print("Musbat son kiriting!")