import os
os.system("cls")

n = int(input("Nechta parol saqlamoqchisiz: "))
ilova = []
parol = []

for i in range(n):
    ism = input("Nimani parolini kiritmoqchi siz: ")
    ilova.append(ism)
    parollar = input("Parolni kiriting: ")
    parol.append(parollar)

ismlar = input("\nNimani parolini kormoqchisiz: ")
if ismlar in ilova:
    index = ilova.index(ismlar)
    print("Parol:", parol[index])
else:
    print("Buni parolini saqlamagan siz")