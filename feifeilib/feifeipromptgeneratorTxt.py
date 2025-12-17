import linecache
import random
import re

def get_random_line_linecache():
    # 统计文件行数
    filename = 'feifeilib/feifeipromptgeneratorTxt.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        line_count = sum(1 for _ in file)
    
    if line_count == 0:
        return ""
    
    random_line_num = random.randint(1, line_count)  # linecache从1开始计数
    result_txt = linecache.getline(filename, random_line_num).strip()
    result = re.sub(r'^\d+\.\s*', '', result_txt)
    return result