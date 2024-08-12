
import re
import random
from .sd_webui_prompt_all_in_one_app import launch
import os
import pkg_resources
import comfy.lora
import folder_paths
import comfy.utils
import logging
import re

#正向提示词
class WeiLinComfyUIPromptAllInOneGreat:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "",
                    "placeholder": "输入正向提示词",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    # RETURN_TYPES = ("MODEL", "CLIP")
    # RETURN_TYPES = ("MODEL", "CONDITIONING")
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "encode"

    #OUTPUT_NODE = False

    CATEGORY = "WeiLin Nodes (WeiLin节点)"

    def encode(self, text):
        text= extract_tags(text)
        return (text,)


# 正向提示词的Lora加载器
class WeiLinComfyUIPromptAllInOneGreatLoras:

    def __init__(self):
        self.loaded_lora = None
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP", ),
                "text": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "",
                    "placeholder": "输入正向提示词",
                }),
            },
        }

    # RETURN_TYPES = ("STRING",)
    # RETURN_TYPES = ("MODEL", "CLIP")
    RETURN_TYPES = ("MODEL", "CONDITIONING")
    #RETURN_NAMES = ("image_output_name",)

    # FUNCTION = "encode"
    FUNCTION = "load_lora_great"

    #OUTPUT_NODE = False

    CATEGORY = "WeiLin Nodes (WeiLin节点)"
    
    # 加载Lora
    def load_lora_great(self, model, clip, text):
        arr,rel_str = replaceStrFunc(text)
        model_lora_second = model
        clip_lora_second = clip

        for str_lora_item in arr:
            loar_sim_path,str_n_arr = getStrLoraName(str_lora_item)
            # print(loar_sim_path,str_n_arr)
            strength_model = 1
            strength_clip = 1
            if len(str_n_arr) > 0:
                if len(str_n_arr) == 1:
                    strength_model = int(str_n_arr[0])
                    strength_clip = int(str_n_arr[0])
                if len(str_n_arr) > 1:
                    strength_model = int(str_n_arr[0])
                    strength_clip = int(str_n_arr[1])
            
            lora_path = folder_paths.get_full_path("loras", loar_sim_path)
            lora = None
            if self.loaded_lora is not None:
                if self.loaded_lora[0] == lora_path:
                    lora = self.loaded_lora[1]
                else:
                    temp = self.loaded_lora
                    self.loaded_lora = None
                    del temp

            if lora is None:
                lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
                self.loaded_lora = (lora_path, lora)

            model_lora_second, clip_lora_second = load_lora_for_models(model_lora_second, clip_lora_second, lora, strength_model, strength_clip)
        
        # prompt处理
        tokens = clip_lora_second.tokenize(rel_str)
        output = clip_lora_second.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
        cond = output.pop("cond")
        return (model_lora_second,[[cond, output]])
        # return (model_lora_second, clip_lora_second)
    

#反向提示词
class WeiLinComfyUIPromptAllInOneNeg:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "",
                    "placeholder": "输入反向提示词",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "encode"

    #OUTPUT_NODE = False

    CATEGORY = "WeiLin Nodes (WeiLin节点)"

    def encode(self, text):
        text= extract_tags(text)
        return (text,)



