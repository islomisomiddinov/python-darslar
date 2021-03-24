# 10.03.2021

# 11-dars if-elif-else

# Muallif: Islamic

#yosh = int(input("Yoshingiz nechida?\n>>> "))
#if yosh<=7:
#    print("Sizga kirish bepul!")
#elif yosh>=60:
#    print("Siz uchun 70% chegirma mavjud!")
#elif yosh<=18:
#    print("Sizga 50% chegirma bor!")
#else:
#    print("Sizga kirish 30.000 so'm.")

## print ni qayta-qayta yozmaslik usuli:
#yosh = int(input("Yoshingiz nechida?\n>>> "))
#if yosh<=7:
#   narx = 0
#elif yosh>=60:
#   narx = 3000
#elif yosh<=18:
#   narx = 5000
#else:
#    narx = 10000   
#print(f"Sizga kirish {narx} so'm.")        

## OR operatori:
    
#kun = input("Bugun qaysi kun?\n>>> ")
#if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#    print("Bugun dam olish kuni!")
#else:
#    print("Bugun ish kuni.")

## AND operatori:
    
#kun = input("Bugun qaysi kun?\n>>> ")
#harorat = float(input("Havo harorati nechi gradus?\n>>> "))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("Bugun cho'milgani boramiz.")
#elif kun.lower()=="yakshanba" and harorat<30:
#    print("Uyda qolamiz.")
#else:
#    print("Ishga borishim kerak.")
    
## OR va AND larni birga qo'llashga misol:
    
#kun = input("Bugun qaysi kun?\n>>> ")
#harorat = float(input("Havo harorati nechi gradus?\n>>> "))
#if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#    print("Bugun cho'milgani boramiz.")
#elif (kun.lower()=="yakshanba" or kun.lower()=='shanba') and harorat<30:
#    print("Uyda qolamiz.")
#else:
#    print("Ishga borishim kerak.")    

## BOOLEAN - ma'lumot turi:
    
#narx = 15000  ##mijoz 15000 so'mga taom oldi
#choy = True  ##mijoz choy ham oldi
#salat = False  ##mijoz salat olmadi

#if choy and salat:  ##agar mijoz choy ham salat ham olgan bo'lsa
#    narx = narx + 10000  ##narxga 7000 ming so'm qo'shamiz
#elif choy or salat:  ##agar choy yoki salat olgan bo'lsa
#    narx = narx + 5000
#print(f"Jami {narx} so'm")  ##yakuniy narxni chiqaramiz


## Har bir shart alohida bajarilishi va bir-biriga bog'liq emasligi:
#narx = 15000
#non = True
#choy = False
#salat = True
#suzma = False
#kompot = True

#if choy:  ## agar choy olsa
#    print("choy")
#    narx = narx + 2000

#if non:  ## agar non olsa
#    print("Mijoz non oldi")
#    narx = narx + 3000
    
#if salat:  ## agar salat olsa
#    print("Mijoz salat oldi")
#    narx = narx + 5000
    
#if suzma:  ## agar suzma olsa
#    print("Mijoz suzma oldi")
#    narx = narx + 3000
    
#if kompot:  ## agar kompot olsa
#    print("Mijoz kompot oldi")
#    narx = narx + 3000
    
#print(f"Jami {narx} so'm")
## Yuqoridagi kod da True/False o'rniga 0/1 lardan foydalansak ham bo'ladi

## IN operatori:  (elementning ro'yxatda borligini tekshiradi.)

#menu = ['osh', 'qozonkabob', 'somsa', "lag'mon", "shashlik"]
#"sho'rva" in menu  ## menu da sho'rva bormi?

#menu = ['osh', 'qozonkabob', 'somsa', "lag'mon", "shashlik"]
#ovqat = input("Nima ovqat buyurtma qilasiz?\n> ")
#if ovqat.lower() in menu:
#    print("Buyurtmangiz qabul qilindi.")
#else:
#    print("Hozir bizda bunday ovqat yo'q.")
    
## NOT IN operatori: (elementning ro'yxatda yo'qligini tekshiradi.)
    
#menu = ['osh', 'qozonkabob', 'somsa', "lag'mon", "shashlik"]
#ovqat = input("Nima ovqat buyurtma qilasiz?\n> ")
#if ovqat.lower() not in menu:
#    print("Hozir bizda bunday ovqat yo'q.") 
#else:
#    print("Buyurtmangiz qabul qilindi.")

