# 5-dars   Matn bilan ishlash (String)
# String ustida amallar
# 24/02/2021(Qor yog'moqda,kuchli sovuq)
# Islamic

# shahar = "Toshkent"
# viloyat = "Toshkent"

# matn = "Men yangi 🛩 sotib oldim"
# smayl = "🥰"

# print(matn)
# print(smayl)

# ism = "Islom"
# print("Mening ismim " + ism)

# ism = "Bahrom"
# familiya = "Xatamov"
# print(ism + familiya)
# print(ism + " " + familiya)   # ikki o'zgaruvchi orasiga bo'sh joy qo'shadi

# f-string

# ism = "Bill"
# familiya = "Gates"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# ism = "James"
# familiya = "Bond"
# print(f"Salom, mening ismim {familiya}, {ism} {familiya}!")
# print("james bond".upper())

# print("Hello world!")
# print("Hello \tworld!")  # \t-orada katta joy ochadi
# print("Hello \nworld!") # \n-keyingi qatorga ko'chirish uchun xizmat qiladi

# STRING METODLAR

# ism = "james"
# familiya = "bond"
# ism_sharif = f"{ism} {familiya}"
# ism_sharif = ism_sharif.upper()
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())

# meva = "     olma     "
# print(meva)
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# INPUT funksiyasi (foydalanuvchidan ma'lumot olish uchun ishlatiladi)

# ism = input("Ismingiz nima?")
# print("Assalom aleykum, " + ism)

# ism = input("Ismingiz nima?\n>>>" # foydalanuvchi ismini yangi qatorda yozish
# print("Assalom aleykum, " + ism.title())

# UYGA VAZIFALAR

# kocha = "Bog'bon"
# mahalla = "Jaloir"
# tuman = "Sergeli"
# viloyat = "Samarqand"
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
# tuman + " tumani, " + viloyat + " viloyati")

# print("\nIltimos, quyidagi ma'lumotlarni kiriting:")
# kocha = input("Ko'cha nomini kiriting?\n-")
# mahalla = input("Mahallangiz nomini kiriting:\n-")
# tuman = input("Tumaningiz nomini kiriting:\n-")
# viloyat = input("Viloyat nomini kiriting:\n-")
# print("\n" + kocha.title() + " ko'chasi,\n" + mahalla.title() + \
# " mahallasi,\n" + tuman.title() + " tumani,\n" + \
# viloyat.title() + " viloyati.\n")

# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, \
# {viloyat} viloyati"
# manzil = f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, \
# {tuman.title()} tumani, \
# {viloyat.title()} viloyati"

# print(manzil)
# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())