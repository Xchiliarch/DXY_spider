import time
import requests
import hashlib
import random
from fake_useragent import UserAgent
headers = {
    'authority': 'www.dxy.cn',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'accept': 'application/json',
    'content-type': 'application/json;charset=utf-8',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.dxy.cn/bbs/newweb/pc/board/47',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Connection': 'close'
}
#proxies={'https':'http://127.0.0.1:7890'}

def get_serverTimestamp(proxies):
    noncestr = str(random.randint(10000000, 99999999))
    timestamp = str(int(time.time() * 1000))
    sha1 = hashlib.sha1()
    sha1.update(
        'appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&'
        f'noncestr={noncestr}&'
        f'serverTimestamp=0&timestamp={timestamp}'.encode('utf-8'))
    sign = sha1.hexdigest()
    params = (
        ('serverTimestamp', '0'),
        ('timestamp', timestamp),
        ('noncestr', noncestr),
        ('sign', sign),
    )
    headers['user-agent']= UserAgent().random
    response= requests.get('https://www.dxy.cn/bbs/newweb/sys/time-millis/info', headers=headers, params=params,proxies=proxies,timeout=5)
    response.close()
    return str(response.json().get("data"))

def get_postId(sTs,boardId,subBoardId,pageNum,proxies):
    noncestr = str(random.randint(10000000, 99999999))
    timestamp = int(time.time() * 1000)
    serverTimestamp = sTs
    timestamp = str(timestamp)
    sha1 = hashlib.sha1()
    sha1.update(
        'appSignKey='
        '4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&'
        f'boardId={boardId}&'
        f'noncestr={noncestr}&'
        f'orderType=1&'
        f'pageNum={pageNum}&'
        f'pageSize=30&'
        f'postType=0&'
        f'serverTimestamp={serverTimestamp}&'
        f'showType=0&subBoardId={subBoardId}&timestamp={timestamp}'.encode('utf-8'))
    sign = sha1.hexdigest()
    params = (
        ('boardId', boardId),
        ('subBoardId', subBoardId),
        ('postType', '0'),
        ('orderType', '1'),
        ('pageNum', pageNum),
        ('pageSize', '30'),
        ('showType', '0'),
        ('serverTimestamp', serverTimestamp),
        ('timestamp', timestamp),
        ('noncestr', noncestr),
        ('sign', sign),
    )
    headers['user-agent']= UserAgent().random
    response = requests.get('https://www.dxy.cn/bbs/newweb/board/post/page', headers=headers, params=params,proxies=proxies,timeout=5)
    response.close()
    return(response.json())

def get_postInfo(sTs,postId,proxies):
    noncestr = str(random.randint(10000000, 99999999))
    timestamp = int(time.time() * 1000)
    serverTimestamp = sTs
    timestamp = str(timestamp)
    sha1 = hashlib.sha1()
    sha1.update(
        'appSignKey='
        '4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&'
        f'noncestr={noncestr}&'
        f'postId={postId}&'
        f'serverTimestamp={serverTimestamp}&'
        f'timestamp={timestamp}'.encode('utf-8'))
    sign = sha1.hexdigest()
    params = (
        ('postId',{postId}),
        ('serverTimestamp', serverTimestamp),
        ('timestamp', timestamp),
        ('noncestr', noncestr),
        ('sign', sign),
    )
    headers['user-agent']= UserAgent().random
    response = requests.get('https://www.dxy.cn/bbs/newweb/post/detail', headers=headers, params=params,proxies=proxies,timeout=5)
    response.close()
    return(response.json())

def get_userInfo(sTs,userId,proxies):
    noncestr = str(random.randint(10000000, 99999999))
    timestamp = int(time.time() * 1000)
    serverTimestamp = sTs
    timestamp = str(timestamp)
    sha1 = hashlib.sha1()
    sha1.update(
        'appSignKey='
        '4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&'
        f'noncestr={noncestr}&'
        
        f'serverTimestamp={serverTimestamp}&'
        f'timestamp={timestamp}&userId={userId}'.encode('utf-8'))
    sign = sha1.hexdigest()
    params = (
        ('userId',{userId}),
        ('serverTimestamp', serverTimestamp),
        ('timestamp', timestamp),
        ('noncestr', noncestr),
        ('sign', sign),
    )

    headers['user-agent']= UserAgent().random
    response = requests.get('https://www.dxy.cn/bbs/newweb/personal-page/user-info', headers=headers, params=params,proxies=proxies,timeout=5)
    response.close()
    return(response.json())

def get_replyList(postId,pageNum,sTs,proxies):
    noncestr = str(random.randint(10000000, 99999999))
    timestamp = int(time.time() * 1000)
    serverTimestamp = sTs
    timestamp = str(timestamp)
    sha1 = hashlib.sha1()
    sha1.update(
        'appSignKey='
        '4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&'
        f'noncestr={noncestr}&'
        f'onlyQuality=false&'
        f'orderType=1&'
        f'pageNum={pageNum}&'
        f'pageSize=100&'
        f'postId={postId}&'
        f'serverTimestamp={serverTimestamp}&'
        f'timestamp={timestamp}'.encode('utf-8'))
    sign = sha1.hexdigest()
    params = (
        ('postId',{postId}),
        ('pageNum',{pageNum}),
        ('pageSize',100),
        ('orderType',1),
        ('onlyQuality','false'),
        ('serverTimestamp', serverTimestamp),
        ('timestamp', timestamp),
        ('noncestr', noncestr),
        ('sign', sign),
    )

    response = requests.get('https://www.dxy.cn/bbs/newweb/post/reply/tree-list', headers=headers, params=params,proxies=proxies)

    return(response.json())

