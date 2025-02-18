---
slug: hello-searxng
datetime: 2024-08-16 17:05
summary: 闲着没事搭个搜索引擎
tags:
  - hello
  - 折腾
cover_image_url: https://s2.loli.net/2024/08/16/8akNej5qu93fSRm.webp
title: Hello，SearXNG
date: 2024-08-16
description: 本文讨论如何在内地服务器上使用 1Panel 和 OpenResty 搭建开源的 SearXNG 私有搜索引擎。SearXNG 是一个元搜索引擎，不收集用户数据，并支持本地偏好设置。只需一台服务器、代理和基本配置，便可顺利部署。一些设置包括修改访问密钥、环境变量和代理配置，最终可以将其设置为默认搜索引擎。总体来说，SearXNG 速度可接受，但搜索结果有时不够精准，建议与 DuckDuckGo 搭配使用。
categories: ["逍遥游"]
featuredImage: https://img.clnya.fun/hello-searxng-cover.webp
draft: false
share: true
---

各位老友们好，我是 Chlorine。今天继续水文。

其实本期正确的标题应该是：

《如何基于 1Panel 和 OpenResty 在内地服务器上搭建开源私有化的搜索引擎》

这样或许对 SEO 好点，但是小氯对于这件事一向是摆烂（~~你对什么事情不摆烂啊喂~~），所以直接加入 hello 宇宙就好了。

## 前言

众所周知，全球的搜索引擎巨头们都对用户隐私有着非常高的尊重，从不收集你的历史记录、搜索记录、位置、时间、联系信息、联系人、使用数据、财务信息、健康状况、诊断信息、购买项目、设备标识符、敏感信息等你不希望它们收集的东西，也不会使用你的数据去分析你的偏好或者产出内容农场。同时它们对于广告也有着非常好的管控，每一次的搜索结果都不会含有任何广告，尤其是在中国大陆拥有最大影响力的百度，确保了你良好的搜索体验。而且它们也尊重竞争对手的权利，不会对竞争对手的搜索结果 SEO 做任何的打压。这种负责任的做法获得了全球计算机爱好者和广大用户的一致好评。好的，请还在笑的老友收一收，茶都洒到衣服上了。

在隐私保护方面，可能也就是 DuckDuckGo 能做得好点。不过 DuckDuckGo 在大陆地区因为某些原因访问并不顺畅，而且这毕竟还是把数据交给第三方，肯定会有老友感觉不大舒服的。

不过没关系，小氯曾经说：开源社区是万能的。如果所有搜索引擎的巨头都做不好这一点，那么我们自托管一个开源的就好了。那么，有请今天的主角——SearXNG。

## SearXNG

我不大清楚 SearXNG 的名字是怎么来的，可能和 SearX 有关。

