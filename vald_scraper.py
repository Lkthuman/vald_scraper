from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

BOT_TOKEN = "7931205039:AAGgCaBrEthLALnJXPWhT_V1_YfD80SvIIA"
CHAT_ID = "7952868775"

URL = "https://www.ticketmaster.fr/fr/manifestation/vald-billet/idmanif/618630"

def send_telegram(msg):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg})

options = Options()
options.add_argument("--headless")  # pour ne pas ouvrir la fenêtre
driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(5)  # laisse la page charger

html = driver.page_source

if "Catégorie 3" in html and "Épuisé" not in html and "Sold Out" not in html:
    send_telegram("🔥 Des places en CATÉGORIE 3 sont DISPONIBLES pour VALD ! 🚀")
else:
    print("❌ Catégorie 3 toujours épuisée...")

driver.quit()
