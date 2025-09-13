import requests

# ⚠️ Mets ton vrai token et chat_id ici
BOT_TOKEN = "7931205039:AAGgCaBrEthLALnJXPWhT_V1_YfD80SvIIA"
CHAT_ID = "7952868775"

def send_telegram(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    r = requests.post(url, data=payload)
    print("Statut :", r.status_code, r.text)

if __name__ == "__main__":
    send_telegram("✅ Test : ton bot Telegram fonctionne ! 🚀")
