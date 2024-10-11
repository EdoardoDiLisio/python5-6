from flask import Flask, json, request
from myjson import JsonSerialize,JsonDeserialize


lListaCampil = ["nome", "cognome", "data nascita", "codice fiscale"]
# if campoRicevutoDalClient in lListaCampi:
    


Anagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type=="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        #carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(Anagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe,Anagrafe)
            jResponse = {"Error":"000", "Msg": "ok"}
            return json.dumps(jResponse),200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale gia presente in anagrafe"}
            return json.dumps(jResponse),200
    else:
        return "Errore, formato non riconosciuto",401
    #controlla che il cittadino non Ã¨ gia presente in anagrafe
    #rispondi

@api.route('/get_cittadino', methods = ['POST'])
def GestisciGetCittadino():
    # gestisco la richiesta
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata" + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto" + sCodiceFiscale)
    # carico l'anagrafe
        dAnagrafe = JsonDeserialize(Anagrafe)
        if sCodiceFiscale in dAnagrafe:
            dJsonRespons = dAnagrafe[sCodiceFiscale]
            return json.dumps(dJsonRespons),200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale gia presente in anagrafe"}
            return json.dumps(jResponse),200




api.run(host="127.0.0.1", port=8080)