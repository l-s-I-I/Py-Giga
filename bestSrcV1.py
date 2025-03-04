print("""يا قلبي السورس متعوب عليه اتمنى تقدر ولا تخمط 
      المبرمج : ايرور @error_3mk
      ما تنسى تدخل القناة لو منت بيها
      @giga_py""")

# احفظو الحقوق يخوانا


# libraryes / مكاتب
from telethon import TelegramClient, events, functions, types, Button, errors
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import ReportPeerRequest
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerChannel, InputReportReasonPornography, InputReportReasonSpam, InputReportReasonViolence, InputReportReasonFake, InputReportReasonChildAbuse, InputReportReasonOther,InputPhoto,PeerChannel
from difflib import get_close_matches
from yt_dlp import YoutubeDL
import sys
import subprocess
import os
import aiohttp
import json
from pytube import YouTube
import random
import string
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.errors.rpcerrorlist import UsernamePurchaseAvailableError
from colorama import Fore
from datetime import datetime, timedelta
import user_agent
from googletrans import Translator
import json
import asyncio
from dotenv import load_dotenv
from youtube_search import YoutubeSearch as error
import requests
import base64
import instaloader
import yt_dlp
from bs4 import BeautifulSoup
from time import sleep
from threading import Thread
import re
from gtts import gTTS
import time
import sqlite3
from typing import List, Tuple
import logging
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import DeleteMessagesRequest
from telethon.errors.rpcerrorlist import MediaEmptyError
from io import BytesIO
from pathlib import Path
from bs4 import BeautifulSoup as br


# main vars
chList = []
conn = sqlite3.connect("channels.db")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS channels (id INTEGER PRIMARY KEY AUTOINCREMENT, channel TEXT)"
)
conn.commit()
tokFiles = "tokens.json"
translator = Translator()
imgbApi = "7b41ee6cbdacae4fbe92e82fadfe8be0"
delayT = None
r = Fore.RED
g = Fore.GREEN
y = Fore.YELLOW
p = Fore.MAGENTA
apId = os.getenv("api_id")
apHa = os.getenv("api_hash")
king = os.getenv("tele_id")
Pname = os.getenv("name")
Pimg = os.getenv("url_image")
session = os.getenv("SESSION_telethon")
client = TelegramClient(StringSession(session), apId, apHa)
gch = None
tus = None
rwl = None
hred = False
mutes = {}

succesUs = []
ava = []
badUs = []
acChk = True
us = user_agent.generate_user_agent()
headers = {
    "authority": "api.pikwy.com",
    "accept": "*/*",
    "accept-language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "dnt": "1",
    "origin": "https://pikwy.com",
    "referer": "https://pikwy.com/",
    "sec-ch-ua": '"Chromium";v="105", "Not)A;Brand";v="8"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": us,
}
zzk = 0
repTypes = {
    "porn": {
        "keywords": ["porn", "adult", "sex", "18+", "nsfw","fuck","اباحي","سكس"],
        "reason": InputReportReasonPornography(),
        "messages": [
            "This channel contains explicit adult content and pornographic material that violates TG's terms",
            "Channel posting unauthorized adult content and explicit material",
            "Multiple instances of pornographic content detected in this channel",
            "Channel distributing adult content without age verification",
        ],
    },
    "spam": {
        "keywords": ["spam", "unwanted", "ads", "advertising","اعلانات","سبام"],
        "reason": InputReportReasonSpam(),
        "messages": [
            "Channel engaging in mass spam activities and unauthorized advertising",
            "Continuous spam messages and unwanted commercial content",
            "Channel spamming promotional content across multiple groups",
            "Automated spam behavior detected from this channel",
        ],
    },
    "violence": {
        "keywords": ["violence", "violent", "gore", "blood", "fight","دم","حرب","عنف"],
        "reason": InputReportReasonViolence(),
        "messages": [
            "Channel contains extreme violence and graphic content",
            "Multiple instances of violent content violating platform guidelines",
            "Channel promoting and sharing violent extremist content",
            "Dangerous violent content being distributed through this channel",
        ],
    },
    "fake": {
        "keywords": ["fake", "scam", "fraud", "impersonation","نصب","احتيالي","احتيال"],
        "reason": InputReportReasonFake(),
        "messages": [
            "Channel impersonating official entities and spreading misinformation",
            "Fraudulent activities and scam content detected",
            "Channel engaging in deceptive practices and false representation",
            "Multiple instances of fake news and misleading information",
        ],
    },
    "child": {
        "keywords": ["child", "children", "kid", "underage", "minor","اطفال","اندرايج","عيال","بيبي"],
        "reason": InputReportReasonChildAbuse(),
        "messages": [
            "Channel contains content exploiting minors",
            "Multiple violations involving underage individuals detected",
            "Channel sharing inappropriate content involving minors",
            "Serious child protection violations found in this channel",
        ],
    },
    "other": {
        "keywords": ["other", "else", "unknown","idk","معرفش","اخرى","غير"],
        "reason": InputReportReasonOther(),
        "messages": [
            "Multiple violations of Telegram's terms of service",
            "Channel engaging in prohibited activities",
            "Various instances of policy violations detected",
            "Channel reported for multiple guideline violations",
        ],
    },
}
bgRemoveApi = "PawTQh5RB1AQiqeiW2sS5kpy"
stringTime = time.asctime()
heads = {
    "authority": "www.fancytextpro.com",
    "accept": "text/plain, */*; q=0.01",
    "accept-language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.fancytextpro.com",
    "referer": "https://www.fancytextpro.com/",
    "sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}
vocSelf = True


# main funcs
load_dotenv()
def ranWrd():
    url = "https://random-word-api.herokuapp.com/word?length=5"
    try:
        res = requests.get(url)
        res.raise_for_status()
        wrd = str(res.json())
        if wrd:
            wrd = wrd.replace("[", "").replace("]", "")
            return wrd.replace("'", "")
        else:
            return "No word found!"
    except requests.RequestException as e:
        return f"Error fetching word: {e}"
def chkUsr(usr):
    res = requests.get(f"https://fragment.com/username/{usr}")
    if (
        '<span class="tm-section-header-status tm-status-taken">Taken</span>'
        in res.text
    ):
        return "Used"
    elif (
        '<span class="tm-section-header-status tm-status-unavail">Sold</span>'
        in res.text
    ):
        return "For Sell(NFT)"
    elif '<div class="table-cell-status-thin thin-only tm-status-unavail">Unavailable</div>':
        return True
    return "Bad"
def genUsr(ptrn):
    usr = ""
    rptChrZ = ""
    rptChrM = ""
    rptNumN = None
    for chr in ptrn:
        if chr == "z":
            if not rptChrZ:
                rptChrZ = random.choice(string.ascii_lowercase)
            usr += rptChrZ
        elif chr == "m":
            if not rptChrM:
                rptChrM = random.choice(string.ascii_lowercase)
            usr += rptChrM
        elif chr == "x":
            usr += random.choice(string.ascii_lowercase)
        elif chr == "n":
            usr += str(random.randint(0, 9))
        elif chr == "N":
            if rptNumN is None:
                rptNumN = str(random.randint(0, 9))
            usr += rptNumN
        else:
            usr += chr
    return usr
async def crePubCh(chName, chDesc, usr):
    try:
        res = await client(
            CreateChannelRequest(title=chName, about=chDesc, megagroup=False)
        )
        ch = res.chats[0]
        await client(functions.channels.UpdateUsernameRequest(channel=ch, username=usr))
        return True
    except errors.UsernameInvalidError:
        return "INVALID"
    except errors.UsernameOccupiedError:
        return "TAKEN"
    except Exception as e:
        return "ERROR"
def getTok():
    hdrs = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ar-EG,ar;q=0.9,en-GB;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "referer": "https://www.google.com/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": us,
    }
    res = requests.get("https://www.blackbox.ai/", headers=hdrs, timeout=20)
    try:
        chat = res.text.split("chat-")[1][:7]
    except:
        return "FVByyio"
    else:
        return chat
