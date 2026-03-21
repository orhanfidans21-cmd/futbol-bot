import requests
import time

TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"
API_KEY = "5d21ec75e8mshd677bd9e11f5b81p15ed7ajsn581a07c02212"

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
                # Test için her canlı maçı atıyoruz abem!
                mesaj = f"✅ BOT AKTİF: {ev} vs {dep} maçı oynanıyor!"
                requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    # Bot açılır açılmaz sana mesaj atacak!
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Abe_bot_simdi_gercekten_uyandi!")
    while True:
        maclari_tara()
        time.sleep(300) # 5 dakikada bir kontrol
