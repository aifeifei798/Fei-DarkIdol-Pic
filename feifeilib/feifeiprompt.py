import numpy as np
import random
import re
import torch
import os
import config_zh

# ================= 配置预处理 =================
# 1. 安全加载艺术家列表
artist_file = "artist.txt"
if os.path.exists(artist_file):
    with open(artist_file, "r", encoding='utf-8') as file:
        # 过滤空行并去除首尾空格
        artists = [line.strip() for line in file if line.strip()]
else:
    artists = ["Van Gogh", "Monet", "Picasso"] # 默认保底，防止文件缺失报错

MAX_SEED = np.iinfo(np.int32).max

# 2. 【关键优化】将风格列表转为字典，提高查找速度 (O(1)时间复杂度)
# 结构变成: {'空气透视': {'name':..., 'prompt':...}, ...}
STYLE_MAP = {style["name"]: style for style in config_zh.style_list}


def feifeiprompt(
    randomize_seed,
    seed,
    prompt,
    quality_select,
    styles_Radio,
    FeiFei_select,
):
    # --- 1. 随机种子处理 ---
    if randomize_seed:
        seed = random.randint(0, MAX_SEED)
    else:
        seed = int(seed)
    
    # 注意：通常返回 seed 数值给前端展示更有用，这里保留你原逻辑返回 generator
    generator = torch.Generator().manual_seed(seed)

    # --- 2. 艺术家标签替换 (__artist__) ---
    if "__artist__" in prompt and artists:
        # 随机打乱列表，保证每次取出的不一样
        shuffled_artists = random.sample(artists, len(artists))
        
        def replace_func(match):
            # 如果列表取空了，给个默认值，防止程序崩
            return shuffled_artists.pop() if shuffled_artists else "Unknown Artist"

        prompt = re.sub(r"__artist__", replace_func, prompt)

    # --- 3. 质量词追加 ---
    if quality_select:
        # 建议加个逗号，防止粘连
        prompt += ", masterpiece, best quality, very aesthetic, absurdres"

    # --- 4. FeiFei 角色特定替换 ---
    if FeiFei_select:
        replacement = " feifei, A beautiful, 18 yo kpop idol, large-busted Korea slim girl, with light makeup, gazing deeply into the camera, "
        
        # 【优化】使用正则表达式的一条语句替换多个词，且加上 \b 匹配单词边界
        # 这样不会把 "supermodel" 变成 "super feifei..."
        pattern = r"\b(girl|young woman|woman|model)\b"
        prompt = re.sub(pattern, replacement, prompt, flags=re.IGNORECASE)

    # --- 5. 风格处理 (Style & Negative Prompt) ---
    active_negative_prompts = []

    if styles_Radio:
        # 容错处理：如果单选传进来是字符串，转成列表
        selected_names = styles_Radio if isinstance(styles_Radio, list) else [styles_Radio]

        for name in selected_names:
            if name == "(None)":
                continue
            
            # 【优化】直接从字典取值，不用再循环遍历 config_zh.style_list
            style = STYLE_MAP.get(name)
            
            if style:
                # 处理 Positive Prompt (套娃叠加)
                prompt = style["prompt"].replace("{prompt}", prompt)
                
                # 处理 Negative Prompt (收集)
                if style.get("negative_prompt"):
                    active_negative_prompts.append(style["negative_prompt"])

    # --- 6. 结果拼接 ---
    # 使用 set 去重（防止选了两个风格导致负面词重复），然后再拼接
    # final_negative_prompt = ", ".join(list(set(active_negative_prompts))) 
    # 如果不在意重复，直接拼也可以：
    final_negative_prompt = ", ".join(active_negative_prompts)

    # 【修复】返回计算好的 final_negative_prompt，而不是空的 negative_prompt
    return prompt, final_negative_prompt, generator