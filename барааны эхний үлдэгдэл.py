open_cass = float(input("Кассын эхний үлдэгдэл: "))
baraanuud = []
baraanii_too = int(input("Хэдэн бараа бүртгэх вэ?: "))
for i in range(baraanii_too):
    print(f"\n{i + 1}-р бараа")

    ner = input("Барааны нэр: ")
    angilal = input("Ангилал: ")
    baraanii_urtug = float(input("Барааны өртөг: "))
    zarah_une = float(input("Зарах үнэ: "))
    too_shirkheg = int(input("Эхний үлдэгдэл: "))
    baraa = {"Барааны нэр" : ner,
             "Ангилал" : angilal,
             "Барааны өртөг" : baraanii_urtug,
              "Зарах үнэ" : zarah_une,
               "Тоо ширхэг" : too_shirkheg }
    baraanuud.append(baraa)
with open("cass.txt", "w") as file:
    file.write(str(open_cass))
with open("baraa.txt", "w") as file:
    for baraa in baraanuud:
        file.write(
            baraa["Барааны нэр"] + "|" +
            baraa["Ангилал"] + "|" +
            str(baraa["Барааны өртөг"]) + "|" +
            str(baraa["Зарах үнэ"]) + "|" +
            str(baraa["Тоо ширхэг"]) + "\n"
        )