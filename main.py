import requests
import time

# --- AYARLAR ---
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"
RAPID_API_KEY = "5d21ec75e8mshd677bd9e11f5b81p15ed7ajsn581a07c02212" # RapidAPI panelinden kopyala

def analiz_et(mac_id):
    # Bu fonksiyon maçın xG ve baskı verilerini çeker
    url = f"https://football-xg-statistics.p.rapidapi.com/stats/{mac_id}"
    headers = {"X-RapidAPI-Key": RAPID_API_KEY, "X-RapidAPI-Host": "football-xg-statistics.p.rapidapi.com"}
    
    try:
        data = requests.get(url, headers=headers).json()
        # rtP Formülümüz: (xG * 50) + Kornerler + İsabetli Şut
        xg_home = float(data.get('home_xg', 0))
        xg_away = float(data.get('away_xg', 0))
        total_rtp = (xg_home + xg_away) * 50 
        
        return round(total_rtp, 2), xg_home, xg_away
    except:
        return 0, 0, 0

def maclari_tara():
    # Mevcut canlı maçları bulur
    url = "https://football-xg-statistics.p.rapidapi.com/matches/live"
    headers = {"X-RapidAPI-Key": RAPID_API_KEY}
    
    try:
        response = requests.get(url, headers=headers).json()
        for mac in response:
            ev = mac['home_team']
            dep = mac['away_team']
            rtp, h_xg, a_xg = analiz_et(mac['id'])
            
            # STRATEJİ: rtP 70'ten büyükse sinyal çak!
            if rtp >= 70:
                mesaj = f"🔥 xG SİNYALİ (rtP: {rtp})\n🏟 {ev} vs {dep}\n📈 Ev xG: {h_xg} | Dep xG: {a_xg}\n🚀 Baskı tavan, gol kapıda!"
                requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}")
                
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    while True:
        maclari_tara()
        time.sleep(600) # API limitini yememek için 10 dk'da bir bak
