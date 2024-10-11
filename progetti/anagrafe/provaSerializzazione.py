from myjson import JsonSerialize, JsonDeserialize

sFile = "./prova.json"
myDict = {"nome":"Mario", "cognome":"Rossi"}
print(type(myDict))
serializzazione = JsonSerialize(myDict, sFile)
if serializzazione == 0:
    print("Operazione andata a buon fine")
elif serializzazione == 1:
    print("Errore, dati errati, atteso dict")
else:
    print("Errore salvataggio su file")
