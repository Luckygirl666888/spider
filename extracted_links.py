# from bs4 import BeautifulSoup
# import os
# import re

# def extract_links_from_html(html_file):
#     """从HTML文件中提取所有符合条件的href链接"""
#     with open(html_file, 'r', encoding='utf-8') as f:
#         content = f.read()
    
#     soup = BeautifulSoup(content, 'html.parser')
    
#     # 查找所有class包含thumbwook的li标签
#     links = []
#     for li in soup.find_all('li', class_=lambda x: x and 'thumbwook' in x):
#         # 在li标签中查找带有href的a标签
#         a_tag = li.find('a', class_='rel-link', href=True)
#         if a_tag and a_tag.get('href'):
#             links.append(a_tag['href'])
    
#     return links

# def process_html_files(input_dir):
#     """处理目录下所有HTML文件"""
#     # 遍历目录下的所有文件
#     for root, dirs, files in os.walk(input_dir):
#         for file in files:
#             if file.endswith('.html'):
#                 html_file = os.path.join(root, file)
#                 file_name = os.path.splitext(file)[0]
                
#                 # 创建输出目录
#                 output_dir = os.path.join(root + '_links', file_name)
#                 os.makedirs(output_dir, exist_ok=True)
                
#                 # 提取链接
#                 links = extract_links_from_html(html_file)
                
#                 # 保存链接到文件
#                 output_file = os.path.join(output_dir, 'links.txt')
#                 with open(output_file, 'w', encoding='utf-8') as f:
#                     for link in links:
#                         f.write(f"{link}\n")
                
#                 print(f"已处理文件: {html_file}")
#                 print(f"提取的链接数量: {len(links)}")
#                 print(f"保存到: {output_file}\n")

# def main():
#     # 设置输入目录
#     input_dir = r"/data0/work/Ahri/workspace/spider/extracted_links_links"
    
#     try:
#         process_html_files(input_dir)
#         print("处理完成!")
#     except Exception as e:
#         print(f"处理过程中出现错误: {str(e)}")

# if __name__ == "__main__":
#     main()

from bs4 import BeautifulSoup
import os
import re

def extract_links_from_html(html_file):
    """从HTML文件中提取所有符合条件的href链接"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 查找所有class包含thumbwook的li标签
    links = []
    for li in soup.find_all('li', class_=lambda x: x and 'thumbwook' in x):
        # 在li标签中查找带有href的a标签
        a_tag = li.find('a', class_='rel-link', href=True)
        if a_tag and a_tag.get('href'):
            #print(a_tag['href'])
            if 'https://www' in a_tag['href']:
                # 只提取包含'/photo/'的链接
                links.append(a_tag['href'])
    
    return links

def process_html_files(input_dir):
    """处理目录下所有HTML文件"""
    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]
                
                # 创建新的输出目录
                # 修改为 spider/extracted_links_links_links/#_links/_tags_69_
                output_dir = os.path.join(
                    "/data0/work/Ahri/workspace/spider/extracted_links_links_links",
                    os.path.basename(root),  # 父目录名
                    file_name
                )
                os.makedirs(output_dir, exist_ok=True)
                
                # 提取链接
                links = extract_links_from_html(html_file)
                
                # 保存链接到文件
                output_file = os.path.join(output_dir, 'links.txt')
                with open(output_file, 'w', encoding='utf-8') as f:
                    for link in links:
                        f.write(f"{link}\n")
                
                print(f"已处理文件: {html_file}")
                print(f"提取的链接数量: {len(links)}")
                print(f"保存到: {output_file}\n")

def main():
    # 设置输入目录
    input_dir = r"/data0/work/Ahri/workspace/spider/extracted_links_links"
    
    try:
        process_html_files(input_dir)
        print("处理完成!")
    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")

if __name__ == "__main__":
    main()