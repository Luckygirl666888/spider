from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import random
import requests
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

# 下载图片函数
def download_pic(url, path):
    try:
        # 发起请求下载图片
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            # 生成文件名并确保扩展名正确
            file_name = url.split("/")[-1].split("?")[0]  # 使用 URL 的最后一部分作为文件名
            if not file_name.endswith(".jpg"):
                file_name += ".jpg"  # 确保文件名以 .jpg 结尾
            file_path = os.path.join(path, file_name)
            
            # 保存图片到本地
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"图片已保存: {file_path}")
            return True
        else:
            print(f"下载失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"下载图片失败: {str(e)}")
    return False

# 使用 Selenium 模拟浏览器行为
def download_with_selenium(keys, output_root, download_count=100):
    # 配置 Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # 无头模式
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # 自动管理驱动程序
    driver = webdriver.Chrome(options=options)

    for key in keys:
        print(f"搜索关键词: {key}")
        dst_folder = os.path.join(output_root, key)
        os.makedirs(dst_folder, exist_ok=True)  # 确保目标文件夹存在
        current_count = 0
        page = 1
        processed_urls = set()  # 用于记录已处理的图片 URL，避免重复下载

        while current_count < download_count and page <= 100:
            try:
                # 构造搜索 URL
                url = f"https://unsplash.com/s/photos/{key.replace(' ', '-')}"
                print(f"正在请求页面: {url}")
                driver.get(url)
                time.sleep(3)  # 等待页面加载

                # 提取图片 URL
                images = driver.find_elements(By.CSS_SELECTOR, "figure img")
                print(f"找到 {len(images)} 张图片")

                for img in images:
                    if current_count >= download_count:
                        break
                    try:
                        img_url = img.get_attribute("src")
                        if not img_url or "images.unsplash.com" not in img_url:
                            print(f"跳过无效图片 URL: {img_url}")
                            continue

                        # 检查是否已处理过该图片
                        if img_url in processed_urls:
                            print(f"跳过重复图片: {img_url}")
                            continue
                        processed_urls.add(img_url)

                        # 检查文件名是否符合完整图片的命名规则
                        file_name = img_url.split("/")[-1].split("?")[0]
                        if file_name.startswith("profile-"):
                            print(f"跳过不完整的图片: {img_url}")
                            continue

                        print(f"下载图片: {img_url}")
                        is_success = download_pic(img_url, dst_folder)  # 调用下载函数
                        if is_success:
                            current_count += 1
                            print(f"进度: {current_count}/{download_count}")
                            time.sleep(random.uniform(1, 2))  # 下载间隔
                        else:
                            print(f"下载失败: {img_url}")
                    except Exception as e:
                        print(f"处理图片时出错: {str(e)}")
                        continue

                page += 1
                time.sleep(random.uniform(2, 3))  # 页面间隔
            except Exception as e:
                print(f"请求出错: {str(e)}")
                time.sleep(5)
                continue

        print(f"完成关键词: {key}")

    driver.quit()

# 示例调用
if __name__ == '__main__':
    keys = ["pug", "maltese"]  # 搜索关键词
    output_root = "/data0/work/Ahri/workspace/spider/0331data"  # 图片保存路径
    download_with_selenium(keys, output_root, download_count=50)