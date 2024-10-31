from flask import Flask, render_template, request
from myjson import *
import requests
import base64
import os

api = Flask(__name__)

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-exp-0827:generateContent?key="

googleAPIKey = "AIzaSyDqe4mFnJ62eYkMRqjl5v9KyMj4j9H86Es"

api_url = base_url + googleAPIKey

@api.route('/', methods=['GET'])

def index():
    return render_template('index.html')

@api.route('/mansendfile', methods=['POST'])

def mansendfile():
    domanda = request.form['question']
    print("domanda: " + domanda)
    bottone = request.form['yes_no']
    print("bottone: " + bottone)
    

    # Elaborazione domanda
    if domanda == "":
        return render_template('errore_no_domanda.html')
    elif domanda != "":
        # domanda = domanda + " tradotta in italiano"

        # Elaborazione presenza file
        if bottone == 'no':
            jsonDataRequest = {"contents": [{"parts":[{"text": domanda}]}]}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
        else:
            # estenzioni supportate
            extension_supportate: dict = {".pdf": "application/pdf", ".gif": "image/gif", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", "png": "image/png"} 
            #os.listdir prende in input un path di una directory e restituisce una lista di elementi al suo interno
            for f in os.listdir('./file_ricevuti/'):
                os.remove('./file_ricevuti/' + f)
            file = request.files['file']
            # divido il nome originale del file in modo da salvare l'estenzione
            filename, file_extension = os.path.splitext(file.filename)
            # controllo che l'estenzione sia supportata
            if file_extension not in extension_supportate:
                return render_template('file_non_supportato.html')
            # salvo il file con il nome 'file01'
            file.filename = 'file01' + file_extension
            file.save('./file_ricevuti/' + file.filename)
            file_path = './file_ricevuti/' + file.filename
            # trasformo il file in base64
            with open(file_path, "rb") as file_to_read:
                file_base_64 = base64.b64encode(file_to_read.read())
            # A seconda del file che invio prendo il mime_type
            mime_type = extension_supportate[file_extension]
            # Creo la richiesta
            jsonDataRequest = {"contents": [{"parts":[{"text": domanda},{"inline_data": {"mime_type": mime_type, "data": file_base_64}}]}]}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
        # Elaboro la risposta
        if response.status_code == 200:
                response = response.json()
                testo = response['candidates'][0]['content']['parts'][0]['text']
                return render_template('risposta.html', domanda=domanda, testo=testo)
    else:
        return render_template('errore_server.html')
        
            
            
             
    


    


api.run(host="0.0.0.0",port=8085)


