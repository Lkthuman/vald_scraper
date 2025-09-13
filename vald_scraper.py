import requests
from bs4 import BeautifulSoup
import os

# 🔑 Récupération des secrets GitHub (ou variables d'environnement locales)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# 🎫 URL Ticketmaster (Vald)
URL = "https://www.ticketmaster.fr/fr/manifestation/vald-billet/idmanif/618630"

def send_telegram(msg: str):
    """Envoie un message Telegram via le bot."""
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ BOT_TOKEN ou CHAT_ID manquants")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    try:
        requests.post(url, data=payload, timeout=10)
        print("✅ Alerte envoyée sur Telegram")
    except Exception as e:
        print(f"❌ Erreur envoi Telegram : {e}")

def check_fosse_normale() -> bool:
    """Vérifie si la fosse normale est dispo."""
    try:
        resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        txt = soup.get_text().lower()
        # Vérifie présence de "fosse" et absence de "épuisée" ou "sold out"
        return "fosse" in txt and "épuisée" not in txt and "sold out" not in txt
    except Exception as e:
        print(f"❌ Erreur lors du scraping : {e}")
        return False

if __name__ == "__main__":
    dispo = check_fosse_normale()
    if dispo:
        send_telegram("🔥 Fosse normale dispo pour VALD ! Dépêche-toi 🚀")
    else:
        print("❌ Pas dispo pour l’instant")
