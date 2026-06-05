
import requests, uuid, sys, re, urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def bypass_wifi():
    print("[... ] Connecting to Internet...")
    try:
        res = requests.get("http://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html", verify=False)
        match = re.search(r'sessionId=([a-zA-Z0-9]+)', res.url)
        if match:
            sid = match.group(1)
            requests.get(f"http://portal-as.ruijienetworks.com/api/login?sessionId={sid}&action=login", verify=False)
            print("[ SUCCESS ✅ ] အင်တာနက် အသုံးပြုနိုင်ပါပြီ။")
        else:
            print("[ ERROR ⚠️ ] WiFi Portal မတွေ့ပါ။")
    except Exception as e:
        print(f"[ ERROR ] {e}")

def main():
    device_id = str(uuid.getnode())
    print(f"--- Login System ---")
    print(f"Your Device ID: {device_id}")
    
    user_code = input("Enter Access Code: ")
    
    key_url = "https://raw.githubusercontent.com/SoeHtet-bot8888/Starlink-bypass/main/key.txt"
    try:
        data = requests.get(key_url, verify=False).text
        found = False
        
        for line in data.splitlines():
            # ပုံစံ: ID|Password|YYYY-MM-DD
            if device_id in line:
                parts = line.split('|')
                if parts[1] == user_code:
                    found = True
                    # ရက်စွဲစစ်ဆေးခြင်း
                    expiry_date = datetime.strptime(parts[2], "%Y-%m-%d")
                    if datetime.now() <= expiry_date:
                        print(f"[ ACCESS GRANTED ✅ ] သက်တမ်း: {parts[2]} အထိ")
                        bypass_wifi()
                        return
                    else:
                        print(f"[ EXPIRED ❌ ] သက်တမ်းကုန်ဆုံးသွားပါပြီ ({parts[2]})။")
                        return
        
        if not found:
            print("[ ACCESS DENIED ❌ ] ID သို့မဟုတ် Password မှားနေပါသည်။")
            
    except Exception as e:
        print(f"[ ERROR ] ချိတ်ဆက်မှုကို စစ်ဆေးပါ။ ({e})")

if __name__ == "__main__":
    main()
