<div align="center">
  
### [🇨🇳 简体中文](README.md) | [🇺🇸 English](README_EN.md)

</div>

# 版本更新介绍

> 3.5.0 版本介绍
>
> 0. 由于之前仓库上传了一些非常大的文件，2024-8-16 仓库进行了清空所以之前的仓库版本都删除了这是为了减小仓库大小
> 1. 修复了已知 BUG
> 2. 修改-恢复了以前旧版本的功能，支持了更多的节点搭配
> 3. 新增-增加了本地 LLM 模型使用，可以帮你续写提示词

> 3.0.0 版本介绍
>
> 1. 修复了已知 BUG
> 2. 新增-Tag 添加、删除、修改 功能
> 3. 新增-开启窗口模式可以随意拖动窗口右小角可以调节窗口大小方便在 ComfyUI 中使用
> 4. 新增-Lora 查看器，在 Lora 卡片中右上角有个提示按钮点击即可查看 Lora 信息且可以同步 C 站和设置 Lora 封面的功能
> 5. 新增-Lora 的提示词有专属适配 ComfyUI 的模型强度和 CLIP 强度的调节器

> 2.4.0 版本介绍</br>1. 修复了提示词补全的 BUG</br>2. 仅中文新增了 NSFW 提示词库</br>3. 新增了 Lora 提示词自动加载，只需要在 PromptUI 添加 Lora 即可与 WebUI 提示词写法一样</br>4. 在 ComfyUI 设置里面可以修改 PromptUI 的关闭按钮切换到右边

> 2.3.0 版本介绍</br>1. 新增了提示词补全功能

> 2.2.0 版本介绍 </br>1. 修复了已知 BUG</br>2. 更新了新的功能：全局提示词 UI、放大窗口功能

# Lora 提示词写法提示

<lora:xxxx:0.3:0.4>这种写法解释 0.3 是模型强度 0.4 是 CLIP 强度
如果你是<lora:xxxx:0.4>那么这种写法解释 模型强度和 CLIP 强度都是 0.4

# 概要说明

本项目可以让你在 ComfyUI 中像 WebUI 一样写提示词，从 Prompt-all-in-one 项目修改而来但已做了大部分的修改适配 ComfyUI，新增了许多不一样的功能，以及提示词补全的插件，提示词补全插件是从 ComfyUI-Custom-Scripts 项目修改而来，感谢你对本插件的支持。

如果你对本项目有兴趣赏一个 Star 吧！

# 安装教程，可以直接 git 本项目即可

> https://github.com/weilin9999/WeiLin-ComfyUI-prompt-all-in-one.git

# 安装插件详细介绍，手动安装版本

直接下载本项目最新的 Release 然后解压，放到 ComfyUI 直接启动 ComfyUI 即可使用本插件。
![](https://github.com/weilin9999/WeiLin-ComfyUI-prompt-all-in-one/blob/master/step/1.png)

# 节点使用方法

按以下操作使用即可
![](https://github.com/weilin9999/WeiLin-ComfyUI-prompt-all-in-one/blob/master/step/2.png)
![](https://github.com/weilin9999/WeiLin-ComfyUI-prompt-all-in-one/blob/master/step/3.png)
![](https://github.com/weilin9999/WeiLin-ComfyUI-prompt-all-in-one/blob/master/step/4.png)

# WeiLin-ComfyUI-Prompt-all-in-one 借鉴项目

WeiLin-ComfyUI-Prompt-all-in-one ComfyUI 版的 prompt-all-in-one，在基于 sd-webui-prompt-all-in-one-app https://github.com/Physton/sd-webui-prompt-all-in-one-app 项目上修改而来的 ComfyUI 版本，只需要在 ComfyUI 中添加本项目的 ComfyUI 节点即可使用可视化的 tag 编辑器 ，提示词补全使用了 https://github.com/pythongosssss/ComfyUI-Custom-Scripts 项目进行修改只用了补全功能并做了修改，项目使用的本地 LLM 大模型借鉴了https://github.com/thisjam/comfyui-sixgod_prompt仓库的代码

如果你喜欢本项目赏一个 star 吧！

# 本项目简要说明

项目初始只是方便编辑 tag，所以自己写了插件，有问题可以提交 issue，不一定会处理哈。
