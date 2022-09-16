lentele = {
    7: "•", 8: "•", 9: "•",
    4: "•", 5: "•", 6: "•",
    1: "•", 2: "•", 3: "•", }


def spausdinti_lentele():
    print(lentele[7] + '|' + lentele[8] + '|' + lentele[9])
    print(lentele[4] + '|' + lentele[5] + '|' + lentele[6])
    print(lentele[1] + '|' + lentele[2] + '|' + lentele[3])


def laimejimas(ejimas):
    if lentele[1] == ejimas and lentele[2] == ejimas and lentele[3] == ejimas:
        return True
    elif lentele[1] == ejimas and lentele[4] == ejimas and lentele[7] == ejimas:
        return True
    elif lentele[1] == ejimas and lentele[5] == ejimas and lentele[9] == ejimas:
        return True
    elif lentele[4] == ejimas and lentele[5] == ejimas and lentele[6] == ejimas:
        return True
    elif lentele[7] == ejimas and lentele[8] == ejimas and lentele[9] == ejimas:
        return True
    elif lentele[2] == ejimas and lentele[5] == ejimas and lentele[8] == ejimas:
        return True
    elif lentele[7] == ejimas and lentele[5] == ejimas and lentele[3] == ejimas:
        return True
    elif lentele[3] == ejimas and lentele[6] == ejimas and lentele[9] == ejimas:
        return True
    else:
        return False


def uzimtumas(pozicija):
    uzimtas = False
    if lentele[pozicija] != "•":
        uzimtas = True
    return uzimtas


def irasyti_i_lentele(pozicija, pasirinkimas):
    lentele[pozicija] = pasirinkimas


def ar_teisingas_irasas(pasirinkimas):
    patikrinti_irasa = True
    if not pasirinkimas.isnumeric():
        print("Pasirinkimai galimi 1-9")
        patikrinti_irasa = False
    elif 0 == int(pasirinkimas) or int(pasirinkimas) >= 10:
        print("Pasirinkimai galimi 1-9")
        patikrinti_irasa = False
    elif uzimtumas(int(pasirinkimas)):
        print("Pozicija jau užimta")
        patikrinti_irasa = False

    return patikrinti_irasa


ejimas = "X"
ejimu_kiekis = 0


while True:
    spausdinti_lentele()
    if ejimas == "X":
        pasirinkimasX = input("X eilė:  ")
        valueX = "X"

        if not ar_teisingas_irasas(pasirinkimasX):
            continue

        irasyti_i_lentele(int(pasirinkimasX), valueX)
        ejimu_kiekis += 1
        laimeti = laimejimas(ejimas)
        if laimeti:
            spausdinti_lentele()
            print("Laimėjo X")
            break
        else:
            ejimas = "O"

    elif ejimas == "O":
        pasirinkimasO = input("O eilė: ")
        valueO = "O"

        if not ar_teisingas_irasas(pasirinkimasO):
            continue

        irasyti_i_lentele(int(pasirinkimasO), valueO)
        ejimu_kiekis += 1

        laimeti = laimejimas(ejimas)

        if laimeti:
            spausdinti_lentele()
            print("Laimėjo O")
            break
        else:
            ejimas = "X"

    if ejimu_kiekis == 9:
        spausdinti_lentele()
        print("Lygiosios")
        break