[SearXNG](https://docs.searxng.org) 是一个用 Python 写的**元搜索引擎**。That is，它自己并不提供搜索引擎的职能，而是通过分析和综合各大搜索引擎的结果来进行高效的查找（当然，用我们的小服务器去爬整个互联网也是不现实的）。SearXNG 不收集任何用户数据，一切的偏好全部以 Cookie 的形式存在于本地，同时采用各种方式来避免任何在搜索过程中暴露个人信息的行为。

如果各位老友没有条件自部署，也可以去 [https://searx.space](https://searx.space) 找几个已经部署好的实例尝尝鲜。

## 前置说明

请注意，如果您的已有条件和需求不满足下面所述，那小氯推荐您还是先别看文章了，还是先去紫荆公寓的公共空间喝杯茶更能体现对您生命的尊重。

条件：

- 一台自己的服务器
- 一个能够顺利访问世界互联网的 endpoint
- 一台电脑
- 手，脑子

需求：

- 希望部署一个私有化的搜索引擎
- 不希望使用 SearXNG 原生的 Caddy 作为反代（本文使用 1Panel 面板和 OpenResty，其他反代服务器应该可以类推，但是这需要您自己来做）

好的，我们开始。

## 拉取 Git 仓库

> [!TIP]
> 如果您有能够可视化上传的面板的话，在本地编辑也没问题。我就是这么干的。

首先随便选个目录，比如 `/usr/local`。按理说在哪应该都无所谓，但是我推荐就在这里，防止出现什么奇奇怪怪的问题。

官方的仓库有点问题，小氯给大家准备了一个修复版的，具体改动是：

- 删除了 Caddy 相关配置
- 创建了 `uwsgi.ini` 以避免 `# cp: can't create '/etc/searxng/uwsgi.ini': Permission denied` 报错（官方居然把这个文件加到 `.gitignore` 了，难绷）
- 直接增加了出站代理设置
- 默认关闭 limiter 限制（个人实例一般不用，如果希望打开，修改 `settings.yml` 的 `limiter` 键为 `true`）

```bash
cd /usr/local # 或者你的目录
git clone https://github.com/chlorine3545/searxng-docker-fixed.git
```

如果访问不畅，可以使用 SSH 或者是我准备的国内镜像：

```bash
cd /usr/local
git clone https://gitee.com/chlorine3545/searxng-docker-fixed.git
```

完事之后，用你喜欢的编辑器打开仓库，进行一点小小的编辑。

### 设置访问密钥

执行命令：

```bash
sed -i "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml
```

如果出现报错就试一试：

```bash
sed -i"" -e "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml
```

Windows 用户可以使用（官方的，我没试过）：

```ps
$randomBytes = New-Object byte[] 32
(New-Object Security.Cryptography.RNGCryptoServiceProvider).GetBytes($randomBytes)
$secretKey = -join ($randomBytes | ForEach-Object { "{0:x2}" -f $_ })
(Get-Content searxng/settings.yml) -replace 'ultrasecretkey', $secretKey | Set-Content searxng/settings.yml
```

然后打开 `settings.yml`，如果发现原本的 `ultrasecretkey` 变成了一串乱七八糟的字符，那么就成功了。

### 编辑环境变量

编辑 `.env` 文件，将 `# SEARXNG_HOSTNAME=<host` 那一行取消注释，`<host` 改为你希望绑定的域名。不需要带 HTTP 或者 HTTPS。

### 修改 `docker-compose.yml`

找到第 32 行，就是我写注释的那个位置。把左边的端口改成你喜欢的。

### 增加代理

由于某些原因，境内服务器能访问的搜索引擎比较有限。为了让我们的信息获取渠道更加多样，我们需要配置一下代理。别问我哪来的代理，问就是光荣而伟大的孙哥。

在 `settings.yml` 中的第 32 行，把两个 `http://ip:port` 改成你的 endpoint 即可。

这里我照抄了官方配置，更多信息请参考这里。

## 启！动！

编辑完文件后，就可以开始启动了。

在目录下以 `sudo` 模式执行：

```bash
docker-compose up -d
```

等待部署完成即可。友情提示，如果有代理推荐打开，可以避免一些问题，但是一般没事。

完成后打开你的部署地址，如果看到：

![|566](https://img.clnya.fun/IMG-20240816105021.avif)

恭喜你，部署成功。现在试着搜索一下吧。可以在首选项那里进行各种配置。

不过有点难绷的一点是，我搜索我自己的站点没有任何结果，但是在 Google、Bing 和 DuckDuckGo 上页面的权重都是第一。而且我使用别的 SearXNG 实例搜索，结果是不一样的。我很难理解这一点。

## 设置反代

略。

## 设置密码

我们部署的是私人实例，为了防止被一些 unwanted visitor 使用，我们可以使用一个密码来进行保护。当然，不开也行。只要你不分享你的域名，同时禁止掉爬虫，基本上只可能通过 DNS 扫描来扫出来有这么个域名（还无法知道这个域名是干什么的）。

在 1Panel 上设置密码相当容易，在网站-网站设置-密码访问中设置就可以。

## 设置默认搜索引擎

这么好的引擎，不用起来怎么能行。这里我只讲 Arc（Chrome 系，比如 Chrome、Edge 等基本同理）和 LibreWolf（Firefox 系基本同理）的方法。

### Arc

在地址栏键入 `arc://settings` 进入设置界面，点击「搜索引擎」选项卡。滑到「网站搜索」，按如下格式填写：

![](https://img.clnya.fun/IMG-20240816105428.avif)

添加后右面三个点，选择设为默认即可。

### LibreWolf

快捷键 `⌘ + ,` 进入设置界面，在搜索选项卡配置。方法与 Arc 基本一样。

小氯温馨提示：这种注重隐私的搜索引擎，和 LibreWolf 这种注重隐私的浏览器更配哦。

## 总结

总体而言 SearXNG 还是相当不错的，我目前已经将它设置为全平台通用的默认引擎了。

大体响应速度是 2-3s，还算可以接受。不过感觉有时候结果不是很准，所以我现在把它和 DuckDuckGo 混用。

再次感谢伟大的开源社区。祝各位老友互联网之旅愉快。
