import requests
import time
import os

# Senin bilgilerini buraya tırnak içinde yazdım
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"

def mesaj_at():
    text = "Abe_sonunda_baglandim_analiz_hazir!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    try:
        requests.get(url)
        print("Mesaj gönderildi!")
    except:
        print("Hata!")

if __name__ == "__main__":
    # Render'ın "Port" hatası vermemesi için bu 2 satır şart:
    print("Bot baslatiliyor...")
    mesaj_at() # Çalışır çalışmaz ilk mesajı atar
    
    while True:
        # Botun kapanmaması için döngüde tutuyoruz
        time.sleep(60)