def get_reReply(postId,sTs,proxies):
    noncestr = str(random.randint(10000000, 99999999))
    timestamp = int(time.time() * 1000)
    serverTimestamp = sTs
    timestamp = str(timestamp)
    sha1 = hashlib.sha1()
    sha1.update(
        'appSignKey='
        '4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&'
        f'noncestr={noncestr}&'
        f'orderType=1&'
        f'page=1&'
        f'postId={postId}&'
        f'serverTimestamp={serverTimestamp}&'
        f'size=20&'
        f'timestamp={timestamp}'.encode('utf-8'))
    sign = sha1.hexdigest()
    params = (
        ('postId',{postId}),
        ('orderType',1),
        ('page',1),
        ('size',20),
        ('serverTimestamp', serverTimestamp),
        ('timestamp', timestamp),
        ('noncestr', noncestr),
        ('sign', sign),
    )

    response = requests.get('https://www.dxy.cn/bbs/newweb/post/discuss/list', headers=headers, params=params,proxies=proxies)

    return(response.json())

def get_replyInfo(postId,sTs,proxies):
    result =[]
    for page in range(1,100):
        datas=get_replyList(postId,page,sTs,proxies) 
        lastPage = datas.get('data').get('lastPage')
        if lastPage!= True:
            aa =datas.get('data').get('result')
            for a in aa:
                replys = parse_replyList(a,sTs,proxies)
                for reply in replys:
                    result.append(reply)
        else:
            break
    return result

def parse_userInfo(json):  
    if json:  
        userInfo = {}  
        userInfo['userId'] = json.get('data').get('userId')
        
        userInfo['nickname'] = json.get('data').get('nickname')
        userInfo['bbsStatusTitle'] = json.get('data').get('bbsStatusTitle')
        userInfo['isTalent'] = json.get('data').get('isTalent')
        userInfo['intelligent'] = json.get('data').get('intelligent')
        userInfo['bbsVotes'] = json.get('data').get('bbsVotes')
        userInfo['bbsPosts'] = json.get('data').get('bbsPosts')
        userInfo['qualityPostCount'] = json.get('data').get('qualityPostCount')
        userInfo['qualityReplyCount'] = json.get('data').get('qualityReplyCount')
        userInfo['followers'] = json.get('data').get('followers')
        userInfo['identificationTitle'] = json.get('data').get('identificationTitle')
        userInfo['isCommentator'] = json.get('data').get('isCommentator')
        if json.get('data').get('regTime') != None:
            userInfo['regTime'] = round(json.get('data').get('regTime')/1000)
            userInfo['regTimeTrans'] = time.strftime('%F %T', time.localtime(round(json.get('data').get('regTime')/1000)))
        else:
            userInfo['regTime'] = -1
        yield userInfo

def parse_postId(json):  
    if json:  
        items = json.get('data').get('result')  
        for item in items:  
            postId = {}  
            postId['entityId'] = item.get('entityId')
            postId['createdTime'] = item.get('createdTime')
            postId['createdTime_trans'] = time.strftime('%F %T', time.localtime(round(item.get('createdTime')/1000)))
            postId['subject'] = item.get('postInfo').get('subject')
            yield postId

def parse_postInfo(json):  
    if json:  
        postId = {}  
        postId['postId'] = json.get('data').get('id')
        postId['createdTime'] = time.strftime('%F %T', time.localtime(round(json.get('data').get('createTime')/1000)))
        postId['subject'] = json.get('data').get('subject')
        postId['votes'] = json.get('data').get('votes')
        postId['reads'] = json.get('data').get('reads')
        postId['replies'] = json.get('data').get('replies')
        postId['qualityPost'] = json.get('data').get('qualityPost')
        postId['approved'] = json.get('data').get('approved')
        postId['postUser'] = json.get('data').get('postUser').get('userId')
        yield postId

def parse_replyList(json,sTs,proxies): 
    replyInfo = {} 
    replyInfo['userId'] = json.get('userId')
    replyInfo['replyId'] = json.get('id')
    if json.get('hasTalk'):                                 #回复的回复
        replyInfo['talkCount'] = json.get('talkCount')
        replies = []
        if json.get('talkCount')<4:                         #回复的回复小于4可直接获取
            replyList = json.get('itemList')
        else:                                               #大于等于4需要再拉取
            replyData = get_reReply(json.get('id'),sTs,proxies)
            replyList= replyData.get('data').get('result')
        for reply in replyList:
            replies.append(reply.get('userId'))

        replyInfo['reply'] = replies
    else:
        replyInfo['talkCount'] =0
    yield replyInfo

def txt2list(txt_path):
    data_list = []
    with open(txt_path) as f:
        data = f.readlines()
    for line in data:
        line = line.strip("\n")  # 去除末尾的换行符
        temp = int(line)
        data_list.append(temp)
    return data_list