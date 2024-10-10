import requests
from requests.auth import HTTPBasicAuth

# Funzione per autenticarsi e inserire cittadino
def add_cittadino(url, username, password):
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    data_nascita = input("Data di nascita (gg/mm/aaaa): ")
    cod_fiscale = input("Codice fiscale: ")
    
    nuovo_cittadino = {
        "nome": nome,
        "cognome": cognome,
        "dataNascita": data_nascita,
        "codFiscale": cod_fiscale
    }
    
    response = requests.post(
        url + "/cittadini", 
        json=nuovo_cittadino, 
        auth=HTTPBasicAuth(username, password),
        verify=False  # Disabilita la verifica SSL (solo per testing)
    )
    
    if response.status_code == 201:
        print("Cittadino aggiunto con successo!")
    elif response.status_code == 403:
        print("Permesso negato: utente senza privilegi di scrittura.")
    else:
        print("Errore:", response.status_code, response.text)

# Funzione per ottenere la lista dei cittadini
def get_cittadini(url, username, password):
    response = requests.get(
        url + "/cittadini", 
        auth=HTTPBasicAuth(username, password),
        verify=False  # Disabilita la verifica SSL (solo per testing)
    )
    
    if response.status_code == 200:
        cittadini = response.json()
        for cittadino in cittadini:
            print(f"{cittadino['nome']} {cittadino['cognome']}, Nato il {cittadino['dataNascita']}, CF: {cittadino['codFiscale']}")
    elif response.status_code == 403:
        print("Permesso negato: utente senza privilegi di lettura.")
    else:
        print("Errore:", response.status_code, response.text)

if __name__ == "__main__":
    server_url = "https://127.0.0.1:8080"
    username = input("Inserisci username: ")
    password = input("Inserisci password: ")
    
    while True:
        print("\n1. Visualizza cittadini")
        print("2. Aggiungi cittadino")
        print("3. Esci")
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == '1':
            get_cittadini(server_url, username, password)
        elif scelta == '2':
            add_cittadino(server_url, username, password)
        elif scelta == '3':
            print("Uscita in corso...")
            break
        else:
            print("Opzione non valida. Riprova.")
