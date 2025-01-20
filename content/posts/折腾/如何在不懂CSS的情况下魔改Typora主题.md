---
title: 如何在不懂CSS的情况下魔改Typora主题
date: 2024-01-29 12:00:00
categories: 图灵机
tags:
  - Typora
  - 折腾
  - CSS
summary: CSS 小白历险记
description: 本文介绍了作者在不熟悉 CSS 的情况下，如何通过修改现有 Typora 主题 Lapis 来创建一个新的主题 Marble 的过程。文章详细描述了从前期准备、确定需要的效果、观察主题结构到具体的修改步骤，包括字体替换、颜色调整、标题样式修改、引用块和代码块样式的变更等。作者通过使用 VS Code、AI 助手（如 ChatGPT 和 Github Copilot）以及大量的试错和学习，成功实现了主题的自定义。最终，作者将新主题 Marble 开源至 Github 和 Gitee，供大家下载使用。
slug: how-to-modify-typora-themes
---
嗨，大家好，我是 Chlorine。

本期的标题看起来非常扯，和"如何在不懂英语的情况下出一本译著"有一拼。但是这是真的，效果如下：

![|525](https://img.clnya.fun/IMG-20240129120000-1.webp)

看起来还挺不错的。事实上我这周末就在干这活。话不多说，直接开讲。

## 前期准备

- 一个基础主题：毫无疑问，都说了不会写 CSS 了。我选择的依旧是最喜欢的 Lapis 主题。
- VS Code 或者其他能编辑 CSS 代码的 IDE
- （Optional）AI 助手，例如 ChatGPT 和 Github Copilot。

## 第一步：确定你需要的效果

魔改的目的是让**已有的东西更好地适应我们的需要**。那你首先就得清楚自己想要什么样式。

以我为例，我的要求如下：

1. 字体：换上我最喜欢的霞鹜文楷。
2. 界面颜色：调得柔和一些，Lapis 原本的白色有点刺眼。
3. 标题样式：间距统一；二级标题样式修改；低级标题字体大小调整；二到六级标题加上标注，等等。
4. 引用块：样式调整，去掉左侧的 bar，换成另一个配饰。
5. 代码高亮：采取更加自然柔和的配色方案。

## 第二步：观察主题结构

### 工程结构

我们进入 Typora 的主题文件夹，简单观察下 Lapis 主题的组成部分。可以发现只有两部分：控制样式的 `lapis.css` 文件和存放字体的 `lapis` 文件夹。

### `.css` 文件结构

这步有点艰难，不仅需要一定的英语水平，还需要瞎猜的胆识。

在 IDE 中打开文件，耐心地从头看到尾。如果你的英语水平足够好，你应该可以猜出很多部分的功能。举几个例子：

```css
/*
 * Font-face for Cantarell, Source Han Serif CN and JetBrains Mono
 */

@font-face {
    font-family: "Cantarell";
    src: url('lapis/Cantarell-VF-fixed.otf');
}

@font-face {
    font-family: "JetBrainsMono";
    src: url('lapis/JetBrainsMono-Regular.ttf');
}

@font-face {
    font-family: "SourceHanSerifCN";
    src: url('lapis/SourceHanSerifCN-Medium.otf');
}

@font-face {
    font-family: "SourceHanSerifCN";
    src: url('lapis/SourceHanSerifCN-Bold.otf');
    font-weight: bold;
}
```

开猜。这段明显是定义字体的，引入了 Cantarell，Source Han Serif CN（思源宋体）和 JetBrains Mono 三种字体。根据每一部分的格式，我们可以猜测，我们在引入新的字体时的格式为：

```css
@fontface{
	font-family: "<字体名称>";
    src: url('<字体文件路径>');
}
```

同时注意到，粗体字需要单独引入。

再比如：

```css
#write h2 {
    background-color: var(--header-span-color);
    color: var(--bg-color);
    padding: 1px 12.5px;
    border-radius: 4px;
    display: inline-block;
}
```

H2 显然是二级标题，`background-color` 是背景颜色的意思，其值是前面定义的 `--header-span-color`；颜色是 `--bg-color`，和背景颜色一样，说明想制造出镂空的效果；`padding` 是内边距的意思；`border-radius` 看着似乎和圆角大小有关；`display` 也许是指展示方式，不用管。总而言之，这应该是用来定义二级标题样式的。

诸如此类，一直猜就可以。看不懂不要紧，如果看起来不是和你要改的东西相关就不用管，如果相关，可以询问 AI 助手或者 CV 过去查字典/搜索。

![|471](https://img.clnya.fun/IMG-20240129120000-2.webp)

## 第三步：开改

终于到了开始改的时候了。我会以我的过程为例讲解一下改动的基本思路。

### 字体修改

在 `lapis` 文件夹中加入字体文件：

![](https://img.clnya.fun/IMG-20240129120000-3.webp)

然后在 `@font-family` 处引入字体文件代替思源宋体：

```css
@font-face {
    font-family: "LXGWWenKaiGB";
    src: url('lapis/LXGWWenKaiGB-Regular.ttf');
}

@font-face {
    font-family: "LXGWWenKaiGB";
    src: url('lapis/LXGWWenKaiGB-Bold.ttf');
    font-weight: bold;
}
```

在 `#write`（基本配置区）中加入字体的名称：

```css
#write {
    max-width: 950px;
    font-size: 1.1rem;
    color: var(--text-color);
    line-height: 1.6;
    word-spacing: 0px;
    letter-spacing: 0px;
    word-break: break-word;
    word-wrap: break-word;
    text-align: justify;

    font-family: 'Cantarell', 'LXGWWenKaiGB', 'JetBrainsMono';
    /* 在上面这里修改 */
    margin-bottom: 20rem;
}
```

同时修改下文的目录、标题等处除代码块外所有内容的字族为 `'Cantarell', 'LXGWWenKaiGB'`。

根据 Github Copilot 的回答，CSS 中会优先使用靠前的字族，在字符搜索不到时递补到后面的字族进行搜索。Cantarell 是纯拉丁字体，没有中文字，这样就可以实现中英文字体分别设置。当然，如果你的字族是中英文混合的，例如 LXGWBrightGB（霞鹜文楷 GB 和 Ysabeau 的融合字体，相当好看），就可以只设置一个。

### 修改颜色

颜色代码位于文件开头处 6-42 行（行数为相对于原始文件而言，下同）：

```css
:root {
    --text-color: #40464f;
    /* Text */
    --primary-color: #4870ac;
    /* Primary Color */
    --bg-color: #ffffff;
    --side-bar-bg-color: var(--bg-color);
    /* Background */

    --marker-color: #a2b6d4;
    /* List Marker */
    --highlight-color: #ffffb5c2;
    /* Highlight */
    --header-span-color: var(--primary-color);
    /* h2 Span Color */
    --block-bg-color: #f6f8fa;
    /* Block Background */
    --img-shadow-color: #e3e8f0;

    /* Overwrite of Typora Base Color */
    --search-hit-bg-color: var(--select-text-bg-color);
    --search-select-bg-color: #5bb3ff;
    --control-text-hover-color: #a2b6d4;
    --rawblock-edit-panel-bd: var(--block-bg-color);
    --item-hover-bg-color: rgb(246 248 250);
    --active-file-bg-color: var(--block-bg-color);
}
```

大家按照自己的喜好修改即可。VS Code 有颜色预览，非常方便。

### 标题样式

这个比较复杂。首先定位控制标题的代码，位于文件 208-305 行，header 注释的下方。代码太多，我省略了一部分。

```css
#write h4,
#write h5,
#write h6 {
    font-weight: normal;
}

#write h1,
#write h2,
#write h3,
#write h4,
#write h5,
#write h6 {
    font-family: 'SourceHanSerifCN';
    padding: 0px;
    color: var(--primary-color);
}

/* 基础样式 */

#write h1 {
    text-align: center;
}

#write h2 {
    background-color: var(--header-span-color);
    color: var(--bg-color);
    padding: 1px 12.5px;
    border-radius: 4px;
    display: inline-block;
}

/* H2的一堆样式 */

#write h1 {
    font-size: 2rem;
}

/* 字体大小 */

#write h1 {
    padding-top: 0.9rem;
    margin-bottom: 2.3rem;
}

/* 设置间距 */

blockquote h3.md-focus:before,
blockquote h4.md-focus:before,
blockquote h5.md-focus:before,
blockquote h6.md-focus:before {
    left: -1.3rem;
}
/* 不知道是什么，也不用知道 */
```

首先修改标题字重为粗体（strong）。事实上只需要去掉原本 H4-H6 的设置，因为标题默认是粗体。

下面修改 H2 的样式。请教了 Github Copilot 后，我得到了这样的代码：

```css
#write h2 {
    color: var(--primary-color);
    padding: 1px 0px;
    display: inline-block;
    background-image: linear-gradient(to left, transparent, var(--block-bg-color), transparent);
    background-repeat: no-repeat;
    background-size: 120% 1.2px;
    background-position: center bottom;
    /* 做了一条很浅的渐变下划线 */
}
```

下面删除除一级标题间距外的间距（margin）代码，加入我们设置的统一间距：

```css
#write h2,
#write h3,
#write h4,
#write h5,
#write h6 {
    margin: 0.5em 0 0.5em;
}
```

调整字体大小：

```css
#write h1 {
    font-size: 2.2em;
}

#write h2 {
    font-size: 2rem;
}

#write h3 {
    font-size: 1.8rem;
}

#write h4 {
    font-size: 1.6rem;
}

#write h5 {
    font-size: 1.4rem;
}

#write h6 {
    font-size: 1.2rem;
}
```

为二至六级标题加上 H2-H6 角标。此时需要使用这样的代码：

```css
#write h2::before,
#write h3::before,
#write h4::before,
#write h5::before,
#write h6::before {
    vertical-align: super;
    font-size: 0.35em;
    margin-right: 0.4em;
}

#write h2::before {
    content: "H2";
}

#write h3::before {
    content: "H3";
}

#write h4::before {
    content: "H4";
}

#write h5::before {
    content: "H5";
}

#write h6::before {
    content: "H6";
}
```

前面的一坨是统一的样式，后面是内容。

### 引用块样式修改

对应源代码的 `blockquote` 部分。还是询问 AI 助手后得到如下灵感：

```css
#write blockquote {
    display: block;
    font-size: .9em;
    overflow: auto;
    padding: 15px 30px 15px 42px;
    margin-bottom: 20px;
    margin-top: 20px;
    background: var(--block-bg-color);
    position: relative;
}

#write blockquote::before {
    content: ">";
    /*加了一个小标记“>”*/
    font-size: 2.3em;
    position: absolute;
    left: 20px;
    /* 调整左侧位置 */
    top: 50%;
    /* 居中显示 */
    transform: translateY(-55%);
    /* 用于垂直居中 */
    color: #E0E0E0;
}
```

### 分割线样式修改

对应于 dividing line 部分。与前面的 H2 一样使用渐变方案：

```css
/* 分割线 Dividing line */

hr {
    margin-top: 20px;
    margin-bottom: 20px;
    border: 0;
    border-top: 1.4px solid;
    border-image: linear-gradient(to right, transparent 10%, #D0DDE6 25%, #D0DDE6 75%, transparent 90%) 1;
    border-radius: 2px;
    /* 渐变分割线 */
}
```

### 代码块

这是最让我头大的一部分，头大的原因不是技术问题，而是如何配色。在请教了 AI 助手，并且查了一堆颜色对照表之后，我简单定出了这个方案：

```css
/* 关键字 - 海蓝石 */
.cm-s-inner .cm-keyword {
    color: #87d4eb !important;
}

/* 操作符 - 铁灰色 */
.cm-s-inner .cm-operator {
    color: #43464B !important;
}

/* 变量、内置对象、头标题、标签、属性、引用 - 紫水晶 */
.cm-s-inner .cm-variable,
.cm-s-inner .cm-builtin,
.cm-s-inner .cm-header,
.cm-s-inner .cm-tag,
.cm-s-inner .cm-property,
.cm-s-inner .cm-quote {
    color: #9932CC !important;
}

/* 变量2 - 绿松石 */
.cm-s-inner .cm-variable-2 {
    color: #30d5b1 !important;
}

/* 变量3、类型、原子 - 蓝宝石 */
.cm-s-inner .cm-variable-3,
.cm-s-inner .cm-type,
.cm-s-inner .cm-atom {
    color: #3c7ce3 !important;
}

/* 数字 - 玫瑰石膏 */
.cm-s-inner .cm-number {
    color: #e5c0ff !important;
}

/* 定义、限定符 - 青金石 */
.cm-s-inner .cm-def,
.cm-s-inner .cm-qualifier {
    color: #1357a5c2 !important;
}

/* 字符串 - 黄铁矿 */
.cm-s-inner .cm-string {
    color: #8B4513 !important;
}

/* 字符串2 - 绿松石 */
.cm-s-inner .cm-string-2 {
    color: #30D5C8 !important;
}

/* 注释 - 银灰 */
.cm-s-inner .cm-comment {
    color: #C0C0C0 !important;
}

/* 元数据 - 暗金色 */
.cm-s-inner .cm-meta {
    color: #B8860B !important;
}

/* 属性 - 紫水晶 */
.cm-s-inner .cm-attribute {
    color: #9932CC !important;
}

/* 错误 - 铁玫瑰 */
.cm-s-inner .cm-error {
    color: #FFFFFF !important;
    background-color: #D02537 !important;
}

/* 匹配的括号 - 白垩石 */
.cm-s-inner .CodeMirror-matchingbracket {
    text-decoration: underline;
    color: #ffffffc3 !important;
}
```

其中的 `!important` 应该是高优先级的意思。这套方案不是很好看，但也还行。

### 总结

我还对文件进行了一些小修改，就不多说了。由于我的修改太多了，我干脆照着原本的文件重写了一个，变成了一个新的主题，这也就是开头那张图。根据我的配色和原本的主题 Lapis（天青石），我把主题命名为 Marble（大理石）。

主题现已开源至 [Github](https://github.com/chlorine3545/typora-theme-marble) 和 [Gitee](https://gitee.com/chlorine3545/typora-theme-marble)，欢迎大家前去下载尝试。如果可以的话，想要一颗 star (\*^▽^\*)。

这些修改看着复杂，实际上主要还是依靠猜代码含义和借助 AI。

## 后记

总体而言，魔改主题还是挺费事的。不过只要有足够的耐心，虽说写出全新的主题比较难，但是改出一些自己喜欢的效果还是可以的。

Marble 主题我会尽力维护，但是由于不懂 CSS+平时事的确比较多，更新就随缘了。

下一步似乎可以用这种方式魔改 Obsidian 的主题……算了我还是去学学 HTML 和 CSS 吧（乐）
