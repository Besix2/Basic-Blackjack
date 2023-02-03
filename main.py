import random
import time

kartlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Hand = 0
Bank = 0
Guthaben = 500


def karten():
    x = kartlist[random.randrange(1, len(kartlist))]
    return x


def winning(wahl, Bank, Hand, guthaben, Einsatz):
    if Hand > 21:
        print("verkackt")
        summe = guthaben - Einsatz
        return (int(summe), False)
    if Hand == 21:
        print("!Blackjack!")
        summe = guthaben + Einsatz * 2
        return (int(summe), False)
    if wahl == "b":
        while Bank < Hand:
            Bank = Bank + karten()
            print("Bank Karten: " + str(Bank))
            if Bank > 21:
                print("Spieler gewinnt")
                summe = guthaben + Einsatz
                return (int(summe), False)
            if Bank > Hand:
                print("Bank gewinnt")
                summe = guthaben - Einsatz
                return (int(summe), False)
            if Bank == Hand:
                print("Unentschieden")
                return (int(guthaben), False)
            time.sleep(1)
    return (guthaben, True)


def Eingabe(hand):
    x = input("Noch eine karte: a  Keine Karte: b" + "\n").lower()
    if x == "a":
        hand = hand + karten()
        print("Deine Karten: " + str(hand))
    elif x != "a" and x != "b":
        print("Falsche Eingabe!")
    elif x == "b" and Hand == 0:
        print("Erst aufnehmen")
    return (x, hand)


def starten():
    x = input("a. spielen b. Verlassen" + "\n").lower()
    if x == "b":
        print("ok")
        exit()
    return x


def einsatz(guthaben):
    print("Dein Guthaben: " + str(guthaben))
    while True:
        x = input("Einsatz: ")
        if not x.isdigit():
            print("Keine Zahl eingegeben")
        elif int(x) > guthaben:
            print("so viel hast du nicht")
        elif int(x) <= 0:
            print("zu wenig")
        else:
            return int(x)


while True:
    print("\n" + "Black Jack" + "\n")
    if Guthaben == 0:
        print("zu arm")
        break
    x = starten()
    Einsatz = einsatz(Guthaben)
    Hand = 0
    Bank = 0
    if x == "a":
        while True:
            result = Eingabe(Hand)
            Hand = result[1]
            y = winning(result[0], Bank, result[1], Guthaben, Einsatz)
            Guthaben = y[0]
            if y[1] == False:
                break
