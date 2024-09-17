from rfid_reader import ler_etiqueta
from firebase_config import enviar_dados_firebase, monitorar_tempo_uso
from dashboard import criar_dashboard
from threading import Thread

def main():
    # Simulação de leitura e envio de dados
    id, texto = ler_etiqueta()
    local_atual = "A"  # Local simulado
    enviar_dados_firebase(id, texto, local_atual)

    # Iniciar monitoramento e dashboard em threads separadas
    monitoramento_thread = Thread(target=monitorar_tempo_uso)
    monitoramento_thread.start()

    dashboard_thread = Thread(target=criar_dashboard)
    dashboard_thread.start()

if __name__ == "__main__":
    main()