## Ro'yxatlarni bir-biri bn solishtirish:       
#menu = ['osh', 'qozonkabob', 'norin', 'somsa', 'shashlik']
#buyurtmalar = ['osh', 'somsa', 'non']
#for taom in buyurtmalar:
#    if taom.lower() in menu:
#        print(f"Menu da {taom} bor.")
#    else:
#        print(f"Kechirasiz, menu da {taom} yo'q.")
        
#menu = ['osh', 'qozonkabob', 'norin', 'somsa', 'shashlik']
#buyurtmalar = ['osh', 'somsa', 'non']
#if buyurtmalar:  ## ro'yxatda biror element bo'lsa, bu ifoda true qaytaradi.
#    for taom in buyurtmalar:
#        if taom.lower() in menu:
#            print(f"Menu da {taom} bor.")
#        else:  ## agar menuda taom yo'q bo'lsa
#            print(f"Kechirasiz, menu da {taom} yo'q.")
#else:  ## agar ro'yxat bo'sh bo'lsa
#    print("Savatchangiz bo'sh!")

### AMALIYOT :

##Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son \
    ##kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" \
        ##degan xabarni chiqaring.  
# son = float(input("Juft son kiriting.\n>>> "))
# if son%2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas!")         
    
## Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini \
    ##quyidagicha chiqaring:
##Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
##Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
##Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#yosh = int(input("Yoshingiz nechida?\n>>> "))
#if yosh<=4 or yosh>=60:
#    narx = 0
#elif yosh<=18:
#    narx=10000
#elif yosh>18:
#    narx=20000
#print(f"Sizga kirish {narx} so'm.")
 
##Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va \
    ##ularning teng yoki katta/kichikligi haqida xabarni chiqaring  
#print("Istalgan ikkita son kiriting.")
#a = float(input("a = "))
#b = float(input("b = "))
#if a==b:
#    print(f"{a}={b}")
#elif a>b:
#    print(f"{a}>{b}")
#else:
#    print(f"{a}<{b}")

## Mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni \
##kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan \
##savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, \
##mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa \
##"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan \
##xabarlarni chiqaring.
# mahsulotlar = ["qalam", "qaychi", "kofe", "tort", "tuz", "fanta", "sabzi", \
#               "kefir", "shokolad", "sut", "non"]
# print("Savatingizga 5 ta mahsulot kiriting?")
# savat = []
# for k in range(5):
#   savat.append(input(f"Savatga {k+1}-mahsulotni qo'shing: "))
# if savat:   ###Savatning to'la yoki bo'shligini tekshirish uchun
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"{mahsulot.title()} do'konimizda bor.")
#         else:
#             print(f"do'konimizda {mahsulot.title()} yo'q.")
# else:
#     print("\nSavatingiz bo'sh!")   
##### "Savatingiz bo'sh" degan xabar chiqmadi !!!

## Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta \
##mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor \
##mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga, do'konda yo'q \
##mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas \
##ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" \
##degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda \
##yo'q: ....." degan xabarni chiqaring.
#mahsulotlar = ["qalam", "qaychi", "kofe", "tort", "tuz", "fanta", "sabzi", \
#               "kefir", "shokolad", "sut", "non"]
#print("Savatingizga 5 ta mahsulot kiriting?")
#savat = []    
#for k in range(5):
#    savat.append(input(f"Savatingizga {k+1}-mahsulotni kiriting: "))
#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)
#if mavjud_emas:
#    print("Quyidagi mahsulotlar do'konimizda yo'q:")
#    for mahsulot in mavjud_emas:
#        print(f"{mahsulot}")
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor!")
    
##foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. \
##Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan \
##loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. \
##Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login \
##tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
#users = ['islamic', 'aligarx', 'bobursher', 'maks', '007']
#login = input("Yangi login tanlang\n>>> ")
#if login.lower() in users:
#    print("Bu login band, yangi login tanlang.")
#else:
#    print(f"Xush kelibsiz, {login.title()}!")

# # Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi \
# #kiritgan sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz \
# #bo'linishini konsolga chiqaring. 
# son =  int(input("Istalgan butun son kiriting:\n>>> "))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")


