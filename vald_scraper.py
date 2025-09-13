import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("7931205039:AAGgCaBrEthLALnJXPWhT_V1_YfD80SvIIA")   # Ton token Telegram
CHAT_ID = os.getenv("7952868775")       # Ton chat_id Telegram

URL = "https://www.ticketmaster.fr/fr/manifestation/vald-billet/idmanif/618630"

def send_telegram(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=payload)

def check_fosse_normale() -> bool:
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    txt = soup.get_text().lower()
    return "fosse" in txt and "épuisée" not in txt and "sold out" not in txt

if __name__ == "__main__":
    if check_fosse_normale():
        send_telegram("🔥 Fosse normale dispo pour VALD ! 🚀")
    else:
        print("❌ Pas dispo")
