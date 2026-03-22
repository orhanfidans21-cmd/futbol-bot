import requests
import time

# --- AYARLAR ---
TOKEN = "8722918294:AAEcpreA9fn9qtVXz5YBBAC7M19jo8-KUTE"
CHAT_ID = "1157525263"
API_KEY = "B593e35b098c8cd3ddb1ec1da155c7d3fa88dcad76edd70532018a90a91c9133"

def test_et():
    # Bu adres API-Football'un standart canlı maç listesidir
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers).json()
        if "response" in response and len(response["response"]) > 0:
            mac_sayisi = len(response["response"])
            mesaj = f"✅ ANAHTAR CALISIYOR! Su an canlıda {mac_sayisi} maç var abem."
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mesaj}")
            return True
        else:
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=❌ Anahtar kabul edildi ama canlı maç verisi boş dönüyor.")
            return False
    except Exception as e:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=⚠️ Bağlantı hatası: {str(e)[:50]}")
        return False

if __name__ == "__main__":
    test_et()
