from flask import Flask, request, jsonify
from functools import wraps
import ssl

app = Flask(__name__)

# Dati degli utenti per l'autenticazione di base (esempio)
USERS = {
    "reader": "password_reader",   # Utente con permessi di sola lettura
    "writer": "password_writer",   # Utente con permessi di scrittura
}

# Dati dell'anagrafe comunale (mock data)
cittadini = [
    {"nome": "Mario", "cognome": "Rossi", "dataNascita": "20/02/1990", "codFiscale": "dfcged90b28h501u"},
    {"nome": "Mario", "cognome": "Bianchi", "dataNascita": "20/02/1990", "codFiscale": "dfcged90b28h501u"},
    {"nome": "Giuseppe", "cognome": "Verdi", "dataNascita": "20/12/1956", "codFiscale": "dfcvds90b28h501u"}
]

# Funzione per autenticare gli utenti tramite Basic Authentication
def check_auth(username, password):
    return USERS.get(username) == password

# Decoratore per richiedere l'autenticazione
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated

# Rotta per ottenere i cittadini (solo lettura)
@app.route('/cittadini', methods=['GET'])
@require_auth
def get_cittadini():
    auth = request.authorization
    if auth.username == "reader":
        return jsonify(cittadini)
    else:
        return jsonify({"message": "Permission denied"}), 403

# Rotta per aggiungere un cittadino (scrittura)
@app.route('/cittadini', methods=['POST'])
@require_auth
def add_cittadino():
    auth = request.authorization
    if auth.username == "writer":
        new_cittadino = request.get_json()
        cittadini.append(new_cittadino)
        return jsonify({"message": "Cittadino aggiunto con successo"}), 201
    else:
        return jsonify({"message": "Permission denied"}), 403

if __name__ == '__main__':
    # Configurazione HTTPS con certificati (devi avere il certificato e la chiave)
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('cert.pem', 'key.pem')
    
    # Avvia il server su HTTPS
    app.run(host="127.0.0.1", port=8080, ssl_context=context)
