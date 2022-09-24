import pymongo
import re
import random
import requests
from tqdm import *
from fake_useragent import UserAgent
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
from bson.objectid import ObjectId

def get(page):
    if page>3:
        response= requests.get('http://www.kxdaili.com/dailiip/2/1.html',timeout=5)
    else:
        response= requests.get(f'https://www.beesproxy.com/free/page/{page}',timeout=5)
    response.close()
    html = response.text
    return(html)
def parse(html):
    
    pattern = re.compile(
    f'<tr.*?>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',re.S)
    items = re.findall(pattern, html)
    return items

def update_proxy(collection,Timespan):                                 #填入数据表、IP生命周期，更新代理，返回 可用IP数
    ipf = 0
    ipu = 0
    print('updating Proxy')
    for page in range(0,4):                         #获取、验证代理ip
        html = get(page+1)
        ips= parse(html)
        rang = len(ips)
        ipf += rang
        count = 0
        for i in tqdm(range(rang)):
            proxies = {
                'https':'https://'+ips[i][0]+':'+ips[i][1],
                'http':'http://'+ips[i][0]+':'+ips[i][1]
                }
            headers = {
            'Connection': 'close'
            }

            try:
                response = requests.get('http://httpbin.org/get',headers = headers ,proxies = proxies,timeout = 3)
                response.close()
                if response.status_code ==200 :
                    result = {'ip':f'{ips[i][0]}','port':f'{ips[i][1]}','usage' : Timespan}
                    collection.insert_one(result)
                    count += 1
                else:
                    continue
            except requests.exceptions.RequestException as r:
                continue
            except requests.exceptions.ConnectionError as e:
                continue
        ipu += count
    print(f'{ipf} ips found,{ipu} ips available.')
    return count

def check(collection):                                                    #检查，删除Timespan=0的IP，返回可用IP、删除的ip数量                                              
    condition1 = {'usage': {'$lte':0} }   
    condition2 = {'usage': {'$gt':0} }
    deleted = collection.delete_many(( condition1 ))    #筛选timespan>0 IP
    proxyNum = collection.count_documents( condition2 )

    return proxyNum,deleted.deleted_count

def get_ip(collection):                                       #从Timespan>0的IP中随机选取一个并减少其Timespan
    condition = {'usage': {'$gt':0} }           
    proxyList = list(collection.find( condition )) #筛选timespan>0 IP

    if len(proxyList) <= 0:
        return 1
    rand = random.randint(0,len(proxyList)-1)
    proxyId = {'_id':(proxyList[rand].get('_id'))}            #记录选择的ID

    proxies = {'http':'http://' + proxyList[rand].get('ip')+':'+proxyList[rand ].get('port') }
    collection.update_one(proxyId ,{"$inc":{"usage":-1}} )    #更新IP的usage
    return proxies

def proxy(collection):
    Timespan = 200
    ipStatus = check(collection)
    if ipStatus[0] >0:
        proxies = get_ip(collection)
        if proxy != 1:
            return proxies
    update_proxy(collection,Timespan)
    proxies = proxy(collection)
    return proxies

def update_paid_proxy(collection,Timespan):                                 #填入数据表、IP生命周期，更新代理，返回 可用IP数
    ipf = 0
    ipu = 0
    #print('updating Proxy')
    response = requests.get('http://webapi.http.zhimacangku.com/getip?num=20&type=1&pro=&city=0&yys=0&port=1&pack=265267&ts=0&ys=0&cs=0&lb=6&sb=a&pb=4&mr=1&regions=')
    ips = re.findall('(.*?):(.*?)a',response.text)
    rang = len(ips)
    ipf += rang
    count = 0
    for i in range(rang):
        result = {'ip':f'{ips[i][0]}','port':f'{ips[i][1]}','usage' : Timespan}
        collection.insert_one(result)
        count += 1
    ipu += count
    #print(f'{ipf} ips found,{ipu} ips available.')
    return count

def paid_proxy(collection):
    Timespan = 5
    ipStatus = check(collection)
    if ipStatus[0] >0:
        proxies = get_ip(collection)
        if proxy != 1:
            return proxies
    update_paid_proxy(collection,Timespan)
    proxies =paid_proxy(collection)
    return proxies

