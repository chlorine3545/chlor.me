---
title: Hugo博客迁移日志（1）
date: 2024-06-29
summary: 关于为什么又双叒叕搬家的一些狡辩（划掉）解释
description: 本文介绍了作者关于从 NotionNext 再一次迁移到 Hugo 的一些原因的叙述，主要原因是喜欢 Hugo Landscape 主题的外观和构建速度。
categories: ["百草园"]
series: Hugo博客迁移日志
tags:
  - 博客
  - Hugo
  - Efímero
  - 折腾
featuredImage: https://img.clnya.fun/cover/migrating-to-hugo-1-cover.webp
draft: false
share: true
slug: migrating-to-hugo-1
---
芜湖，各位老友们好，我是 Chlorine。几天不见，我又回来水文章了。

本期开一个新坑，主要讲我从 NotionNext 又回到 Hugo 的原因。

## 前言——从 Fuwari 讲起

行吧，我也不废话了，就是因为颜值。

NotionNext 当然好看，尤其是 Hexo 和 Heo 主题。但是，有一天我在 GitHub 上闲逛的时候，偶然发现了这个框架：

{{< github repo="saicaca/fuwari" >}}

当时我的反应就是：**惊为天人**。

这世界上怎么会有这么丝滑的博客框架啊！

于是我可耻地动心了。不过可惜，Fuwari 基于 Astro，但是我对 Astro 一窍不通。于是我就没继续，转而继续折腾我的 Hugo Blowfish。

可就在我的 Blowfish 即将大功告成之际，我发现，[恐咖兵糖](https://www.ftls.xyz/)大佬居然已经写了一个类 Fuwari 的 Hugo 主题，名为 Landscape。

{{< github repo="kkbt0/Hugo-Landscape" >}}

好的，我是小丑。

但是 Blowfish 折腾了这么久，扔是不可能的。于是，我开启了漫长的魔改之路。最终兜兜转转，可算是有了个雏形。由于自我感觉添加了不少元素，因此厚颜无耻地将之作为了一个新的主题，取名 Efímero，中文名「浮光」。

总体而言，浮光不算一个很沉的主题，构建时间大概十几秒。虽说比不过 Virgo 的不超过 10s，但是比 NotionNext 的将近一分半还是强多了。

本篇比较短，主要是讲一讲前言。明天在高铁上更具体经过（的第一篇）。
