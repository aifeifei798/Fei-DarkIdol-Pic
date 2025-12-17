import feifeilib.feifeipromptjueselist as feifeipromptjueselist

def feifeipromptjuese(style_name):
    for style in feifeipromptjueselist.juese_list:
        if style["name"] == style_name:
            prompt = style["prompt"]
    return prompt