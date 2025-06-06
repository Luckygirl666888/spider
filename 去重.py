import os
import shutil

# 定义源目录和参考目录的路径
source_dir = "/data0/work/Ahri/workspace/spider/extracted_links_links/A_links"
reference_dir = "/data0/work/Ahri/workspace/spider/extracted_links_links_1/A_links"

def remove_duplicate_files():
    # 确保两个目录都存在
    if not os.path.exists(source_dir) or not os.path.exists(reference_dir):
        print("目录不存在，请检查路径")
        return

    # 获取参考目录中的所有文件名
    reference_files = set(os.listdir(reference_dir))
    
    # 获取源目录中的所有文件
    source_files = os.listdir(source_dir)
    
    # 计数器
    removed_count = 0
    
    # 遍历源目录中的文件
    for file_name in source_files:
        if file_name in reference_files:
            # 如果文件在参考目录中存在，则删除源目录中的文件
            file_path = os.path.join(source_dir, file_name)
            try:
                os.remove(file_path)
                removed_count += 1
                print(f"已删除: {file_name}")
            except Exception as e:
                print(f"删除 {file_name} 时出错: {str(e)}")
    
    print(f"\n完成! 共删除了 {removed_count} 个重复文件")

if __name__ == "__main__":
    remove_duplicate_files()