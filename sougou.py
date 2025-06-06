import requests
from PIL import Image
import json
import os
import random


url = "https://pic.sogou.com/napi/pc/searchList"

params = {
    "mode": 1,
    "tagQSign": "美国短毛猫",
    "start": 48,
    "xml_len": 48,
    "query": "美短"
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "Host": "pic.sogou.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Cookie": "SUID=DD4D68DF364A910A0000000063AAB47C; SUV=1672131695153647; SMYUV=1672139171724083; wuid=1691475769445; FUV=9bf36b60ad283cdf60fde51a87672abe; SNUID=3EF915EA9E9B9CFEF8EB577E9E7D4A4D; search_tip=1691475787358; fullscreen_tip=1691475813487; flip_tip=1691475813488"
}

load_json_timeout = 5
download_pic_timeout = 5
sess = requests.session()

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
        page = 10
        start = 48
        dst_folder = os.path.join(output_root, key)
        for it in range(page):
            params['query'] = key
            params['start'] = it*start
            try:
                resp = sess.get(url=url, params = params, headers=headers, timeout=load_json_timeout).content
                data_json = json.loads(resp).get("data").get("items")

            
                for data in data_json:
                    pic_url = data.get("oriPicUrl")
                    pic_name = os.path.join(dst_folder, "%s_%d.jpg" % (key, download_count))

                    if(os.path.exists(pic_name)):
                        print("pic exists!skip")
                        continue
                    try:
                        is_success = download_pic(pic_url, pic_name)
                        if is_success:
                            download_count += 1
                    except:
                        print("load pic error, skip")
                        continue
            except:
                print("load json error, skip")
    return download_count


# if __name__ == '__main__':
#     path_d = '/datafile/chenbaocheng/dataset/pets/raw/dogs'
#     page = 20
#     start = 48

 
#     cat_keys = []
    

#     for key in cat_keys:
#          for it in range(page):
#             try:
#                 doit(key, it*start, path_d)
#             except:
#                 continue
    





