from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager  # 自动管理驱动程序
import os
import time

# 配置 Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无头模式
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# 自动管理驱动程序
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

keys_path = '/data0/work/Ahri/workspace/spider/extracted_links'

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
        
        try:
            # 打开网页
            driver.get(search_url)
            time.sleep(2)  # 等待页面加载
            
            # 模拟下滑加载
            load_count = 0
            max_loads = 10  # 设置最大加载次数
            while load_count < max_loads:
                print(f"第 {load_count + 1} 次下滑加载...")
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)  # 模拟按下 "End" 键
                time.sleep(2)  # 等待加载完成
                load_count += 1
            
            # 获取网页内容
            page_source = driver.page_source
            
            # 替换特殊字符，确保文件名安全
            safe_keyword = keyword.replace("/", "_")
            
            # 保存HTML文件
            output_dir = f"/data0/work/Ahri/workspace/spider/extracted_links_links/{keys_txt_name}"
            os.makedirs(output_dir, exist_ok=True)  # 确保目录存在
            output_file = os.path.join(output_dir, f"{safe_keyword}.html")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(page_source)
            print(f"保存页面: {output_file}")
                
        except Exception as e:
            print(f"请求出错: {e}")
            continue

# 关闭浏览器
driver.quit()