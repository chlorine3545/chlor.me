---
title: Markdown 图片管理实践
date: 2024-03-14T11:01:25+08:00
categories: 百草园
tags:
  - 博客
  - 折腾
slug: markdown-pic-management
showTableOfContents: true
summary: 很长的一篇废话，各位慢慢看
description: 本文介绍了Markdown图片管理的实用技巧，包括在本地Markdown编辑器中使用图片的方法、图床的选择与配置，以及如何通过工具如PicList进行高效管理。作者比较了本地存储与在线图床的优劣，推荐了Obsidian插件和Squoosh等工具，并分享了对各大图床服务的评测，为Markdown用户提供了全面的图片管理解决方案。
---
各位老友们好，我是 Chlorine。

本期想谈一谈我心目中，本地 Markdown 编辑器/笔记软件（Obsidian/Typora/思源笔记/……）的图片管理实践。本文超长且杂乱，请备好茶和早餐饼干，慢慢看。

更新：本文在粘贴的时候发生了大量格式错误，我已经尽可能修正。

## 前言：Markdown 中的图片是什么样的？

> Markdown 是一种轻量级标记语言，创始人为约翰·格鲁伯。它允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的 XHTML（或者 HTML）文档。这种语言吸收了很多在电子邮件中已有的纯文本标记的特性。
>
> ——Wikipedia

如各位所见，Markdown 的本质是纯文本文件，只是因为有 Markdown 渲染器才有了我们看到的斜体、粗体等效果。

那 Markdown 的图片是怎么显示的呢？事实上，Markdown 的图片是依靠链接的形式显示的，其格式为 `![<替代文本>](<图片链接> <图片标题（optional>)` 。其中的感叹号代表需要显示其内容。

在 Obsidian 中，我们也可以使用 wiki 双链 `![[<图片链接>|<图片宽度（optional）>]]` 进行图片引用，不过这并不是 Markdown 的标准语法。[^1]Obsidian 提供了使用 Markdown 标准链接的选项（尽管使用起来不如 wiki 链接方便），也有插件可以将 wiki 链接和标准链接互转。

图片可以放在本地，使用文件路径（可以是最短路径，相对路径和绝对路径）进行引用，也可以放在图床上，使用图床链接进行引用。图床（Image Hosting Service，IHS）就是一个能存储图片的服务器。与一般的服务器不同, 它允许将图片以 URL 链接的形式插入文章并展示图片内容。

## 郑重声明

1. 由于 Markdown 图片管理是个经久不衰的问题，因此网上的教程也极为丰富。所以，一些已经有详细教程的实践，例如阿里云 OSS/腾讯云 COS/GitHub 图床/SMMS/……的注册以及密钥获取、PicGo/PicList 等的配置我会一笔带过，大家可以自行搜索相关教程。例如，你可以搜索“PicGo+OSS“等。
2. 以下内容较（ji）为（hu）简（mei）略（you）：其他在线图床的配置；MinIO 等本地图床的配置；自建服务器图床……
3. 本文含有大量项目，对于未经测试的项目，我已经明确标出；对于经过测试的项目，我会给出成功时的测试环境。无论测试与否，本人不对文中提到的任何项目的任何特性负责。
4. 本文含有大量链接，如无特殊说明，链接均摘自作者获取的第一级信息，但作者不对链接的内容和安全性负责。
5. 本文为作者原创，若您认为本文含有侵犯您权益的内容，请立即联系我。

## 省流

- 上手容易程度：本地 `file` 协议 > 本地附件文件夹 ≈ 在线图床 >> 本地 `http` 协议图床 > 服务器自建图床
- 隐私保护程度：本地 `file` 协议 = 本地附件文件夹 > 本地 `http` 协议图床 = 服务器自建图床 >> 在线图床
- 多平台同步/分享便捷程度：在线图床 ≥  服务器自建图床 ≥ 本地 `http` 协议图床 >> 本地 `file` 协议 = 本地附件文件夹

最推荐的方案：