def sendMsg(msg, code):
    hdrs = {
        "accept": "*/*",
        "accept-language": "ar-EG,ar;q=0.9,en-GB;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5",
        "content-type": "application/json",
        "origin": "https://www.blackbox.ai",
        "priority": "u=1, i",
        "referer": f"https://www.blackbox.ai/chat/{code}",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": us,
    }
    jsonData = {
        "messages": [{"id": code, "content": msg, "role": "user"}],
        "agentMode": {},
        "id": code,
        "previewToken": None,
        "userId": None,
        "codeModelMode": True,
        "trendingAgentMode": {},
        "isMicMode": False,
        "userSystemPrompt": None,
        "maxTokens": 1024,
        "playgroundTopP": None,
        "playgroundTemperature": None,
        "isChromeExt": False,
        "githubToken": "",
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "clickedForceWebSearch": False,
        "visitFromDelta": False,
        "isMemoryEnabled": False,
        "mobileClient": False,
        "userSelectedModel": None,
        "validated": "00f37b34-a166-4efb-bce5-1312d87f2f94",
        "imageGenerationMode": False,
        "webSearchModePrompt": False,
        "deepSearchMode": False,
        "domains": None,
        "vscodeClient": False,
        "codeInterpreterMode": False,
    }
    res = requests.post(
        "https://www.blackbox.ai/api/chat", headers=hdrs, json=jsonData, timeout=20
    )
    try:
        r = res.text.split("$~~~$")[2]
    except:
        return res.text
    else:
        return r
def loadTks():
    try:
        with open(tokFiles, "r", encoding="utf-8") as f:
            tks = json.load(f)
            return tks if tks else {}
    except FileNotFoundError:
        return {}
def saveTks(tks):
    with open(tokFiles, "w", encoding="utf-8") as f:
        json.dump(tks, f, ensure_ascii=False, indent=4)
def getNewTok():
    url = "https://aboadel.serv00.net/ChatGpt/index.php?key=true"
    res = requests.get(url, timeout=20)
    if res.status_code == 200:
        data = res.json()
        return data.get("token")
    return None
def chatAi(tok, msg):
    url = f"https://aboadel.serv00.net/ChatGpt/index.php?key={tok}&msg={msg}"
    res = requests.get(url, timeout=20)
    if res.status_code == 200:
        data = res.json()
        return data.get("response")
    return None
def careUs(msg):
    tks = loadTks()
    tok = tks.get("errorh622")

    if not tok:
        tok = getNewTok()
        if tok:
            tks["errorh622"] = tok
            saveTks(tks)
        else:
            return "فشل في الحصول على توكن جديد."

    res = chatAi(tok, msg)

    if not res:
        tok = getNewTok()
        if tok:
            tks["errorh622"] = tok
            saveTks(tks)
            res = chatAi(tok, msg)
        else:
            return "فشل في الحصول على توكن جديد بعد المحاولة الثانية."

    return res
def isOwn(usrId):
    return usrId == king
async def conv(am, frst, sec):
    url = f"https://api.exchangerate-api.com/v4/latest/{frst}"
    res = requests.get(url)

    if res.status_code != 200:
        return "حدث خطأ أثناء جلب البيانات. حاول مرة أخرى لاحقًا."

    data = res.json()
    if sec not in data["rates"]:
        return f"العملة {sec} غير مدعومة."

    rate = data["rates"][sec]
    amt = float(am) * rate
    return f"{am} {frst} = {amt:.2f} {sec}"
def mkHtml(usr, photoUrl=None):
    defaultPhoto = "/api/placeholder/150/150"
    photoSrc = photoUrl if photoUrl else defaultPhoto

    tmpl = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Personal Website</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet">
    <style>
        :root {{
            --primary-color: #2563eb;
            --secondary-color: #1d4ed8;
            --accent-color: #60a5fa;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f0f7ff 0%, #ffffff 100%);
            min-height: 100vh;
        }}
        
        .card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
        }}
        
        .hover-scale {{
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .hover-scale:hover {{
            transform: scale(1.05);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }}
        
        .profile-image {{
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 50%;
        }}
        
        .custom-shape {{
            clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
        }}
        
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}
        
        .floating {{
            animation: float 3s ease-in-out infinite;
        }}
    </style>
</head>
<body class="flex items-center justify-center min-h-screen p-4">
    <div class="max-w-xl w-full">
        <div class="card rounded-2xl shadow-2xl p-8 animate__animated animate__fadeIn">
            <div class="custom-shape bg-gradient-to-r from-blue-500 to-blue-600 -mt-8 -mx-8 p-8 mb-6 rounded-t-2xl">
                <img src="{photoSrc}" alt="Profile" 
                     class="mx-auto profile-image border-4 border-white shadow-lg floating">
                <h1 class="text-4xl font-bold text-white text-center mt-4">Welcome to My Website!</h1>
                <p class="text-blue-100 text-center mt-2">Web Developer & Designer</p>
            </div>

            <div class="space-y-6 text-center">
                <p class="text-gray-600 text-lg leading-relaxed">
                    Hello! I'm a passionate web developer dedicated to creating exceptional digital experiences. 
                    I'd love to discuss your next project and bring your ideas to life.
                </p>

                <div class="flex justify-center space-x-4">
                    <a href="https://t.me/{usr}" 
                       class="hover-scale inline-flex items-center bg-blue-500 text-white font-bold py-3 px-6 rounded-full shadow-md hover:bg-blue-600">
                        <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path d="M21.5 2L2 10.5L21.5 19L21.5 2Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        Connect on Telegram
                    </a>
                </div>

                <div class="mt-8">
                    <h2 class="text-2xl font-bold text-gray-800 mb-4">My Skills</h2>
                    <div class="flex flex-wrap justify-center gap-3">
                        <span class="px-4 py-2 bg-blue-100 text-blue-600 rounded-full text-sm font-medium">HTML5</span>
                        <span class="px-4 py-2 bg-blue-100 text-blue-600 rounded-full text-sm font-medium">CSS3</span>
                        <span class="px-4 py-2 bg-blue-100 text-blue-600 rounded-full text-sm font-medium">JavaScript</span>
                        <span class="px-4 py-2 bg-blue-100 text-blue-600 rounded-full text-sm font-medium">React</span>
                    </div>
                </div>

                <div class="mt-8">
                    <h2 class="text-2xl font-bold text-gray-800 mb-4">Contact Me</h2>
                    <form class="space-y-4">
                        <div>
                            <input type="text" placeholder="Your Name" 
                                   class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200">
                        </div>
                        <div>
                            <input type="email" placeholder="Your Email" 
                                   class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200">
                        </div>
                        <div>
                            <textarea placeholder="Your Message" rows="4" 
                                      class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200"></textarea>
                        </div>
                        <button type="submit" 
                                class="w-full bg-blue-500 text-white font-bold py-3 px-6 rounded-lg hover:bg-blue-600 transition duration-300">
                            Send Message
                        </button>
                    </form>
                </div>
            </div>

            <div class="mt-8 pt-6 border-t border-gray-200">
                <p class="text-sm text-gray-500 text-center">© 2025 All Rights Reserved</p>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const usr = '{usr}';
            const link = document.querySelector('a[href*="t.me"]');
            link.href = `https://t.me/${{usr}}`;

            const form = document.querySelector('form');
            form.addEventListener('submit', function(e) {{
                e.preventDefault();
                alert('Thanks for your message! We will get back to you soon.');
                form.reset();
            }});
        }});
    </script>
