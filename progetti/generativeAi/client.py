from myjson import *
import requests
import subprocess
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def ComponiJsonPerImmagine(sImagePath):
    subprocess.run(["rm", "./image.jpg"])
    subprocess.run(["rm", "./request.json"])
    subprocess.run(["cp", sImagePath,"./image.jpg"])
    subprocess.run(["bash", "./creajsonpersf.sh"])

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="

googleAPIKey = "AIzaSyDqe4mFnJ62eYkMRqjl5v9KyMj4j9H86Es"

api_url = base_url + googleAPIKey

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
    print("3. Rispondere ad una domanda su file img")
    print("4. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        argomento_favola = input("Aggiungi un argomento per la favola: ")
        jsonDataRequest = {"contents": [{"parts":[{"text": argomento_favola}]}]}
        # EseguiOperazione(1, api_url, jsonDataRequest)
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        if response.status_code == 200:
            response = response.json()
            #print(response.json())
            testo = response['candidates'][0]['content']['parts'][0]['text']
            print(testo)

    elif iOper == 2:
        print("Rispondere ad una domanda")
        

    elif iOper == 3:
        print("Rispondere ad una domanda su file img")       
        immagine = input("Inserisci il path competo del file che vuoi analizzare: ")
        domanda = input("Inserisci la domanda: ")
        domanda = domanda + "tradotto in italiano"
        ComponiJsonPerImmagine(immagine)
        RequestJson = JsonDeserialize("request.json")
        RequestJson['contents'][0]['parts'][0]['text'] = domanda
        response = requests.post(api_url, json=RequestJson, verify=False)
        print()
        if response.status_code == 200:
            response = response.json()
            testo = response['candidates'][0]['content']['parts'][0]['text']
            print(testo)      

    elif iOper == 4:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")