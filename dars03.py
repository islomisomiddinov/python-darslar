# 03-dars. PRINT() funksiyaasi
# sana: 23.02.2021
# Muallif: Islamic

# Quyidagi kod Hello world jumlasini konsolga chiqaradi
# print("Hello world") # Izoh
# print("Assalom aleykum")

# Izoh: Ikkala, qo'shtirnoq va bir tirnoqlar bilan ham yozish mumkin.
# print("Xayrli tong!")
# print('Xayrli tong')

# Izoh: qo'shtirnoqning matn ichida ishlatilish qoidalari:
# print('Men "UzAvtoMotors"ni yoqtirmayman')
# print("Men \"UzAvtoMotors\"ni yoqtirmayman")

# Izoh: Matnni qatorlarga bo'lish qoidalari:
# print("""Odami ersang, demagil odamiy,
# Oniki, yo'q xalq g'amidin g'ami""" )
# print("odami ersang, \ndemagil odami,\nOniki, yo'q xalq g'amidin g'ami")
# print('Odami ersang, demagil odamiy, \nOniki, yo\'q xalq g\'amidin g\'ami')

# print(2+4*2) # arifmetik amallar ketma=ket bajariladi
# print(19/5)  # bo'ladi to'liq javobni beradi
# print(20/5)
# print(17//4) # bo'lish javobning butun qismini chiqaradi
# print(17/4)
# print(2**4)    # sonni darajaga oshirib beradi
# print(15%2)      # bo'linmaning qoldig'ini ko'rsatadi

# Matn, ifoda va amallarni bir qatorda birlashtirish usuli:
# print("To'qqizning kvadrati", 9**2, "ga teng")
# print('3 x 3 =',3*3)

# Uy vazifalari:
    
# print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")

# 1-misol: 5 ning 4-darajasini toping
print("5 ning 4-darajasi", 5**4, "ga teng")

# 2-misol: 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print("\n22 ni 4 ga bo'lganda", 22%4, "qoldiq qoladi")

# 3-misol: Tomonlari 125 ga teng kvadratning yuzi va perimaetrini toping.
print("\nTomonlari 125 ga teng bo'lgan kvadratning yuzi", 125*125, "ga,", 
"perimetri esa", 2*(125+125), "ga teng" )

# 4-misol: Diametri 12 ga teng bo'lgan doiraning yuzini toping.(p=3.14 deb oling)
print("\nDiametri 12 ga teng bo'lgan doiraning yuzi", 3.14*6**2, "ga teng")

# 5-misol: Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning 
# gipotenuzasini toping (Pifagor teoremasidan foydalaning).
print("\nKatetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi ", (6**2+7**2)**(1/2), "ga teng")
