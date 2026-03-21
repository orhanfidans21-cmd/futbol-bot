import requests
import time

# --- HAFIZADAKİ AYARLAR ---
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"
RAPID_API_KEY = "5d21ec75e8mshd677bd9e11f5b81p15ed7ajsn581a07c02212"

def maclari_tara():
    # Football xG Statistics API'sinden canlı maçları ve xG verilerini çekiyoruz
    url = "https://football-xg-statistics.p.rapidapi.com/matches/live"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "football-xg-statistics.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers).json()
        
        # Eğer API'den liste gelirse tara
        if isinstance(response, list):
            for mac in response:
                ev = mac.get('home_team', 'Bilinmiyor')
                dep = mac.get('away_team', 'Bilinmiyor')
                h_xg = float(mac.get('home_xg', 0))
                a_xg = float(mac.get('away_xg', 0))
                dakika = mac.get('minute', '??')
                skor = mac.get('score', '0-0')

                # rtP HESAPLAMA (xG verisini 100 ile çarpıp baskı puanı yapıyoruz)
                # Örn: 0.80 xG varsa rtP = 80 olur.
                rtp_puani = (h_xg + a_xg) * 100

                # STRATEJİ: rtP 70'ten büyükse ve maç hala berabere veya 1 farkla bitiyorsa
                if rtp_puani >= 70:
                    mesaj = (f"🔥 xG BASKI SİNYALİ (rtP: {int(rtp_puani)})\n"
                             f"🏟 {ev} vs {dep}\n"
                             f"⏰ Dakika: {dakika} | Skor: {skor}\n"
                             f"📈 Toplam xG: {round(h_xg + a_xg, 2)}\n"
                             f"🚀 Bu maçta gol kokusu var abem!")
                    
                    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}")
        
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    # Bot başladığında Telegram'a haber versin
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Abe_xG_Botu_Goreve_Basladi!")
    
    while True:
        maclari_tara()
        time.sleep(600) # API limitini korumak için 10 dakikada bir tarar
