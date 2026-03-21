import requests
import time
import os

# Ayarlar (Buraya Telegram bilgilerini girebilirsin veya Render üzerinden bağlayabiliriz)
TOKEN = "TELEGRAM_BOT_TOKEN_BURAYA"
CHAT_ID = "TELEGRAM_ID_BURAYA"

def analiz_et():
    # Burada ücretsiz bir canlı skor API'si kullanacağız
    # Örnek olarak mantığı kuruyorum:
    url = "https://fixturedownload.com/feed/json/epl-2025" # Örnek ücretsiz veri
    try:
        data = requests.get(url).json()
        for mac in data:
            # Senin %90'lık stratejin buraya gelecek
            # Eğer dakika ve baskı verisi uygunsa mesaj at:
            if "Baskı Kriteri" == "Uygun":
                 msg = f"🎯 Sinyal: {mac['HomeTeam']} maçı kriterlere uyuyor!"
                 requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
    except:
        print("Veri çekilemedi...")

while True:
    analiz_et()
    time.sleep(300) # 5 dakikada bir kontrol et
