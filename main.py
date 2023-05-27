import random

# Funzione per disegnare la scacchiera
def disegna_scacchiera(scacchiera):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(scacchiera[i][j], end=" | ")
        print("\n-------------")

# Funzione per controllare la vittoria
def controlla_vittoria(scacchiera, simbolo):
    # Controllo delle righe
    for i in range(3):
        if (riga := scacchiera[i]) == [simbolo] * 3:
            return True
    # Controllo delle colonne
    for j in range(3):
        if [scacchiera[i][j] for i in range(3)] == [simbolo] * 3:
            return True
    # Controllo delle diagonali
    if [scacchiera[i][i] for i in range(3)] == [simbolo] * 3:
        return True
    if [scacchiera[i][2-i] for i in range(3)] == [simbolo] * 3:
        return True
    return False

# Funzione per il turno dell'IA
def turno_ia(scacchiera, simbolo_giocatore, simbolo_ia):
    # Controllo se l'IA può vincere al prossimo turno
    for i in range(3):
        for j in range(3):
            if scacchiera[i][j] == "-":
                scacchiera[i][j] = simbolo_ia
                if controlla_vittoria(scacchiera, simbolo_ia):
                    return
                else:
                    scacchiera[i][j] = "-"

    # Controllo se il giocatore può vincere al prossimo turno e lo blocco
    for i in range(3):
        for j in range(3):
            if scacchiera[i][j] == "-":
                scacchiera[i][j] = simbolo_giocatore
                if controlla_vittoria(scacchiera, simbolo_giocatore):
                    scacchiera[i][j] = simbolo_ia
                    return
                else:
                    scacchiera[i][j] = "-"

    # Se nessuna mossa vincente è possibile, scelgo una posizione casuale
    posizioni_disponibili = []
    for i in range(3):
        for j in range(3):
            if scacchiera[i][j] == "-":
                posizioni_disponibili.append((i, j))
    if posizioni_disponibili:
        posizione_scelta = random.choice(posizioni_disponibili)
        scacchiera[posizione_scelta[0]][posizione_scelta[1]] = simbolo_ia

# Funzione principale del gioco
def gioca_tris():
    scacchiera = [["-", "-", "-"],
                  ["-", "-", "-"],
                  ["-", "-", "-"]]

    simbolo_giocatore = "X"
    simbolo_ia = "O"

    turno_giocatore = True

    while True:
        disegna_scacchiera(scacchiera)

        if turno_giocatore:
            riga = int(input("Inserisci la riga (0-2): "))
            colonna = int(input("Inserisci la colonna (0-2): "))
            if scacchiera[riga][colonna] != "-":
                print("Posizione non valida. Riprova.")
                continue

            scacchiera[riga][colonna] = simbolo_giocatore

            if controlla_vittoria(scacchiera, simbolo_giocatore):
                disegna_scacchiera(scacchiera)
                print("Hai vinto!")
                break

            turno_giocatore = False
        else:
            turno_ia(scacchiera, simbolo_giocatore, simbolo_ia)

            if controlla_vittoria(scacchiera, simbolo_ia):
                disegna_scacchiera(scacchiera)
                print("Hai perso!")
                break

            turno_giocatore = True

        if all(scacchiera[i][j] != "-" for i in range(3) for j in range(3)):
            disegna_scacchiera(scacchiera)
            print("È un pareggio!")
            break

gioca_tris()
