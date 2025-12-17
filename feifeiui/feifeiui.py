import gradio as gr
import numpy as np
import config_zh
import feifeilib.feifeipromptjueselist as feifeipromptjueselist

from feifeilib.feifeitexttoimg import feifeitexttoimg
from feifeilib.feifeipromptgeneratorBrooklyn import feifeigenerateprompt
from feifeilib.feifeipromptgeneratorTxt import get_random_line_linecache
from feifeilib.feifeipromptjuese import feifeipromptjuese
from feifeilib.feifeillama import feifeillama

MAX_SEED = np.iinfo(np.int32).max
MAX_IMAGE_SIZE = 2368


css = """
#col-container {
    margin: 0 auto;
    max-width: 500px;
}
"""


def create_ui():
    with gr.Blocks() as FeiFei:
        with gr.Row(elem_id="col-container"):
            with gr.Column():
                with gr.Row():
                    with gr.Column(scale=1):
                        imagegallery = gr.Gallery(
                            label="Generated images",
                            show_label=False,
                            columns=[2],
                            rows=[12],
                            object_fit="contain",
                            height=820,
                        )
                        styles_prompt = gr.Dropdown(
                            ["CILP", "T5"],
                            label="text_encoder",
                            show_label=False,
                            multiselect=False,
                            value="T5",
                        )
                        pic_num = gr.Slider(
                                label="Pic Num",
                                minimum=1,
                                maximum=8,
                                step=1,
                                value=2,
                        ) 
                    with gr.Column(scale=2):
                        result = gr.Gallery(
                            label="Result",
                            show_label=False,
                            interactive=False,
                            object_fit="contain",
                            allow_preview=True,
                            preview=False,
                            selected_index = None,
                            type="filepath",
                            height=820,
                            format="png",
                            columns=2,
                            rows=2,
                        )
                        feifei_button = gr.Button("Gen Pic")
                    with gr.Column(scale=1):
                        juese_name = [
                            style["name"] for style in feifeipromptjueselist.juese_list
                        ]
                        juese_Radio = gr.Dropdown(
                            juese_name,
                            label="角色",
                            show_label=False,
                            multiselect=False,
                            value="(None)",
                        )
                        styles_name = [
                            style["name"] for style in config_zh.style_list
                        ]
                        styles_Radio = gr.Dropdown(
                            styles_name,
                            label="Styles",
                            show_label=False,
                            multiselect=True,
                            value="(None)",
                        )

                        gen_prompt = gr.Button("Gen Prompt")
                        gen_txt_prompt = gr.Button("Gen Txt Prompt")
                        gen_prompt_gen = gr.Button("Gen By LLM")
                        
                        prompt_gen = gr.Text(
                            label="Prompt",
                            show_label=False,
                            placeholder="Enter your prompt",
                            value="一位漂亮的韩国美女,",
                            lines=3,
                            max_lines=30,
                            container=False,
                        )     
                        prompt_1 = gr.Text(
                            label="Prompt",
                            show_label=False,
                            placeholder="Enter your prompt",
                            value="a beautiful Korean woman, Kpop idol,",
                            lines=3,
                            max_lines=30,
                            container=False,
                        )
                        prompt_2 = gr.Text(
                            label="Prompt",
                            show_label=False,
                            placeholder="Enter your prompt",
                            value="",
                            lines=5,
                            max_lines=30,
                            container=False,
                        )
                        gr.HTML("by __artist__")
                        
                        with gr.Accordion("More", open=False):
                            with gr.Row():
                                add_watermark_select = gr.Checkbox(
                                    label="watermark", value=True
                                )
                                FeiFei_select = gr.Checkbox(
                                    label="feifei", value=False
                                )
                                quality_select = gr.Checkbox(
                                    label="quality", value=False
                                )

                            out_prompt = gr.Text(
                                label="Prompt",
                                show_label=False,
                                lines=5,
                                max_lines=12,
                                placeholder="this photo prompt",
                                value="",
                                container=False,
                            )

                            feifei_lora = gr.Checkbox(
                                label="Fei Lora", value=False
                            )
                            feifei_lora_num = gr.Slider(
                                label="Seed",
                                minimum=0,
                                maximum=2,
                                step=0.05,
                                value=0.85,
                            )
                            skin_lora = gr.Checkbox(
                                label="Skin Lora", value=False
                            )
                            skin_lora_num = gr.Slider(
                                label="Seed",
                                minimum=0,
                                maximum=2,
                                step=0.05,
                                value=1,
                            )
                            nsfw_v2_lora = gr.Checkbox(
                                label="NSFW Lora", value=False
                            )
                            nsfw_v2_num = gr.Slider(
                                label="Seed",
                                minimum=0,
                                maximum=2,
                                step=0.05,
                                value=1,
                            )                                
                            negative_prompt_check = gr.Checkbox(
                                label="Negative Prompt", value=False
                            )
                            negative_prompt  = gr.Text(
                                label="Prompt",
                                show_label=False,
                                placeholder="Enter your negative prompt",
                                value="(worst quality, low quality, bad quality:1.4), JPEG artifacts, ugly, blurry, grainy, deformed, disfigured, mutilated, bad anatomy, malformed limbs, extra limbs, extra arms, extra legs, missing arms, missing legs, fused fingers, extra fingers, fewer fingers, mutated hands, (poorly drawn hands, bad hands:1.3), poorly drawn face, long neck, tiling, out of frame, body out of frame, cropped, cut off, draft, watermark, signature, subtitles, username, noisy, low contrast, realistic",
                                lines=5,
                                max_lines=30,
                                container=False,
                            )
                            seed = gr.Slider(
                                label="Seed",
                                minimum=0,
                                maximum=MAX_SEED,
                                step=1,
                                value=0,
                            )

                            randomize_seed = gr.Checkbox(
                                label="Randomize seed", value=True
                            )
                            gr.Markdown(
                                """ - 21:9 2368x1024
                                        - 16:9 1792x1024
                                        - 9:7  1664x1280 """
                            )
                            width = gr.Slider(
                                label="Width",
                                minimum=512,
                                maximum=MAX_IMAGE_SIZE,
                                step=64,
                                value=1088,
                            )
                            height = gr.Slider(
                                label="Height",
                                minimum=512,
                                maximum=MAX_IMAGE_SIZE,
                                step=64,
                                value=1856,
                            )

                            num_inference_steps = gr.Slider(
                                label="Number of inference steps",
                                minimum=1,
                                maximum=50,
                                step=1,
                                value=5,
                            )
                            guidancescale = gr.Slider(
                                label="Guidance scale",
                                minimum=0,
                                maximum=20,
                                step=0.1,
                                value=0,
                            )
        gen_prompt.click(
            fn=feifeigenerateprompt,
            outputs=[prompt_2]
        )
        gen_txt_prompt.click(
            fn=get_random_line_linecache,
            outputs=[prompt_2]
        )
        feifei_button.click(
            fn=feifeitexttoimg,  # Function to run for this button
            inputs=[
                pic_num,
                prompt_1,
                prompt_2,
                negative_prompt_check,
                negative_prompt,
                styles_Radio,
                styles_prompt,
                add_watermark_select,
                feifei_lora,
                feifei_lora_num,
                skin_lora,
                skin_lora_num,
                nsfw_v2_lora,
                nsfw_v2_num,
                seed,
                randomize_seed,
                width,
                height,
                num_inference_steps,
                guidancescale,
                FeiFei_select,
                quality_select,
            ],
            outputs=[result, out_prompt, imagegallery],
        )
        juese_Radio.change(
            fn = feifeipromptjuese,
            inputs = [juese_Radio],
            outputs = [prompt_1]
        )
        gen_prompt_gen.click(
            fn = feifeillama,
            inputs = [prompt_gen],
            outputs = [prompt_2]
        )
    return FeiFei
