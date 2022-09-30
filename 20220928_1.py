
import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
def getraodname(address):
    address = address[3:]

    r = [str(i) for i in range(0, 10, 1)]
    r.extend(['樓', '號'])
    k = ['市','鎮','里','村','鄰','區']
    ban =['嘉里路','鎮環市路','美村路','路科十路','東村路','鐮村路','竹區路科十路']
    for t in r:
        address = address.replace(t,"")
    for t in k:
        b = True
        for d in ban:
            if t in d and address.find(d)!=-1:
                b =False
                break
        if b:
            address = address[address.find(t) + 1 if address.find(t) != -1 else 0:]
    ans = []
    if address.find('街')!=-1and address.find('路')!=-1:
        ans.append(address[:min([address.find('街'),address.find('路')])+1])
        ans.append(address[min([address.find('街'), address.find('路')]) + 2:max(address.find('街'), address.find('路'))+1])
    elif address.find('街')!=-1 or address.find('路')!=-1:
        ans.append(address[:max([address.find('街'), address.find('路')]) + 1])
    return ans
html = requests.get("https://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
data = []
Dict1 = dict()
for country in bsObj.find("table").find('select').findAll("option"):
    name = country.text
    respond = requests.post('https://www.ibon.com.tw/retail_inquiry_ajax.aspx',data={'strTargetField':'COUNTY',
'strKeyWords':country.text}).content
    bsObj1 = BeautifulSoup(respond, "lxml")
    for tr in bsObj1.find('table').findAll('tr')[1:-1]:
        td = tr.findAll('td')
        shop_name = td[1].text
        shop_address = td[2].text
        for k in getraodname(shop_address):
            if k not in Dict1:
                Dict1[k]=1
            else:
                Dict1[k]+=1
ans = sorted(list(Dict1.items()),key=lambda k:k[1],reverse=True)
print(ans[:3])