- 本地附件文件夹：Attachment Management + Image Converter
- 本地图床：Image Auto Upload + PicList + File 协议
- 在线图床：Image Auto Upload + PicList + 缤纷云/CloudFlare R2/大厂对象存储
- 局域网图床/自建服务器图床：前面的区域，以后再来探索吧！

## 推荐工具

### PicList

图床管理工具有很多，例如著名的 PicGo，再比如 uPic，iPic 和 PicList 等，这里我们选择 PicList。

PicList 是基于著名图床管理工具 PicGo 的二次开发版本，兼容 PicGo 的特性，同时加入了 AWS S3，兰空图床，本地图床，WebDAV 和 Telegraph 等多种新的内置图床类型以及多种功能，支持在 Windows，macOS 和 Linux 上运行，是一款非常优秀的开源图床管理工具。

上面的介绍……好官方啊（笑）。

[这里](https://piclist.cn/)是 PicList 的官方网站。可以在 GitHub release 或者官方的直链中下载。

对于大部分图床，PicList 的配置方法和 PicGo 基本上是一样的。

### Typora 配置

在 Typora 的设置中，找到 `图像-插入图片时…`，选择“上传图片”；上传服务设定选择自己的图床管理软件即可。选择之后可以进行验证（左下角按钮）。

目前支持 PicGo（app/命令行），PicList，Picsee，iPic，uPic 和自定义命令。

*PS：如果配置完成显示验证失败，可以直接贴张图上去，很可能已经能成功上传了。*

### Obsidian 相应插件

对于访问 GitHub 有困难的老友，可以前往 PKMer 进行下载： https://pkmer.cn/products/plugin/pluginMarket/

#### Image Auto Upload

GitHub 仓库地址： https://github.com/renmu123/obsidian-image-auto-upload-plugin

在 Obsidian 图片管理界德隆望尊的插件，可以配合 PicGo 实现粘贴图片自动上传。

#### Image Upload Toolkit

GitHub 仓库地址： https://github.com/addozhang/obsidian-image-upload-toolkit

来自大佬 [Addo Zhang](https://atbug.com/) 的作品，可以一键将图片上传到图床，然后将上传后到全文复制到剪贴板，但是不改变原本的文章，对于希望在本地附件文件夹中存储图片，但是又有时不时的上传需求（例如：写博客）的老友来说可谓是福音。

大佬在[博客](https://atbug.com/obsidian-plugin-image-upload-toolkit/)中给出了详细的教程。我曾经在使用的时候发现几个 bug，在文章下面留言后，大佬很快就把问题修复了，不得不敬佩大佬的技术力和责任心。

遗憾的是目前仅仅支持 Imgur，阿里云 OSS 和 ImageKit（ImageKit 也是一家不错的对象存储服务，我在做霞鹜文楷 Lite 字体分包的时候曾经用过，可以配合 LightCDN 等免费服务使用，可以参考[这里](https://chinese-font.netlify.app/post/deploy_to_cdn/)）。

#### Attachment Uploader

GitHub 仓库地址： https://github.com/zhuxining/obsidian-attachment-uploader

这个插件和 Image Auto Upload 很接近，但是调用的是 uPic/Picsee。我没有正式测试过。

#### Image Converter

GitHub 仓库地址： https://github.com/xRyul/obsidian-image-converter

图片转换器，支持将图片转换为多种格式（同时也可以进行压缩），同时支持拖拽图片边缘进行大小调节（但是结果似乎无法保留）。

#### Paste Image Rename

GitHub 仓库地址： https://github.com/reorx/obsidian-paste-image-rename

粘贴图片重命名，支持自定义命名规则。如果你使用图床，可以在 PicList 上配置命名规则，省一个插件。

#### Attachment Management

GitHub 仓库地址： https://github.com/trganda/obsidian-attachment-management

附件管理器，可以在指定的附件文件夹下建立与原本的文件层级完全相同的附件文件夹结构，有利于对某个文章图片的集中管理。支持全库图片转移。

#### Attachment Manager

GitHub 仓库地址： https://github.com/chenfeicqq/obsidian-attachment-manager

同样是附件管理器，但是其会在每个文章的同级建立隐藏文件夹，不过这个插件和 Image Converter 似乎有冲突。

#### 其他

包括一键下载的 Local Images Plus，提升图像交互体验的 Image Toolkit，支持滚动调节图片大小的 Mousewheel Image Zoom 等。

### Squoosh

官网： https://squoosh.app/

GitHub 仓库地址： https://github.com/GoogleChromeLabs/squoosh

来自 Google 的开源神作，在图片压缩领域冠绝群雄。

国内可用，完全免费，压缩极快，支持多种输出格式，支持参数调节。唯一的缺点是不能批量压缩，不过可以下载 Squoosh CLI 进行批量处理（请自行搜索教程）。此外有大神用 Electron 写了 GUI 版本，[参考这里](https://www.imoolee.com/electron-da-bao-squoosh-lib/)。我没有测试过，无法评价。

## 这是一个过渡

> 图乌片，启一动！

## 附件文件夹存储

这应该是最简单的方法之一了。优点是省心，而且文件都在本地，离线可用，绝对安全；缺点也非常明显，迁移性极差。Obsidian 的文件，扔到 Typora 就用不了了，多设备同步和分享更是白扯，除非你能在另一个设备建立一模一样的文件结构。

以下是一些推荐的实践。

### 图片压缩和 `.webp` 格式

对于大部分人来说，图片的清晰度其实没必要很高。比如我的图片大部分是代码的运行时截图，这种图片只要不糊成马赛克就能接受，既然如此，为什么不省点地方呢？

常见的图片压缩网站包括 TinyPNG 等，当然我最推荐的还是上面说的 Squoosh。此外可以在 Image Converter 插件中设置压缩，尽管不如 Squoosh 压得那么出色，但是也及格，而且更方便，可以像以前一样直接粘贴无感压缩。

此外，对于像我这样的 ~~强迫症~~ 追求图片大小和性能的人，传统的 `.jpg`和 `.png`已经无法满足需求了，我们需要使用 `.webp`格式。

 搬运 Wiki：

> WebP（发音：weppy）是一种同时提供了有损压缩与无损压缩（可逆压缩）的图片文件格式。
> ……
> WebP 的设计目标是在减少文件大小的同时，达到和 JPG、PNG、GIF 格式相同的图片质量，并希望借此能够减少图片档在网络上的发送时间。

关于 `.webp` 图片的具体原理我们不需要知道 ~~(实际上是我不知道)~~，只需要知道 `.webp` 的图片比较小而且在网站上加载起来比较快就好了。

Squoosh 和 Image Converter 都支持输出 `.webp`格式。

### 图片管理

图片管理可以使用上面提到的 Attachment Management 和 Attachment Manager，看你习惯哪种方式了。如果你在使用 Obsidian 的同时使用 Typora，那么我建议使用 Attachment Manager，同时将图片存储位置改为与 Typora 风格一致的 `./${filename}.assets`。

如果你的图片实在是太复杂，也可以使用 Billfish 和 Eagle 这类专业的媒体资源管理器。

### 图片重命名

Paste Image Rename 支持复杂的重命名规则，同时 Attachment Management 和 Image Converter 都支持一些方式的重命名。下面是一些推荐的命名方式：

- 时间戳
- MD5 Hash 值
- 文档名 + 时间戳
- 文档名 + 序号
- ImageNameKey + 序号（ImageNameKey 是 Paste Image Rename 的一个选项，在文章的 YAML Front Matter——也就是 Obsidian 的属性中使用。可以配合 Quickadd 的模板功能实现时间戳等 ImageNameKey）

### 相对路径

大部分 Markdown 编辑器对于相对路径等支持都比较良好，因此推荐在 Obsidian 和 Typora 中将相对路径打开，方便多软件打开和迁移。

## 在线图床

在线图床，就是将图片上传到提供图床服务等厂家处，在本地保留返回的链接。优点是不用费劲管理图片，省地方，而且同步和分享非常方便；缺点是离线不可用（Obsidian 似乎会有一份本地缓存），依赖于第三方服务（有跑路风险，有的要收费，有的速度不行，而且都可以说毫无隐私可言）。

我在我的博客中曾经简单提到过图床的搭建流程，这里仅仅是补充一些 ~~废话~~。

### 图床推荐

为了看起来方便，我就不列表格了。

#### 大厂对象存储（阿里云 OSS、腾讯云 COS、华为云 OBS 等）

- 官网
  - 阿里云： https://www.aliyun.com/product/oss
  - 腾讯云： https://cloud.tencent.com/product/cos
  - 华为云： https://www.huaweicloud.com/intl/zh-cn/product/obs.html
  - 百度云： https://cloud.baidu.com/product/bos.html
- 价格：没有（通常意义上的）免费额度，但是一般有试用包；计费规则极其复杂，包括存储费用、外网流入、外网流出、CDN 回流等。一般来说，存储的费用极低，但是流量（主要是流出流量）较贵，具体可以参考官方文档。
- 稳定性：估计你敲不动代码了它们还是活得好好的。
- 速度：国内速度良好，国外如果套 CDN 应该可以，没试过。
- 优点
  - 稳定性好
  - 国内访问快
- 缺点
  - 计费规则极其复杂
  - 要收费，不能 100%白嫖
- 推荐指数：4.5

2024-03-18 更新：目前又发现了网易数帆 NOS，似乎也有很高的免费额度，大家可以自行了解，我就不折腾了（逃）。

#### 缤纷云对象存储

- 官网： https://www.bitiful.com/
- 价格
  - 免费额度（账户需实名认证，下面一堆直接摘自官方文档）
    - 前 50 GiB 存储
    - 每月前 30 GB HTTP/HTTPS 流量（每日每项限 5 GB）
      - S4 出口流量 10GB/月
      - 内置 CDN 回源 S4 流量 10GB/月
      - 内置 CDN 出口流量 10GB/月
    - 每月前 30 万次请求（每日每项限 1 万次）
      - S4 请求数 10 万次/月
      - 内置 CDN 回源 S4 请求数 10 万次/月
      - 内置 CDN 请求数 10 万次/月
  - 收费部分：费用不高，[请自行查阅官方文档](https://www.bitiful.com/docs/categories/%E8%AE%A1%E8%B4%B9%E8%AF%B4%E6%98%8E-1/)。
- 稳定性：应该不错。
- 速度：国内只有北京节点，个人测试的速度良好（如果有备案域名还可以免费套 CDN），国外未知。
- 优点
  - 免费额度比较充足
  - 国内访问快
  - 除了实名认证不需要额外条件
- 缺点
  - 知名度不如大厂高
  - CDN 和自定义域名要备案
- 推荐指数：4.5

#### 七牛云

- 官网： https://qiniu.com/
- 价格
  - 免费额度
    - 标准存储每月免费空间 10G
    - 标准存储每月免费 CDN 回源流量 10G
    - 标准存储每月免费写请求 PUT/DELETE 10 万次
    - 标准存储每月免费读请求 GET 100 万次
  - 收费部分：我打累了，自己看吧。[价格 | 对象存储 - 七牛云 (qiniu.com)](https://www.qiniu.com/prices/kodo)
- 稳定性：也算是个知名厂商，应该不错。
- 速度：国内速度良好。
- 优点
  - 可靠性较高
  - 有一定免费额度
- 缺点
  - 测试域名一个月就会过期，需要绑定已备案的域名。
- 推荐指数：3.5

#### 又拍云

- 官网： https://upyun.com/
- 价格
  - 免费额度
    - 新用户注册会赠送相当数额的代金劵，但是和七牛云一样，测试域名是有期限的。
    - 加入又拍云联盟：每年会发放代金券，相当于每月 10G 空间 + 15G 流量（由于是按年发放的，因此可以用一个月剩下的抵另一个月不足的）。
  - 收费部分：[这是又拍云的价格计算器](https://www.upyun.com/pricing)，不过我不太能说清楚，因为这主要是针对网站而非单纯的图床的。总体上价格和阿里云、腾讯云等相差不大。
- 稳定性：又拍云的对象存储和 CDN 在站长圈里相当有名，还是可以相信的。
- 速度：国内速度良好。
- 优点：和七牛云差不多。
- 缺点
  - 需要加入又拍云联盟（在网站底端放上又拍云的 Logo），需要备案域名和网站。
- 推荐指数：3.5

#### CloudFlare R2

- 官网： https://developers.cloudflare.com/r2/
- 价格
- 免费额度
  - 每月 10G 存储
  - 每月 1M 次 A 请求（写入）
  - 每月 10M 次 B 请求（读取）
  - 无限流量（是的，CloudFlare R2 没有流量费用，毕竟人家 CloudFlare 的节点遍布蓝星🤣）
  - 收费部分
    - 存储$0.015 / GB·月
    - A 请求$4.50 / 百万次
    - B 请求$0.36 / 百万次
- 稳定性：估计你敲不动代码了它还是活得好好的。
- 速度：国外没得说，国内出乎意料地还不错。
- 优点
  - 免费额度充足
  - 无流量费
  - 支持免备案自定义域名
  - 付费部分价格低廉
- 缺点
  - 需要绑定外币信用卡/PayPal（推荐注册一个 PayPal，极其简单）
  - 国内访问速度比国内对象存储稍逊一筹
- 推荐指数：4.5

---

总体而言，只要你的站点流量不是极大，图床的成本都不高，甚至可以使用免费额度实现零成本图床。综合来看，我个人最推荐的还是缤纷云和 CloudFlare R2。当然，如果你想用其他的我也不反对，见仁见智的问题。

我并不推荐那些公共免费图床，即使是已经运行多年的也一般不推荐（如果你执意要用的话，那我推荐 [SM.MS](https://smms.app/)）；同时我也不推荐使用 GitHub 仓库作为图床（虽然 GitHub 本身稳定性很好，但是有了 Gitee 图床的前车之鉴，谁知道以后会出什么事；此外 GitHub 图床的国内速度属实是一言难尽，就算是开了 jsDelivr 也是如此）；更不推荐用各种奇奇怪怪的方式薅大厂的产品（比如京东，微博，B 站）当图床。

此外，缤纷云和 CloudFlare R2 本质上还是兼容 Amazon S3 协议的对象存储，因此可以拿来干很多事，比如当网盘分享文件，作为 Obsidian remotely save 和思源 S3 同步的免费提供方等。

### 配置指南

#### SMMS

诶，不是说好不推荐免费公共图床了吗？

emmm，SMMS 的确是个很稳的公共图床，速度也还可以。估计有很多老友会想用，所以还是放一下吧 ~~（才不会告诉你们其实是想对我远古时期的文章进行废物利用）~~ 。

##### 注册 SM.MS 账号

登录 SM. MS [官网](https://sm.ms)或[备用域名](https://smms.app)，用邮箱进行注册即可。

##### 获取 SM.MS 的 token

首先我们在主页点击 user，选中 dashboard。

![](https://s2.loli.net/2023/10/04/bSp12tG3X9w8OZC.png)

~~这甚至都还是远古时期我用 SMMS 图床的图片~~

在 dashboard 中选择 API token，点击 generate token，生成一个专属的 token，复制好备用。

![](https://s2.loli.net/2023/10/04/1QbgvZu7fpnceqH.png)

##### 下载安装 PicList

这个没啥可说的。

##### 为 PicList 配置 SM. MS 的 token

在 PicList 页面里选择图床设置，进入 SM. MS 的配置。

![](https://s2.loli.net/2023/10/04/ySMNxhCzatG3wFs.png)

~~这不是远古时期 PicGo 的图片吗~~

##### 设置 PicList server

在 PicList 设置中选择 server，将配置改成这个样子：

![](https://qsol.yoghurtlee.com/IMG-20240313190240.webp)

##### 配置 Image Auto Upload

先把插件下载好，启用，然后把配置改成这个样子就可以了。

![](https://s2.loli.net/2023/10/04/EcONhMRKz8IJvgZ.png)

~~你就看这复古的 Obsidianite 主题就知道小氯这家伙就是在废文利用~~

#### 缤纷云

可以参考我的博客文章。

#### CloudFlare R2

##### 注册 PayPal 账户

想薅 CloudFlare 的羊毛，你首先需要有一个 PayPal 账户。当然，你有 Visa 卡一类的更好。

[这里](https://www.paypal.com/)是 PayPal 的官网，直接进去注册就完事，不需要双币卡。关于其中的注意事项，可以参考我的老友[嗣檙](https://sicheng.taoooist.org)的文章[浪花_注册paypal账号并正常付款使用](https://taoyifan.cn/#%E6%B5%AA%E8%8A%B1_%E6%B3%A8%E5%86%8Cpaypal%E8%B4%A6%E5%8F%B7%E5%B9%B6%E6%AD%A3%E5%B8%B8%E4%BB%98%E6%AC%BE%E4%BD%BF%E7%94%A8)。

*PS：不必担心，只要你的用量不超过免费额度，即使是绑定了账户也是不会扣费的。*

##### 注册 CloudFlare 账户

略，我相信大家都有。

##### 创建存储桶

在 CloudFlare 的 [dashboard](https://dash.cloudflare.com) 中选择 R2，进行 PayPal 账户绑定。

然后点击右上角的创建存储桶。

![](https://qsol.yoghurtlee.com/IMG-20240314115904.webp)

##### 公开访问，自定义域名和 CORS

简单来说，开启公开访问可以让你在 CloudFlare 之外的地址（包括本机）访问图片，自定义域名可以让你有一个自己的图床域名，CORS 策略可以让其他网站访问此处的资源。

![](https://qsol.yoghurtlee.com/IMG-20240313190421.webp)

##### Token 设置

在概览界面的右上角，点击“管理 R2 API 令牌”即可。权限选读写，限定在你创建的桶就好。各个平台 Token 的设置都是大同小异。

##### PicList 配置

CloudFlare R2 兼容 AWS S3 协议，就按下面的来就好。

![](https://qsol.yoghurtlee.com/IMG-20240314115815.webp)

##### 缓存策略（Optional）

这个对于博客图床比较有用，不过需要你配置自定义域名。

![](https://qsol.yoghurtlee.com/IMG-20240314110034.webp)

## 本地图床

这是我最近折腾出来的新玩意。简单来说，将一个本地文件夹作为图床，并且将文件夹使用某种协议向外暴露，使得 Markdown 编辑器能够进行读取。优点是既保留了本地的隐私性，又满足了不同 Markdown 编辑器之间的同步需求；缺点是只能本机访问，需要进行一定的配置才能转化为局域网可访问，要想转化为公开图床则需要很复杂的配置。

> 瘟锌锑逝
>
> 此处讨论的不是局域网图床。下面的配置仅限在本机使用，局域网图床的配置可以参考[这里](https://zhuanlan.zhihu.com/p/349707695)。
>
> 对于拥有 NAS 或者长时间开机的设备，并且有同步需求的老友来说，局域网图床是一个好选择。

### 使用 `file`协议

首先我们讲讲 file 协议。

我们在输入一个网站的完整地址的时候，总会加上一个 `http`或者 `https`。所谓的 http，其实是超文本传输协议（HyperText Transfer Protocol）的简写，其允许客户端（一般是浏览器）向服务器请求资源，是整个万维网传输信息的基础。而 https 就是 http secure，代表使用了 SSL/TLS 加密协议的 http，更为安全。

而 file 也是一种协议，不过它不是用于访问网络资源的，而是访问本地文件。例如，你用 Edge 或者 Chrome 打开一个 PDF，仔细看上面地址栏的路径，就是 file 协议下的绝对路径。

目前支持 file 协议的包括 Obsidian，思源笔记和 Typora 等编辑器/笔记软件。[^2]

配置 file 协议简单得惊人，整个配置可以在几分钟内搞定。

1. 找一个你喜欢的地方建个文件夹，例如我的是 `/Users/chlorine/Pictures/picbed`。
2. 打开 PicList，找到“本地上传”，配置如下。

![](https://qsol.yoghurtlee.com/IMG-20240314115714.webp)

测试一下，完事了。

这个方案实在是太简单了，简单到折腾了一天的本理性人都开始痛惜我的沉没成本。

> 瘟锌锑逝
>
> 1. Windows 上的默认文件路径分隔符是反斜杠，如果路径不对劲，可以同时试一下斜杠、反斜杠、双反斜杠。
> 2. 本方案无法局域网化。

### 使用 http 图床

除了使用 file 协议，我们还可以使用 http 协议，也就是把本机的一个端口暴露出来作为上传服务。

下面是几种方案，我没有一一尝试过，仅供参考。

#### 使用 My-Easy-Pic-Bed

[My-Easy-Pic-Bed](https://github.com/fslongjin/My-Easy-Pic-Bed) 是一个使用 Python 开发的轻量级图床程序，应该是下面这几个方案里面最轻量的了。

关于 Windows 上的使用可以参考[这篇教程](https://zhuanlan.zhihu.com/p/349707695)，我只讲 macOS 的几个注意事项。

##### 启动服务

在终端（推荐用 VS Code 打开项目文件夹，在内置终端中运行或者使用 Code Runner）中执行：

```bash
python -u app. py
```

然后就可以在 `http://127.0.0.1:<端口，在下面配置>`找到你的服务了，图片的路径是 `http://127.0.0.1/upload/<图片名>`。

##### 修改默认端口

由于原本的程序使用的是 80 端口，所以直接运行会被 Permission Denied。解决方案有两个：

1. 使用管理员权限（在命令前面加个 `sudo`），然后输入密码即可，输入过程不会显示，不必慌张。
2. 修改默认端口。

我们着重讲第二种。打开项目的 `config.ini`，将其中的 `port`参数修改为一个闲置的 **1024 以后的** 端口，例如我使用的是 8567。

##### 配置 PicList

PicList 内置了对本地图床的支持，配置和上面的 file 协议很像，把自定义域名改为 ` http://127.0.0.1/upload`就可以了 。

##### 添加支持格式

在 `app.py`的 13 行那个列表中添加扩展名即可。

```py
allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'} # 添加自己需要的格式
```

##### 修改命名规则

命名的代码位于 `app.py`的 35 行：

```py
if file and allowed_file (file. filename):
            filename = str (int (time.time ())) + str (random.randint (1, 99999)) + secure_filename (str (random.randint (1, 7887)) + file. filename)
```

提供几种命名的替代方案，如果需要其他的，可以自行搜索/询问 AI。

时间戳：

```py
# 需要包含一个模块
from datetime import datetime
# ……
if file and allowed_file (file. filename):
            filename = datetime.now (). strftime ('%Y%m%d %H%M%S') + os.path.splitext (file. filename)[1]
```

MD5（来自 GitHub Copilot）：

```py
import hashlib
# ……
if file and allowed_file (file. filename):
    file_bytes = file.read ()
    file_hash = hashlib.md5 (file_bytes). hexdigest ()
    extension = os.path.splitext (file. filename)[1]
    filename = file_hash + extension
```

不重命名（推荐，可以在 PicList 中配置命名规则）：

```python
if file and allowed_file (file. filename):
    filename = file. filename
```

##### 后台运行

可以在运行命令的时候加一个 `nohup`前缀。

##### 开机自启

这个需要配置 launchd，极其复杂，可以参考 [Mac OS 利用launchctl开机运行python程序 | Voezy](https://blog.voezy.com/cyber/MacOS-Launchctl-Scripts.html)。我自己没成功。

##### 私有域名

如果你不喜欢 `127.0.0.1` 这种方式，那么你可以稍做一点手脚，自娱自乐一个好看的域名。

简单来说，我们需要修改 `hosts` 文件——这是一个将主机名（域名）映射到 IP 地址的文件。`hosts` 文件在所有解析中具有最高效力，这样，我们就可以绕过 DNS 解析来进行 IP 和域名的对应。

为了避免使用烦人的 Vim 或者 Nano，我们使用 VS Code 进行编辑。

在 `/etc` 文件夹（位于 macOS 的根目录 Macintosh HD 中，使用 `command+shift+.` 以显示隐藏文件夹）中找到 `hosts` 文件，右键打开方式选择 VS Code。

打开之后你应该看到类似这样的内容：

```txt
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
255.255.255.255	broadcasthost
:: 1             localhost
```

在底端添加一行：

```txt
127.0.0.1	<你想要的域名>
```

注意，此处的域名可以是任何字符串，因为这个“域名”只会在本机进行解析，所以不符合规范也没问题。**但是，为了不出现奇奇怪怪的问题，最好不要使用现实世界中存在的域名。**

解释一下，我们前面说过，`hosts` 文件在所有解析中具有最高效力，如果我们将一个存在的域名映射到本机了，那你再访问这个域名，原本的 DNS 可就不作数了。举个例子，如果你将 ` www.baidu.com` 映射到本机，那你再在浏览器地址栏输入 ` www.baidu.com` ，访问的就是本机，不是百度了。所以说，最好使用一些不存在的域名，例如不存在的后缀，特别奇怪的前缀等。比如，可以使用 `chlorinechan.chem`（`小氯酱.化学`），因为 chem 这个后缀是不存在的。

这样，你就可以使用 `http://<你的私有域名>/upload/<图片名>` 进行访问啦～

##### 域名防火墙

如果你的局域网是较为开放的局域网（比如小氯使用的带清校园网）或者不可信任的局域网，那么推荐你打开域名防火墙。否则，局域网内的其他人只要知道你的 IP 地址就可以访问你的图床，这是非常危险的。

域名防火墙配置可以参考[这里](https://zhuanlan.zhihu.com/p/351973632)。

#### 使用兰空图床

[兰空图床](https://www.lsky.pro/)是一个著名的开源云端相册管理项目。你不仅可以将其作为单独的图床使用，还可以将多种图床整理进去，变成真正意义上的云端相册。具体内容可以参考其[官方文档](https://docs.lsky.pro/docs/free/v2/)。

但是：**兰空图床基于 PHP 和数据库，操作较为复杂，因此并不方便在本机部署。**

#### 使用 MinIO

[MinIO](https://min.io/) 是一个开源的对象存储服务，没错，就是对象存储。

[这里](https://min.io/docs/minio/kubernetes/upstream/index.html)是 MinIO 的官方文档，不过是全英的，比较难读。可以自行搜索一些教程。

我曾经测试过，在我的 MacBook 上，一个简单的 MinIO server 占的内存近 1G。而且其文件是以 `.meta`格式存储的。所以我没用这个。不过 MinIO 的界面真的很赞，有专业的对象存储的味道。

PicList 需要安装 MinIO 插件，其配置内容和一般的对象存储很像。

#### 其他方案

包括但不限于 http-server，EasyWebSvr 等，自己探索吧。

## 局域网图床和自建服务器图床

这个方案相当于将本地图床向外开放，可以在局域网范围内使用，也可以向公网开放，作为真正意义上的图床。

需要有服务器或者 NAS 一类的设备，其方案和上面的 http 本地图床基本相同。由于有专业的环境，部署兰空、MinIO 等项目会方便很多。当然，会有亿点折腾。

## 结语

花了好几天，终于把文章写完了。

本文长且杂乱，相比前人丰富的文章，似乎也没太多新的东西。不过这篇文章应该会持续更新或者打补丁，介绍我新的折腾结果。

**写到这里，我都快忘记，我为什么要写这篇文章了。**

[^1]: 这个说法是不严谨的，因为 **Markdown 并没有事实上的标准语法** 。目前比较通行的 Markdown 语法包括 GitHub-favored Markdown（GFM）和 CommonMark 等。
    
[^2]: 我目前使用的 Markdown 编辑器都是这三个，其他编辑器我大都没有亲身测试。目前已知 VS Code 明确不允许引用工作区之外的资源，RemNote 允许使用 file 协议（信息来源：[RemNote威廉笔记教学016之PDF批注建立知识树超越Marginnote（一）导入与卸载PDF - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/351229230)）。
