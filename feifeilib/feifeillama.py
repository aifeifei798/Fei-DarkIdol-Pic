from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer, BitsAndBytesConfig
from threading import Thread
import torch

quantization_config = BitsAndBytesConfig(
    # load_in_8bit=True,
    # 如果你想用 4-bit (更省显存)，把上面改成 False，下面改成 True
    load_in_4bit=True, 
    # bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
)

# 模型路径
model_name = "./Llama-3.2-3B-Instruct-abliterated" 

dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

# 加载模型
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto",
    tie_word_embeddings=False 
)

def feifeillama(prompt):
    """
    流式生成函数 v2.0 (纯摄影版)
    针对 Flux.1 优化，专门修复"胡乱堆砌渲染引擎参数"和"逻辑错误"的问题。
    """
    
    # --- 1. System Prompt: 包含"违禁词"列表 ---
    system_instruction = (
        "You are a professional photographer assisting Flux AI. "
        "Convert user input into a PHOTOREALISTIC image description. "
        
        "CRITICAL RULES:\n"
        "1. VISUALS ONLY: Describe the Subject, Clothing, Action, Background, and Lighting.\n"
        "2. LOGIC CHECK: Ensure elements match the season (e.g., NO cherry blossoms in winter/snow).\n"
        "3. PHOTOGRAPHY ONLY: The output must look like a real photo. \n"
        "4. BANNED WORDS (DO NOT USE): 'Zbrush', 'Maya', 'Arnold', 'Cinema 4D', 'Blender', 'rendering', 'scent', 'smell', 'perfume', 'HKS system'.\n"
        "5. KEEP IT CLEAN: Do not invent shops selling random items unless specified.\n"
        
        "Structure: [Main Subject Description]. [Environment & Atmosphere]. [Camera & Lighting Keywords]."
    )

    # --- 2. Few-Shot Examples (纯摄影风格，无 3D 术语) ---
    messages = [
        {"role": "system", "content": system_instruction},
        
        # 示例 1
        {"role": "user", "content": "一只在太空的猫"},
        {"role": "assistant", "content": "A fluffy tabby cat wearing a detailed white spacesuit, floating inside a spaceship cockpit. The earth is visible through the window behind. Cinematic lighting, lens flare, 8k resolution, photorealistic, highly detailed fur texture."},
        
        # 示例 2
        {"role": "user", "content": "赛博朋克雨夜"},
        {"role": "assistant", "content": "A futuristic city street at night, heavy rain falling, neon signs reflecting on the wet asphalt. A mysterious woman in a transparent raincoat stands in the foreground. Volumetric fog, cyberpunk color palette of cyan and magenta, shallow depth of field, bokeh, masterpiece."},
        
        # 真实提问
        {"role": "user", "content": prompt}
    ]

    # --- 格式化 ---
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    
    # --- Streamer ---
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

    # --- 生成参数 ---
    generation_kwargs = dict(
        model_inputs,
        streamer=streamer,
        max_new_tokens=200,        
        do_sample=True,
        temperature=0.3,           # 保持低温，稳定输出
        top_p=0.9,
        # [核心] 重复惩罚稍微提高到 1.25，抑制它像念经一样列参数
        repetition_penalty=1.25,   
        eos_token_id=tokenizer.eos_token_id
    )

    # 启动线程
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    # for new_text in streamer:
        # yield new_text

    # --- 输出 ---
    out_new_text = ""
    for new_text in streamer:
        out_new_text += new_text
        yield out_new_text

# if __name__ == "__main__":
    # # 测试
    # user_input = "一位漂亮的韩国美女,穿着奢侈大衣,在下雪的首尔街头"
    
    # print(f"Input: {user_input}\n")
    # print("Flux Prompt > ", end="")
    
    # for chunk in feifeillama(user_input):
        # print(chunk, end="", flush=True)
    
    # print("\n\nDone.")