import gradio as gr
# import spaces
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import uuid
from feifeilib.feifeimodload import feifeimodload
from feifeilib.feifeiprompt import feifeiprompt
from openai import OpenAI
import json
import os
import torch

pipe = feifeimodload()
MAX_SEED = np.iinfo(np.int32).max
# --- 新增：配置缓存目录 ---
IMAGE_CACHE_DIR = "image_cache"
# 确保缓存目录存在
os.makedirs(IMAGE_CACHE_DIR, exist_ok=True)

def add_watermark(image, font_path,
                  watermark_text_line1="妃妃", font_size_line1=40,
                  watermark_text_line2="aiFeiFei", font_size_line2=30):
    """
    Adds a two-line watermark to an image with individually adjustable font sizes.
    Args:
        image (PIL.Image.Image): The input PIL Image object.
        font_path (str): The file path to the TrueType font.
        watermark_text_line1 (str): The text for the first line of the watermark.
        font_size_line1 (int): The font size for the first line.
        watermark_text_line2 (str): The text for the second line of the watermark.
        font_size_line2 (int): The font size for the second line.
    Returns:
        PIL.Image.Image: The image with the watermark added.
    """

    # Ensure the input is an Image object
    if not isinstance(image, Image.Image):
        raise ValueError("Input must be a PIL Image object")

    width, height = image.size

    # Create a drawing object to draw on the image
    draw = ImageDraw.Draw(image)

    # Load the custom font for line 1
    try:
        font1 = ImageFont.truetype(font_path, font_size_line1)
    except IOError:
        raise ValueError(f"Font file not found or invalid font path: {font_path}")

    # Load the custom font for line 2
    try:
        font2 = ImageFont.truetype(font_path, font_size_line2)
    except IOError:
        raise ValueError(f"Font file not found or invalid font path: {font_path}")

    # --- Process Line 1 ---
    # Calculate the width and height of the first line text
    bbox1 = draw.textbbox((0, 0), watermark_text_line1, font=font1)
    text_width_line1 = bbox1[2] - bbox1[0]
    text_height_line1 = bbox1[3] - bbox1[1]

    # --- Process Line 2 ---
    # Calculate the width and height of the second line text
    bbox2 = draw.textbbox((0, 0), watermark_text_line2, font=font2)
    text_width_line2 = bbox2[2] - bbox2[0]
    text_height_line2 = bbox2[3] - bbox2[1]

    # --- Calculate positions for both lines (bottom-right aligned) ---
    margin = 20 # Adjust margin as needed (e.g., 20 pixels from bottom/right)
    line_spacing = 10 # Adjust spacing between lines

    # Calculate y-position for the second line (bottom-most)
    y_line2 = height - text_height_line2 - margin
    # Calculate x-position for the second line (right-aligned)
    x_line2 = width - text_width_line2 - margin

    # Calculate y-position for the first line (above the second line)
    y_line1 = y_line2 - text_height_line1 - line_spacing
    # Calculate x-position for the first line (right-aligned, relative to its own width)
    x_line1 = width - text_width_line1 - margin


    # Add the watermark text to the image
    # Use a semi-transparent white color (R, G, B, Alpha)
    draw.text((x_line1, y_line1), watermark_text_line1, font=font1, fill=(255, 255, 255, 128))
    draw.text((x_line2, y_line2), watermark_text_line2, font=font2, fill=(255, 255, 255, 128))

    # Return the modified image object
    return image


