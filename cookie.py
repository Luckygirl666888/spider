def convert_cookies(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cookie_pairs = []
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 2:
            cookie_pairs.append(f"{parts[0]}={parts[1]}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('; '.join(cookie_pairs))

# 使用示例
input_file = "/data0/work/Ahri/workspace/spider/11111.txt"
output_file = "/data0/work/Ahri/workspace/spider/cookies_converted.txt"
convert_cookies(input_file, output_file)