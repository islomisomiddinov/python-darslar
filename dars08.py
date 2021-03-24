# 8-dars Ro'yxatlar bilan ishlash
# 03.03.2021
#Muallif: Islamic

# cars = ["rolls royce", "ferrari", "audi", "lexus", "kia", "volvo", "bmw"]
# cars.sort()  # .sort() - ro'yxatni  tartiblaydi
# print(cars)

### KATTA VA KICHIK HARF
## Ro'yxatlarda kichik harf bn yozilgan so'z katta harf bn yozilgan\
## so'zlardan keyin keladi
# cars = ["rolls royce", "ferrari", "audi", "lexus", "Kia", "volvo", "bmw"]
# cars.sort()
# print(cars)

### TESKARI TARTIB
# cars = ["rolls royce", "ferrari", "audi", "lexus", "kia", "volvo", "bmw"]
# cars.sort(reverse=True)
# print(cars)
## .sort(reverse=True) - ro'yxatni teskari tartiblaydi

### SORTED()
## Asl ro'yxatni o'zgartirmagan holda, ro'yxatni tartiblash
# cars = ["rolls royce", "ferrari", "audi", "lexus", "kia", "volvo", "bmw"]
# print(sorted(cars))  ## asl ro'yxatni o'zgartirmagan holda, tartiblash
# print(sorted(cars, reverse=True))  ## asl ro'yxatni o'zgartirmagan holda,\
## ro'yxatni teskari tartiblash

### SONLI RO'YXATLAR
# numbers = [12, 56, -47, 6.31, 3, -21.8, 97]
# numbers.sort()
# print(numbers)

## Ro'yxatni ortidan boshlab chiqarish
# print(sorted(numbers, reverse=True)) 

### Ro'yxatni uzunligini chiqarish
# fruits = ["pear", "banana", "apple", "mandarin", "watermelon"]
# print("Elementlar soni: ", len(fruits))  
## len(...) - ro'yxat uzunligini chiqaradi

### LIST(RANGE())
## Ko'rsatilgan oraliqdagi ma'lumotlarni chiqaradi
# sonlar = list(range(0,10))
# print(sonlar)

### RANGE va QADAM
# juft_sonlar = list(range(0,20,2))  ## 0 dan 20 gacha 2 qadam
# toq_sonlar = list(range(1,20,2))  ## 1 dan 20 gacha 2 qadam 
# print("Juft sonlar:", juft_sonlar)
# print("Toq sonlar:", toq_sonlar)

### MIN(), MAX(), SUM()
# narxlar = [12000, 22500, 4500, 5600, 2_500_000]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon narx:", arzon, ".\nEng qimmati", qimmat, ".\nJami narxlar\
# yig'indisi:", jami)

### RO'YXATNI KESISH
# qushlar = ["burgut", "lochin", "chumchuq", "qarg'a", "flamingo", "laylak"]
# yirtqich_qushlar = qushlar[0:2]  
## 0-indeksdan boshlab 2 ta element ajratib oladi
# print(yirtqich_qushlar)
# print(qushlar[2:5])  ## 2-,3-,4-elementlarni ajratib olamiz
# print(qushlar[:4])  ## ro'yxat boshidan 4-gacha kesadi
# print(qushlar[2:])  ## 2-elementdan boshlab ro'yxat oxirigacha kesadi

### RO'YXATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5]  ##sonlar degan ro'yxat yaratamiz
# sonlar2 = sonlar  ##sonlar2 degan ro'yxatni sonlar ga tenglashtiramiz
# sonlar2.append(6)  ##sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7)  ## sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar2 = sonlar[:]  ## [:] - ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6)  ##sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7)  ##sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

### TUPLES (O'zgarmas ro'yxatlar)
# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ("bus", "car", "robot", "lego", "bear")
# print(toys[0])
# print(toys[-1])
# print(toys[1:4])

# toys = ("bus", "car", "robot", "lego", "bear")
# toys[3] = "teddy"  ## tuple ro'yxatiga o'zgartirish kiritib bo'lmaydi

### TUPLES <-> LIST
# toys = ("bus", "car", "robot", "lego", "bear")  ## o'zgarmas ro'yxat
# toys = list(toys)  ## o'zgarmas ro'yxatni oddiy ro'yxatga list(...)\
##yordamida aylantiramiz
## Ro'yxatga o'zgartirish kiritamiz
# toys.append("teddy")
# toys.remove("bear")
# toys[1] = "barbi"
# toys = tuple(toys)  ## Ro'yxatni qaytadan o'zgarmas ro'yxat \
    ##ko'rinishiga keltiramiz
# print(toys)


# # # UY VAZIFALARI:

### O'zingizga ma'lum davlatlarning ro'yxatini tuzing va\
    ##ro'yxatni konsolga chiqaring    
# davlatlar = ["italy", "japan", "uzbekistan", "russia", "china", "algeria"]
# print(davlatlar)

## Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

## sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda\
    ##konsolga chiqaring
# print(sorted(davlatlar))

## sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))

## Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

## reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

## sort() metodi yordamida ro'yxatni avval alifbo bo'yicha,\
    ##keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

### 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120,1200,2))

## Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print("Juft sonlar yig'indisi=", sum(juft_sonlar))

## Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani\
    ##hisoblang va konsolga chiqaring
# print("Max.son - Min.son = ", max(juft_sonlar) - min(juft_sonlar))

## Ro'yxatdagi elementlar sonini hisoblang
# print(len(juft_sonlar))

## Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni\
    ##konsolga chiqaring
# print(juft_sonlar[:20])
# print(juft_sonlar[-20:])
# print(juft_sonlar[260:280])

### taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = ["somsa", "burger", "shashlik", "dimlama", "go'ja"]

## nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[:]

## Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring\
    ##va qo'shimcha 2 ta taom qo'shing
# nonushta.remove("shashlik")
# del nonushta[2]
# nonushta.append("kasha")
# nonushta.insert(0, "chocotella")
# nonushta.insert(3, "moloko")
# nonushta[4] = "non"

## Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar, "\n")
# print(nonushta)

## Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring\
    ##va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"