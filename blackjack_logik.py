import random

def erstelle_deck():
    #Deck aufbauen
    werte = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(werte)
    return werte

def berechne_punkte(hand):
    """Berechnet Punkte und berücksichtigt die As-Regel."""
    score = sum(hand)
    # Wenn über 21 und ein Ass (11) da ist, ziehe 10 ab
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def prüfe_gewinner(spieler_score, dealer_score):
    if spieler_score > 21:
        return "verloren"
    if dealer_score > 21 or spieler_score > dealer_score:
        return "sieg"
    if spieler_score < dealer_score:
        return "verloren"
    return "unentschieden"
