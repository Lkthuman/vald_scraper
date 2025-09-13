import requests
from bs4 import BeautifulSoup

# ⚠️ Remplace par ton vrai token et chat_id
BOT_TOKEN = "7931205039:AAGgCaBrEthLALnJXPWhT_V1_YfD80SvIIA"
CHAT_ID = "7952868775"

URL = "https://www.ticketmaster.fr/fr/manifestation/vald-billet/idmanif/618630"

def send_telegram(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    r = requests.post(url, data=payload)
    print("Envoi Telegram :", r.status_code, r.text)

def check_categorie3():
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")

    # Cherche tous les blocs de catégories
    categories = soup.find_all(string=lambda t: "catégorie 3" in t.lower())

    for cat in categories:
        bloc = cat.parent.get_text(" ", strip=True).lower()
        print("Bloc trouvé :", bloc)  # debug
        if "épuisé" not in bloc and "sold out" not in bloc:
            return True
    return False

if __name__ == "__main__":
    if check_categorie3():
        send_telegram("🔥 Des places en CATÉGORIE 3 sont DISPONIBLES pour VALD ! 🚀")
    else:
        print("❌ Catégorie 3 toujours épuisée...")
