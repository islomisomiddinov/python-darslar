# 6-dars  Sonlar bilan ishlash
# 26.02.2021
# Muallif: Islamic

# a = 20
# b = 5.5
# temp = 36.6
# print(type(a))  # type(...) - o'zgaruvchining turini aniqlab beradi

# aholi_soni = 7_597_364_128
# print("Aholi soni:", aholi_soni)

# x, y, z = 10, 7.5, -39

# c = a*b

# ism = "Ahror"
# print(type(ism))

# d = 100//2

# radius = 20
# PI = 3.14159
# diametr = 2*radius
# print("Aylana uzunligi=", PI*diametr)

# ism = "Jobir"
# yosh = 36
# xabar = ism + " " + str(yosh) + " yoshda"
# print(xabar)

# str() - int yoki float turidagi sonlarni matnga o'zgartiradi.
# int() - matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi.\
# ...Bunda matn butun son ko'rinishida bo'lishi kerak.
# float() - matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.

# Input - foydalanuvchi bilan muloqot

# tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))  
# yosh = 2021 - tugilgan_yil
# print("Siz ", yosh, " yoshda ekansiz")

# yoki:

# tugilgan_yil = input("Tug'ilgan yilingizni kiriting: ")
# tugilgan_yil = int(tugilgan_yil)
# yosh = 2021 - tugilgan_yil
# print("Siz ", yosh, " yoshda ekansiz") 

# a = int("10")
# b = float("10")
# temp = str(36.6)


# Uy vazifalar:

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
    
# son = int(input("Istalgan sonni kiriting: \n>>> "))
# kvadrat = son**2
# kub = son**3
# print(son, " ning kvadrati ", kvadrat, " ga teng")
# print(son, " ning kubi ", kub, " ga teng")

# Foydalanuvchining yoshini so'rang,
# va uning tug'ilgan yilini hisoblab, konsolga chiqaring

# yosh = int(input("Yoshingiz nechida? \n>>> "))
# t_yil = 2021 - yosh
# print("Siz ", t_yil, "- yilda tugilgansiz")

# Foydalanuvchidan ikki son kiritishini so'rab,
# kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi, bo'linmasini
# chiqaruvchi dastur

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# yigindi = son1 + son2
# ayirma = son1 - son2
# kopaytma = son1 * son2
# bolinma = son1 / son2
# print(son1, " + ", son2, " = ", yigindi, "\n",
# son1, " - ", son2, " = ", ayirma, "\n",
# son1, " * ", son2, " = ", kopaytma, "\n",
# son1, " / ", son2, " = ", bolinma)