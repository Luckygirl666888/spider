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

# 更新URL和搜索参数
url = "https://www.pornpics.com/"
# params = {
#     "phrase": "",
#     # "mediatype": "photography",
#     # "phrase_direct": "true",
#     # "family": "creative",
#     # "sortOrder": "best",
#     "page": 1
# }

# 更新请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": "PP_UVM=1; PP_UVM_NU=1; _ga=GA1.2.910321927.1743588448; _gid=GA1.2.519161683.1743588448; _rel_uid=17436428465451350094; _stats-ref=; ar_debug=1; is_logged_3=%7B%22status%22%3A%22error%22%2C%22message%22%3A%22session%20was%20not%20started%22%7D; pp_lang=en; region=3",
    "Referer": "https://www.pornpics.com/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1"
}
sess = requests.session()
# page = 1
# while page <= 10:
keys_path = '/data0/work/Ahri/workspace/spider/extracted_links'
# for keys_txt in os.listdir(keys_path):
#     keys_file_path = os.path.join(keys_path, keys_txt)
#     print(f"读取关键词文件: {keys_file_path}")
#     # 读取关键词文件
#     with open(keys_file_path, 'r', encoding='utf-8') as f:
#             keys = [line.strip() for line in f if line.strip()]  # 去除空行和多余的空格
#             print(f"读取到 {len(keys)} 个关键词")
#     resp = sess.get(
#                     url=url,
#                     # params={"page": page},  # 仅传递分页参数
#                     headers=headers,
#                     timeout=5,
#                     proxies={"http": "http://127.0.0.1:7880"}  # 注意这里改成7890端口
#                     )
                            
#     if resp.status_code != 200:
#         print(f"请求失败: {resp.status_code}")
#         # else:
#         with open(f"debug_page_{keys_txt}.html", "wb") as f:
#             f.write(resp.content)

for keys_txt in os.listdir(keys_path):
    keys_file_path = os.path.join(keys_path, keys_txt)
    print(f"读取关键词文件: {keys_file_path}")
    
    # 去掉 .txt 后缀
    keys_txt_name = os.path.splitext(keys_txt)[0]
    
    with open(keys_file_path, 'r', encoding='utf-8') as f:
        keys = [line.strip() for line in f if line.strip()]
        print(f"读取到 {len(keys)} 个关键词")
    
    for keyword in keys:
        print(f"请求关键词: {keyword}")
        search_url = f"https://www.pornpics.com/{keyword}/"
        headers['Referer'] = search_url
        
        try:
            resp = sess.get(url=search_url, headers=headers, timeout=5, proxies={"http": "http://127.0.0.1:7880"})
                
            if resp.status_code != 200:
                print(f"请求失败: {resp.status_code}")
                break
            else:
                # 替换特殊字符，确保文件名安全
                safe_keyword = keyword.replace("/", "_")
                
                # 保存HTML文件
                output_dir = f"/data0/work/Ahri/workspace/spider/extracted_links_links/{keys_txt_name}"
                os.makedirs(output_dir, exist_ok=True)  # 确保目录存在
                output_file = os.path.join(output_dir, f"{safe_keyword}.html")
                with open(output_file, "wb") as f:
                    f.write(resp.content)
                print(f"保存页面: {output_file}")
                
        except Exception as e:
            print(f"请求出错: {e}")
            continue
            
# from bs4 import BeautifulSoup

# def extract_links_and_save_by_group(html_file_path, output_dir, group_ids):
#     """
#     从HTML文件中提取多个分组下的链接，并分别保存到txt文件
#     :param html_file_path: HTML文件路径
#     :param output_dir: 输出的txt文件保存目录
#     :param group_ids: 分组ID列表，例如 ["A", "B", "C"]
#     """
#     # 读取HTML文件
#     with open(html_file_path, 'r', encoding='utf-8') as f:
#         html_content = f.read()
    
#     # 使用BeautifulSoup解析HTML
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     # 遍历每个分组ID
#     for group_id in group_ids:
#         # 找到指定分组的<div>标签
#         group_div = soup.find('div', {'class': 'list-group clearfix', 'id': group_id})
#         if not group_div:
#             print(f"未找到ID为 {group_id} 的分组")
#             continue
        
#         # 在分组下找到所有<a>标签
#         links = []
#         list_items = group_div.find_all('a', href=True)
#         for item in list_items:
#             href = item['href']  # 提取href属性
#             links.append(href)
        
#         # 将链接保存到对应的txt文件
#         output_txt_path = f"{output_dir}/{group_id}_links.txt"
#         with open(output_txt_path, 'w', encoding='utf-8') as f:
#             for link in links:
#                 f.write(link + '\n')
        
#         print(f"分组 {group_id} 的链接已保存到 {output_txt_path}")

# # 示例使用
# html_file_path = '/data0/work/Ahri/workspace/spider/debug_page_1.html'  # HTML文件路径
# output_dir = '/data0/work/Ahri/workspace/spider/extracted_links'  # 输出目录
# group_ids = [
#     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
#     "U", "V", "W", "Y", "#"  # 分组ID列表
#     ]  # 分组ID列表

# # 创建输出目录（如果不存在）
# os.makedirs(output_dir, exist_ok=True)

# extract_links_and_save_by_group(html_file_path, output_dir, group_ids)                    


# if __name__ == '__main__':
#     cookie = "PP_UVM=1; PP_UVM_NU=1; _ga=GA1.2.910321927.1743588448; _gid=GA1.2.519161683.1743588448; _rel_uid=17436428465451350094; _stats-ref=; ar_debug=1; is_logged_3=%7B%22status%22%3A%22error%22%2C%22message%22%3A%22session%20was%20not%20started%22%7D; pp_lang=en; region=3"
#     keys_file_path = "/data0/work/Ahri/workspace/spider/pornpics.txt"
#     output_root = "/data0/work/Ahri/workspace/spider/0402data"
#     download_count = 20  # 每个关键词下载的图片数量
#     download(cookie, keys_file_path, output_root, download_count)





