---
title: "Hello，iTerm2"
date: 2024-05-05T20:18:00
featuredImage: https://img.clnya.fun/cover/hello-iterm2-cover.webp
slug: hello-iterm2
categories: ["逍遥游"]
summary: 找到了一个好用的终端啦
description: 本文介绍了作者使用 iTerm2 作为终端模拟器的过程及配置。作者最初因担心兼容性问题放弃了 Hyper，尝试了多个终端，包括默认终端、Warp、Wave、Wind 和 Tabby，但各自都有不足，最终选择了 iTerm2。文章详细介绍了通过 Homebrew 安装 iTerm2，并推荐了 Oh-my-zsh、zsh 插件、tmux 等工具来提升使用体验。此外，作者分享了如何自定义 iTerm2 的配色、字体、状态栏及图标等美化步骤，推荐了 Starship 作为终端美化插件，并展示了最终配置效果。
tags:
    - 折腾
    - iTerm2
---
# Hello, iTerm2

各位老友们好，我是 Chlorine。

最近兜兜转转，换了许多个 Terminal emulator，最终选择了 iTerm2。所以写点东西记一下。

## 前言

其实单纯是因为看到 Hyper 太久没放新的 release 了，害怕出什么兼容性问题。所以，折腾吧。

### 默认终端

这自然是最原生的选择。但是，默认终端浑身上下都散发着一个字：难看（通辽汉字 1/1）. 而且，默认终端还换不了图标。这对别人来说可能不是什么事，但是对我来说，有点难绷。

### Warp

这个终端十分逆天。具体来说，这个终端是闭源的，还需要登录。

