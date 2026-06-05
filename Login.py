import requests, uuid, re, urllib3
from datetime import datetime

# SSL Error မတက်အောင် ပိတ်ထားသည်
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def bypass_wifi():
    print("[... ] Connecting to Internet...")
    try:
        # Ruijie Portal URL
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
    print(f"Your Device ID: {device_id}")
    user_code = input("Enter Access Code: ").strip()
    
    # [!] ဒီနေရာမှာ သင့် Google Sheet ရဲ့ Link ကို ထည့်ပါ
    sheet_url ="https://docs.google.com/spreadsheets/d/1bMDcruZ54e_9eAoxDZgySsL-nLDCdOrB3aE_jHpdWLA/export?format=csv" "YOUR_GOOGLE_SHEET_CSV_LINK_HERE" 
    
    try:
        response = requests.get(sheet_url, verify=False)
        data = response.text
        
        # Google Sheet က data တွေကို စစ်ဆေးမယ်
        for line in data.splitlines()[1:]: 
            parts = [p.strip() for p in line.split(',')]
            if len(parts) >= 3:
                # Device ID | Password | Date (YYYY-MM-DD)
                if parts[0] == str(device_id) and parts[1] == user_code:
                    if datetime.now() <= datetime.strptime(parts[2], "%Y-%m-%d"):
                        print("[ ACCESS GRANTED ✅ ]")
                        bypass_wifi()
                        return
                    else:
                        print("[ EXPIRED ❌ ] သင်၏ သက်တမ်း ကုန်ဆုံးသွားပါပြီ။")
                        return
        print("[ ACCESS DENIED ❌ ] ID သို့မဟုတ် Password မှားနေပါသည်။")
    except Exception as e:
        print(f"[ ERROR ] ချိတ်ဆက်၍ မရပါ။ ({e})")

if __name__ == "__main__":
    main()
