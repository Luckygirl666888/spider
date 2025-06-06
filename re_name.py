import os

def rename_spaces(directory):
    """
    递归地将目录中的所有文件和目录名中的空格替换为下划线。
    """
    # 遍历目录
    for root, dirs, files in os.walk(directory, topdown=False):
        # 处理文件
        for filename in files:
            if " " in filename:
                old_file_path = os.path.join(root, filename)
                new_filename = filename.replace(" ", "_")
                new_file_path = os.path.join(root, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")

        # 处理目录
        for dirname in dirs:
            if " " in dirname:
                old_dir_path = os.path.join(root, dirname)
                new_dirname = dirname.replace(" ", "_")
                new_dir_path = os.path.join(root, new_dirname)
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed: {old_dir_path} -> {new_dir_path}")

if __name__ == "__main__":
    target_dir = "/data0/work/Ahri/workspace/spider/0328data"
    rename_spaces(target_dir)