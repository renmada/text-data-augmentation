import http.client
import hashlib
import urllib
import random
import json
from tqdm import tqdm

appid = '20200403000411315'  # 填写你的appid
secretKey = '7HjoylhCni3lBsLmeWIr'  # 填写你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'


def _translate(sent, from_lan, to_lan):
    salt = random.randint(32768, 65536)
    sign = appid + sent + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(sent) + '&from=' + from_lan + '&to=' + \
          to_lan + '&salt=' + str(salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)['trans_result'][0]['dst']
        if httpClient:
            httpClient.close()
        return result
    except Exception as e:
        print(e)


def translate_and_back(sent):
    res1 = _translate(sent, 'zh', 'en')
    return _translate(res1, 'en', 'zh')


def translate(inp):
    if isinstance(inp, str):
        return translate_and_back(inp)
    else:
        res = []
        for sent in tqdm(inp):
            res.append(translate_and_back(sent))
    return res
