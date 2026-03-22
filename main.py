import requests
import time

# --- AYARLAR ---
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"
API_KEY = "B593e35b098c8cd3ddb1ec1da155c7d3fa88dcad76edd70532018a90a91c9133"

def analiz_et():
    # Canlı maçları ve istatistikleri çeken ana fonksiyon
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers).json()
        fixtures = response.get('response', [])
        
        if not fixtures:
            print("Su an analiz edilecek canli mac bulunamadi.")
            return

        for mac in fixtures:
            f_id = mac['fixture']['id']
            ev = mac['teams']['home']['name']
            dep = mac['teams']['away']['name']
            dakika = mac['fixture']['status']['elapsed']
            skor = f"{mac['goals']['home']}-{mac['goals']['away']}"

            # ISTAITSTIKLERI CEK (rtP icin lazim olanlar)
            stats_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/statistics"
            stats_res = requests.get(stats_url, headers=headers, params={"fixture": f_id}).json()
            
            corners, shots, dangerous_attacks = 0, 0, 0
            for team_stats in stats_res.get('response', []):
                for s in team_stats['statistics']:
                    if s['type'] == 'Corner Kicks': corners += (s['value'] or 0)
                    if s['type'] == 'Shots on Goal': shots += (s['value'] or 0)
                    if s['type'] == 'Dangerous Attacks': dangerous_attacks += (s['value'] or 0)

            # rtP HESABI: (Korner * 3) + (Sut * 5) + (Tehlikeli Atak * 1)
            rtp_puani = (corners * 3) + (shots * 5) + (dangerous_attacks * 1)

            # SINYAL: rtP 70'ten büyükse Telegram'a yardır!
            if rtp_puani >= 70:
                mesaj = (f"🚀 **rtP BASKI SINYALI: {int(rtp_puani)}**\n"
                         f"🏟 {ev} vs {dep}\n"
                         f"⏰ Dakika: {dakika} | Skor: {skor}\n"
                         f"🚩 Korner: {corners} | 🎯 Sut: {shots}\n"
                         f"🔥 Tehlikeli Atak: {dangerous_attacks}\n"
                         f"Abe gol yaklasiyor!")
                requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}")

    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    # Bot acildiginda bir selam versin
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Abe_Analiz_Motoru_Calisti_Mac_Bekliyorum!")
    while True:
        analiz_et()
        time.sleep(300) # 5 dakikada bir kontrol