# @spaces.GPU()
@torch.no_grad()
def feifeitexttoimg(
    pic_num=4,
    prompt_1="",
    prompt_2="",
    negative_prompt_check=False,
    negative_prompt="",
    styles_Radio=["(None)"],
    styles_prompt=["CLIP"],
    add_watermark_select=True,
    feifei_lora = False,
    feifei_lora_num = 0.35,
    skin_lora = False,
    skin_lora_num = 1,
    nsfw_v2_lora = False,
    nsfw_v2_num = 0.65,
    seed=random.randint(0, MAX_SEED),
    randomize_seed=True,
    width=896,
    height=1152,
    num_inference_steps=4,
    guidance_scale=3.5,
    FeiFei_select=True,
    quality_select=False,
    progress=gr.Progress(track_tqdm=True),
):
    BATCH_SIZE = pic_num
    # x_prompt = to_x_prompt(prompt)
    # x_prompt = ""
    #print(f"--- [DEBUG] --- feifei_lora: {feifei_lora}, Type: {type(feifei_lora)}")
    prompt = prompt_1 + prompt_2
    prompt, negative_prompt1, generator = feifeiprompt(
        randomize_seed,
        seed,
        prompt,
        quality_select,
        styles_Radio,
        FeiFei_select,
    )
    if negative_prompt_check:
        negative_prompt1 = negative_prompt + "," + negative_prompt1
    
    if feifei_lora:
        #adapters = ["feifei_lora", "skin_lora", "nsfw_v2_lora"]
        adapters = ["feifei_lora"]
        weights = [
            feifei_lora_num if feifei_lora else 0,
            #skin_lora_num if skin_lora else 0,
            #nsfw_v2_num if nsfw_v2_lora else 0
        ]

        pipe.set_adapters(adapters, adapter_weights=weights)
    if styles_prompt == ["CLIP"]:
        output = pipe(
            prompt=prompt,
            prompt_2="",
            negative_prompt=negative_prompt1,
            negative_prompt_2="",
            width=width,
            height=height,
            num_inference_steps=num_inference_steps,
            generator=generator,
            guidance_scale=guidance_scale,
            num_images_per_prompt=BATCH_SIZE, 
            output_type="pil",
        )
    else:
        output = pipe(
            prompt="",
            prompt_2=prompt,
            negative_prompt="",
            negative_prompt_2=negative_prompt,
            width=width,
            height=height,
            num_inference_steps=num_inference_steps,
            generator=generator,
            guidance_scale=guidance_scale,
            num_images_per_prompt=BATCH_SIZE, 
            output_type="pil",
        )

    # 获取生成的图片列表 (包含 4 张图)
    images_list = output.images 
    
    # --- 修改点 2: 循环处理列表中的每一张图片 ---
    
    saved_image_paths = [] # 用于存储本次生成的所有图片路径
    
    # 读取已有的 gallery JSON (为了把新图加进去)
    temp_json_file = "image_cache/temp_image_filenames.json"
    if os.path.exists(temp_json_file):
        with open(temp_json_file, "r") as f:
            imagesgallery = json.load(f)
    else:
        imagesgallery = []
    
    # 循环处理每一张生成的图片
    for img in images_list:
        # 1. 加水印
        if add_watermark_select:
            font_path = "Iansui-Regular.ttf"
            img = add_watermark(
                img,
                font_path, 
                watermark_text_line1="妃妃",
                font_size_line1=72, 
                watermark_text_line2="aiFeiFei",
                font_size_line2=48   
            )
        
        # 2. 生成 UUID 并保存
        image_uuid = uuid.uuid4()
        image_filename = f"{image_uuid}.png"
        save_path = f"image_cache/{image_filename}"
        img.save(save_path)
        
        # 3. 记录路径
        saved_image_paths.append(save_path)
        
        # 4. 将当前图片路径插入到 gallery 列表的最前面
        imagesgallery.insert(0, save_path)
    
    # --- 修改点 3: 保存更新后的 JSON ---
    with open(temp_json_file, "w") as f:
        json.dump(imagesgallery, f)
    
    # --- 修改点 4: 返回值 ---
    # 如果你的 Gradio 界面有一个主要展示区，通常展示第一张图
    # imagesgallery[:24] 会包含刚刚生成的所有 4 张图以及之前的图
    return saved_image_paths, prompt, imagesgallery[:24]
