import requests
import time

# Bilgilerini buraya tırnak içinde yaz
TOKEN = "8122918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"

def test_mesaji():
    print("Telegram'a mesaj gönderiliyor...")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Abe_test_basarili_baglanti_kuruldu!"
    try:
        r = requests.get(url)
        print(f"Sonuç: {r.status_code}")
    except Exception as e:
        print(f"Hata: {e}")

# Botu başlat ve her 1 dakikada bir mesaj at
if __name__ == "__main__":
    while True:
        test_mesaji()
        time.sleep(60)
