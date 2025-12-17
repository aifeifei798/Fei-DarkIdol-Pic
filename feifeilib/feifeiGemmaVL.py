from transformers import (
    AutoProcessor, 
    Gemma3nForConditionalGeneration, 
    BitsAndBytesConfig, 
    TextIteratorStreamer
)
from PIL import Image
import requests
import torch
from threading import Thread
import os

# --- 1. 配置量化 ---
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True, 
    bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
    bnb_4bit_quant_type="nf4",       
    bnb_4bit_use_double_quant=True,
    llm_int8_skip_modules=["correction_coefs", "altup", "lm_head"] 
)

model_id = "../Huihui-gemma-3n-E2B-it-abliterated" 

# --- 2. 加载模型 ---
print(f"正在加载模型: {model_id} ...")
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = Gemma3nForConditionalGeneration.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto",
    tie_word_embeddings=True,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True
)
print("模型加载完成。")

def load_image(image_input):
    if image_input is None:
        return None
    if isinstance(image_input, Image.Image):
        return image_input
    if isinstance(image_input, str):
        if image_input.startswith("http"):
            return Image.open(requests.get(image_input, stream=True).raw)
        elif os.path.exists(image_input):
            return Image.open(image_input)
    print(f"[Warning] 无法加载图片: {image_input}")
    return None

def feifeillama(prompt, image_input=None):
    pil_image = load_image(image_input)
    
    user_content_list = []
    
    if pil_image:
        print(f"\033[92m[模式切换] 视觉感知模式 (Vision)\033[0m")
        
        # --- 最终版 System Prompt：平衡准确性与丰富度 ---
        system_text = (
            "Role: Flux Prompt Expert.\n"
            "Task: Generate a descriptive prompt based strictly on the image content.\n"
            "Requirements:\n"
            "1. Describe COLORS and MATERIALS (e.g., white silk shirt, black trousers).\n"
            "2. Describe LIGHTING (e.g., golden hour, warm sunset).\n"
            "3. Format: [Subject]. [Outfit details]. [Environment]. [Camera style].\n"
            "Constraint: Be descriptive but factual. Do not hallucinate objects not present."
        )
        user_content_list.append({"type": "image", "image": pil_image})
        
        # --- 引导它关注细节 ---
        force_prompt = (
            "Describe the woman in detail. "
            "Focus on the texture of her white shirt and black pants. "
            "Describe the city skyline background and the lighting."
        )
        
        final_prompt = prompt if prompt else force_prompt
        user_content_list.append({"type": "text", "text": final_prompt})
    else:
        print(f"\033[96m[模式切换] 文本扩写模式 (Text)\033[0m")
        system_text = (
            "Role: Flux AI Prompt Generator.\n"
            "Task: Convert user input into a single, raw photorealistic image prompt.\n"
            "Format: [Subject]. [Environment]. [Lighting & Camera].\n"
            "STRICT: Output ONLY the prompt string. No explanations."
        )
        user_content_list.append({"type": "text", "text": prompt})

    messages = [
        {"role": "system", "content": [{"type": "text", "text": system_text}]},
        {"role": "user", "content": user_content_list}
    ]

    # --- 关键修复区域 START ---
    inputs = processor.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    # 【修复核心】：如果包含图片数据(pixel_values)，强制转为 bfloat16
    if "pixel_values" in inputs:
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
    # --- 关键修复区域 END ---

    streamer = TextIteratorStreamer(processor.tokenizer, skip_prompt=True, skip_special_tokens=True)
    
    generation_kwargs = dict(
        **inputs,
        streamer=streamer,
        max_new_tokens=300,        
        do_sample=True,
        temperature=0.4,           
        top_p=0.9,
        repetition_penalty=1.05,
    )
    
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    for new_text in streamer:
        clean_text = new_text.replace("**", "") 
        yield clean_text

if __name__ == "__main__":
    print("\n" + "="*30 + " FLUX PROMPT GENERATOR " + "="*30 + "\n")
    
    img_url = "test.jpg"
    prompt = "" # 留空，让它用默认的引导词
    
    print(f"👉 正在分析: {img_url}")
    
    if os.path.exists(img_url):
        with torch.inference_mode():
            for chunk in feifeillama(prompt, img_url): 
                print(chunk, end="", flush=True)
    else:
        print("❌ 找不到图片")
            
    print("\n\nDone.")