
import requests, uuid, sys, os
from datetime import datetime

def login():
    device_id = str(uuid.getnode())
    key_data = requests.get("https://raw.githubusercontent.com/SoeHtet-bot8888/Starlink-bypass/main/key.txt").text
    
    for line in key_data.splitlines():
        if device_id in line:
            parts = line.split('|')
            if datetime.now() <= datetime.strptime(parts[1], "%Y-%m-%d"):
                print(f"[ ACCESS GRANTED ✅ ]")
                # WiFi Bypass လုပ်ခြင်း
                bypass_wifi(parts[2]) 
                return
    print("[ ACCESS DENIED ❌ ] ID မှားနေသည် သို့မဟုတ် ရက်ကုန်နေပြီ။")

def bypass_wifi(wifi_type):
    # Ruijie ဖြစ်ဖြစ် Starlink ဖြစ်ဖြစ် ဒီနေရာမှာ URL ကို အလိုအလျောက်ရယူရမယ်
    print(f"Bypassing {wifi_type} WiFi...")
    # သင်ရလာတဲ့ Session ID ကို ဒီမှာ Variable အနေနဲ့ ထည့်ပြီး အလိုအလျောက် Request ပို့ခိုင်းပါ
    os.system("curl -s 'http://portal-as.ruijienetworks.com/api/login?sessionId=YOUR_SESSION_ID&action=login'")
    print("[ SUCCESS ✅ ] အင်တာနက် သုံးနိုင်ပါပြီ။")

login()
