import requests
import time

# --- AYARLAR ---
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE" # Senin Token'ın
CHAT_ID = "1157525263" # Senin ID'n
API_KEY = "775097e24c484be096fe49a8c0fb75ca"

def maclari_tara():
    # Canlı maçları çeken adres
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_KEY}
    
    try:
        response = requests.get(url, headers=headers).json()
        matches = response.get('matches', [])
        
        for mac in matches:
            # Sadece canlı (IN_PLAY) olan maçlara bakıyoruz
            if mac['status'] == 'IN_PLAY':
                ev_sahibi = mac['homeTeam']['name']
                deplasman = mac['awayTeam']['name']
                skor_ev = mac['score']['fullTime']['home']
                skor_dep = mac['score']['fullTime']['away']
                
                # rtP ANALİZ MANTIĞI: 
                # Ücretsiz API'ler anlık baskı (rtP) verisini her zaman vermez.
                # Bu yüzden skor takibi ve önemli anlara göre botu kuruyoruz.
                
                mesaj = f"⚽ CANLI MAÇ SİNYALİ\n\n🏟 {ev_sahibi} {skor_ev} - {skor_dep} {deplasman}\n📈 Durum: Maç devam ediyor!\n🚀 rtP Analizi Bekleniyor..."
                
                # Telegram'a gönder
                requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}")
                
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    print("Analiz botu devreye girdi, maçlar taranıyor...")
    while True:
        maclari_tara()
        time.sleep(600) # Ücretsiz sınır dolmasın diye 10 dakikada bir kontrol eder
