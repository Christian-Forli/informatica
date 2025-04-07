import pandas as pd
import random

pokemon_data = pd.read_csv('Esercitazioni/pokemon.csv1' \')
punti_utente = 100
collezione = []

probabilita_rarita = ['Comune'] * 70 + ['Non Comune'] * 20 + ['Rara'] * 9 + ['Ultra Rara'] * 1

def apri_pacchetto():
    pacchetto = []
    punti_guadagnati = 0
    i = 0
    while i < 5:
        rarita_scelta = random.choice(probabilita_rarita)
        carte_disponibili = pokemon_data[pokemon_data['Rarità'] == rarita_scelta]
        if len(carte_disponibili) == 0:
            print("Nessuna carta disponibile per la rarità:", rarita_scelta)
        else:
            carta = carte_disponibili.iloc[random.randint(0, len(carte_disponibili) - 1)]
            pacchetto.append(carta.to_dict())
            if rarita_scelta == 'Comune':
                punti_guadagnati += 1
            elif rarita_scelta == 'Non Comune':
                punti_guadagnati += 10
            elif rarita_scelta == 'Rara':
                punti_guadagnati += 30
            elif rarita_scelta == 'Ultra Rara':
                punti_guadagnati += 104
            i += 1
    return pacchetto, punti_guadagnati

def mostra_collezione():
    if len(collezione) == 0:
        print("La tua collezione è vuota.")
    else:
        for carta in collezione:
            print(carta)

while True:
    print("\nCosa vuoi fare?")
    print("1. Apri un pacchetto")
    print("2. Mostra collezione")
    print("3. Mostra punti")
    print("4. Esci")
    scelta = input("Inserisci la tua scelta: ")

    if scelta == "1":
        if punti_utente >= 10:
            punti_utente -= 10
            pacchetto, punti_guadagnati = apri_pacchetto()
            collezione.extend(pacchetto)
            punti_utente += punti_guadagnati
            print("Hai aperto un pacchetto!")
            for carta in pacchetto:
                print(carta)
            print(f"Hai guadagnato {punti_guadagnati} punti!")
            print(f"Punti totali: {punti_utente}")
        else:
            print("Non hai abbastanza punti per aprire un pacchetto.")
    elif scelta == "2":
        mostra_collezione()
    elif scelta == "3":
        print(f"Hai {punti_utente} punti.")
    elif scelta == "4":
        print("Grazie per aver giocato a Pokémon!")
        break
    else:
        print("Inserisci un valore valido.")