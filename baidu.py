import requests
from PIL import Image
import json
import os
import random
import numpy as np
import cv2
import hashlib
import base64


# url = "https://image.baidu.com/search/acjson"
# params = {
#     "tn": "resultjson_com",
#     "logid": 9946654843348324489,
#     "ipn": "rj",
#     "ct": 201326592,
#     "fp": "result",
#     "word": "投篮",
#     "queryWord": "投篮",
#     "cl": 2,
#     "lm": -1,
#     "ie": "utf-8",
#     "oe": "utf-8",
#     "st": -1,
#     "ic": 0,
#     "face": 0,
#     "istype": 2,
#     "nc": 1,
#     "pn": 60,
#     "rn": 30,
#     "gsm": "3c",
# }

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     "Cache-Control":"max-age=0",
#     "Host": "image.baidu.com",
#     "X-Requested-With": "XMLHttpRequest",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Cookie": ""
# }


# load_json_timeout = 5
# download_pic_timeout = 5
# sess = requests.session()

# def get_hash_file_name(base64_string):
#     hash_object = hashlib.sha256(base64_string.encode())
#     file_name = hash_object.hexdigest()[:10] + '_' + hash_object.hexdigest()[-10:]
#     return file_name.upper()

# def download_pic(url, path):
#     pic_content = sess.get(url=url, timeout=download_pic_timeout).content
#     base64_encoded = base64.b64encode(pic_content)
#     base64_string = base64_encoded.decode('utf-8')
#     file_name = get_hash_file_name(base64_string)
#     path = os.path.join(path, file_name + '.jpg')
    
#     nparr = np.frombuffer(pic_content, np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     if not img is None:
#         with open(path, 'wb') as f:
#             f.write(pic_content)
#         print("download %s success!" % path)
#         return True
#     return False


# def download(cookie, keys, output_root):
#     if headers['Cookie'] == "":
#         headers['Cookie'] = cookie

#     for key in keys:
#         print("downloading: ", key)
#         page = 100
#         pc = 30
#         dst_folder = os.path.join(output_root, key)
#         for it in range(page):
#             try:
#                 params['word'] = key
#                 params['pn'] = it*pc
#                 try:
#                     resp = sess.get(url     =   url, 
#                                     params  =   params, 
#                                     headers =   headers, 
#                                     timeout =   load_json_timeout,
#                                     # proxies =   {"http": "http://127.0.0.1:24000"}
#                                     )
#                     print(resp.headers.get('Content-Encoding'))
#                     resp = resp.content
#                 except:
#                     print("load json error, skip")

#                 data_json = json.loads(resp).get("data")

#                 for data in data_json:
#                     pic_url = data.get("middleURL")
#                     # pic_name = os.path.join(dst_folder, "%s_%d_%s_%s.jpg" % (key, download_count, data.get("width"), data.get("height")))
#                     try:
#                         is_success = download_pic(pic_url, dst_folder)
#                         if is_success:
#                             download_count += 1
#                     except:
#                         print("load pic error, skip")
#                         continue
                    
#                     if(data.get("setList") is not None):
#                         for idx, i in enumerate(data.get("setList")):
#                             pic_url = i.get("objURL")
#                             # pic_name = os.path.join(dst_folder, "%s_%d_%s_%s.jpg" % (key, download_count, i.get("width"), i.get("height")))
#                             try:
#                                 is_success = download_pic(pic_url, dst_folder)
#                                 if is_success:
#                                     download_count += 1
#                                     if download_count >=3000:
#                                         break
#                             except:
#                                 print("load pic error, skip")
#                                 continue
#             except Exception as e:
#                 print(e)
#                 continue
            # if download_count >= 500:
            #     return download_count
    # return download_count


# # if __name__ == '__main__':
#     # path_d = '/datafile/chenbaocheng/dataset/credentials/download/'
#     # page = 5
#     # pc = 30
#     # key = "行驶证"


#     # for it in range(page):
#     #     try:
#     #         doit(key, it*pc, path_d)
#     #     except:
#     #         continue

