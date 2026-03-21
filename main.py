import requests
import time

TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"

def mesaj_at():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Abe_test_basarili!"
    try:
        requests.get(url)
        print("Mesaj gönderildi!")
    except:
        print("Hata!")

if __name__ == "__main__":
    while True:
        mesaj_at()
        time.sleep(60)
