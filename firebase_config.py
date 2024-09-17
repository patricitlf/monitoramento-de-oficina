import pyrebase
import os
import time
from dotenv import load_dotenv
import uuid

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configuração do Firebase
config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Limite máximo de ferramentas
LIMITE_FERRAMENTAS = 30

def enviar_dados_firebase(id, texto, local_atual):
    ferramentas = db.child("tools").get().val()

    if ferramentas and len(ferramentas) >= LIMITE_FERRAMENTAS:
        print("Limite de ferramentas atingido!")
        return

    id_unico = str(uuid.uuid4())
    ferramenta = {
        "id": id_unico,
        "texto": texto,
        "local_atual": local_atual,
        "usage_time": 0
    }

    db.child("tools").push(ferramenta)

def monitorar_tempo_uso():
    while True:
        ferramentas = db.child("tools").get().val()

        if ferramentas:
            for key, value in ferramentas.items():
                print(f"Ferramenta ID: {value['id']}, Tempo de uso: {value.get('usage_time', 0)}")
        else:
            print("Nenhuma ferramenta encontrada no Firebase.")

        time.sleep(60)

