
import requests, uuid, sys, re
from datetime import datetime

def bypass_wifi():
    print("[... ] Connecting to Internet...")
    try:
        # Portal URL ကို ရှာဖွေခြင်း
        res = requests.get("http://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html")
        match = re.search(r'sessionId=([a-zA-Z0-9]+)', res.url)
        if match:
            sid = match.group(1)
            # Bypass လုပ်ခြင်း
            requests.get(f"http://portal-as.ruijienetworks.com/api/login?sessionId={sid}&action=login")
            print("[ SUCCESS ✅ ] အင်တာနက် အသုံးပြုနိုင်ပါပြီ။")
        else:
            print("[ ERROR ⚠️ ] WiFi Portal မတွေ့ပါ။")
    except:
        print("[ ERROR ] WiFi ချိတ်ဆက်မှု မရပါ။")

def main():
    device_id = str(uuid.getnode())
    # User ကို Password (boot7777) ရိုက်ခိုင်းခြင်း
    user_code = input("Enter Access Code: ")
    
    # GitHub က Data ကို ဆွဲယူခြင်း
    key_url = "https://raw.githubusercontent.com/SoeHtet-bot8888/Starlink-bypass/main/key.txt"
    try:
        data = requests.get(key_url).text
        found = False
        
        for line in data.splitlines():
            # ပုံစံ: ID|Password|ရက်စွဲ
            if device_id in line:
                parts = line.split('|')
                if parts[1] == user_code: # Password စစ်ဆေးခြင်း
                    found = True
                    # ရက်စွဲစစ်ဆေးခြင်း
                    expiry_date = parts[2]
                    if datetime.now() <= datetime.strptime(expiry_date, "%Y-%m-%d"):
                        print("[ ACCESS GRANTED ✅ ]")
                        bypass_wifi()
                        return
                    else:
                        print("[ EXPIRED ❌ ] သင်၏ သက်တမ်း ကုန်ဆုံးသွားပါပြီ။")
                        return
        
        if not found:
            print("[ ACCESS DENIED ❌ ] ID သို့မဟုတ် Password မှားနေပါသည်။")
            
    except Exception as e:
        print(f"[ ERROR ] {e}")

if __name__ == "__main__":
    main()
