import requests, json, sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
googleApiKey = "AIzaSyBUNGwjvWKB6K9dFxDLUcNoQggUlq89ElY"

def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova piÃ¹ tardi.")

print("Benvenuti nella mia Generative AI")

print("\nImmettere le credenziali: ")


iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Creare una favola")
    print("2. Rispondere ad una domanda")
    print("3. Rispondere ad una domanda su un file img")
    print("4. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        argomentoFav = input("Inserisci l'argomento della favola: ")
        api_url = base_url + googleApiKey
        jsonDataRequest = {"contents": [{"parts":[{"text": argomentoFav}]}]}
        #EseguiOperazione(1, api_url, jsonDataRequest)
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        if response.status_code==200:
            response = response.json()
            #print(response.json())
            testo = response['candidates'][0]['content']['parts'][0]['text']
            print(testo)

    elif iOper == 2:
        print("Richiesta dati cittadino")

    elif iOper == 3:
        print("Modifica cittadino")
        
    elif iOper == 4:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")