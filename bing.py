import requests
from PIL import Image
import json
import os


url = "https://cn.bing.com/images/api/custom/search"

params = {
    "q": "护照",
    "count": 25,
    "offset": 31,
    "skey": "9bYB7l0JWN5eEhDcnPQSQPpB-BVtEfCwB5wHoMb6StI",
    "safeSearch": "Strict",
    "mkt": "zh-cn",
    "setLang": "zh-cn",
    "IG": "5A2960EBA90E4138AC0CDA486D41FA60",
    "IID": "idpfs",
    "SFX": 2
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Cookie": ""
}

load_json_timeout = 5
download_pic_timeout = 20
sess = requests.session()
count = 1000
offset = 0

def download_pic(url, path):
    pic_content = sess.get(url=url, timeout=download_pic_timeout).content
    with open(path, 'wb') as f:
        f.write(pic_content)
    print("download %s success!" % path)

    return True

def download(cookie, keys, output_root, download_count):
    if headers['Cookie'] == "":
        headers['Cookie'] = cookie

    for key in keys:
        print("downloading: ", key)
        params['q'] = key
        params['count'] = count
        params['offset'] = offset
        dst_folder = os.path.join(output_root, key)

        try:
            resp = sess.get(url=url, params = params, headers=headers, timeout=load_json_timeout).content
        except:
            print("load json error, skip")
        pic_json = json.loads(resp).get("value")
        for i in pic_json:
            pic_url = i.get("contentUrl")
            pic_name = os.path.join(dst_folder, "%s_%d_%s_%s.jpg" % (key, download_count, i.get("width"), i.get("height")))
            if os.path.exists(pic_name):
                download_count += 1
                continue
            try:
                is_success = download_pic(pic_url, pic_name)
                if is_success:
                    download_count += 1
            except:
                print("load pic error, skip")
                continue

    return download_count

# if __name__ == '__main__':
    # path_c = '/datafile/chenbaocheng/dataset/credentials/download'
    # count = 100
    # offset = 0
    # keys = ["驾驶证","行驶证","身份证","港澳证","学生证","户口本","护照"]

    # # dog_keys = []
    # # with open('./dog.txt', 'r') as f:
    # #     dog_keys = f.readlines()
    
    # # for key in dog_keys:
    # #     doit(key, count, offset, path_d)
    # for key in keys:
    #     doit(key, count, offset, path_c)
    





