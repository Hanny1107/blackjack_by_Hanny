from blackjack_logik import erstelle_deck, berechne_punkte, prüfe_gewinner


def spiel_starten():
    print("=== Willkommen in Hannys Casino beim Blackjack-Modell ===")
    name = input("Dein Name: ") or "Spieler"
    konto = 100

    while konto > 0:
        print(f"\nDein Kontostand: {konto} Chips")
        einsatz = input("Dein Einsatz: ")

        if not einsatz.isdigit() or int(einsatz) <= 0 or int(einsatz) > konto:
            print("Ungültiger Einsatz!")
            continue

        einsatz = int(einsatz)
        deck = erstelle_deck()
        spieler_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Spieler-Zug
        while berechne_punkte(spieler_hand) < 21:
            print(f"Deine Hand: {spieler_hand} (Score: {berechne_punkte(spieler_hand)})")
            print(f"Dealer zeigt: {dealer_hand[0]}")
            wahl = input("Noch eine Karte? (j/n): ").lower()
            if wahl == 'j':
                spieler_hand.append(deck.pop())
            else:
                break

        # Anzeige der finalen Hand (auch bei über 21)
        spieler_score = berechne_punkte(spieler_hand)
        print(f"\nDeine finale Hand: {spieler_hand} (Score: {spieler_score})")

        # Auswertung
        if spieler_score <= 21:
            while berechne_punkte(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            dealer_score = berechne_punkte(dealer_hand)
            print(f"Dealer Hand: {dealer_hand} (Score: {dealer_score})")

    
            ergebnis = prüfe_gewinner(spieler_score, dealer_score)
        else:
            print("Über 21! VERZOCKT!.")
            ergebnis = "verloren"

        # Konto-Logik
        if ergebnis == "sieg":
            print(f"Sieg! Du gewinnst {einsatz}. Der Dealer freut sich über Trinkgeld.")
            konto += einsatz
        elif ergebnis == "verloren":
            print("Verloren! Der Einsatz ist weg. Schade für dich :/")
            konto -= einsatz
        else:
            print("Unentschieden! Einsatz zurück.")

        if input("\nNoch eine Runde? (j/n): ").lower() != 'j':
            break

    print(f"\nSpiel beendet. Dein Endstand: {konto} Chips.")


if __name__ == "__main__":
    spiel_starten()
