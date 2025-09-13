from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

BOT_TOKEN = "7931205039:AAGgCaBrEthLALnJXPWhT_V1_YfD80SvIIA"
CHAT_ID = "7952868775"
URL = "https://www.ticketmaster.fr/fr/manifestation/vald-billet/idmanif/618630"

def send_telegram(msg):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg})

options = Options()
options.add_argument("--headless")  # mode sans fenêtre
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(URL)
time.sleep(5)  # laisse le JS charger
html = driver.page_source

if "Catégorie 3" in html and "Épuisé" not in html and "Sold Out" not in html:
    send_telegram("🔥 Des places en CATÉGORIE 3 sont DISPONIBLES pour VALD ! 🚀")
else:
    print("❌ Catégorie 3 toujours épuisée...")

driver.quit()
