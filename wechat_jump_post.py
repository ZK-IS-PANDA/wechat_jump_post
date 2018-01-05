# -*- coding:utf-8 -*-
import requests
import json
from Crypto.Cipher import AES
import base64
import logging

import sys
session_id = sys.argv[1]
#session_id = "k971ELR2ii+bWlwpb2nSUsbdR4qKlXYxWoPDkkfHXi+3cITLovsHdzR/sFKWGSv9LooqvMshATVWERRfN95LWxJPXSzBbU7nt6A06HOOxFtKUPphUf7QA5xgI0n+2DRxBTrgEGdIAzSOSB0HLlFs+A=="
aes_key = session_id[0:16]
aes_iv  = aes_key
#print aes_key


#enmessage = base64.b64decode("jP1vmLEHYSfOIIy2W0iBjCRbCLBKad/ttkVS3TM8vwFWrjQVSHlCoGY+69G6Zbt9S4uGdwB5CImrzXHkwZ0m8Bw2oLmoFV9xL9z0HphmCPaKvhJchdh1sKOVr5KQTaNweDSf8D5KgemhErxLy6WILpQ+GwJYtH/2U5pFPY6eDyyTjbZAlSF/8CId1k5xSoPCpJuAYggz7FWr8JLVYeh3c49SyuLreJ99U/8qHEPXHG05TUGySv5ws3Jr7Tc53At48zAf0gVJI6GbBVQWz6Evu4xCf4rE79yQ9e8+B4OJDwEzvAGNfYji0RQEmw/aaHXngiVXVWnbzL+HmKNdmrjyrMXC5+yYLDDE68LwBX6Y+n7pVVWvBrcaZz1HoNsdEpXtrgi5oxG9n82uxF7fpcTU48ZUa14bFXCHzO66tdu/g+8+AIZk02DpyIjllCTC697063iA5Y57OlrJ/xH7YZGqntrKbfrnA0W+rZjysewi4d5y0i490sCkb6wlOT/ZT0fYZCbFHxwFaRi7qKy/rxO+6C+83kNGyEoZ23hxhZOtxhGqIAoZKwL/1kOJmgWQUOjCEm3Tzt6vxOuO8nevlqeAAX4lgcJpsl/jKtC2sUnoKyJUusfoi4q8fzQDXMo8906IHi/tdfqs9hut8fS8TVnYW+rvO03gOm+ESvBlljliF1+09pYo3ZM8L8LRP9Y8mBDmn/h4jIea13trqINJnpQSmJF32ZjJHPW7JXYuVOFP4xivOMt9sEe9szUljPaGS1KgymKb37WKTAmTHT08mnTY+pQBjm5+zjh1GzkZGqgvS38OXjia1VWwimPZAHPckQRH")

message = '{"score":1314,"times":18,"game_data":"{\"seed\":1514998996323,\"action\":[[0.777,1.36,false],[0.921,0.99,false],[0.456,1.94,false],[0.716,1.46,false],[0.766,1.23,false],' + '[0.661,1.53,false],'*1310 + '],\"musicList\":[null,false,' +'false,'*1310 + ']}"}'


BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
obj = AES.new(aes_key, AES.MODE_CBC, aes_iv)
ciphertext = base64.b64encode(obj.encrypt(pad(message)))
#obj1 = AES.new(aes_key, AES.MODE_CBC, aes_iv)
#deciphertext = obj.decrypt(pad(enmessage))
#print deciphertext
payload = '{"base_req":{"session_id":"' + session_id + '","fast":1},"action_data":"' + ciphertext + '"}'

url = 'https://mp.weixin.qq.com/wxagame/wxagame_settlement'
headerinfo = {'Content-Type': 'application/json','Accept-Encoding': 'gzip','referer': 'https://servicewechat.com/wx7c8d593b2c3a7703/5/page-frame.html','charset': 'utf-8','User-Agent': 'MicroMessenger/6.6.1.1220(0x26060133) NetType/WIFI Language/zh_CN','Connection': 'Keep-Alive'}
r = requests.post(url, data=payload, headers=headerinfo)
print '*'*60
print 'stat_code:'
print r.status_code
#print '*'*60
msg = json.loads(r.text)
msgdecode = msg['base_resp']['errcode']
#print 'error_code:'
#print msgdecode
print '*'*60
print r.text
print '*'*60
logging.basicConfig(filename='run.log',format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filemode="a",level=logging.DEBUG)
logging.info(r.text)
logging.debug(payload)
#logging.warning(msgdecode)
