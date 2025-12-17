import os
from openai import OpenAI

feifei_photo = """You are an expert visual prompt generator. Your task is to convert any given concept, scene, or idea into a highly descriptive, vivid, and imaginative English prompt suitable for a text-to-image AI model called Flux. The result should include:
1. A clear subject with visual detail (e.g. a dragon flying over snowy mountains)
2. Style or mood suggestions (e.g. cinematic, surrealism, watercolor)
3. Optional camera angles or composition hints (e.g. wide shot, close-up, low angle)
4. Lighting and atmosphere description (e.g. golden hour, rainy mood, neon lighting)
5. Use natural, fluent, and creative English phrasing.
Keep the output around 1–2 sentences. Avoid technical jargon. Focus on visual storytelling.
"""


myclient = OpenAI(api_key=os.getenv("myapikey"), base_url=os.getenv("mybase_url"))


def feifeiprompt(message_text=""):
    input_prompt = []
    message_text = f"{message_text}"
    system_prompt = {"role": "system", "content": feifei_photo}
    user_input_part = {"role": "user", "content": str(message_text)}
    input_prompt = [system_prompt] + [user_input_part]
    return input_prompt


def feifeichat(feifei_chat_text1="", feifei_chat_text2="", feifei_chat_text3=""):
    feifei_chat_all = f"{feifei_chat_text1}, {feifei_chat_text2},"
    message_text = f"{feifei_chat_all}"
    feifei_prompt = feifeiprompt(message_text)
    completion = myclient.chat.completions.create(
        model=os.getenv("mymodel"), messages=feifei_prompt, stream=True
    )
    temp = f"{feifei_chat_text3},"
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            temp += content
            yield temp