</body>
</html>"""
    return tmpl.format(usr=usr, photoSrc=photoSrc)
async def uplImg(imgPath):
    url = "https://api.imgbb.com/1/upload"
    with open(imgPath, "rb") as file:
        res = requests.post(url, data={"key": imgbApi}, files={"image": file})
    if res.status_code == 200:
        return res.json()["data"]["url"]
    else:
        print(f"Failed to upload image: {res.text}")
        return None
async def hndMute(evt, act):
    if evt.is_reply:
        try:
            repMsg = await evt.get_reply_message()
            usrId = repMsg.sender_id
            if act == "mute":
                mutes[usrId] = True
                await evt.reply(f"**تم كتم المستخدم: `{usrId}`**")
            elif act == "unmute":
                mutes.pop(usrId, None)
                await evt.reply(f"**تم إلغاء الكتم عن المستخدم: `{usrId}`**")
        except Exception as e:
            await evt.reply(f"**خطأ: {str(e)}**")
    else:
        await evt.reply("**يرجى الرد على رسالة المستخدم المطلوب كتمه أو إلغاء كتمه.**")
async def mkChnl(evt, ttl, dtls, lnk=None):
    try:
        res = await client(
            functions.channels.CreateChannelRequest(
                title=ttl, about=dtls, megagroup=False
            )
        )
        newChId = res.chats[0].id
        if lnk:
            await client(
                functions.channels.UpdateUsernameRequest(channel=newChId, username=lnk)
            )
        await evt.reply(
            f"✅ **Channel Created:** {ttl}\n📌 **Description:** {dtls}\n🔗 {'https://t.me/' + lnk if lnk else 'Private Channel'}"
        )
    except Exception as e:
        await evt.reply(f"❌ **Failed:** {str(e)}")
async def mkGrp(evt, ttl, dtls):
    try:
        res = await client(
            functions.channels.CreateChannelRequest(
                title=ttl, about=dtls, megagroup=True
            )
        )
        newChId = res.chats[0].id
        await evt.reply(
            f"✅ **Group Created:** {ttl}\n📌 **Description:** {dtls}\n🔗 **Private Group**"
        )
    except Exception as e:
        await evt.reply(f"❌ **Failed:** {str(e)}")
def tshkTxt(txt):
    try:
        url = f"https://www.arabic-keyboard.org/tashkeel/import.php?area={txt}"
        hdrs = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        res = requests.get(url, headers=hdrs)
        if res.status_code == 200:
            data = json.loads(res.text)
            return data.get("text", "❌ لم يتم التشكيل")
        else:
            return "❌ خطأ في جلب التشكيل"
    except Exception as e:
        return f"⚠️ خطأ غير متوقع: {str(e)}"
def getHj():
    try:
        url = "https://www.karbala-tv.iq/live.php"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")
        clsLst = [
            "kufi fp160 col-xs-5 col-sm-12",
            "ktvfont fp250 col-xs-2 col-sm-12",
            "kufi fp180 col-xs-5 col-sm-12",
        ]
        for cls in clsLst:
            elm = soup.find("p", class_=cls)
            if elm:
                return elm.get_text()
        return "❌ لم يتم العثور على التاريخ الهجري"
    except Exception as e:
        return f"⚠️ خطأ غير متوقع: {str(e)}"
async def getEnt(chUsr):
    try:
        ent = await client.get_entity(chUsr)
        return InputPeerChannel(ent.id, ent.access_hash)
    except Exception as e:
        return None
def getTyp(txt):
    txt = txt.lower()
    for typ, data in repTypes.items():
        if txt in data["keywords"]:
            return typ
    allKw = []
    for data in repTypes.values():
        allKw.extend(data["keywords"])
    mtch = get_close_matches(txt, allKw, n=1, cutoff=0.6)
    if mtch:
        mtchWrd = mtch[0]
        for typ, data in repTypes.items():
            if mtchWrd in data["keywords"]:
                return typ
    return "other"
async def rprt(pr, typ, cnt):
    data = repTypes[typ]
    succ = 0
    for _ in range(cnt):
        try:
            msg = random.choice(data["messages"])
            await client(ReportPeerRequest(peer=pr, reason=data["reason"], message=msg))
            succ += 1
        except Exception as e:
            continue
    return succ
def srchBng(q):
    hdrs = {"User-Agent": us}
    url = f"https://www.bing.com/images/search?q={q}"
    try:
        res = requests.get(url, headers=hdrs, timeout=15)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"حدث خطأ أثناء البحث عن الصور: {e}")
        return []
    soup = BeautifulSoup(res.text, "html.parser")
    imgs = []
    for img in soup.find_all("a", class_="iusc"):
        imgUrl = img.get("m")
        if imgUrl and "murl" in imgUrl:
            start = imgUrl.find("murl") + 7
            end = imgUrl.find('"', start)
            imgs.append(imgUrl[start:end])
    return imgs[:5]
async def sndImgs(imgs, chId):
    for imgUrl in imgs:
        try:
            await client.send_file(chId, imgUrl)
        except Exception as e:
            print(f"حدث خطأ أثناء إرسال الصورة: {e}")
            continue
def isSng(v):
    return False


# commands / الاوامر

@client.on(events.NewMessage)
async def gpt(event):
    id = event.sender_id
    if isOwn(id):
        msg = event.raw_text.strip().lower()
        cmd = "/gpt"

        if msg.startswith(cmd):
            cont = msg.split()[1:]

            if cont:
                try:
                    res = careUs(cont)
                    await event.reply(res)
                except Exception as e:
                    await event.reply("حصل خطأ. حاول تاني بعد شوية.")
                    print(f"ERR IN GPT - {res}")
            else:
                await event.reply("وين الكلام يابني؟")

@client.on(events.NewMessage)
async def ai(event):
    id = event.sender_id
    if isOwn(id):
        msg = event.raw_text

        if msg.startswith(".ذكاء "):
            txt = msg[len(".ذكاء ") :]
            h = {
                "Host": "baithek.com",
                "Content-Type": "application/json",
                "User-Agent": "okhttp/4.9.2",
            }
            d = {"name": "Usama", "messages": [{"role": "user", "content": txt}]}
            r = requests.post(
                "https://baithek.com/chatbee/health_ai/new_health.php", headers=h, json=d
            )
            res = r.json()["choices"][0]["message"]["content"]
            await event.reply(res)

@client.on(events.NewMessage(pattern=r"^/bb\s+\S+"))
async def bb(event):
    id = event.sender_id
    if isOwn(id):
        msg = event.raw_text
        try:
            test = msg.split()[1]
            msg = str(msg.split()[1:])
        except:
            await event.reply("استخدم الامر صح يا معلم.\nمثال: '/bb كيفك يقلبي'")
        else:
            mess = "".join(word for word in msg)
            cod = getTok()
            repl = sendMsg(mess, cod)
            await event.reply(str(repl))

@client.on(events.NewMessage(pattern=r"^.انتحال$"))
async def int7al(event):
    if isOwn(event.sender_id):
        if event.is_reply:
            try:
                repMsg = await event.get_reply_message()
                usr = await client.get_entity(repMsg.sender_id)
                fullName = f"{usr.first_name or ''} {usr.last_name or ''}".strip()
                await client(functions.account.UpdateProfileRequest(first_name=fullName))
                pics = await client.get_profile_photos(usr.id)
                if pics:
                    picFile = await client.upload_file(await client.download_media(pics[0]))
                    await client(UploadProfilePhotoRequest(file=picFile))
                await event.reply(f"**تم تغيير الاسم والصورة لـ: {fullName}**")
            except Exception as e:
                await event.reply(f"**حصل خطأ: {str(e)}**")
        else:
            await event.reply("**رد على رسالة اليوزر اللي عايز تنتحله.**")


@client.on(events.NewMessage(pattern=r"^.ترجيع$"))
async def trg3(event):
    if isOwn(event.sender_id):
        try:
            await client(functions.account.UpdateProfileRequest(first_name=Pname))
            currPics = await client.get_profile_photos("me")
            if currPics:
                await client(DeletePhotosRequest(currPics))
            file = await client.upload_file(Pimg)
            await client(UploadProfilePhotoRequest(file=file))
            await event.reply("**تم ترجيع البروفايل.**")
        except Exception as e:
            await event.reply(f"**تم الترجيع مع خطأ\بدون صورة**")


@client.on(events.NewMessage(pattern=r"^ا$"))
async def getId(event):
    if isOwn(event.sender_id):
        await event.reply(f"**ايدي المكان: `{event.chat_id}` 💛**")

@client.on(events.NewMessage(pattern=r"^ايدي$"))
async def getUsrId(event):
    if isOwn(event.sender_id):
        if event.is_reply:
            try:
                repMsg = await event.get_reply_message()
                usr = await client.get_entity(repMsg.sender_id)
                await event.reply(f"**ايدي اليوزر: `{usr.id}` 💛**")
            except Exception as e:
                await event.reply(f"**حصل خطأ: {str(e)}**")
        else:
            await event.reply("**رد على رسالة عشان تجيب الايدي.**")

@client.on(events.NewMessage(pattern=r"^تهكيير$"))
async def thkr(event):
    if isOwn(event.sender_id):
        await event.reply("**📛 تم التهكير بنجاح**")



@client.on(events.NewMessage(pattern="/user (.*)"))
async def f7sUsr(event):
    id = event.sender_id
    if isOwn(id):
        global acChk
        ptrn = event.pattern_match.group(1).strip()
        msg = await event.respond(f"**جاري فحص اليوزرات بالنمط {ptrn}**")

        while acChk:
            usr = genUsr(ptrn)
            stat = chkUsr(usr)

            if stat == True:
                try:
                    await client(functions.account.CheckUsernameRequest(usr))
                    chName = "𝐄𝐑𝐑𝐎𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋"
                    chDesc = "**THIS USER BELONGS TO ERROR\nOWNER : @Error_3mk**"
                    succ = await crePubCh(chName, chDesc, usr)

                    if succ == True:
                        succesUs.append(usr)
                        await msg.edit(
                            f"**جاري الفحص...**\n\n"
                            f"**اليوزرات المسحوبة:** {', '.join(succesUs)}\n\n"
                            f"**اليوزرات المتاحة:** {', '.join(ava)}\n\n"
                            f"**تم سحب اليوزر:** @{usr} **(Success)**"
                        )
                    else:
                        badUs.append(usr)
                        if succ == "INVALID":
                            reason = "**USERNAME IS INVALID**"
                        elif succ == "TAKEN":
                            reason = "**USERNAME IS ALREADY TAKEN**"
                        else:
                            ava.append(usr)
                            await msg.edit(
                                f"**جاري الفحص...**\n\n"
                                f"**اليوزرات المسحوبة:** {', '.join(succesUs)}\n\n"
                                f"**اليوزرات المتاحة:** {', '.join(ava)}\n\n"
                                f"**اليوزر متاح ولكن لم يتم سحبه:** @{usr} **(Avaliable)**"
                            )

                except errors.UsernameNotOccupiedError:
                    badUs.append(usr)
                    print(usr + " not avaible")
                except errors.UsernameInvalidError:
                    badUs.append(usr)
                    print(usr + " bad")
                except UsernamePurchaseAvailableError:
                    badUs.append(usr)
                    print(usr + " For sell")
                except Exception as e:
                    badUs.append(usr)
                    print(usr + " Error")
            else:
                badUs.append(usr)
                print(usr + " Invaild")

@client.on(events.NewMessage(pattern=".توقيف_الفحص"))
async def stopF7s(event):
    id = event.sender_id
    if isOwn(id):
        global acChk
        acChk = False
        await event.respond("**تم إيقاف الفحص.**")

@client.on(events.NewMessage(pattern=".اكمال_الفحص"))
async def resumeF7s(event):
    id = event.sender_id
    if isOwn(id):
        global acChk
        acChk = True
        await event.respond("**تم استئناف الفحص.**")

@client.on(events.NewMessage(pattern=".حذف_اليوزرات"))
async def delUsrs(event):
    id = event.sender_id
    if isOwn(id):
        global succesUs, badUs, ava
        succesUs.clear()
        badUs.clear()
        ava.clear()
        await event.respond("**تم حذف قائمة اليوزرات.**")

@client.on(events.NewMessage(pattern=r"^/ss\s+(https?://\S+)"))
async def ssWeb(event):
    id = event.sender_id
    if isOwn(id):
        msg = event.message
        await event.reply("**ويت بدخل الموقع..**")
        if msg.text:
            lnk = msg.text.split()[1]
            if isOwn(event.sender_id):
                params = {
                    "tkn": "125",
                    "d": "3000",
                    "u": lnk,
                    "fs": "0",
                    "w": "1280",
                    "h": "1200",
                    "s": "100",
                    "z": "100",
                    "f": "jpg",
                    "rt": "jweb",
                }
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        "https://api.pikwy.com/", params=params
                    ) as res:
                        try:
                            data = await res.json()
                            img = data["iurl"]
                            date = data["date"]
                            dat = f"الوقت : {date}"
                            await event.reply(f"**تفضل صورة الموقع من جوا**", file=img)
                        except KeyError:
                            await event.respond(f"**رابط غلط او انحظرت من الموقع** {data}")

@client.on(events.NewMessage(pattern=".يوت"))
async def ytSrch(e):
    id = e.sender_id
    if isOwn(id):
        try:
            txt = e.raw_text.split()
            if len(txt) < 2:
                await e.reply("اكتب اسم الفيديو بعد الامر.")
                return
            q = txt[1]
            res = error(q, max_results=1).to_dict()
            if not res:
                await e.reply("ما لقيتش حاجة 😢")
                return
            vid = res[0]
            ttl = vid["title"]
            id = vid["id"]
            lnk = f"https://youtu.be/{id}"
            await e.reply(f"بيتم التحميل يا باشا: {ttl}")
            opts = {"format": "bestaudio[ext=m4a]"}
            with yt_dlp.YoutubeDL(opts) as ydl:
                inf = ydl.extract_info(lnk, download=False)
            if int(inf["duration"]) > 3605:
                await e.reply("طول الفيديو كبير اوي، مش هنقدر نحمله 🙄")
                return
            aud = ydl.prepare_filename(inf)
            ydl.process_info(inf)
            thb = inf["thumbnail"]
            thbFile = f"{id}.png"
            r = requests.get(thb)
            with open(thbFile, "wb") as f:
                f.write(r.content)
            await client.send_file(
                e.chat_id,
                aud,
                title=inf["title"],
                performer=inf["channel"],
                duration=int(inf["duration"]),
                thumb=thbFile,
            )
            os.remove(thbFile)
            os.remove(aud)
        except Exception as ex:
            await e.reply(f"حصل خطأ: {str(ex)}")

@client.on(events.NewMessage(pattern=r"\.كرر\s+(.+)\s+(\d+)"))
async def rptMsg(event):
    id = event.sender_id
    if isOwn(id):
        try:
            msg = event.pattern_match.group(1)
            cnt = int(event.pattern_match.group(2))
            if cnt > 100:
                await event.reply("⚠️ الحد الأقصى للتكرار هو 100.")
                return
            rptMsg = (msg + "\n") * cnt
            await event.reply(rptMsg)
        except ValueError:
            await event.reply("❌ حدث خطأ: تأكد من صحة الأمر.")
        except Exception as e:
            await event.reply(f"❌ حدث خطأ غير متوقع: {e}")

@client.on(events.NewMessage(pattern=r"\.تكرار\s+(.+)\s+(\d+)"))
async def rptMsg2(event):
    id = event.sender_id
    if isOwn(id):
        try:
            msg = event.pattern_match.group(1)
            cnt = int(event.pattern_match.group(2))
            if cnt > 50:
                await event.reply("⚠️ الحد الأقصى للتكرار هو 50.")
                return
            for _ in range(cnt):
                await event.respond(msg)
        except ValueError:
            await event.reply("❌ حدث خطأ: تأكد من صحة الأمر.")
        except Exception as e:
            await event.reply(f"❌ حدث خطأ غير متوقع: {e}")

@client.on(events.NewMessage(pattern=r"^/convert (\d+(?:\.\d+)?) ([A-Z]{3}) ([A-Z]{3})$"))
async def convCur(event):
    id = event.sender_id
    if isOwn(id):
        try:
            args = event.pattern_match.groups()
            am, frst, sec = args[0], args[1].upper(), args[2].upper()
            res = await conv(am, frst, sec)
            await event.reply(res)
        except Exception as e:
            await event.reply("حصل خطأ. تأكد من المدخلات.")

@client.on(events.NewMessage(pattern=r"^/yt (https?://[^\s]+)$"))
async def ytDl(event):
    id = event.sender_id
    if isOwn(id):
        lnk = event.pattern_match.group(1)
        ydlOpts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": "video.%(ext)s",
        }

        try:
            with yt_dlp.YoutubeDL(ydlOpts) as ydl:
                inf = ydl.extract_info(lnk, download=True)
                fileName = ydl.prepare_filename(inf)

            await event.reply("تم التحميل! جاري الإرسال...")
            await event.client.send_file(event.chat_id, fileName)
            os.remove(fileName)
            await event.reply("تم الحذف بعد الإرسال.")
        except Exception as e:
            await event.reply(f"حصل خطأ: {str(e)}")

@client.on(events.NewMessage(pattern="/downloadX (https?://x\.com/\S+)"))
async def dlX(event):
    id = event.sender_id
    if isOwn(id):
        url = event.text.split(" ", 1)[1] 
        try:
            msg = await event.respond("🌟 | جار التحميل...")
            ydlOpts = {
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "outtmpl": "%(title)s.%(ext)s",
            }

            with yt_dlp.YoutubeDL(ydlOpts) as ydl:
                inf = ydl.extract_info(url, download=False)
                name = inf.get("title", "video_descargado")
                filePath = ydl.prepare_filename(inf)
            await event.respond(file=filePath)
            os.remove(filePath)
        except Exception as e:
            errMsg = f"""
    ⛔️ | حصل خطأ: 
    🤖 | الخطأ: {e}
    """
            await event.respond(errMsg)
        finally:
            await event.delete()

@client.on(events.NewMessage(pattern=r"\.انطق (.+)"))
async def spk(event):
    id = event.sender_id
    if isOwn(id):
        txt = event.pattern_match.group(1) 
        filePath = "voice.mp3"
        try:
            tts = gTTS(text=txt, lang="ar")
            tts.save(filePath)
            await event.reply("🔊 جاري النطق...")
            await event.respond(file=filePath)
            os.remove(filePath)
        except Exception as e:
            await event.reply(f"❌ حصل خطأ: {e}")

@client.on(events.NewMessage(pattern=r"/ip"))
async def shIp(event):
    id = event.sender_id
    if isOwn(id):
        ip = event.text.strip()

        try:
            res = requests.get(f"https://ipinfo.io/{ip}/geo").json()
            ipInfo = f"""
    📌 **معلومات IP** `{res.get("ip", "غير معروف")}`

    🌆 **المدينة**: {res.get("city", "غير معروف")}
    📍 **المنطقة**: {res.get("region", "غير معروف")}
    🏳️ **الدولة**: {res.get("country", "غير معروف")}
    📌 **الموقع**: {res.get("loc", "غير معروف")}
    🏠 **السكن**: {res.get("org", "غير معروف")}
    ⏳ **الوحدة الزمنية**: {res.get("timezone", "غير معروف")}
    """
            await event.respond(ipInfo)
        except:
            await event.respond("❌ تأكد من صحة الـ IP.")

@client.on(events.NewMessage(pattern=r"/logo"))
async def mkLogo(event):
    id = event.sender_id
    if isOwn(id):
        txt = event.text.strip()
        if len(txt.split(" ", 1)) > 1:
            txt = txt.split(" ", 1)[1]
        else:
            await event.respond("❌ اكتب الاسم بعد /logo.")
            return

        try:
            url = f"https://bcassetcdn.com/asset/logo/ea509e1b-89eb-457b-810b-2f3d42cc6841/logo?v=5&text={txt}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as res:
                    if res.status == 200:
                        imgData = await res.read()
                        img = BytesIO(imgData)
                        await event.respond(file=img)
                    else:
                        await event.respond("❌ فشل في تحميل الصورة.")
        except Exception as e:
            await event.respond(f"❌ حصل خطأ: {str(e)}")

@client.on(events.NewMessage(pattern=r"^/web\s+@?(\w+)$"))
async def mkWeb(event):
    id = event.sender_id
    if isOwn(id):
        usr = event.pattern_match.group(1)
        fileName = f"{event.sender_id}.html"
        try:
            usrEnt = await client.get_entity(usr)
            photoPath = f"profile_photos/{event.sender_id}.jpg"
            os.makedirs("profile_photos", exist_ok=True)
            photoUrl = None
            try:
                pics = await client.get_profile_photos(usrEnt)
                if pics:
                    await client.download_profile_photo(usrEnt, file=photoPath)
                    print("تم تحميل الصورة.")
                    photoUrl = await uplImg(photoPath)
                    if not photoUrl:
                        print("استخدمنا الصورة الافتراضية.")
                        photoUrl = "/api/placeholder/150/150"  
            except Exception as e:
                print(f"حصل خطأ: {e}")
            with open(fileName, "w", encoding="utf-8") as file:
                file.write(mkHtml(usr, photoUrl))
            await client.send_file(event.chat_id, fileName, reply_to=event.id)

        except Exception as e:
            await event.respond(f"حصل خطأ: {str(e)}")

        finally:
            if os.path.exists(fileName):
                os.remove(fileName)
            if os.path.exists(photoPath):
                os.remove(photoPath)

@client.on(events.NewMessage(pattern=r"^/channel\s+(.+?)\s*\|\s*(.+?)(?:\s*\|\s*(\S+))?$"))
async def mkCh(event):
    id = event.sender_id
    if isOwn(id):
        params = event.pattern_match.groups()
        chName, chDesc, chUsr = params[0], params[1], params[2] if params[2] else None
        await mkChnl(event, chName, chDesc, chUsr)

@client.on(events.NewMessage(pattern=r"^/group\s+(.+?)\s*\|\s*(.+?)$"))
async def makeGrppp(event):
    id = event.sender_id
    if isOwn(id):
        params = event.pattern_match.groups()
        grpName, grpDesc = params[0], params[1]
        await mkGrp(event, grpName, grpDesc)

@client.on(events.NewMessage(pattern=r"^\.تشكييل\s+(.+)"))
async def tshk(event):
    id = event.sender_id
    if isOwn(id):
        inp = event.pattern_match.group(1)
        res = tshkTxt(inp)
        await event.reply(f"🔹 **النص بعد التشكيل:**\n{res}")

@client.on(events.NewMessage(pattern=r"^\.هجري$"))
async def hj(event):
    id = event.sender_id
    if isOwn(id):
        date = getHj()
        await event.reply(f"📆 **التاريخ الهجري اليوم:**\n{date}")

@client.on(events.NewMessage(pattern="/enhance"))
async def enh(event):
    id = event.sender_id
    if isOwn(id):
        await event.reply("أرسل الصورة اللي عايز تحسنها")

@client.on(events.NewMessage())
async def w8ForImg(event):
    if event.photo and event.is_reply:
        rep = await event.get_reply_message()
        if rep.message == "أرسل الصورة اللي عايز تحسنها":
            snd = await event.get_sender()
            id = str(snd.id)

            await event.reply("بيتم التعديل...")

            path = await event.download_media(f"image{id}.jpg")

            img = requests.post(
                "https://api2.pixelcut.app/image/upscale/v1",
                files={"image": open(f"image{id}.jpg", "rb")},
                data={"scale": "2"},
            )

            with open(f"image{id}New.jpg", "wb") as newFile:
                newFile.write(img.content)

            await client.send_file(
                event.chat_id,
                f"image{id}New.jpg",
                caption="تـم تعـديل بـواسـطه : @ERROR_3MK",
            )

            os.remove(f"image{id}.jpg")
            os.remove(f"image{id}New.jpg")

@client.on(events.NewMessage(pattern=r'/report(?:@\w+)?$|/report(?:@\w+)?\s+(.+)'))
async def rprtCh(event):
    try:
        parts = event.raw_text.split()
        
        if len(parts) < 4:
            await event.reply('الاستخدام: /report @username النوع العدد\nمثال: /report @example porn 100')
            return
        
        ch = parts[1]
        rprtTyp = getTyp(parts[2])
        
        try:
            cnt = int(parts[3])
            if cnt < 1:
                cnt = 1
            elif cnt > 500:
                cnt = 500
        except:
            cnt = 100
            
        if not ch.startswith('@'):
            await event.reply('يبدأ معرف القناة بـ @')
            return
            
        statusMsg = await event.reply('جاري الإبلاغ...')
        
        pr = await getEnt(ch)
        if not pr:
            await statusMsg.edit('ما لقيتش القناة')
            return
            
        succCnt = await rprt(pr, rprtTyp, cnt)
        await statusMsg.edit(f'تم الإبلاغ\nالبلاغات الناجحة: {succCnt}/{cnt}')
            
    except Exception as e:
        await event.reply('حصل خطأ. حاول تاني.')

@client.on(events.NewMessage(pattern='/deleteBg'))
async def rdy(event):
    await event.reply('أرسل الصورة لإزالة الخلفية')

@client.on(events.NewMessage(func=lambda e: e.photo))
async def delBg(event):
    try:
        if not event.is_reply:
            return

        rep = await event.get_reply_message()
        if rep.message != 'أرسل الصورة لإزالة الخلفية':
            return

        progMsg = await event.reply('⏳ جاري إزالة الخلفية...')
        photo = await event.download_media('input_image.png')
        res = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open('input_image.png', 'rb')},
            headers={'X-Api-Key': bgRemoveApi}
        )

        if res.status_code != requests.codes.ok:
            await progMsg.edit('❌ حصل خطأ')
            return
        with open('output_image.png', 'wb') as out:
            out.write(res.content)
        await progMsg.delete()

        btns = [
            [Button.url('- Dev 👨‍💻 .', 'https://t.me/iita25')]
        ]

        await client.send_file(
            event.chat_id,
            'output_image.png',
            reply_to=event.message.id,
            buttons=btns
        )

    except Exception as e:
        await event.reply(f'❌ حصل خطأ: {str(e)}')

    finally:
        try:
            os.remove('input_image.png')
            os.remove('output_image.png')
        except:
            pass

@client.on(events.NewMessage(pattern=r"/src (.+)"))
async def getSrc(event):
    chatId = event.chat_id
    url = event.pattern_match.group(1)
    try:
        srcCode = requests.get(url).text
        soup = br(srcCode, "html.parser")
        with open("brok.html", "w", encoding="utf-8") as file:
            file.write(str(soup))

        await client.send_file(
            chatId, "brok.html", caption=f"done ✅\ntime : {stringTime}\n- {url}"
        )
    except:
        await event.reply("error")

@client.on(events.NewMessage)
async def msgs(event):
    txt = event.text
    if txt in [".تلاوة"]:
        voiceUrl = f"https://t.me/ALMORTAGELRSK/{random.randint(7, 276)}"
        await client.send_file(event.chat_id, voiceUrl, voice_note=True, caption="« صلي على سيدنا محمد ﷺ »", reply_to=event.message)

@client.on(events.NewMessage(pattern=r"\.زخرفه (.+)"))
async def zkh(event):
    txt = event.pattern_match.group(1)
    data = {
        "text": txt,
        "_csrf": "",
        "pages[]": ["New", "Unique", "CoolText"],
    }
    res = requests.post(
        "https://www.fancytextpro.com/generate", headers=heads, data=data
    )
    data = json.loads(res.content)

    aa = (
        data["MusicalMap"],
        data["neonCharMap"],
        data["boldCharMap"],
        data["EmojiMap"],
        data["italicCharMap"],
        data["AncientMap"],
        data["Ladyleo"],
        data["boldItalicCharMap"],
        data["SinoTibetan"],
        data["monospaceCharMap"],
        data["weirdChar"],
        data["BoldFloara"],
        data["upperAnglesCharMap"],
        data["BuzzChar"],
        data["greekCharMap"],
        data["SunnyDay"],
        data["invertedSquaresCharMap"],
        data["TextDecorated"],
        data["doubleStruckCharMap"],
        data["Dessert"],
        data["oldEnglishCharMap"],
        data["taiVietCharMap"],
        data["oldEnglishCharBoldMap"],
        data["oldItalicText"],
        data["cursiveLetters"],
        data["cursiveLettersBold"],
        data["BoldJavaneseText"],
        data["wideTextCharMap"],
        data["subscriptCharMap"],
        data["GunText"],
        data["superscriptCharMap"],
        data["ak47GunText"],
    )

    m = "\n".join(aa)
    await event.reply(f"<b>{m}\n\nPY : @iita25 • @py_giga</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern="/bing"))
async def bingSrch(event):
    id = event.sender_id
    if isOwn(id):
        qry = event.raw_text.replace("/bing", "").strip()
        if not qry:
            await event.reply("اكتب الكلمة اللي عايز تدور عليها بعد /bing.")
            return

        await event.reply("قاعد ادور عليها ويت....")

        startTime = time.time()
        imgs = srchBng(qry)

        if imgs:
            await sndImgs(imgs, event.chat_id)
            endTime = time.time()
            elapsedTime = round(endTime - startTime)
            await event.reply(
                f"كم اني سريع خلصت كل الصور بس في {elapsedTime} ثانيه\nوش رايك؟🔫"
            )
        else:
            await event.reply("ما لقيت صور يا عمي حل عني")

@client.on(events.NewMessage(pattern="/add-ch (.+)"))
async def addCh(event):
    id = event.sender_id
    if isOwn(id):
        ch = event.pattern_match.group(1)
        try:
            ent = await client.get_entity(ch)
            if ent.broadcast:
                if ch not in chList:
                    chList.append(ch)
                    await event.reply(f"✅ تم إضافة القناة {ch}!")
                else:
                    await event.reply("⚠️ القناة موجودة بالفعل.")
            else:
                await event.reply("❌ القناة مش صحيحة.")
        except:
            await event.reply("❌ المعرف أو الايدي غلط.")
@client.on(events.NewMessage(pattern="/delete-ch (.+)"))
async def delCh(event):
    id = event.sender_id
    if isOwn(id):
        ch = event.pattern_match.group(1)
        if ch in chList:
            chList.remove(ch)
            await event.reply(f"✅ تم حذف القناة {ch}!")
        else:
            await event.reply("⚠️ القناة مش موجودة.")
@client.on(events.NewMessage(pattern="/channels"))
async def lstCh(event):
    id = event.sender_id
    if isOwn(id):
        if chList:
            await event.reply("\n".join(chList))
        else:
            await event.reply("📭 ما فيش قنوات مضافين.")
@client.on(events.NewMessage(pattern="/post"))
async def postCh(event):
    id = event.sender_id
    if isOwn(id):
        if event.reply_to_msg_id:
            msg = await event.get_reply_message()
            succCnt = 0
            failedCh = []
            for ch in chList:
                try:
                    await client.send_message(ch, msg)
                    succCnt += 1
                except:
                    failedCh.append(ch)

            res = f"✅ تم النشر في {succCnt} قنوات."
            if failedCh:
                res += f'\n❌ فشل النشر في: {", ".join(failedCh)}'
            await event.reply(res)
        else:
            await event.reply("⚠️ رد على الرسالة عشان تنشرها.")
@client.on(events.NewMessage(pattern="/postAll"))
async def postAll(event):
    id = event.sender_id
    if isOwn(id):
        if event.reply_to_msg_id:
            msg = await event.get_reply_message()
            cnt = 0
            async for dialog in client.iter_dialogs():
                if dialog.is_user:
                    try:
                        await client.send_message(dialog.id, msg)
                        cnt += 1
                    except:
                        pass
            await event.reply(f"✅ تم الإرسال لـ {cnt} مستخدمين.")
        else:
            await event.reply("⚠️ رد على الرسالة عشان تنشرها.")
@client.on(events.NewMessage(pattern="/add-ch-db (.+)"))
async def addDB(event):
    id = event.sender_id
    if isOwn(id):
        ch = event.pattern_match.group(1)
        try:
            ent = await client.get_entity(ch)
            if ent.broadcast:
                cursor.execute("INSERT INTO channels (channel) VALUES (?)", (ch,))
                conn.commit()
                await event.reply(f"✅ تم إضافة القناة {ch} للداتا بيز!")
            else:
                await event.reply("❌ القناة مش صحيحة.")
        except:
            await event.reply("❌ المعرف أو الايدي غلط.")
@client.on(events.NewMessage(pattern="/delete-ch-db (.+)"))
async def delDB(event):
    id = event.sender_id
    if isOwn(id):
        ch = event.pattern_match.group(1)
        cursor.execute("DELETE FROM channels WHERE channel = ?", (ch,))
        conn.commit()
        await event.reply(f"✅ تم حذف القناة {ch} من الداتا بيز!")

@client.on(events.NewMessage(pattern="(تفعيل البصمه|فعل البصمه)"))
async def strtVocSav(evn):
    id = evn.sender_id
    if isOwn(id):
        global vocSelf
        if vocSelf:
            return await evn.reply("حفظ البصمه شغال من قبل 🎙✅")
        vocSelf = True
        await evn.reply("تم تشغيل حفظ البصمه تلقائي 🎙✅")
@client.on(events.NewMessage(pattern="(ايقاف البصمه|اقف البصمه)"))
async def stpVocSav(evn):
    id = evn.sender_id
    if isOwn(id):
        global vocSelf
        if not vocSelf:
            return await evn.reply("حفظ البصمه معطل من قبل 🎙❌")
        vocSelf = False
        await evn.reply("تم تعطيل حفظ البصمه 🎙❌")

@client.on(
    events.NewMessage(func=lambda e: e.is_private and e.voice and e.media_unread)
)
async def savVoc(evn):
    global vocSelf
    if not vocSelf:
        return
    snd = await evn.get_sender()
    us = f"@{snd.username}" if snd.username else "لا يـوجـد"
    try:
        if not isSng(evn.voice):
            pth = await evn.download_media(file="voicemsgs/")
            await client.send_file(
                "me",
                pth,
                caption=f"تم حفظ البصمه تلقائي 🎙✅\n\n"
                f"المرسل: {snd.first_name} ({snd.id})\n"
                f"اليوزر: {us}\n"
                f"الايدي: {snd.id}",
            )
            os.remove(pth)
    except MediaEmptyError:
        await evn.reply("حصل مشكله وقت الحفظ، جرب تاني.")
    except Exception as ex:
        await evn.reply(f"حصل خطأ: {str(ex)}")

@client.on(events.NewMessage(pattern="/help"))
async def helppppp(event):
    id = event.sender_id
    if isOwn(id):
        help_text = """
    🎉 **مرحبًا بك في قائمة الأوامر!** 🎉

    📌 **الأوامر العامة:**
    - `/help` - عرض قائمة الأوامر.
    - `/gpt <نص>` - التحدث مع الذكاء الاصطناعي (ChatGPT).
    - `.ذكاء <نص>` - التحدث مع ذكاء اصطناعي آخر.
    - `/bb <نص>` - التحدث مع BlackBox AI.

    🔄 **الانتحال:**
    - `.انتحال` - انتحال اسم وصورة المستخدم الذي تم الرد عليه.
    - `.ترجيع` - إعادة البروفايل إلى الإعدادات الافتراضية.

    🆔 **الأيدي:**
    - `ا` - عرض معرف المجموعة الحالية.
    - `ايدي` - عرض معرف المستخدم الذي تم الرد عليه.

    📝 **اليوزرات:**
    - `/user <نمط>` - فحص اليوزرات المتاحة بناءً على النمط.
    - `.توقيف_الفحص` - إيقاف فحص اليوزرات.
    - `.اكمال_الفحص` - استئناف فحص اليوزرات.
    - `.حذف_اليوزرات` - حذف قائمة اليوزرات المحفوظة.

    🌐 **الشاشة:**
    - `/ss <رابط>` - التقاط لقطة شاشة لموقع ويب.

    🎥 **اليوتيوب:**
    - `.يوت <اسم الفيديو>` - البحث عن فيديو على اليوتيوب وتحميله.

    🔁 **التكرار:**
    - `.كرر <نص> <عدد>` - تكرار النص عدة مرات.
    - `.تكرار <نص> <عدد>` - إرسال النص عدة مرات.

    💱 **تحويل العملات:**
    - `/convert <المبلغ> <من العملة> <إلى العملة>` - تحويل العملات.

    📥 **التحميل:**
    - `/yt <رابط>` - تحميل فيديو من اليوتيوب.
    - `/downloadX <رابط>` - تحميل فيديو من X (تويتر).

    🎙 **الصوتيات:**
    - `.انطق <نص>` - تحويل النص إلى صوت.

    🌍 **معلومات IP:**
    - `/ip <عنوان IP>` - الحصول على معلومات عن عنوان IP.

    🖼 **اللوجو:**
    - `/logo <نص>` - إنشاء لوجو بناءً على النص.

    🌐 **إنشاء موقع:**
    - `/web <يوزر>` - إنشاء موقع ويب بناءً على يوزر تيليجرام.

    📢 **إنشاء قنوات ومجموعات:**
    - `/channel <اسم القناة> | <وصف القناة> | <يوزر>` - إنشاء قناة.
    - `/group <اسم المجموعة> | <وصف المجموعة>` - إنشاء مجموعة.

    🔠 **التشكيل:**
    - `.تشكييل <نص>` - تشكيل النص العربي.

    📅 **التاريخ:**
    - `.هجري` - عرض التاريخ الهجري الحالي.

    🖼 **تحسين الصور:**
    - `/enhance` - تحسين جودة الصورة.

    🚩 **البلاغات:**
    - `/report @username <نوع> <عدد>` - الإبلاغ عن قناة أو مستخدم.

    🎨 **إزالة الخلفية:**
    - `/deleteBg` - إزالة الخلفية من الصورة.

    📜 **سورسات المواقع:**
    - `/src <رابط>` - الحصول على سورس كود الموقع.

    🎙 **التلاوة:**
    - `.تلاوة` - إرسال تلاوة عشوائية.

    ✨ **الزخرفة:**
    - `.زخرفه <نص>` - زخرفة النص.

    🔍 **البحث في Bing:**
    - `/bing <كلمة>` - البحث عن صور في Bing.

    📢 **النشر التلقائي:**
    - `/add-ch <قناة>` - إضافة قناة للنشر التلقائي.
    - `/delete-ch <قناة>` - حذف قناة من النشر التلقائي.
    - `/channels` - عرض القنوات المضافة.
    - `/post` - نشر رسالة للقنوات المضافة.
    - `/postAll` - نشر رسالة لجميع الدردشات.
    - `/add-ch-db <قناة>` - إضافة قناة لقاعدة البيانات.
    - `/delete-ch-db <قناة>` - حذف قناة من قاعدة البيانات.

    🎙 **حفظ البصمات:**
    - `تفعيل البصمه` - تفعيل حفظ البصمات تلقائيًا.
    - `ايقاف البصمه` - إيقاف حفظ البصمات تلقائيًا.

    📂 **حفظ الوسائط:**
    - يتم حفظ البصمات تلقائيًا عند تفعيلها.

    🚀 **تشغيل البوت:**
    - البوت يعمل تلقائيًا عند تشغيل السكريبت.

    📜 **ملاحظة:**
    - بعض الأوامر تتطلب صلاحيات خاصة أو تكون مخصصة للمدير فقط.
    """

        await event.reply(help_text)


# run
client.start()
print("Running WiTh ERR..........")
client.run_until_disconnected()
