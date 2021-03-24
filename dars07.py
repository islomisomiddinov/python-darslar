# 02.03.2021 
# 7-dars. Lists (Ro'yxatlar).
# Muallif: Islamic

# mevalar = ["olma", "o'rik", 'anjir', 'shaftoli']  # Mevalar ro'yxati (matnlar)
# narxlar = [12000, 18000, 10500, 22000, -25, 63.2] # narxlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar arlash ro'yxati
# ismlar = [] # bo'sh ro'yxat

# narxlar[0] = 13000  # 1-qiymatni 13000 ga o'zgartiramiz
# narxlar[2] = 11700  # 3-qiymatni 11700 ga o'zgartiramiz
# narxlar[3] = narxlar[3] - 3000  # 4-qiymatdan 3000 ayiramiz
# print(narxlar)

# .append() - ro'yxatning oxiriga element qo'shadi
# mevalar.append("tarvuz")  # mevalar ga tarvuz qo'shamiz
# print(mevalar)
# cars = []  # bo'sh ro'yxat yaratamiz
# cars.append("Nexia 3")  # ro'yxatga Nexia 3 ni qo'shamiz
# cars.append("Onix")  # ro'yxatga Onix avtomobilini qo'shamiz
# cars.append("Damas")  # ro'yxatga Damas ni qo'shamiz
# print(cars)


# .insert() - ro'yxatning istalgan joyiga element qo'shish uchun ishlatiladi
# cars = ["Gentra", "Spark", "Tracker"]
# cars.insert(0, "Malibu 2")  # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)
# cars.insert(2, "Tahoe")  # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)

# del ro'yxat_nomi[indeksi] - ro'yxatdagi elementni indeksi bo'yicha o'chirish
# mevalar = ["behi", "bodom", "anor", "gilos"]
# del mevalar[1]  # 2-element (bodom) ni o'chiramiz
# print(mevalar)


# ro'yxat_nomi.remove("...") - ro'yxatdagi elementni qiymati (nomi)
#bo'yicha o'chirish
# mevalar = ["behi", "bodom", "anor", "gilos"]
# mevalar.remove("anor")  # ro'yxatdan anor ni o'chirdik
# print(mevalar)
# hayvonlar = ["tovuq","echki","it","ot","sigir", "echki"]
# hayvonlar.remove("echki")  # ro'yxatda 2 ta echki bor,ulardan 1-si o'chadi
# print(hayvonlar)

# (ro'yxat_nomi).pop(...) - ro'yxatdan shu indeksdagi yoki shu nomdagi 
#elementni sug'urib oladi,
# agar indeks yoki qiymat berilmasa ro'yxat oxiridagi elementni oladi
# bozorlik = ["yog'", "un", "go'sht", "piyoz", "nok"]
# mahsulot = bozorlik.pop(3)   # Ro'yxatdan piyoz ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# print(narxlar[1] + narxlar[2])

# car_models = ["BMW", "Lexus", "Kia", "Toyota"]
# print(car_models[-1])  # Ro'yxatning eng oxirgi elementiga -1 bilan
# murojaat qiladi

# Uy vazifalar:

#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting    
# names = ["Fazliddin", "Shohrux", "Jahongir"]
# print("Salom " + names[0] + ", bugun futbol soat nechida?")
# print(names[1] + ", bugun uyda bo'lasanmi?")
# print(names[2] + " kecha telefon qilganingni eshitmadim")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni \
#yuklang (musbat, manfiy, butun, o'nlik). 
# numbers = [11, "uch yuz", -23, 17.4]
# print(numbers[0] + numbers[2])
# print(numbers[3] - numbers[2])
# numbers[1] = 300
# print(numbers)
# numbers[2] = numbers[2] + (-7)
# print(numbers)
# numbers[3] = 21.4
# print(numbers)

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga \
#o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, \
#ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning \
#ismini kiriting.
# t_shaxslar = ["Muhammad (s.a.v.)", "Beruniy", "Amir Temur"]
# z_shaxslar = ["Bill Gates", "Rowan Atkinson", "Elon Musk"]
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)}ni ko'rishni,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan ingliz tilida\nsuhbat \
# qurishni xohlayman")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta \
#mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append("Jasur")
friends.append("Fazi")
friends.append("Asilxon")
friends.append("Abror")
friends.append("Akmal")
# print(friends)
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni \
#.remove() metodi yordamida o'chrib tashlang. 
friends.remove("Jasur")
friends.remove("Asilxon")
# print(friends)
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, "Bobur")
friends.insert(1, "Axror")
friends.insert(9, "Otabek")
# print(friends)
friends.append("Sarvar")
# print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. \
#.pop() va .append() metodlari yordamida mehmonga kelgan \
#do'stlaringizning ismini friends ro'yxatidan sug'urib olib, \
#mehmonlar ro'yxatiga qo'shing.

guests = []
guests.append(friends.pop(1))
guests.append(friends.pop(0))
guests.append(friends.pop(2))
print("\nKelgan mehmonlar: ", guests)