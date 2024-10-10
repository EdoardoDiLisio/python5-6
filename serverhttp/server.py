from flask import Flask, render_template, request

utenti = [["Edoardo", "Bilbo", "edoardo@gmail.com" ,"DDDRRR50K60G000F", "0"], ["Pippo" ,"Frodo" ,"pippo@gmail.com" ,"DDDRRR50k60v000r", "0"], ["Baudo" ,"Bilbo" ,"baudo@gmail.com" ,"DDDRRR50k60v000r", "0"]]

api = Flask("__name__")

@api.route('/registrati', methods=['POST'])
def submit():
    nome = request.form['nome']
    cognome = request.form['cognome']
    email = request.form['email']
    codice_fiscale = request.form['codice_fiscale']
    
    # Verifica se l'utente esiste nella lista
    for utente in utenti:
        print(utente)
        if (utente[0] == nome and
            utente[1] == cognome and
            utente[2] == email and
            utente[3] == codice_fiscale):
                return render_template('regok.html')  # Se i dati corrispondono, carica reggok.html

    return render_template('regko.html')



@api.route('/', methods=['GET'])

def index():
    return render_template('index.html')

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)

print(nome, cognome, email, codice_fiscale)