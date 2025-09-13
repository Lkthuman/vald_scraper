import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")   # Ton token Telegram
CHAT_ID = os.getenv("CHAT_ID")       # Ton chat_id Telegram

URL = "https://www.ticketmaster.fr/fr/manifestation/vald-billet/idmanif/618630"

def send_telegram(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=payload)

def check_categorie3() -> bool:
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    txt = soup.get_text().lower()

    # Vérifie si "catégorie 3" existe et n’est pas marqué comme épuisé
    return "catégorie 3" in txt and "épuisé" not in txt and "sold out" not in txt

if __name__ == "__main__":
    if check_categorie3():
        send_telegram("🔥 Des places en CATÉGORIE 3 sont DISPONIBLES pour VALD ! 🚀")
    else:
        print("❌ Catégorie 3 toujours épuisée...")
