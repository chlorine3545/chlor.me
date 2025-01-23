---
title: 在Hugo博客中正确渲染多行数学公式
date: 2024-02-20 15:10:45
categories: 百草园
tags:
  - 折腾
  - Hugo
  - KaTeX
  - 博客
summary: LaTeX，没了你我可怎么活啊 LaTeX
description: 本文介绍了为 Hugo 博客增加基于 KaTeX 的多行数学公式渲染的步骤，包括引入 JavaScript 和修改 Hugo 配置文件等步骤。作者指出，MathJax 能够原生渲染物理和化学公式，而 KaTeX 需要引入扩展包。
slug: hugo-math-rendering
math: true
---

> [!IMPORTANT]
> 本文距离发布已经很久了，在此期间我的数学公式渲染方法出现了变化。我更新了文章的部分内容，使得文章中的方法依然具有基本可用性。在合适的时机我会重写本文。

如果本文的数学公式不渲染，可能是 Swup.js 的问题，刷新页面即可。

—— 2024.11.25

---

各位老友们好，我是 Chlorine。本期可以说是建站教程的一个小番外，也是我迄今为止用时最短的一次折腾。

## 前言

作为计算机系的学生，我对于在博客中插入数学公式还是有一定需求的，不仅是技术博客的刚需，有时候对于整活也是必要的。比如：

$$
\begin{cases}
x = \sin t, \\ 
y = \frac{t \cos t}{2}
\end{cases} 
\quad 0 \leq t \leq 2 \pi
$$

至于这个参数方程是什么含义，大家可以找个绘图工具，比如 Desmos 或者 Geogebra 试一下（doge）。

但是，就在我昨天发布第一条数学笔记的时候，我发现我的 KaTeX 迟迟无法正确渲染一些公式，例如 `\left\{`。刚开始我没太在意，随便试了几种方法，改正了就完事了。

但是今天，在我打出上面那串参数方程的时候，我突然发现，换行符 `\\` 没生效。

![黑人问号.webp](https://img.clnya.fun/emoji/EMJ-confused.webp)

我不信邪，刚刚试了一下这个矩阵式的公式块：

$$
\mathbf{V}_1 \times \mathbf{V}_2 =  
\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\[0.4em]
  \frac{\partial X}{\partial u}& \frac{\partial Y}{\partial u}& 0 \\[0.4em] 
  \frac{\partial X}{\partial v}& \frac{\partial Y}{\partial v}& 0 \\[0.4em] 
\end{vmatrix}
$$

发现也没正确渲染。

这可麻烦了，毕竟这学期的 VA（2）和高代（高等线性代数选讲），上学期还没填的线代可都靠着多行公式环境活呢。

问了 GitHub Copilot 和 Kimi  AI，都没得到什么有用的信息，遂一头问号大如斗，问号随风满地走。

再回去看那串没被渲染的公式，突然发现了奇怪的东西：

**这换行符咋就剩下一个反斜杠了？**

众所周知，反斜杠在 Markdown 中是转义符，双反斜杠在单纯的 Markdown 环境里会被解读成单反斜杠。会不会 KaTeX 和 Hugo 内置的 goldmark 渲染器冲突了？毕竟，我的 KaTeX 是自己加的，与原本的工程冲突也很正常。

于是前往收集信息，最终找到了解决方案。

## 引入 KaTeX

如果你已经引入了 KaTeX，请跳过这一部分。

众所周知，Markdown 中输入数学公式靠的是 LaTeX，而 [KaTeX](https://katex.org/) 是一个轻量化的 LaTeX 公式渲染器。KaTeX 的本质就是一堆 js 和 CSS 文件，因此用 CDN 引入就好了。

在 `themes/<你的主题>/layouts/partials/head.html` 中加入这段代码即可：

```html
{{/* KaTeX */}}
<link rel="stylesheet" href="https://cdn.jsdmirror.com/npm/katex@0.16.11/dist/katex.min.css" />
<script defer src="https://cdn.jsdmirror.com/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdmirror.com/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"
  onload="renderMathInElement(document.body, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false
        });"></script>
```

这里的 CDN 可以替换，例如 jsDelivr 主站、Gcore jsDelivr 等。

## 设置 passthrough 插件

goldmark 有一个叫 passthrough 的插件，可以识别数学公式的定界符，使得多行公式的双斜杠免遭毒手。

在 `config.toml` 文件的 `markup` 下添加这段代码：

```toml
[markup.goldmark.extensions.passthrough]
      enable = true
      delimiters.block = [
        ["\\[", "\\]"],
        ["$$", "$$"]
      ]
      delimiters.inline = [
        ["\\(", "\\)"],
        ["$", "$"]
      ]
```

如果你使用的是 `config.yaml`，那么就添加：

```yaml
markup:
  goldmark:
    extensions:
      passthrough:
        delimiters:
          block:
          - - \[
            - \]
          - - $$
            - $$
          inline:
          - - \(
            - \)
          - - $
            - $
        enable: true

```

然后就可以正确进行渲染了~

## PS

1. Hugo 官方推荐的方案与这里有所不同，如果你希望能使用 front matter 来控制渲染与否，可以参考[这里](https://gohugo.io/content-management/mathematics/)。
2. 如果你有渲染物理/化学公式的需求，MathJax 会更好。KaTeX 需要再引入一些扩展包，我没那个需求，就不整了。

下面是一个物理公式的示例：

$$
d \mathord{ \buildrel{ \lower3pt \hbox{$ \scriptscriptstyle \rightharpoonup$}} \over B} = \frac{{{ \mu _0}}}{{4 \pi }} \frac{{Idl \times \mathord{ \buildrel{ \lower3pt \hbox{$ \scriptscriptstyle \rightharpoonup$}} \over r} }}{{{r^3}}} =  \frac{{{ \mu _0}}}{{4 \pi }} \frac{{Idl \sin \theta }}{{{r^2}}}
$$

下面是一个化学公式的示例：

$$
\ce{Zn^2+  <=>[+ 2OH-][+ 2H+]  $\underset{\text{amphoteres Hydroxid}}{\ce{Zn(OH)2 v}}$  <=>[+ 2OH-][+ 2H+]  $\underset{\text{Hydroxozikat}}{\ce{[Zn(OH)4]^2-}}$}
$$

其真实效果应该是：

![使用Obsidian进行的渲染](https://img.clnya.fun/IMG-20240220151045.webp)

3. 参考资料：[Hugo 数学公式支持 | Finley&#39;s Blog (f1nley.xyz)](https://blog.f1nley.xyz/post/hugo-math-support/)
