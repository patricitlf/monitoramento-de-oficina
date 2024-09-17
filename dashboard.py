import tkinter as tk
from tkinter import ttk
import pyrebase
import os
from dotenv import load_dotenv

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

def atualizar_dashboard(tree):
    tools = db.child("tools").get().val()

    if tools:
        for item in tree.get_children():
            tree.delete(item)

        for key, value in tools.items():
            tree.insert("", "end", values=(value.get("id", "N/A"), value.get("texto", "N/A"), value.get("local_atual", "N/A"), value.get("usage_time", "N/A")))
    else:
        print("Nenhuma ferramenta encontrada no Firebase.")

def criar_dashboard():
    root = tk.Tk()
    root.title("Dashboard de Ferramentas")

    columns = ("ID", "Nome", "Local", "Tempo de Uso")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Local", text="Local")
    tree.heading("Tempo de Uso", text="Tempo de Uso")

    tree.pack(fill="both", expand=True)

    atualizar_dashboard(tree)

    root.mainloop()