当然，这种设计招致了大量用户的不满。具体请看 [https://github.com/warpdotdev/Warp/discussions/400](https://github.com/warpdotdev/Warp/discussions/400) 。

不知道大家敢不敢用，反正我是不敢，尽管这个终端确实优秀。

### Wave

可以说是 Warp 的开源替代品。特色是自带一个有趣的文本编辑器 `codeedit`，能在终端中实现类似于 GUI 文本编辑器的功能。不过缺点是没有高亮，我已经[提 issue](https://github.com/wavetermdev/waveterm/issues/636) 了。

（小声：而且我也没有 GPT 的 API，这个 AI 也就没什么大用）

### Wind

这个终端看起来很有特色，有点像 IDE。不过我用起来有点不顺手。

最难绷的是，它可以换图标，但是在启动的时候，图标就会换回去。

> 我去除了大部分的 Wind 的图标，但是我保留了一部分，我觉得保留了一部分 Wind 的图标才知道你用的是 Wind。

### Tabby

这个我用了一段时间。优点是超级好看，缺点是启动非常慢，这是我无法忍受的。而且，可能是 bug，在显示命令的时候有时候会重叠。

### 其他

略略略略略。

## 瘟锌锑逝

- 本文不完全是教程，有许多步骤讲得不清晰。
- 大家各有各的需求，请根据自己的实际情况因地制宜。
- 后面会经常涉及 `.zshrc` 的编辑，新手推荐用 nano 而不是 Vim 作为编辑器。或者是在用户根目录点击 `⌘ + ⇧ + .` 显示隐藏文件，找到后用 VS Code 等编辑。
- 别问为什么封面是 Ubuntu，问就是找不到图。

## 前置准备

- 一台电脑（对我来说就是 MacBook）
- 作为默认终端的 Zsh
- Homebrew（最好是有。可以搜索 Homebrew-CN 加速。）
- 脑子，眼睛，手

## iTerm2 简介

很多人说 iTerm2 是 macOS 上所有 Terminal emulator 的终点。这话有点夸张，但是也的确说明了这个终端的优秀和受欢迎。

iTerm2 是一个在 GPL-2.0 协议下开源的 macOS 终端模拟器，具有出色的性能和极高的可玩性。

- 官方网站：[https://iterm2.com](https://iterm2.com)
- GitHub 地址：[https://github.com/gnachman/iTerm2](https://github.com/gnachman/iTerm2)

## 安装 iTerm2

这里推荐使用 Homebrew 安装。在终端（没错，在安装终端之前，你需要一个终端 🤣）中输入：

```bash
brew install iterm2
```

等着安装完成，在启动台打开就可以了。

理论上说，这个时候已经可以开始用了。但是，我建议继续看，进行一点美化。

## Oh-my-zsh 及其插件

[Oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 是一个 Zsh 插件，能够为 Zsh 提供许多的加持。

### Zsh-syntax-highlighting

这是一个能给命令带来高亮的插件。这个相当有用，例如，在你输入一个命令时，如果命令是红色的，那么就说明你这个命令有问题了。

### Zsh-auto-suggestion

这个插件可以使用你的命令历史记录进行自动补全建议。不过这东西比 GitHub Copilot 之类的肯定差多了，因为只能用你的历史记录进行推断。

### 其他

包括 autojump 和 z 等。大家可以在[https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins)看一看。

### 配置

我能不写了不 qaq，好长啊。可以参考项目的官方文档和网上的教程，搜索 oh my zsh 教程即可。

## tmux

又是一个项目，简单来说就是增添多标签页功能。

依然使用 Homebrew：

```bash
brew install tmux
```

## 状态栏

在设置-Appearance-Theme 中改为 Minimal，Status bar location 可以调整到自己喜欢的位置，我选择底部。

然后在设置-Profiles-（选择某一个）-Session 中，底部选择 status bar enabled，config 一下自己喜欢的元素即可。

![](https://img.clnya.fun/IMG-20240505203843.webp)

## 导入配色方案

[iTerm2 的配色方案](https://github.com/mbadolato/iTerm2-Color-Schemes)非常多，这里我选择 [Catppuccin](https://github.com/catppuccin/catppuccin)。

在[这里](https://github.com/catppuccin/iterm/tree/main/colors)下载一个 `.itermcolors` 格式的文件，然后在设置-Profiles-（选择某一个）-Colors-Color Presets-Import 导入并启用即可。

## 自定义字体

设置-Profiles-（选择某一个）-Text-Font 改变字体即可。由于我们后面可能涉及特殊符号，所以建议选择一个 Nerd font，例如 Fira code Nerd font。缺点就是没办法设置中文字体，不过终端也很少出现中文吧。

## 换图标

没错，换图标不仅是一种行为，更是一种习惯。

依然是在 [macosicons.com](https://macosicons.com/#/) 搜索图标。由于换图标是给自己看的，因此也不需要拘泥于 iTerm2 的图标，搜索 iTerm2、Terminal 等关键词都可以。我用的是这个：

![](https://img.clnya.fun/IMG-20240505203620.webp)

原本是 `>_`，加上一半之后瞬间可爱了。

直接把图标下载下来，在应用程序中选中 iTerm2，`⌘ + I` 显示简介，然后将新图标拖拽到左上角的应用程序名称旁边的图标上就好。

## 背景图片

![](https://img.clnya.fun/IMG-20240505204053.webp)

在这里的 Background Image 处修改就好，建议选成 Scale to Fill。

## 安装 Starship

[Starship](https://starship.rs) 是一个用 Rust 写的终端（我感觉更应该称为终端插件），非常好看。

我们依然选择 Homebrew 进行安装：

```bash
brew install starship
```

安装好之后，打开 `.zshrc` ，在最后添加一行：

```txt
eval "$(starship init zsh)"
```

也不需要什么额外配置。如果想玩一玩，可以参考其官方文档。

## 最终效果

![](https://img.clnya.fun/IMG-20240505202811.webp)

我个人还是挺满意的。实际上我用的不是这张背景图，为了防止侵权，临时换的。

以及，image auto upload 真是好样的，我图全没了。

并且，我鼠须管坏了，更新不了。大乐。
