def tarkista_iban(tilinumero):
    # Poista välilyönnit ja tarkista pituus
    tilinumero = tilinumero.replace(" ", "")
    if len(tilinumero) != 18:
        return False

    # Siirrä maatunnus ja tarkistenumero loppuun
    tilinumero = tilinumero[4:] + tilinumero[:4]

    # Korvaa kirjaimet numeroilla
    tilinumero_numeroina = ""
    for merkki in tilinumero:
        if merkki.isdigit():
            tilinumero_numeroina += merkki
        else:
            tilinumero_numeroina += str(ord(merkki.upper()) - ord('A') + 10)

    # Laske jakojäännös
    jakojäännös = int(tilinumero_numeroina) % 97

    return jakojäännös == 1

# Testausta varten
tilinumerot = [
    "FI56 0002 1980 5789 69",
    "FI55 2515 8869 5718 77",
    "FI95 1786 3769 6731 97",
    "FI07 5762 9588 4181 13",
    "FI52 8592 6874 8382 54",
    "SE76 9449 8965 5115 5139 7733"
]

for tilinumero in tilinumerot:
    if tarkista_iban(tilinumero):
        print(f"{tilinumero} -> True")
    else:
        print(f"{tilinumero} -> False")