# 反向提示词的Lora加载器
class WeiLinComfyUIPromptAllInOneNegLoras:

    def __init__(self):
        self.loaded_lora = None
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP", ),
                "text": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "",
                    "placeholder": "输入反向提示词",
                }),
            },
        }

    # RETURN_TYPES = ("STRING",)
    # RETURN_TYPES = ("MODEL", "CLIP")
    RETURN_TYPES = ("MODEL", "CONDITIONING")
    #RETURN_NAMES = ("image_output_name",)

    # FUNCTION = "encode"
    FUNCTION = "load_lora_great"

    #OUTPUT_NODE = False

    CATEGORY = "WeiLin Nodes (WeiLin节点)"
    
    # 加载Lora
    def load_lora_great(self, model, clip, text):
        arr,rel_str = replaceStrFunc(text)
        model_lora_second = model
        clip_lora_second = clip

        for str_lora_item in arr:
            loar_sim_path,str_n_arr = getStrLoraName(str_lora_item)
            # print(loar_sim_path,str_n_arr)
            strength_model = 1
            strength_clip = 1
            if len(str_n_arr) > 0:
                if len(str_n_arr) == 1:
                    strength_model = int(str_n_arr[0])
                    strength_clip = int(str_n_arr[0])
                if len(str_n_arr) > 1:
                    strength_model = int(str_n_arr[0])
                    strength_clip = int(str_n_arr[1])
            
            lora_path = folder_paths.get_full_path("loras", loar_sim_path)
            lora = None
            if self.loaded_lora is not None:
                if self.loaded_lora[0] == lora_path:
                    lora = self.loaded_lora[1]
                else:
                    temp = self.loaded_lora
                    self.loaded_lora = None
                    del temp

            if lora is None:
                lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
                self.loaded_lora = (lora_path, lora)

            model_lora_second, clip_lora_second = load_lora_for_models(model_lora_second, clip_lora_second, lora, strength_model, strength_clip)
        
        # prompt处理
        tokens = clip_lora_second.tokenize(rel_str)
        output = clip_lora_second.encode_from_tokens(tokens, return_pooled=True, return_dict=True)
        cond = output.pop("cond")
        return (model_lora_second,[[cond, output]])
        # return (model_lora_second, clip_lora_second)
    


def extract_tags(text):
    pattern = r'#\[(.*?)\]'
    matches=re.findall(pattern, text)  
    for i in matches:
        newarr=i.split(',')
        random.seed(random.random())
        rdindex=random.randint(0,len(newarr)-1)
        rdtext=newarr[rdindex]
        text = re.sub(pattern, rdtext, text,count=1)
    return text



def load_lora_for_models(model, clip, lora, strength_model, strength_clip):
    key_map = {}
    if model is not None:
        key_map = comfy.lora.model_lora_keys_unet(model.model, key_map)
    if clip is not None:
        key_map = comfy.lora.model_lora_keys_clip(clip.cond_stage_model, key_map)

    loaded = comfy.lora.load_lora(lora, key_map)
    if model is not None:
        new_modelpatcher = model.clone()
        k = new_modelpatcher.add_patches(loaded, strength_model)
    else:
        k = ()
        new_modelpatcher = None

    if clip is not None:
        new_clip = clip.clone()
        k1 = new_clip.add_patches(loaded, strength_clip)
    else:
        k1 = ()
        new_clip = None
    k = set(k)
    k1 = set(k1)
    for x in loaded:
        if (x not in k) and (x not in k1):
            logging.warning("NOT LOADED {}".format(x))

    return (new_modelpatcher, new_clip)

# 匹配串
def replaceStrFunc(nom_str):
    # 原始字符串
    original_str  = nom_str
    # 使用正则表达式找到所有匹配的lora字符串
    lora_patterns = re.findall(r"<lora:[^<>]*>", original_str)
    # 初始化一个空字符串来存储修改后的结果
    modified_str = ""
    # 遍历原始字符串，移除匹配的lora字符串及其后的逗号
    last_index = 0  # 上一个lora字符串或字符串开头的索引
    for pattern in lora_patterns:
        # 将当前lora字符串之前的内容添加到modified_str中，跳过lora字符串及其后的逗号
        modified_str += original_str[last_index:original_str.find(pattern)]
        # 更新last_index为当前lora字符串之后的位置
        last_index = original_str.find(pattern) + len(pattern)
        # 如果lora字符串后面有逗号，则跳过逗号
        if last_index < len(original_str) and original_str[last_index] == ',':
            last_index += 1
    # 添加原始字符串中最后一个lora字符串之后的所有内容（如果有的话）
    modified_str += original_str[last_index:]
    # 移除尾部可能多余的逗号
    if modified_str.endswith(','):
        modified_str = modified_str[:-1]
    return (lora_patterns,modified_str)