# url = "https://image.baidu.com/"
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     "Cache-Control":"max-age=0",
#     "Host": "image.baidu.com",
#     "X-Requested-With": "XMLHttpRequest",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
#     "cookie":"BAIDUID=1167EBDE62C878D91EB445DBF9F720C3:FG=1; BAIDUID_BFESS=1167EBDE62C878D91EB445DBF9F720C3:FG=1; BA_HECTOR=8k80a02h8021a524ahak25252td26v1k00o8l23; BDB2BID=1167EBDE62C878D91EB445DBF9F720C3:FG=1; .b2b.baidu.com=/; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[ac6JbONI1t6]=FrLfllaoGA6Tvd3TB4WUvY; BDSFRCVID=tKLOJeC627R7LzvJpLrVUCU0VLrNLuRTH6aobkxG6WV0ztYg9mwsEG0PUx8g0Ku-S2aWogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=tKLOJeC627R7LzvJpLrVUCU0VLrNLuRTH6aobkxG6WV0ztYg9mwsEG0PUx8g0Ku-S2aWogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSVRTM=388; www.baidu.com=/; BDUSS=J3a0YwV25uS3JCWkNsYXUwSnJzeWF4T3BSeGhtUEswLUdTYlZFTGxlQ0gwcHBuSVFBQUFBJCQAAAAAAQAAAAEAAAA4WcA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdFc2eHRXNnaj; BDUSS_BFESS=J3a0YwV25uS3JCWkNsYXUwSnJzeWF4T3BSeGhtUEswLUdTYlZFTGxlQ0gwcHBuSVFBQUFBJCQAAAAAAQAAAAEAAAA4WcA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdFc2eHRXNnaj; BD_CK_SAM=1; www.baidu.com=/; BD_UPN=12314753; www.baidu.com=/; BIDUPSID=1167EBDE62C878D9B5CFBB09CBA64856; COOKIE_SESSION=8_0_9_9_3_13_0_1_9_8_136_1_103366_0_132_0_1744871839_0_1744871971%7C9%237794191_39_1744616929%7C7; www.baidu.com=/; HMACCOUNT=FED6291D1593E407; .aistudio.baidu.com=/; HMACCOUNT=FED6291D1593E407; .www.baidu.com=/; HMACCOUNT_BFESS=FED6291D1593E407; .hm.baidu.com=/; HOSUPPORT=1; .passport.baidu.com=/; HOSUPPORT_BFESS=1; .passport.baidu.com=/; H_BDCLCKID_SF=tRAOoCP5JKvHjtOm5tOEhICV-frb-C62aKDshPc1BhcqEIL4jpKbXbIByl3G04bP0aIj-qR-BqRhVxbSj4Qo-4PbQNjULjOEbN5MVR65-h5nhMJa257JDMP0qJ-H5lby523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjJbDHAft5nK267JLRbVa5rDHJTg5DTjhPrM5-RrWMT-0bFH_M_5BPc-O4JsKljlLpQQ34vHWf7tLHn7_JjOKJvWsIQ536305hFsefcfbMQxtNRPXInjtpvhKf84-qJobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-lDjKB3e; H_BDCLCKID_SF_BFESS=tRAOoCP5JKvHjtOm5tOEhICV-frb-C62aKDshPc1BhcqEIL4jpKbXbIByl3G04bP0aIj-qR-BqRhVxbSj4Qo-4PbQNjULjOEbN5MVR65-h5nhMJa257JDMP0qJ-H5lby523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjJbDHAft5nK267JLRbVa5rDHJTg5DTjhPrM5-RrWMT-0bFH_M_5BPc-O4JsKljlLpQQ34vHWf7tLHn7_JjOKJvWsIQ536305hFsefcfbMQxtNRPXInjtpvhKf84-qJobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-lDjKB3e; H_PS_645EC=4b19kL2WdFj%2FuGhiWSQkvOAo8mJJlXD61ew6TP3XjOCMmWd0uQ5d2ISW6pjoncdhtm1oCmTExtI; www.baidu.com=/; H_PS_PSSID=61027_62339_62327_62832_62848_62868_62883_62888_62909_62919_62921_62939; H_WISE_SIDS=62327_62832_62848_62868_62909; H_WISE_SIDS_BFESS=61027_62339_62327_62832_62848_62868_62883_62888_62909_62919_62921_62939; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1744871837; .www.baidu.com=/; Hm_lpvt_be6b0f3e9ab579df8f47db4641a0a406=1744617454; .aistudio.baidu.com=/; Hm_lvt_01e907653ac089993ee83ed00ef9c2f3=1736158512,1736216420,1737027587,1737439183; .yiyan.baidu.com=/; Hm_lvt_20c5d09058effeaad8703343e5fa9c95=1739157763,1739257091,1739446857; /usercenter/paper/show/=2026-02-13T11:40:57.000Z; Hm_lvt_28a17f66627d87f1d046eae152a1c93d=1738745964; .developer.baidu.com=/; Hm_lvt_292b2e1608b0823c1cb6beef7243ef34=1740377484; .tieba.baidu.com=/; Hm_lvt_3abe3fb0969d25e335f1fe7559defcc6=1738745964; .developer.baidu.com=/; Hm_lvt_46c8852ae89f7d9526f0082fafa15edd=1736156873; .jingyan.baidu.com=/; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1741607713; .pan.baidu.com=/; Hm_lvt_a1adbfa038f57bb04cf9a0fbd880fad1=1742201593; /view/=2026-03-17T08:53:13.000Z; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1744871837; .www.baidu.com=/; Hm_lvt_be6b0f3e9ab579df8f47db4641a0a406=1744616809; .aistudio.baidu.com=/; Hm_lvt_fa0277816200010a74ab7d2895df481b=1741608094; .pan.baidu.com=/; Hm_up_be6b0f3e9ab579df8f47db4641a0a406=%7B%22user_reg_date%22%3A%7B%22value%22%3A%2220230910%22%2C%22scope%22%3A1%7D%2C%22user_course_rt%22%3A%7B%22value%22%3A%22%E9%9D%9E%E8%AF%BE%E7%A8%8B%E7%94%A8%E6%88%B7%22%2C%22scope%22%3A1%7D%2C%22user_center_type%22%3A%7B%22value%22%3A%22%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%226078314%22%2C%22scope%22%3A1%7D%7D; .aistudio.baidu.com=/; IV=100711B3EA4F6DBB563ED4823B65B943; ada.baidu.com=/; MAWEBCUID=web_komrkesepDngOzsnADqxNGtJpYdDvByQhPJCnCFdAkFCbHpTlC; PANWEB=1; .pan.baidu.com=/; PSINO=6; PSTM=1735524678; PTOKEN=f3241c9c96609fa0410358ca42bc91a0; .passport.baidu.com=/; PTOKEN_BFESS=f3241c9c96609fa0410358ca42bc91a0; .passport.baidu.com=/; STOKEN=fd1750c8e453b3fbc55c5cae9c10ddb0d887b571c8881f474c42b5f3055e2da9; .passport.baidu.com=/; STOKEN_BFESS=fd1750c8e453b3fbc55c5cae9c10ddb0d887b571c8881f474c42b5f3055e2da9; .passport.baidu.com=/; UBI=fi_PncwhpxZ%7ETaJc7C80yyLSBOod6yqJFA1; .passport.baidu.com=/; UBI_BFESS=fi_PncwhpxZ%7ETaJc7C80yyLSBOod6yqJFA1; .passport.baidu.com=/; ZFY=f0GSlHnudSYjyJqEV0vIDBlGoyvhIMGkM0U3ehnkNMs:C; ab_bid=2e63dbd197deafc1f4b6a1d7171a00d64450; .miao.baidu.com=/; ab_jid=404329ff6d7a0439b1a76db48597ca8c77ac; .miao.baidu.com=/; ab_jid_BFESS=404329ff6d7a0439b1a76db48597ca8c77ac; .miao.baidu.com=/; ab_sr=1.0.1_NThiNWMzNDc5ZGFmNjc0MDY4NmU2Mjc2OTJhNjU1NDVmZTU4Nzk1NjdjMmY2ZTMyYzYxMjlmNzNkZTFlNGQyMTg0MTcyYzMyYWQzY2UyNDBhZmUxMmVjOTg1Y2FmZWIwY2Y2YWIyNzVjYmExNDBmMzQ1MzlkYjU2MzA4NGFlOWY2ZjJhZWQ2NWQyODkxNDg1NDE2YjFkNTYzNzY5YWY0Nw==; ai-studio-lc=zh_CN; aistudio.baidu.com=/; baikeVisitId=a2126f96-e880-440a-a221-4288c982ec67; .baike.baidu.com=/; baikeVisitId=2153f7a5-7677-4710-8ac4-9b5b3312dbd5; .www.baidu.com=/; channel=baidusearch; .baike.baidu.com=/; channel=guge.smxr.com; .www.baidu.com=/; delPer=0; indexPageSugList=%5B%22%E6%96%AF%E8%8A%AC%E5%85%8B%E6%96%AF%E7%8C%AB%22%2C%22%E9%9B%AA%E5%A5%88%E7%91%9E%22%2C%22%E9%BB%91%E8%89%B2%E6%8B%89%E5%B8%83%E6%8B%89%E5%A4%9A%22%2C%22%E7%BD%97%E5%A8%81%E7%BA%B3%E7%8A%AC%22%2C%22%E6%9D%9C%E5%AE%BE%E7%8A%AC%22%2C%22%E5%9C%A8jupyter%E4%B8%AD%E5%AE%89%E8%A3%85%E5%BA%93%E6%80%8E%E4%B9%88%E5%AE%89%E8%A3%85%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E6%80%A7%E6%84%9F%E5%A5%B3%E6%A8%A1%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3%E6%80%A7%E6%84%9F%E5%A5%B3%E6%A8%A1%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3%22%5D; image.baidu.com=/; jsdk-uuid=0516b316-b08c-49e3-be4e-fce991fda388; aistudio.baidu.com=/"
# }
# # 建立连接
# sess = requests.session()
# load_json_timeout = 5
# download_pic_timeout = 5
# download_count = 0
# key ="宝宝照片"
# search_url = "https://image.baidu.com/{key}"
# # 打印连接状态
# if sess.get(url=url, headers=headers).status_code == 200:
#     print("连接成功")
#     # 打印响应内容、响应头和保存baidu_1.html文件
#     print(sess.get(url=url, headers=headers).content)
#     with open("baidu_1.html", "wb") as f:
#         f.write(sess.get(url=url, headers=headers).content)
# else:
#     print("连接失败")
#     # 打印响应内容、响应头和保存连接的页面html文件
#     print(sess.get(url=url, headers=headers).content)
#     with open("baidu.html", "wb") as f:
#         f.write(sess.get(url=url, headers=headers).content)

