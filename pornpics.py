import requests
from PIL import Image
import json
import os
import random
import numpy as np
import cv2
import hashlib
import base64
from bs4 import BeautifulSoup
import os
import time
import random
import requests 
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import re
# url = "https://www.istockphoto.com/"
# # https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=%E6%96%AF%E8%8A%AC%E5%85%8B%E6%96%AF%E7%8C%AB
# # https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%96%AF%E8%8A%AC%E5%85%8B%E6%96%AF%E7%8C%AB&step_word=&hs=0&pn=4&spn=0&di=7466852183703552001&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=undefined&lm=undefined&st=undefined&cs=2061952667%2C1023291064&os=2282945841%2C1647553880&simid=3378554361%2C427637603&adpicid=0&lpn=0&ln=1731&fr=&fmq=1743128651814_R&fm=result&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fb0.bdstatic.com%2Fadb19c299e1342bcf8142708db4e6363.jpg%40h_1280&fromurl=ipprf_z2C%24qAzdH3FAzdH3F4k1_z%26e3Bkwt17_z%26e3Bv54AzdH3Fgjofrw2jAzdH3F1wpwAzdH3F1pswg1tg2otfj%3Fgt1%3D1p_9addbbn09099cc88n8n%26f576vjF654%3Di54jrw2j&gsm=1e&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&lid=11330918254511385506

# # https://www.istockphoto.com/search/2/image-film?family=creative&phrase=pug
# # https://www.istockphoto.com/photo/pug-sitting-and-panting-1-year-old-isolated-on-white-gm450709593-24934266?searchscope=image%2Cfilm
# # https://www.istockphoto.com/photo/pug-puppy-dog-gm454238885-30352606?searchscope=image%2Cfilm
# params = {
#     "phrase":"pug",
#     "searchscope":"image%2Cfilm",
# }
# 更新URL和搜索参数
url = "https://www.pornpics.com/"
params = {
    "phrase": "",
    # "mediatype": "photography",
    # "phrase_direct": "true",
    # "family": "creative",
    # "sortOrder": "best",
    "page": 1
}

