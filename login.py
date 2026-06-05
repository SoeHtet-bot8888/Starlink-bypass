
def bypass_wifi():
    print("[... ] Connecting to Internet...")
    try:
        # သင်ပေးလိုက်တဲ့ လင့်ခ်အတိုင်း အတိအကျ ပြင်ထားပါတယ်
        # Portal URL ကို အခုလို အသေထားလိုက်ပါမယ်
        target_url = "http://portal-as.ruijienetworks.com/api/login"
        
        # သင့်ဖုန်း Browser မှာ ပေါ်လာတဲ့ SessionID ကို ရအောင်ယူမယ်
        # ဒီနေရာမှာ SessionID ကို ရှာတဲ့နည်းလမ်းကို ပိုသေချာအောင် လုပ်ထားပါတယ်
        res = requests.get("http://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html", verify=False)
        match = re.search(r'sessionId=([a-zA-Z0-9]+)', res.url)
        
        if match:
            sid = match.group(1)
            print(f"Found SessionID: {sid}")
            
            # API လင့်ခ်ကို တိကျစွာ ခေါ်ယူခြင်း
            payload = {'sessionId': sid, 'action': 'login'}
            requests.get(target_url, params=payload, verify=False)
            
            print("[ SUCCESS ✅ ] အင်တာနက် အသုံးပြုနိုင်ပါပြီ။")
        else:
            print("[ ERROR ⚠️ ] WiFi Portal မှ SessionID ကို ရှာမတွေ့ပါ။")
    except Exception as e:
        print(f"[ ERROR ] {e}")
