with open("cass.txt", "r") as file:
    open_cass = float(file.read())
baraanuud = []
with open("baraa.txt", "r") as file:
    baraa_first = file.read()
mur = baraa_first.split("\n")
for i in mur:
     if i:
        utga = i.split("|")
        baraa = {
            "Барааны нэр": utga[0],
            "Ангилал": utga[1],
            "Барааны өртөг": float(utga[2]),
            "Зарах үнэ": float(utga[3]),
            "Тоо ширхэг": int(utga[4])
        }

        baraanuud.append(baraa)

def buh_baraa_harah():
    print("========== БҮХ БАРАА ==========")

    limit = int(input("Үлдэгдлийн лимит: "))

    baga_uldgdel = []

    for i, baraa in enumerate(baraanuud, 1):
        print(f"\n{i}. {baraa['Барааны нэр']}")
        print(f"   Ангилал: {baraa['Ангилал']}")
        print(f"   Өртөг: {baraa['Барааны өртөг']:,.0f}₮")
        print(f"   Зарах үнэ: {baraa['Зарах үнэ']:,.0f}₮")
        print(f"   Үлдэгдэл: {baraa['Тоо ширхэг']}")

        if baraa["Тоо ширхэг"] <= limit:
            print("   ⚠️ Үлдэгдэл бага байна!")
            baga_uldgdel.append(baraa)
    return baga_uldgdel
def baraa_nemej_avah(baga_uldgdel):
    global open_cass

    if not baga_uldgdel:
        print("\nҮлдэгдэл бага бараа байхгүй.")
        return

    print("\n========== НӨХӨН АВАХ БАРАА ==========")

    for i, baraa in enumerate(baga_uldgdel, 1):
        print(f"{i}. {baraa['Барааны нэр']} - үлдэгдэл: {baraa['Тоо ширхэг']}")

    niit_zardal = 0

    while True:
        songolt = input("\nЯмар бараа нэмж авах вэ? Дугаар (done - дуусгах): ")

        if songolt.lower() == "done":
            break

        songolt = int(songolt)
        baraa = baga_uldgdel[songolt - 1]

        too = int(input("Хэдэн ширхэг авах вэ?: "))

        negj_urtug = baraa["Барааны өртөг"]
        niit_une = negj_urtug * too

        baraa["Тоо ширхэг"] += too
        niit_zardal += niit_une

        print(f"\nБараа: {baraa['Барааны нэр']}")
        print(f"Нэгж өртөг: {negj_urtug:,.0f}₮")
        print(f"Нэмсэн тоо: {too}")
        print(f"Нийт үнэ: {niit_une:,.0f}₮")
        print(f"Шинэ үлдэгдэл: {baraa['Тоо ширхэг']}")

    open_cass -= niit_zardal

    print("\n========== НӨХӨН АВАЛТЫН ДҮН ==========")
    print(f"Нийт нөхөн авалтын зардал: {niit_zardal:,.0f}₮")
    print(f"Кассын үлдэгдэл: {open_cass:,.0f}₮")
baga_uldgdel = buh_baraa_harah()

baraa_nemej_avah(baga_uldgdel)