# 更新请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": "",
    "Referer": "",# 跟着url的
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
    """从HTML中提取图片URL"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 尝试多种方式查找图片
    image_urls = []
    img_tags = soup.find_all('img', {'data-src': True})
    for img in img_tags:
        # 获取图片的完整 URL
        src = img['data-src']
        if src.startswith('//'):
            src = 'https:' + src  # 补全协议头
        image_urls.append(src)
    
    # 1. 查找所有图片标签
    # img_tags = soup.find_all('img', src=True)
    # for img in img_tags:
    #     src = img.get('src', '')
    #     if '/photo/' in src and not src.startswith('data:'):
    #         image_urls.append(src)
    img_tags = soup.find_all('img', src=True)
    for img in img_tags:
        src = img.get('src', '')
        if '.jpg' in src and not src.startswith('data:'):
            image_urls.append(src)
            
    # 2. 查找srcset属性
    srcset_tags = soup.find_all(lambda tag: tag.get('srcset', ''))
    for tag in srcset_tags:
        srcset = tag.get('srcset', '')
        if '/photo/' in srcset:
            urls = srcset.split(',')
            for url in urls:
                if '/photo/' in url:
                    clean_url = url.strip().split(' ')[0]
                    image_urls.append(clean_url)
                    
    # 3. 查找背景图片URL
    style_tags = soup.find_all(lambda tag: tag.get('style', ''))
    for tag in style_tags:
        style = tag.get('style', '')
        if 'background-image' in style:
            urls = re.findall(r'url\(["\']?(.*?)["\']?\)', style)
            image_urls.extend([url for url in urls if '/photo/' in url])
    
    # 去重
    return list(set(image_urls))

# def download(cookie, keys, output_root, download_count):
#     if headers['Cookie'] == "":
#         headers['Cookie'] = cookie
    
    
#     for key in keys:
#         print(f"搜索关键词: {key}")
#         dst_folder = os.path.join(output_root, key)
#         os.makedirs(dst_folder, exist_ok=True)
#         current_count = 0
#         page = 1
#         while current_count < download_count and page <= 100:
#             try:
#                 # 更新搜索参数
#                 params.update({
#                     'phrase': key,
#                     'page': page
#                 })
                
#                 # 添加随机延迟
#                 time.sleep(random.uniform(2, 4))
                
#                 print(f"请求第 {page} 页...")
#                 resp = sess.get(
#                     url=url,
#                     params=params,
#                     headers=headers,
#                     timeout=load_json_timeout,
#                     proxies={"http": "http://127.0.0.1:7880"}  # 注意这里改成7890端口
#                 )
                
#                 if resp.status_code != 200:
#                     print(f"请求失败: {resp.status_code}")
#                     break
#                 else:
#                     print("相应内容: ", resp.text)
#                     print("相应内容: ", resp.content)
#                     print("响应头: ", resp.headers)
                
#                 # 提取图片URL
#                 image_urls = extract_image_urls(resp.content)
                
#                 if not image_urls:
#                     print("未找到图片URL")
#                     print(f"页面URL: {resp.url}")
#                     # 保存页面内容以供调试
#                     with open(f"debug_page_{page}.html", "wb") as f:
#                         f.write(resp.content)
#                     break
                
#                 print(f"找到 {len(image_urls)} 个图片URL")
                
#                 # 下载图片
#                 for img_url in image_urls:
#                     try:
#                         print(f"下载图片: {img_url}")
#                         is_success = download_pic(img_url, dst_folder)
                        
#                         if is_success:
#                             current_count += 1
#                             print(f"进度: {current_count}/{download_count}")
                            
#                             if current_count >= download_count:
#                                 return
                                
#                         # 下载间隔
#                         time.sleep(random.uniform(1, 2))
                        
#                     except Exception as e:
#                         print(f"下载出错: {str(e)}")
#                         continue
                
#                 page += 1
                
#             except Exception as e:
#                 print(f"页面处理出错: {str(e)}")
#                 time.sleep(5)
#                 continue
            
#         print(f"完成关键词: {key}")
def download(cookie, keys_file_path, output_root, download_count):
    if headers['Cookie'] == "":
        headers['Cookie'] = cookie
    
    # 读取关键词文件
    with open(keys_file_path, 'r', encoding='utf-8') as f:
        keys = [line.strip() for line in f if line.strip()]  # 去除空行和多余的空格
        print(f"读取到 {len(keys)} 个关键词")

    for key in keys:
        print(f"搜索关键词: {key}")
        dst_folder = os.path.join(output_root, key)
        os.makedirs(dst_folder, exist_ok=True)
        current_count = 0
        page = 1
        while current_count < download_count and page <= 100:
            try:
                # 构造新的 URL，将关键词直接拼接到 URL 中
                search_url = f"https://www.pornpics.com/{key}/"
                headers['Referer'] = search_url

                # 添加随机延迟
                time.sleep(random.uniform(2, 4))
                
                print(f"请求第 {page} 页...")
                resp = sess.get(
                    url=search_url,
                    # params={"page": page},  # 仅传递分页参数
                    headers=headers,
                    timeout=load_json_timeout,
                    proxies={"http": "http://127.0.0.1:7880"}  # 注意这里改成7890端口
                )
                
                # 检查响应状态码
                if resp.status_code != 200:
                    print(f"请求失败: {resp.status_code}")
                    break
                
                # 提取图片URL
                image_urls = extract_image_urls(resp.content)
                
                if not image_urls:
                    print("未找到图片URL")
                    print(f"页面URL: {resp.url}")
                    # 保存页面内容以供调试
                    debug_file = os.path.join(dst_folder, f"debug_page_{page}.html")
                    with open(debug_file, "wb") as f:
                        f.write(resp.content)
                    print(f"调试页面内容已保存到: {debug_file}")
                    break
                
                print(f"找到 {len(image_urls)} 个图片URL")
                print("前五个图片urls", image_urls[:5])
                
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
if __name__ == '__main__':
    cookie = "PP_UVM=1; PP_UVM_NU=1; _ga=GA1.2.910321927.1743588448; _gid=GA1.2.519161683.1743588448; _rel_uid=17436428465451350094; _stats-ref=; ar_debug=1; is_logged_3=%7B%22status%22%3A%22error%22%2C%22message%22%3A%22session%20was%20not%20started%22%7D; pp_lang=en; region=3"
    keys_file_path = "/data0/work/Ahri/workspace/spider/pornpics.txt"
    output_root = "/data0/work/Ahri/workspace/spider/0402data"
    download_count = 20  # 每个关键词下载的图片数量
    download(cookie, keys_file_path, output_root, download_count)





