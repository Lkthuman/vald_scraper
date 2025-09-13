import requests
import os

# Récupération des secrets (ou tu peux mettre directement ton token et chat_id pour tester)
BOT_TOKEN = os.getenv("BOT_TOKEN")  # ou remplace par "123456:ABC..."
CHAT_ID = os.getenv("CHAT_ID")      # ou remplace par ton chat_id

def send_telegram(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    try:
        response = requests.post(url, data=payload, timeout=10)
        if response.status_code == 200:
            print("✅ Message envoyé avec succès !")
        else:
            print(f"❌ Erreur {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    send_telegram("Test du bot Telegram : ça fonctionne ! 🚀")
