import 
import requests

# သင့် GitHub ရဲ့ key.txt လင့်ခ်ကို ဒီနေရာမှာ ထည့်ပါ (Raw link ဖြစ်ရပါမယ်)
KEY_URL = "https://raw.githubusercontent.com/SoeHtet-bot8888/Starlink-bypass/main/key.txt"

def check_auth():
    # ဖုန်းရဲ့ Device ID ကို Termux ကနေ ယူမယ်
    device_id = "19948128" # ဒီနေရာမှာ အခုပေါ်နေတဲ့ ID ကို ထည့်ပါ
    
    print("================================")
    print("   STARLINK BYPASS KEY SYSTEM   ")
    print("================================")
    print(f"[YOUR DEVICE ID] => {device_id}")
    print("Checking authorization from GitHub...")
    
    try:
        response = requests.get(KEY_URL)
        if device_id in response.text:
            print("--------------------------------")
            print("[ ACCESS GRANTED ✅ ]")
        else:
            print("--------------------------------")
            print("Status: [ ACCESS DENIED ❌ ]")
            print(f"❌ သင့် ID [{device_id}] ကို Server တွင် မတွေ့ပါ။")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_auth()

# key.txt ရဲ့ Raw URL ကို ဒီနေရာမှာ ထည့်ပါ
KEY_URL = "https://raw.githubusercontent.com/SoeHtet-bot8888/Starlink-bypass/main/key.txt"

def check_auth():
    # သင့် Device ID ကို ဒီနေရာမှာ ထည့်ပေးပါ
    device_id = "19948128"
    
    print("================================")
    print("   STARLINK BYPASS KEY SYSTEM   ")
    print("================================")
    print(f"[YOUR DEVICE ID] => {device_id}")
    print("Checking authorization from GitHub...")
    
    try:
        response = requests.get(KEY_URL)
        if device_id in response.text:
            print("--------------------------------")
            print("[ ACCESS GRANTED ✅ ]")
        else:
            print("--------------------------------")
            print("Status: [ ACCESS DENIED ❌ ]")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_auth()
    
