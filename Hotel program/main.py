# :) Mexmonhona dasturi

my_list = [{'ism': 'sardor', 'hona_raqam': 22, 'hona_turi': 'lyuks'},
{'ism': 'ilhom', 'hona_raqam': 44, 'hona_turi': 'standart'},
{'ism': 'isroil', 'hona_raqam': 5, 'hona_turi': 'ekonom'},
]

def plus():
    while True:
        ism = input("Ismni kiriting (yoki 'q' tugmasini bosing chiqish uchun): ")
        if ism.lower() == "q":
            break
        else:

                hona_raqam = int(input("Hona raqamini kiriting: "))

                if any(i['hona_raqam'] == hona_raqam for i in my_list):
                    print("Bunday hona mavjud, qayta kiriting.")
                    continue

                print("e - ekonom\ns - standart\nl - lyuks")
                hona_turi = input("Hona turini quydagi belgilar orqali tanlang: ").lower()

                if hona_turi not in ["e", "s", "l"]:
                    print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")
                    continue
                if hona_turi == 'e':
                    a = "ekonom"
                elif hona_turi == 's':
                    a ="standart"
                elif hona_turi == 'l':
                    a = "lyuks"



                my_list.append({"ism": ism, "hona_raqam": hona_raqam, "hona_turi": a})
                print("Mehmon  qo'shildi!\n")

def minus():
    while True:
        delet = input("mexmoni ochirish:  (yoki 'q' tugmasini bosing chiqish uchun): ")
        if delet.lower() == "q":
            break
        else:
            for i in my_list:
                if i['ism'] == delet:
                    print(f"mexmon ochirildi: {i['ism']}")
                    my_list.remove(i)

def show():
    print(f"\t-ism-\t  -hona raqami-\t     -hona turi-")
    for i in my_list:
        print("\t\t |\t\t |")
        print("\t____________________________________________")
        print(f"\t{i['ism']}\t\t{i['hona_raqam']}\t\t{i['hona_turi']}")


while True:
    print("\t\t\t\n Mexmonxonamizga xush kelibsiz!\n")
    print("\t -1 Mexmon qo'shish")
    print("\t -2 Mexmonni ro'yhattan chiqarish")
    print("\t -3 Mexmonlar ro'yhati ")
    print("\t -0 chiqish")
    a = int(input('buyruqni tanlang: '))

    if a == 1:
        plus()
    elif a == 2:
        minus()
    elif a == 3:
        show()
    elif a == 0:
        break

