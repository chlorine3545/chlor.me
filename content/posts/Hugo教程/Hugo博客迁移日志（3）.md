---
title: Hugo博客迁移日志（3）
date: 2024-06-30
summary: 真·迁移日志（2）
description: 作者对于从NotionNext迁移到Hugo的具体过程的简要叙述，包含GitHub、GitLab、Codeberg短代码的构建与Callout块的处理。
categories: 百草园
tags:
  - 博客
  - Hugo
  - 浮光
  - 折腾
slug: migrating-to-hugo-3
featuredImage: https://img.clnya.fun/migrating-to-hugo-3-cover.webp
draft: false
share: true
---
芜湖，各位老友们好啊，我是 Chlorine。接着上一回，继续为您说。

## GitHub/GitLab/Codeberg 短代码

Blowfish 有一个很好的短代码，就是 GitHub/GitLab/Codeberg 项目卡片。本着拿来主义的原则，直接拿过来。

Blowfish 的短代码需要使用 icon 短代码和 SVG 图标，但是我表示根本不需要。用 carbon icons 就可以。

大手一挥改完，然后加载本地服务器……

不是，我图标呢？！

连夜查了一下，中间也不知道怎么改的，反正折腾了半天，可算是搞出来了。

然后……怎么 403 了？

再去查。哦，这个短代码用的 GitHub API 获取信息，而匿名的 API 有调用限制。所以如果有高频的调用需求，可能需要去 GitHub 申请个 API，反正不花钱。

最终效果如下：

{{< github repo="kkbt0/Hugo-Landscape" >}}

GitLab 和 Codeberg 也差不多。

## Callout 块

Callout 块是一个很难办的事情。

其实如果不考虑使用的便利性，最好的办法就是使用 Shortcode。甚至 GitHub 上已经有现成的 notice 短代码了。

但是，作为强迫症的我，希望能够直接使用 GitHub 风格（Obsidian 风格）的语法进行书写，也就是：

```md
> [!Callout-type]
> Content
```

去给 Hugo 官方提了 issue，但是官方表示，他们感觉这并不是一个好的实现，推荐我使用这样的语法，然后写 Markdown render hook：

```txt
callout {level="warning" }
This is a warning.
```

……行吧。

那我还不如写 shortcode 呢！

于是我决定，使用 shortcode 加上 GitHub publisher 的正则替换。很可惜，由于我不会写正则，还是得用 shortcode 的原始语法，就很难评。

下面是一个例子：

> [!TIP]
> 这是一段 Callout。