def getStrLoraName(str):
    # 原始字符串  
    str_input = str
    # 使用正则表达式提取<lora:...>中的字符串
    match = re.search(r"<lora:([^>]*)>", str_input)
    if match:
        lora_content = match.group(1)  # 提取出的字符串，不包括<lora:和>
        # 检查是否包含:
        if ':' in lora_content:
            # 分割字符串
            parts = lora_content.split(':')
            # 处理分割后的部分
            main_part = parts[0]  # 第一个部分，即:前的字符串
            # 检查是否有额外的:和对应的数字
            numbers = []
            for part in parts[1:]:
                # 尝试从每个部分中提取数字
                num_match = re.search(r'(\d+(\.\d+)?)', part)
                if num_match:
                    numbers.append(num_match.group(0))  # 将找到的数字添加到列表中
            # 输出结果
            # print("Main Part:", main_part)
            # print("Numbers:", numbers)
            return (main_part,numbers)
        else:
            # 如果没有:，则只输出提取的字符串
            # print("Content:", lora_content)
            return (lora_content,None)
    else:
        return (None,None)


base_path = os.path.join(os.path.dirname(__file__), "sd_webui_prompt_all_in_one_app")
req_path = os.path.join(base_path,"requirements.txt")

def dist2package(dist: str):
    return ({
        "gradio": "gradio",
    }).get(dist, dist)


def install_requirements(requirements_file_path):
    # copy from controlnet, thanks
    with open(requirements_file_path) as file:
        for package in file:
            try:
                package = package.strip()
                if '==' in package:
                    package_name, package_version = package.split('==')
                    installed_version = pkg_resources.get_distribution(package_name).version
                    if installed_version != package_version:
                        launch.run_pip(f"install {package}", f"WeiLinComfyUIPromptAllInOne requirement: changing {package_name} version from {installed_version} to {package_version}")
                elif not launch.is_installed(dist2package(package)):
                    launch.run_pip(f"install {package}", f"WeiLinComfyUIPromptAllInOne requirement: {package}")
            except Exception as e:
                print(e)
                print(f'[错误]: Failed to install {package}, something may not work.')

#安装原APP依赖
print('WeiLinComfyUIPromptAllInOne 请求安装依赖中.......')
loadErr = 0
try:
    install_requirements(req_path)
except:
    loadErr = 1
    print('WeiLinComfyUIPromptAllInOne 请求安装依赖失败 =======')
if loadErr == 0:
    print('WeiLinComfyUIPromptAllInOne 请求安装依赖成功 =======')

#启动原APP
from .sd_webui_prompt_all_in_one_app.app import app_start
app_start()


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "WeiLinComfyUIPromptAllInOneGreat": WeiLinComfyUIPromptAllInOneGreat,
    "WeiLinComfyUIPromptAllInOneGreatLoras": WeiLinComfyUIPromptAllInOneGreatLoras,
    "WeiLinComfyUIPromptAllInOneNeg": WeiLinComfyUIPromptAllInOneNeg,
    "WeiLinComfyUIPromptAllInOneNegLoras": WeiLinComfyUIPromptAllInOneNegLoras,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "WeiLinComfyUIPromptAllInOneGreat": "WeiLin 正向提示词 Positive",
    "WeiLinComfyUIPromptAllInOneGreatLoras": "WeiLin 正向提示词Lora自动加载 Positive AutoLoras",
    "WeiLinComfyUIPromptAllInOneNeg": "WeiLin 反向提示词 Negative",
    "WeiLinComfyUIPromptAllInOneNegLoras": "WeiLin 反向提示词Lora自动加载 Negative AutoLoras",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]