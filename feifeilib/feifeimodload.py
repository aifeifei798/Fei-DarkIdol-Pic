import os
# os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'backend:cudaMallocAsync'

import torch
# import spaces
from diffusers import (
    DiffusionPipeline,
    AutoencoderTiny,
    FluxImg2ImgPipeline,
    FluxPipeline,
    BitsAndBytesConfig as DiffusersBitsAndBytesConfig,
    FluxTransformer2DModel,
)

from transformers import BitsAndBytesConfig as BitsAndBytesConfig, T5EncoderModel, AutoModel

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA is available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")

dtype = torch.float16

def feifeimodload():

    quant_config = BitsAndBytesConfig(load_in_8bit=True)
    text_encoder_8bit = T5EncoderModel.from_pretrained(
        "./DarkIdol-flux-public",
        subfolder="text_encoder_2",
        quantization_config=quant_config,
        torch_dtype=dtype,
    )

    quant_config = DiffusersBitsAndBytesConfig(load_in_8bit=True)
    transformer_8bit = FluxTransformer2DModel.from_pretrained(
        "./DarkIdol-flux-schnell-v1.1-0.8",
        subfolder="transformer",
        quantization_config=quant_config,
        torch_dtype=dtype,
    )

    pipe = FluxPipeline.from_pretrained(
        "./DarkIdol-flux-public",
        text_encoder_2=text_encoder_8bit,
        transformer=transformer_8bit,
        torch_dtype=dtype,
        device_map="cuda",
    )
    
    # pipe.load_lora_weights(
       # "./lora/feifei.safetensors",
       # adapter_name="feifei_lora",
       # torch_dtype=dtype,
    # )

    # pipe.set_adapters(
    #    ["feifei"],
    #    adapter_weights=[0.85],
    # )

    # pipe.fuse_lora(
    #    adapter_name=["feifei"],
    #    lora_scale=1.0,
    # )
          
    pipe.vae.enable_slicing()
    pipe.vae.enable_tiling()
    # pipe.unload_lora_weights()
    torch.cuda.empty_cache()
    # pipe.enable_model_cpu_offload()
    return pipe
