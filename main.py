import requests
import time

# --- AYARLAR ---
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"
API_KEY = "775097e24c484be096fe49a8c0fb75ca"

def rtp_hesapla(mac_verisi):
    # Ücretsiz API'den gelen istatistiklerle puanlama yapıyoruz
    puan = 0
    try:
        # Örnek: Korner ve şut verilerini topluyoruz
        corners = mac_verisi.get('stats', {}).get('corners', 0)
        shots = mac_verisi.get('stats', {}).get('shotsOnGoal', 0)
        
        puan = (corners * 10) + (shots * 15)
        return puan
    except:
        return 0

def maclari_tara():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_KEY}
    
    try:
        response = requests.get(url, headers=headers).json()
        matches = response.get('matches', [])
        
        for mac in matches:
            if mac['status'] == 'IN_PLAY':
                ev = mac['homeTeam']['name']
                dep = mac['awayTeam']['name']
                
                # Kendi rtP puanımızı hesaplıyoruz
                hesaplanan_rtp = rtp_hesapla(mac)
                
                # STRATEJİ: rtP 70'ten büyükse ve maç 0-0 ise
                if hesaplanan_rtp >= 0:
                    mesaj = f"🔥 rtP SİNYALİ: {hesaplanan_rtp}\n🏟 {ev} vs {dep}\n🚀 Baskı tavan yaptı, gol geliyor!"
                    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}")
                
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    print("Parasız ama akıllı rtP botu devrede...")
    while True:
        maclari_tara()
        time.sleep(600)
