---
slug: hello-sink
datetime: 2024-07-29 22:06
summary: 我也不大知道这个有什么用，但是我认为它有用
tags:
  - CloudFlare
cover_image_url: https://img.clnya.fun/hello-sink-cover.webp
title: Hello，Sink
date: 2024-07-29
description: 本文介绍了 Sink 项目的部署过程。Sink 是一个基于 CloudFlare 的短链接项目，支持数据分析和链接截止日期等功能。本文详细介绍了使用 CloudFlare 部署 Sink 的过程。
categories: ["逍遥游"]
featuredImage: https://img.clnya.fun/hello-sink-cover.webp
draft: false
share: true
---
各位老友们好，我是 Chlorine。

最近在重拾 TypeScript（~~小氯你到底还要开多少个语言的坑啊~~），同时热衷于薅带善人 CloudFlare 的羊毛，于是盯上了 CloudFlare Workers&Pages，然后找到了一个有趣的项目：[Sink](https://sink.cool)。

## 简介

Sink 是一个完全基于 CloudFlare 的短链接（shortURL）项目，支持数据分析和链接截止日期等多种功能。

啥是短链接？简单来说，如果你觉得小氯的文章[解决Swup导致的JavaScript加载失效问题](https://www.yoghurtlee.com/swup-modifying)写得不错（~~行了我知道你并不这么觉得~~），希望分享给朋友，你很可能会把这个链接直接粘贴给你的朋友：

```txt
https://www.yoghurtlee.com/swup-modifying
```

看着还行，不是吗？但是假如小氯的链接是：

```txt
https://ameaninglessprefix.averylongurlforyoghurtlee.ameaninglesstldthatdoesntevenexist/ameaninglessdirthatstandsformyposts/anothermeaninglessprefix/2024/07/26/qwertyuiopasdfghjklzxcvbnm1234567890/swup-modifying
```

我敢打赌你的朋友看到这个链接就会汗流浃背。

但是如果现在你贴心地告诉朋友，这个链接也是一样的：

```txt
https://s.clmoe.top/fmf94q
```

我相信你们之间的友谊会得到相当程度的强化。

概括一下，就是说有时候一个链接实在是太长了，不便于分享和发送，我们就想办法造出一个短链接来，使得这个短链接指向原本长链接一样的位置。

市面上的短链接服务有很多，Sink 是其中能自部署的服务中比较出色的一个。

## What do I need?

- 一个 CloudFlare 账户
- 一个托管在 CloudFlare 的域名，短点最好
- 一个 GitHub 账户
- 一台能顺畅访问互联网的设备
- 手，脑子

## 准备工作

### 获取 CloudFlare Account ID

在 CloudFlare 仪表板中随便点击一个域名，进入概览页面，向下滑，在 API 一栏中就能看到【账户 ID】了。

![|426](https://img.clnya.fun/202407292145948.avif)

### 创建 CloudFlare Account API

在仪表板的右上角点击账户图标-我的个人资料-API 令牌，然后点击创建 API 令牌。

滑动到最下方，选择【创建自定义令牌】，配置如下所示：

![|584](https://img.clnya.fun/IMG-20240729215335.avif)

### 创建 CloudFlare KV

在侧边栏-Workers 和 Pages-KV 创建即可，名字随便起。

## 启动！

首先进入 GitHub，fork [这个仓库](https://github.com/ccbikai/sink)（别忘记给作者点 star~）。然后进入 CloudFlare，在侧边栏点击【Workers 和 Pages】，新建一个 page，选择【通过导入现有 Git 存储库创建】（如果还没绑定 CloudFlare Pages APP 到 GitHub，按要求操作即可），仓库选择刚刚克隆的仓库。

进入配置界面，项目名称随便起，框架预设选择 `Nuxt.js`，然后点击【环境变量（高级）】，增加如下几个环境变量：

- `NUXT_SITE_TOKEN`：这个随便起，但是**长度需要超过 8，且不能是纯数字**！
- `NUXT_CF_ACCOUNT_ID`：你的账户 ID
- `NUXT_CF_API_TOKEN`：你的 API token

然后点击部署，随即取消（~~CloudFlare：你是真的苟~~）。进入项目管理界面-设置-函数，添加以下的绑定：

- KV：键就是 `KV`，值是你刚才的 KV namespace。
- Workers AI（Optional）：键为 `AI`，值会自动给你生成为 `Workers AI Catalog`。
- Analytics Engine：键为 `ANALYTICS` ，值为 `sink`（需要启动 CloudFlare 分析引擎，照做即可）。

> [!IMPORTANT]
> 注意这几个绑定的【生产】和【预览】选项卡是不同步的，需要分别创建！

然后重新部署即可。

## 绑定自定义域名

这个是可选的，但是 CloudFlare Pages 的域名很容易访问不畅，而且也太长了，违背了 short 的初衷。

绑定域名的步骤略过。剩下的时间，各位老友自由发挥吧。
