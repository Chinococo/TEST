import json
import requests
import urllib3
url = 'https://quality.data.gov.tw/dq_download_json.php?nid=137993&md5_url=86ec099baa2d36c22ab3a87350b718de'
respond = requests.get(url).content.decode('utf-8')
respond = json.loads(respond)
respond = sorted(respond,key=lambda item:int(item['bemp']),reverse=True)
print('       站點代號,  場站名稱,                   場站總停車格,    場站目前車輛數量,  地址(中文),   空位數量')
for item in respond:
    if int(item['bemp'])<6:
        break
    print('%15s' %item['sno'], '%15s' %item['sna'], '%15s' %item['tot'], '%15s' %item['sbi'],'%15s' %item['ar'],'%15s' %item['bemp'])


