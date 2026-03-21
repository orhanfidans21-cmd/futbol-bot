import requests
import time

# Buradaki bilgileri resimdeki gibi (tırnak içinde) doldur
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE" # Kendi Token'ını yaz
CHAT_ID = "1157525263"        # Kendi ID'ni yaz

def test_mesaji_gonder():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Abe_mesaj_geldi_mi?"
    try:
        requests.get(url)
        print("Telegram'a mesaj gönderildi!")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Bot her 1 dakikada bir sana mesaj atacak
while True:
    test_mesaji_gonder()
    time.sleep(60)