import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import os
import time
import re
import lxml.html as html
# https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=%E9%AD%94%E6%B3%95%E7%A6%81%E4%B9%A6%E6%BC%AB%E7%94%BB%E5%86%85%E5%AE%B9
# 更新URL和搜索参数
url = "https://image.baidu.com/search/index"
params = {
    "tn": "baiduimage",
    "fm": "result",
    "ie": "utf-8",
    "word": "魔法禁书目录",
    "queryWord": "",
    "pn":"60",
}

# 更新请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": "",
    "Referer": "https://image.baidu.com/",# 跟着url的
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1"
}



load_json_timeout = 5
download_pic_timeout = 5
sess = requests.session()

def get_hash_file_name(base64_string):
    hash_object = hashlib.sha256(base64_string.encode())
    file_name = hash_object.hexdigest()[:10] + '_' + hash_object.hexdigest()[-10:]
    return file_name.upper()

def download_pic(url, path):
    pic_content = sess.get(url=url, timeout=download_pic_timeout).content
    base64_encoded = base64.b64encode(pic_content)
    base64_string = base64_encoded.decode('utf-8')
    file_name = get_hash_file_name(base64_string)
    path = os.path.join(path, file_name + '.jpg')
    
    nparr = np.frombuffer(pic_content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if not img is None:
        with open(path, 'wb') as f:
            f.write(pic_content)
        print("download %s success!" % path)
        return True
    return False

def extract_image_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = []
    img_tags = soup.find_all('img', src=True)
    # 打印前10个img_tags
    print("前10个img_tags:", img_tags[:10])
    for img in img_tags:
        src = img.get('src', '')
        # 如果src中包含https://img+数字.baidu.com/，则认为是图片链接
        image_urls = [src for src in src if re.search(r"https://img\d+\.baidu\.com/.*", src)]
        # if 'https://img' in src and 'baidu.com' in src:
        #     # 过滤掉非图片链接
        #     if src.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        #         image_urls.append(src)
    #打印前10个图片链接
    print("前10个图片链接:", image_urls[:10])
    # 去重
    image_urls = list(set(image_urls))

    return image_urls

def download(cookie, keys, output_root, download_count):
    if headers['Cookie'] == "":
        headers['Cookie'] = cookie
    
    
    for key in keys:
        print(f"搜索关键词: {key}")
        dst_folder = os.path.join(output_root, key)
        os.makedirs(dst_folder, exist_ok=True)
        current_count = 0
        pc = 30
        page = 1
        while current_count < download_count and page <= 100:
            try:
                # 更新搜索参数
                # params.update({
                #     'word': key,
                #     'page': page
                # })
                params['word'] = key
                params['pn'] = page * pc

                search_url = f"https://image.baidu.com/search/index?tn=baiduimage&word={key}"
                # 添加随机延迟
                time.sleep(random.uniform(2, 4))
                
                print(f"请求第 {page} 页...")
                resp = sess.get(
                    url=search_url,
                    params=params,
                    headers=headers,
                    timeout=load_json_timeout,
                    proxies={"http": "http://127.0.0.1:7880"}  # 注意这里改成7890端口
                )
                
                if resp.status_code != 200:
                    print(f"请求失败: {resp.status_code}")
                    break
                
                # 提取图片URL
                image_urls = extract_image_urls(resp.content)
                
                if not image_urls:
                    print("未找到图片URL")
                    print(f"页面URL: {resp.url}")
                    # 保存页面内容以供调试
                    with open(f"debug_page_{page}.html", "wb") as f:
                        f.write(resp.content)
                    break
                
                print(f"找到 {len(image_urls)} 个图片URL")
                
                # 下载图片
                for img_url in image_urls:
                    try:
                        print(f"下载图片: {img_url}")
                        is_success = download_pic(img_url, dst_folder)
                        
                        if is_success:
                            current_count += 1
                            print(f"进度: {current_count}/{download_count}")
                            
                            if current_count >= download_count:
                                break
                                
                        # 下载间隔
                        time.sleep(random.uniform(1, 2))
                        
                    except Exception as e:
                        print(f"下载出错: {str(e)}")
                        continue
                
                page += 1
                
            except Exception as e:
                print(f"页面处理出错: {str(e)}")
                time.sleep(5)
                continue
            
        print(f"完成关键词: {key}")

if __name__ == "__main__":
    category_map = [
        "宝宝生活照",
        "儿童写真照",
        "儿童生活照",
        "儿童艺术照",
        "宝宝艺术照",
        "儿童摄影照",
        "黑白漫画内容",
        "搞笑黑白漫画内容",
        "励志黑白漫画内容",
        "五六岁小孩照片",
        "宝宝满月照片",
        "新生儿创意满月照图片",
        "小孩创意照片",
        "小孩生活照",
        "宝宝游泳图片",
        "婴儿穿尿不湿图片",
        "小女孩水下游泳",
        "小男孩水下游泳",
        "婴儿全身照图片",
        "婴儿照片出生",
        "婴儿洗澡照",
        "宝宝冲凉照",
        "自己画搞笑漫画",
        "漫画内容",
        "禁书漫画内容",
        "魔法禁书漫画内容",
        ]
    cookie = "BAIDUID=1167EBDE62C878D91EB445DBF9F720C3:FG=1; BAIDUID_BFESS=1167EBDE62C878D91EB445DBF9F720C3:FG=1; BA_HECTOR=8k80a02h8021a524ahak25252td26v1k00o8l23; BDB2BID=1167EBDE62C878D91EB445DBF9F720C3:FG=1; .b2b.baidu.com=/; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[ac6JbONI1t6]=FrLfllaoGA6Tvd3TB4WUvY; BDSFRCVID=tKLOJeC627R7LzvJpLrVUCU0VLrNLuRTH6aobkxG6WV0ztYg9mwsEG0PUx8g0Ku-S2aWogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=tKLOJeC627R7LzvJpLrVUCU0VLrNLuRTH6aobkxG6WV0ztYg9mwsEG0PUx8g0Ku-S2aWogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSVRTM=388; www.baidu.com=/; BDUSS=J3a0YwV25uS3JCWkNsYXUwSnJzeWF4T3BSeGhtUEswLUdTYlZFTGxlQ0gwcHBuSVFBQUFBJCQAAAAAAQAAAAEAAAA4WcA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdFc2eHRXNnaj; BDUSS_BFESS=J3a0YwV25uS3JCWkNsYXUwSnJzeWF4T3BSeGhtUEswLUdTYlZFTGxlQ0gwcHBuSVFBQUFBJCQAAAAAAQAAAAEAAAA4WcA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdFc2eHRXNnaj; BD_CK_SAM=1; www.baidu.com=/; BD_UPN=12314753; www.baidu.com=/; BIDUPSID=1167EBDE62C878D9B5CFBB09CBA64856; COOKIE_SESSION=8_0_9_9_3_13_0_1_9_8_136_1_103366_0_132_0_1744871839_0_1744871971%7C9%237794191_39_1744616929%7C7; www.baidu.com=/; HMACCOUNT=FED6291D1593E407; .aistudio.baidu.com=/; HMACCOUNT=FED6291D1593E407; .www.baidu.com=/; HMACCOUNT_BFESS=FED6291D1593E407; .hm.baidu.com=/; HOSUPPORT=1; .passport.baidu.com=/; HOSUPPORT_BFESS=1; .passport.baidu.com=/; H_BDCLCKID_SF=tRAOoCP5JKvHjtOm5tOEhICV-frb-C62aKDshPc1BhcqEIL4jpKbXbIByl3G04bP0aIj-qR-BqRhVxbSj4Qo-4PbQNjULjOEbN5MVR65-h5nhMJa257JDMP0qJ-H5lby523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjJbDHAft5nK267JLRbVa5rDHJTg5DTjhPrM5-RrWMT-0bFH_M_5BPc-O4JsKljlLpQQ34vHWf7tLHn7_JjOKJvWsIQ536305hFsefcfbMQxtNRPXInjtpvhKf84-qJobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-lDjKB3e; H_BDCLCKID_SF_BFESS=tRAOoCP5JKvHjtOm5tOEhICV-frb-C62aKDshPc1BhcqEIL4jpKbXbIByl3G04bP0aIj-qR-BqRhVxbSj4Qo-4PbQNjULjOEbN5MVR65-h5nhMJa257JDMP0qJ-H5lby523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjJbDHAft5nK267JLRbVa5rDHJTg5DTjhPrM5-RrWMT-0bFH_M_5BPc-O4JsKljlLpQQ34vHWf7tLHn7_JjOKJvWsIQ536305hFsefcfbMQxtNRPXInjtpvhKf84-qJobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-lDjKB3e; H_PS_645EC=4b19kL2WdFj%2FuGhiWSQkvOAo8mJJlXD61ew6TP3XjOCMmWd0uQ5d2ISW6pjoncdhtm1oCmTExtI; www.baidu.com=/; H_PS_PSSID=61027_62339_62327_62832_62848_62868_62883_62888_62909_62919_62921_62939; H_WISE_SIDS=62327_62832_62848_62868_62909; H_WISE_SIDS_BFESS=61027_62339_62327_62832_62848_62868_62883_62888_62909_62919_62921_62939; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1744871837; .www.baidu.com=/; Hm_lpvt_be6b0f3e9ab579df8f47db4641a0a406=1744617454; .aistudio.baidu.com=/; Hm_lvt_01e907653ac089993ee83ed00ef9c2f3=1736158512,1736216420,1737027587,1737439183; .yiyan.baidu.com=/; Hm_lvt_20c5d09058effeaad8703343e5fa9c95=1739157763,1739257091,1739446857; /usercenter/paper/show/=2026-02-13T11:40:57.000Z; Hm_lvt_28a17f66627d87f1d046eae152a1c93d=1738745964; .developer.baidu.com=/; Hm_lvt_292b2e1608b0823c1cb6beef7243ef34=1740377484; .tieba.baidu.com=/; Hm_lvt_3abe3fb0969d25e335f1fe7559defcc6=1738745964; .developer.baidu.com=/; Hm_lvt_46c8852ae89f7d9526f0082fafa15edd=1736156873; .jingyan.baidu.com=/; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1741607713; .pan.baidu.com=/; Hm_lvt_a1adbfa038f57bb04cf9a0fbd880fad1=1742201593; /view/=2026-03-17T08:53:13.000Z; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1744871837; .www.baidu.com=/; Hm_lvt_be6b0f3e9ab579df8f47db4641a0a406=1744616809; .aistudio.baidu.com=/; Hm_lvt_fa0277816200010a74ab7d2895df481b=1741608094; .pan.baidu.com=/; Hm_up_be6b0f3e9ab579df8f47db4641a0a406=%7B%22user_reg_date%22%3A%7B%22value%22%3A%2220230910%22%2C%22scope%22%3A1%7D%2C%22user_course_rt%22%3A%7B%22value%22%3A%22%E9%9D%9E%E8%AF%BE%E7%A8%8B%E7%94%A8%E6%88%B7%22%2C%22scope%22%3A1%7D%2C%22user_center_type%22%3A%7B%22value%22%3A%22%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%226078314%22%2C%22scope%22%3A1%7D%7D; .aistudio.baidu.com=/; IV=100711B3EA4F6DBB563ED4823B65B943; ada.baidu.com=/; MAWEBCUID=web_komrkesepDngOzsnADqxNGtJpYdDvByQhPJCnCFdAkFCbHpTlC; PANWEB=1; .pan.baidu.com=/; PSINO=6; PSTM=1735524678; PTOKEN=f3241c9c96609fa0410358ca42bc91a0; .passport.baidu.com=/; PTOKEN_BFESS=f3241c9c96609fa0410358ca42bc91a0; .passport.baidu.com=/; STOKEN=fd1750c8e453b3fbc55c5cae9c10ddb0d887b571c8881f474c42b5f3055e2da9; .passport.baidu.com=/; STOKEN_BFESS=fd1750c8e453b3fbc55c5cae9c10ddb0d887b571c8881f474c42b5f3055e2da9; .passport.baidu.com=/; UBI=fi_PncwhpxZ%7ETaJc7C80yyLSBOod6yqJFA1; .passport.baidu.com=/; UBI_BFESS=fi_PncwhpxZ%7ETaJc7C80yyLSBOod6yqJFA1; .passport.baidu.com=/; ZFY=f0GSlHnudSYjyJqEV0vIDBlGoyvhIMGkM0U3ehnkNMs:C; ab_bid=2e63dbd197deafc1f4b6a1d7171a00d64450; .miao.baidu.com=/; ab_jid=404329ff6d7a0439b1a76db48597ca8c77ac; .miao.baidu.com=/; ab_jid_BFESS=404329ff6d7a0439b1a76db48597ca8c77ac; .miao.baidu.com=/; ab_sr=1.0.1_NThiNWMzNDc5ZGFmNjc0MDY4NmU2Mjc2OTJhNjU1NDVmZTU4Nzk1NjdjMmY2ZTMyYzYxMjlmNzNkZTFlNGQyMTg0MTcyYzMyYWQzY2UyNDBhZmUxMmVjOTg1Y2FmZWIwY2Y2YWIyNzVjYmExNDBmMzQ1MzlkYjU2MzA4NGFlOWY2ZjJhZWQ2NWQyODkxNDg1NDE2YjFkNTYzNzY5YWY0Nw==; ai-studio-lc=zh_CN; aistudio.baidu.com=/; baikeVisitId=a2126f96-e880-440a-a221-4288c982ec67; .baike.baidu.com=/; baikeVisitId=2153f7a5-7677-4710-8ac4-9b5b3312dbd5; .www.baidu.com=/; channel=baidusearch; .baike.baidu.com=/; channel=guge.smxr.com; .www.baidu.com=/; delPer=0; indexPageSugList=%5B%22%E6%96%AF%E8%8A%AC%E5%85%8B%E6%96%AF%E7%8C%AB%22%2C%22%E9%9B%AA%E5%A5%88%E7%91%9E%22%2C%22%E9%BB%91%E8%89%B2%E6%8B%89%E5%B8%83%E6%8B%89%E5%A4%9A%22%2C%22%E7%BD%97%E5%A8%81%E7%BA%B3%E7%8A%AC%22%2C%22%E6%9D%9C%E5%AE%BE%E7%8A%AC%22%2C%22%E5%9C%A8jupyter%E4%B8%AD%E5%AE%89%E8%A3%85%E5%BA%93%E6%80%8E%E4%B9%88%E5%AE%89%E8%A3%85%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E6%80%A7%E6%84%9F%E5%A5%B3%E6%A8%A1%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3%E6%80%A7%E6%84%9F%E5%A5%B3%E6%A8%A1%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3%22%5D; image.baidu.com=/; jsdk-uuid=0516b316-b08c-49e3-be4e-fce991fda388; aistudio.baidu.com=/"
    output_root = '/data0/work/Ahri/workspace/spider/0418data/'    # 输出文件夹
    download_count = 4000  # 每个关键词下载的图片数量
    download(cookie, category_map, output_root, download_count)


# # 使用示例
# cookie = "BAIDUID=1167EBDE62C878D91EB445DBF9F720C3:FG=1; BAIDUID_BFESS=1167EBDE62C878D91EB445DBF9F720C3:FG=1; BA_HECTOR=8k80a02h8021a524ahak25252td26v1k00o8l23; BDB2BID=1167EBDE62C878D91EB445DBF9F720C3:FG=1; .b2b.baidu.com=/; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[ac6JbONI1t6]=FrLfllaoGA6Tvd3TB4WUvY; BDSFRCVID=tKLOJeC627R7LzvJpLrVUCU0VLrNLuRTH6aobkxG6WV0ztYg9mwsEG0PUx8g0Ku-S2aWogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=tKLOJeC627R7LzvJpLrVUCU0VLrNLuRTH6aobkxG6WV0ztYg9mwsEG0PUx8g0Ku-S2aWogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSVRTM=388; www.baidu.com=/; BDUSS=J3a0YwV25uS3JCWkNsYXUwSnJzeWF4T3BSeGhtUEswLUdTYlZFTGxlQ0gwcHBuSVFBQUFBJCQAAAAAAQAAAAEAAAA4WcA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdFc2eHRXNnaj; BDUSS_BFESS=J3a0YwV25uS3JCWkNsYXUwSnJzeWF4T3BSeGhtUEswLUdTYlZFTGxlQ0gwcHBuSVFBQUFBJCQAAAAAAQAAAAEAAAA4WcA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdFc2eHRXNnaj; BD_CK_SAM=1; www.baidu.com=/; BD_UPN=12314753; www.baidu.com=/; BIDUPSID=1167EBDE62C878D9B5CFBB09CBA64856; COOKIE_SESSION=8_0_9_9_3_13_0_1_9_8_136_1_103366_0_132_0_1744871839_0_1744871971%7C9%237794191_39_1744616929%7C7; www.baidu.com=/; HMACCOUNT=FED6291D1593E407; .aistudio.baidu.com=/; HMACCOUNT=FED6291D1593E407; .www.baidu.com=/; HMACCOUNT_BFESS=FED6291D1593E407; .hm.baidu.com=/; HOSUPPORT=1; .passport.baidu.com=/; HOSUPPORT_BFESS=1; .passport.baidu.com=/; H_BDCLCKID_SF=tRAOoCP5JKvHjtOm5tOEhICV-frb-C62aKDshPc1BhcqEIL4jpKbXbIByl3G04bP0aIj-qR-BqRhVxbSj4Qo-4PbQNjULjOEbN5MVR65-h5nhMJa257JDMP0qJ-H5lby523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjJbDHAft5nK267JLRbVa5rDHJTg5DTjhPrM5-RrWMT-0bFH_M_5BPc-O4JsKljlLpQQ34vHWf7tLHn7_JjOKJvWsIQ536305hFsefcfbMQxtNRPXInjtpvhKf84-qJobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-lDjKB3e; H_BDCLCKID_SF_BFESS=tRAOoCP5JKvHjtOm5tOEhICV-frb-C62aKDshPc1BhcqEIL4jpKbXbIByl3G04bP0aIj-qR-BqRhVxbSj4Qo-4PbQNjULjOEbN5MVR65-h5nhMJa257JDMP0qJ-H5lby523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjJbDHAft5nK267JLRbVa5rDHJTg5DTjhPrM5-RrWMT-0bFH_M_5BPc-O4JsKljlLpQQ34vHWf7tLHn7_JjOKJvWsIQ536305hFsefcfbMQxtNRPXInjtpvhKf84-qJobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-lDjKB3e; H_PS_645EC=4b19kL2WdFj%2FuGhiWSQkvOAo8mJJlXD61ew6TP3XjOCMmWd0uQ5d2ISW6pjoncdhtm1oCmTExtI; www.baidu.com=/; H_PS_PSSID=61027_62339_62327_62832_62848_62868_62883_62888_62909_62919_62921_62939; H_WISE_SIDS=62327_62832_62848_62868_62909; H_WISE_SIDS_BFESS=61027_62339_62327_62832_62848_62868_62883_62888_62909_62919_62921_62939; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1744871837; .www.baidu.com=/; Hm_lpvt_be6b0f3e9ab579df8f47db4641a0a406=1744617454; .aistudio.baidu.com=/; Hm_lvt_01e907653ac089993ee83ed00ef9c2f3=1736158512,1736216420,1737027587,1737439183; .yiyan.baidu.com=/; Hm_lvt_20c5d09058effeaad8703343e5fa9c95=1739157763,1739257091,1739446857; /usercenter/paper/show/=2026-02-13T11:40:57.000Z; Hm_lvt_28a17f66627d87f1d046eae152a1c93d=1738745964; .developer.baidu.com=/; Hm_lvt_292b2e1608b0823c1cb6beef7243ef34=1740377484; .tieba.baidu.com=/; Hm_lvt_3abe3fb0969d25e335f1fe7559defcc6=1738745964; .developer.baidu.com=/; Hm_lvt_46c8852ae89f7d9526f0082fafa15edd=1736156873; .jingyan.baidu.com=/; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1741607713; .pan.baidu.com=/; Hm_lvt_a1adbfa038f57bb04cf9a0fbd880fad1=1742201593; /view/=2026-03-17T08:53:13.000Z; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1744871837; .www.baidu.com=/; Hm_lvt_be6b0f3e9ab579df8f47db4641a0a406=1744616809; .aistudio.baidu.com=/; Hm_lvt_fa0277816200010a74ab7d2895df481b=1741608094; .pan.baidu.com=/; Hm_up_be6b0f3e9ab579df8f47db4641a0a406=%7B%22user_reg_date%22%3A%7B%22value%22%3A%2220230910%22%2C%22scope%22%3A1%7D%2C%22user_course_rt%22%3A%7B%22value%22%3A%22%E9%9D%9E%E8%AF%BE%E7%A8%8B%E7%94%A8%E6%88%B7%22%2C%22scope%22%3A1%7D%2C%22user_center_type%22%3A%7B%22value%22%3A%22%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%226078314%22%2C%22scope%22%3A1%7D%7D; .aistudio.baidu.com=/; IV=100711B3EA4F6DBB563ED4823B65B943; ada.baidu.com=/; MAWEBCUID=web_komrkesepDngOzsnADqxNGtJpYdDvByQhPJCnCFdAkFCbHpTlC; PANWEB=1; .pan.baidu.com=/; PSINO=6; PSTM=1735524678; PTOKEN=f3241c9c96609fa0410358ca42bc91a0; .passport.baidu.com=/; PTOKEN_BFESS=f3241c9c96609fa0410358ca42bc91a0; .passport.baidu.com=/; STOKEN=fd1750c8e453b3fbc55c5cae9c10ddb0d887b571c8881f474c42b5f3055e2da9; .passport.baidu.com=/; STOKEN_BFESS=fd1750c8e453b3fbc55c5cae9c10ddb0d887b571c8881f474c42b5f3055e2da9; .passport.baidu.com=/; UBI=fi_PncwhpxZ%7ETaJc7C80yyLSBOod6yqJFA1; .passport.baidu.com=/; UBI_BFESS=fi_PncwhpxZ%7ETaJc7C80yyLSBOod6yqJFA1; .passport.baidu.com=/; ZFY=f0GSlHnudSYjyJqEV0vIDBlGoyvhIMGkM0U3ehnkNMs:C; ab_bid=2e63dbd197deafc1f4b6a1d7171a00d64450; .miao.baidu.com=/; ab_jid=404329ff6d7a0439b1a76db48597ca8c77ac; .miao.baidu.com=/; ab_jid_BFESS=404329ff6d7a0439b1a76db48597ca8c77ac; .miao.baidu.com=/; ab_sr=1.0.1_NThiNWMzNDc5ZGFmNjc0MDY4NmU2Mjc2OTJhNjU1NDVmZTU4Nzk1NjdjMmY2ZTMyYzYxMjlmNzNkZTFlNGQyMTg0MTcyYzMyYWQzY2UyNDBhZmUxMmVjOTg1Y2FmZWIwY2Y2YWIyNzVjYmExNDBmMzQ1MzlkYjU2MzA4NGFlOWY2ZjJhZWQ2NWQyODkxNDg1NDE2YjFkNTYzNzY5YWY0Nw==; ai-studio-lc=zh_CN; aistudio.baidu.com=/; baikeVisitId=a2126f96-e880-440a-a221-4288c982ec67; .baike.baidu.com=/; baikeVisitId=2153f7a5-7677-4710-8ac4-9b5b3312dbd5; .www.baidu.com=/; channel=baidusearch; .baike.baidu.com=/; channel=guge.smxr.com; .www.baidu.com=/; delPer=0; indexPageSugList=%5B%22%E6%96%AF%E8%8A%AC%E5%85%8B%E6%96%AF%E7%8C%AB%22%2C%22%E9%9B%AA%E5%A5%88%E7%91%9E%22%2C%22%E9%BB%91%E8%89%B2%E6%8B%89%E5%B8%83%E6%8B%89%E5%A4%9A%22%2C%22%E7%BD%97%E5%A8%81%E7%BA%B3%E7%8A%AC%22%2C%22%E6%9D%9C%E5%AE%BE%E7%8A%AC%22%2C%22%E5%9C%A8jupyter%E4%B8%AD%E5%AE%89%E8%A3%85%E5%BA%93%E6%80%8E%E4%B9%88%E5%AE%89%E8%A3%85%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E6%80%A7%E6%84%9F%E5%A5%B3%E6%A8%A1%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3%E6%80%A7%E6%84%9F%E5%A5%B3%E6%A8%A1%22%2C%22%E4%BA%8C%E6%AC%A1%E5%85%83%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3%22%5D; image.baidu.com=/; jsdk-uuid=0516b316-b08c-49e3-be4e-fce991fda388; aistudio.baidu.com=/"
# keys = [
#     "宝宝生活照",
#     "儿童写真照",
#     "儿童生活照",
#     "儿童艺术照",
#     "宝宝艺术照",
#     "儿童摄影照",
#     "黑白漫画内容",
#     "搞笑黑白漫画内容",
#     "励志黑白漫画内容",
#     "五六岁小孩照片",
#     "肌肉男",
#     "健美",
#         ]
# output_root = "/data0/work/Ahri/workspace/spider/0417data"
# download_count = 3000
# download(cookie, keys, output_root, download_count)







