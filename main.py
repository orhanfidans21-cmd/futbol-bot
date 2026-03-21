import requests
import time

# --- AYARLAR ---
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"
RAPID_API_KEY = "5d21ec75e8mshd677bd9e11f5b81p15ed7ajsn581a07c02212"

def maclari_tara():
    url = "https://football-xg-statistics.p.rapidapi.com/matches/live"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "football-xg-statistics.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers).json()
        
        if isinstance(response, list):
            for mac in response:
                ev = mac.get('home_team', 'Bilinmiyor')
                dep = mac.get('away_team', 'Bilinmiyor')
                h_xg = float(mac.get('home_xg', 0))
                a_xg = float(mac.get('away_xg', 0))
                skor = mac.get('score', '0-0')
                dakika = mac.get('minute', '??')

                # rtP HESABI: Toplam xG'yi 100 ile çarpıp baskı puanı yapıyoruz
                # Örn: 0.75 xG varsa rtP = 75 olur.
                rtp_puani = (h_xg + a_xg) * 100

                # ANALİZ FİLTRESİ: Sadece baskı 70'i geçerse haber ver!
                if rtp_puani >= 70:
                    mesaj = (f"🔥 **rtP ANALİZ SİNYALİ: {int(rtp_puani)}**\n\n"
                             f"🏟 {ev} vs {dep}\n"
                             f"⏰ Dakika: {dakika} | Skor: {skor}\n"
                             f"📈 Toplam xG: {round(h_xg + a_xg, 2)}\n\n"
                             f"🚀 Abe bu maçta baskı tavan, gol kapıda!")
                    
                    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}&parse_mode=Markdown")
        
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    while True:
        maclari_tara()
        time.sleep(600) # 10 dakikada bir kontrol (Limiti aşmamak için)
