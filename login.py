
    
import requests
import uuid
from datetime import datetime

def login():
    device_id = str(uuid.getnode())
    key_url = "https://raw.githubusercontent.com/SoeHtet-bot8888/Starlink-bypass/main/key.txt"
    
    try:
        response = requests.get(key_url).text
        # ID နဲ့ ရက်ကို ခွဲထုတ်ခြင်း
        for line in response.splitlines():
            if device_id in line:
                parts = line.split('|')
                expiry_date = parts[1]
                
                # ရက်စစ်ဆေးခြင်း
                if datetime.now() <= datetime.strptime(expiry_date, "%Y-%m-%d"):
                    print(f"[ ACCESS GRANTED ✅ ] သက်တမ်း - {expiry_date} ထိရပါမည်။")
                    bypass_ruijie() # အင်တာနက်ကို အလိုအလျောက်ဖွင့်
                    return
                else:
                    print("[ EXPIRED ❌ ] သက်တမ်းကုန်သွားပါပြီ။")
                    return
        print("[ ACCESS DENIED ❌ ] သင်၏ ID ကို စာရင်းတွင်မတွေ့ပါ။")
    except Exception as e:
        print(f"Error: {e}")

def bypass_ruijie():
    # ဒီနေရာမှာ သင့် sessionId ကို အမြဲ Update လုပ်ပေးရပါမယ်
    session_id = "5771263bf1d6414b803fc8e563572315"
    url = f"http://portal-as.ruijienetworks.com/api/login?sessionId={session_id}&action=login"
    
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print("[ SUCCESS ✅ ] အင်တာနက် အသုံးပြုနိုင်ပါပြီ။")
    except:
        print("[ ERROR ] အင်တာနက်ချိတ်ဆက်မှု မရပါ။")

if __name__ == "__main__":
    login()
