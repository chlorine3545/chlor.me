---
title: 理想乡构筑手记（3）：Hello，Nieve
date: 2025-02-21
slug: hello-nieve
featuredImage: https://img.clnya.fun/cover/hello-nieve-cover.webp
categories:
  - 百草园
tags:
  - 博客
  - 图床
  - Obsidian
series: 理想乡构筑手记
summary: 其实你一共也没有几张图片啊
description: 本文介绍了作者构建名为 Nieve 的图片服务系统的过程。由于原先使用的缤纷云图床出现加载问题，博主决定迁移至又拍云作为主图床，并以 Cloudflare R2 作为备份。迁移过程中，使用了 `rclone` 工具进行图片备份和上传。为了优化 Obsidian 中的写作体验，博主弃用了原先的 Image Converter 插件，转而利用 Shell Commands 插件调用自定义脚本。这些脚本实现了图片粘贴时的自动压缩（使用 `cavif`）、重命名、相对路径计算，以及发布文章时查找图片、上传至又拍云（使用官方工具 `upx`）并替换链接的功能。整个过程涉及了多种工具，包括 Python 脚本、AppleScript、`ripgrep` 等，最终构建了一个自动化、高效的图片处理与发布流程。
wikilinks: true
---

诸位老友，上午好，这里是 Chlorine。

本期是「理想乡构筑手记」的第三篇，实际也是最早进行的一篇，主题是园子的图片服务系统——Nieve。本来是想放到新的一期周报里面讲的（~~没想到吧，园子的周报还活着~~），但是这部分内容实在是太琐碎了，遂单题一篇。~~水，你接着水~~。

Nieve 这个名字，也是很久以前就想好的。这个词是西班牙语，意思是「雪」。

## TL ; DR

- 在 Obsidian 写作时粘贴图片前使用 Shell Commands 的自定义脚本压缩图片为 AVIF，并获取压缩后链接。
- 使用 Shell Commands 的另一个自定义脚本上传博客图片到又拍云和 Cloudflare R2
- 又拍云作为主图床，Cloudflare R2 作为对外的图片服务和备份图床

## 前言

作为 Vercel 上的静态博客，园子的图片当然使用的是图床。小氯使用的图床服务几经变易，从免费图床的良心之作 [SMMS](https://smms.app) 到牢巴（Alibaba）的阿里云 OSS，再到缤纷云，期间甚至还写了[[Markdown图片管理实践|一篇将近一万字的文章]]去讲 Markdown 图片管理（当然那篇文章其实挺水的）。缤纷云提供了相当慷慨的免费额度，具体来说是：

- 前 50 GiB 存储
- 每月前 10\*3 GB HTTP/HTTPS 流量（每日每项限 5 GB）
    - S4 出口流量 10GB/月
    - 内置 CDN 回源 S4 流量 10GB/月
    - 内置 CDN 出口流量 10GB/月
- 每月前 10\*3 万次请求（每日每项限 1 万次）
    - S4 请求数 10 万次/月
    - 内置 CDN 回源 S4 请求数 10 万次/月
    - 内置 CDN 请求数 10 万次/月

回来。小氯使用缤纷云已经有快一年了，总体而言速度和稳定性还算可以，有了备案之后还可以用他家的 CDN，可以省一些回源流量之类的（没错，速度其实没快多少）。当然，为了避免免费服务的传统艺能——跑路。小氯也把图片在赛博活佛 Cloudflare 的 R2 上存了一份。和国内的各大对象存储以及 Amazon S3 等同行相比，Cloudflare 的免费额度简直多得不像话，一个月有 10G 的免费空间，1M 次的 A 类操作（存储和删除等），10M 次的 B 类操作（读取等），无限流量。如果不在意国内速度慢一点，那么 Cloudflare R2 堪称是对象存储中的椎间盘——为何你如此突出。

插一句话，小氯写到这里的时候，习惯性地希望使用中文，然后发现自己似乎不知道 Cloudflare 的中文名字……等等，Cloudflare 有中文名字吗？

这个还真难说。Cloudflare 的官网在调为简中后，还是叫作 Cloudflare；而 `cloudflare-cn.com` 使用的是「科赋锐」（注意：小氯不清楚这个网站和 Cloudflare 官方是否有关，请谨慎），说实话，这个名字……真的让小氯很不满意，就和把 Google 翻译为「谷歌」一样。小氯还没有找到一个被 Cloudflare 官方认可的中文名字，但是从社区来看，似乎有一个不错的选择：**云帆**。

「云」对应 cloud，由于「云计算」「云存储」这些词汇的广泛使用，所以用这个词代表相关的技术领域没什么问题；而「帆」是 flare 的音译（其原意为火焰）。这个词整体读起来还比较顺口，而且寓意也很好，「直挂云帆济沧海」。不过如果在正式的技术讨论里面，还是用 Cloudflare 为好。

回来。不过最近（其实离文章发出来已经是几个月之前了），小氯接到了一些老友的反映，博客的图片加载明显变慢了，甚至很多裂掉了（即无法加载）。直接用 URL 看一下，发现 403。奇怪的是，小氯并没有为这种情况加任何的访问限制，而图片也都好好地在那。而当我希望将新的自定义 URL 添加到 CDN 中时，也是一直提示「未备案」（实际上 ICP 和公安备案已经过了快一个月了）。这可不是什么好兆头，说明缤纷云的后端设施可能出了一些问题。此外，小氯发现自己的流量似乎也出了点差错，其用量比实际应该有的流量高。而其分布也比较均匀，不像是攻击（~~而且谁闲着没事去攻击小氯酱这条杂鱼啊~~）。

总而言之，种种因素作用吧，小氯打算换个图片服务了。

## 图片服务的选择

市面上的图片服务——准确来说，能直接或者间接作为图片服务的服务不胜枚举。虽然说小氯不介意花点小钱，但是如果是像流量费这种很可能让人倾家荡产的服务，小氯还是希望尽可能避免的。于是小氯开始收集各种有免费额度的服务，当然这里指的是国内的。我没备案用的是国外的图片服务，备案了用得还是国外的图片服务，那我这不是白备案了嘛。

具体过程不多说了，极其曲折。小氯甚至想过用服务器 + 一些 CDN 搭一个，但一是没有合适的服务器，二是这种方式相当不稳定。举个例子：[杜老师](https://dusays.com)的[去不图床](https://7bu.top)，可以说是博友圈最著名的自建图床了（甚至没有之一），也时常会出现许多奇奇怪怪的问题，小氯可不认为自己的运维能力和服务器集群的质量比杜老师强。所以还是老老实实地找对象存储去了。

几番搜索，小氯找到了一个看起来还可以的选择。这个家伙大家也都不陌生：[又拍云](https://upyun.com)（这个链接不带 AFF，放心点击）。

牢拍也算是小有名气的商家了，跑路的风险不大，而且也没有大到像套路云、凉心云那样令人讨厌的规模。此外牢拍有一个著名的 League，简单来说就是在自己网站底下挂上牢拍的 logo 可以持续领到代金券，均摊一下也就是每个月 10G 的空间和 15G 的流量，基本上够用一段时间了。而且牢拍的代金券是和账户而不是域名挂钩的，这意味着你只需要找一个备案过的域名挂一下，然后就可以随便用了。

那么……就是你了。

## 使用 `rclone` 备份图片

在转移到牢拍之前，我们当然需要把整个图片目录备份下来。这里小氯打算试一下新玩具 [rclone](https://rclone.org)。

rsync 咱都知道，一个有趣的文件传输（这里说的是上传、下载和同步）工具。rsync 的花样很多，甚至可以用它部署静态博客到服务器（这可能是最好的方案之一，不需要装 Gitea 等一堆东西）。rclone 大体可以理解为云存储版的 rsync，支持一大堆各种各样的云存储和云盘。

```bash
brew update && brew install rclone
```

先创建一下配置：

```bash
rclone config
```

下一步输入 n，新建一个配置，选择 S3 - 其他，把 Access Key ID 和 Secret Key ID 之类的参数扔进去就行。

配置好以后，运行：

```bash
rclone ls your-service-name:your-bucket
```

如果能输出你的桶目录结构那就配置成功了，可以下载了：

```bash
rclone copy your-service-name:your-bucket /your/path
```

完工。

## 又拍云的配置

### 申请又拍云联盟

略。注册之后在[这里](https://www.upyun.com/league)申请即可。一般来说审核会有 1 ~ 3 天，小氯的用了大概二十分钟，相当快。

### 创建存储服务

和缤纷云不同的是，牢拍的云存储自带 CDN，所以只创建一个存储服务即可。

### 使用 `rclone` 重新上传图片

USS 兼容 S3，这就意味着我们可以用我们熟悉的各种小道具去把玩 USS。这里为了方便，我们还是使用 rclone 吧。这里小氯踩了点坑，因此说得详细一些。

首先我们需要获得 USS 的 S3 兼容凭据。这可不是你那个操作员的操作凭据，需要在存储服务的控制界面 - 存储管理里面找这里：

![upyun-uss-s3](https://img.clnya.fun/20250220-upyun-uss-s3.avif)

把东西记好喽。

回到终端，创建一个 rclone 配置：

```bash
rclone config
```

输入 n 新建配置，名字随便起，这里我使用 `test` 作为演示。

下面依次跟随指示，键入以下配置。这里的数字是以 `v1.69.0` 为基础的，在键入前，请检查你的版本的相应配置对应于哪个数字：

- `Storage`：4（Amazon S3 及其兼容服务）
- `provider`：34（其他 S3 兼容服务提供商）
- `env_auth`：直接回车，使用默认配置即可。
- `access_key_id`：你刚才获取的那个 `access_key_id`。
- `secret_access_key`：还是刚才那个。
- `region`：直接回车，使用默认配置即可。
- `endpoint`：`s3.api.upyun.com`
- `location_constraint`：直接回车，使用默认配置即可。
- `acl`：直接回车，使用默认配置即可。
- 高级设置：直接回车，使用默认配置即可。

最后保存后，使用 `rclone ls test:` 即可测试是否成功配置。

## Obsidian 配置

小氯在 Obsidian 的配置上花了很多的时间，终于找到了一个自己满意的方案。下面我把思路整理一下。

小氯的需求大概是：

- 图片重命名（语义化命名）
- 使用相对链接
- 自动压缩为 WebP 或者 AVIF
- 发布博客时上传到图床并替换博客文件的链接，而原本的文件保持不变

为了方便，我们就叫粘贴处理和发布处理好了。

### 粘贴处理

能实现一部分功能的 Obsidian 的图片插件有很多，例如 Paste Image Rename，Unique Attachments 等。不过小氯最喜欢的还是这个：

{{< github repo="xRyul/obsidian-image-converter" >}}

这个插件的功能非常全面，从压缩、格式转换、自定义附件位置到标注、裁剪、缩放、对齐都有。而作者也是位乐于听从社区意见的开发者，更新迭代和 Issue / PR 回复都很勤。小氯给这个插件提了个小小的 PR（改了一个拼写错误），混到了人生中第一个 Contributor 认证 (/ω＼)

不过插件的功能虽多，但是小氯主要是用其中的压缩和自定义附件位置，因此整体的功能也有些冗余了。而且，其会和我常用的 Attachflow 插件冲突。至于压缩问题，Image Converter 插件在 1.3.7 版本加入了 AVIF 压缩功能，不过有一个问题：**它异常耗内存**，经常转换着转换着就内存不足崩掉了（虽然说 FFmpeg AVIF 这玩意本来就吃资源）。虽然可以回退到 WebP，但是总归不是最优的解决方案。

那看来只有发挥主观能动性了。那么纵观 Obsidian 的插件，能让小氯在这个意义上发挥主观能动性的插件似乎只有一个：

{{< github repo="Taitava/obsidian-shellcommands" >}}

Obsidian Shell Commands，我愿称之为 Ob 可玩性的 Top3 之一（另外两个小氯认为是 Local REST API 和 Quickadd）。这个插件的功能就是让你在 Obsidian 中调用系统的 Shell 执行命令，支持自定义变量、预输入和自动触发等。说到这里，大家应该也能想象到这个插件的可玩性有多强了。

而且，小氯本身也要用 Shell Commands，既然我们能少装一个插件，那么「如非必要，勿增实体」，自然是极好的。

首先，由于小氯的图片使用的是相对路径，因此需要先获取图片相对于当前笔记的路径。笔记路径有 `{{file_path}}` 变量，图片由于是我们自己规定的，因此也不难获得。问题在于路径的计算。macOS 没有现成的命令行工具计算相对路径，于是小氯写了个 Python 脚本：

```python
#!/usr/bin/env python3

import os
import sys
import argparse


def get_relpath(base_dir, tar_file):
    try:
        relative_path = os.path.relpath(tar_file, base_dir)
        return relative_path
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description="计算 target 相对于 base 的相对路径")
    parser.add_argument("base", help="起始目录）")
    parser.add_argument("target", help="目标文件")
    args = parser.parse_args()

    base_dir = os.path.abspath(args.base)
    tar_file = os.path.abspath(args.target)

    if not os.path.isabs(base_dir) or not os.path.isabs(tar_file):
        print("Err: Please input absolute path.", file=sys.stderr)
        sys.exit(1)

    relative_path = get_relpath(base_dir, tar_file)

    if relative_path is not None:
        print(relative_path)
    else:
        print("Err: Please input correct path.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

```

然后赋予执行权限，移动到 `~/.local/bin` 了事。

下面我们需要读取剪贴板的图片，这里由于是 macOS，我们使用最原生的 AppleScript 即可。

```applescript
on run args
    set outputFile to POSIX file (first item of args)
    try
        write (the clipboard as «class PNGf») to outputFile
        return POSIX path of outputFile
    on error
        return "ERROR: 剪贴板中没有图片"
    end try
end run
```

然后把图片存储到临时文件 `TMPFILE="$(mktemp "/tmp/pasteboard-XXXXXX.jpg")"` 中。当然不要忘了加一个 trap 自动清理。

然后我们需要获取新图片的名字。为了满足小氯的需求，我们加一个 Preaction，让我们可以自己输入文件名。

![compress-preaction|520](https://img.clnya.fun/20250220-compress-preaction.avif)

然后我们就要开始压缩了。小氯第一个想到的自然是古神 FFmpeg，不过大家也知道，FFmpeg 尊者是出了名地脾气古怪，只要你稍微不慎，就会让他老人家掀桌不干。小氯反反复复调了好几次，遇到的问题包括但是不限于：

- 压缩极慢。
- 都把输出重定向到 `/dev/null` 了，还是莫名其妙地冒日志。
- 好不容易能压缩了，结果透明度数据没了，告诉我 libaom-av1 不支持 YUVA 编码。

……好好好。

那我不用 FFmpeg 还不行吗？！

```bash
rustup update
cargo install cavif
```

这玩意也不是不能用，而且比 FFmpeg 快多了。

压缩之后，我们就可以把图片移动到对应的附件文件夹，并且向剪贴板写入我们的相对路径链接了。小氯也尝试过把数据写入剪贴板，但是 macOS 似乎不直接支持写入 AVIF。

完整版的脚本放在[这里](https://gist.viento.cc/chlorine/e644da399d2d48c29bc9177622233ef6)了，大家按需取用。

### 发布处理

由于小氯的 Hermeneutics 支持 Wikilink 和 Alert，所以我们只需要上传图片并替换即可。这里我们还是写脚本解决问题。

这个脚本比较简单，使用 ripgrep 查找图片，再通过文件的路径构建出图片路径，然后一个循环把图片送上去即可。小氯用了 Cloudflare R2 测试成功后就放心地把脚本归档了。直到小氯写[[理想乡构筑手记（2）：Hello，Céfiro|上一篇文章]]，希望调用脚本上传图片时，才发现：

> 你根本没在又拍云！你在哪呢？ 

图片并没有被上传到又拍云。于是，小氯开始了兵荒马乱的排查过程，最终在单独测试 `rclone copyto` 时发现了一大堆奇奇怪怪的报错，不是超时就是缺少 Key 或者各种万泉部诗人的奇怪报错。这可能是因为牢拍的存储空间不完全符合 AWS S3 的标准，所以说 rclone 没办法很好地兼容。

好好好。支持，但是不完全支持。

万般无奈之下小氯开始寻找替代方案，在把又拍云的文档翻了个底朝天之后，小氯终于找到了这个东西：

{{< github repo="upyun/upx" >}}

这个东西不能用 Homebrew 安装（或许小氯可以自己维护一个？），同时小氯的系统里已经有一个叫 `upx` 的家伙了（一个压缩可执行文件的工具，可以把 C++ 编译出的 `./hello-world` 大小压缩一半~~并且使得其报错~~）。所以，我们采取一下自定义安装策略。

首先把东西下载下来：

```bash
wget https://collection.b0.upaiyun.com/softwares/upx/upx_0.4.8_darwin_arm64.tar.gz
```

然后解压缩（或者直接用命令行解压缩也行，看您方便），再移动到 PATH 里面：

```bash
sudo mv /path/to/upx /usr/local/bin/upyun
```

然后验证一下就可以了。

这个命令行工具不支持使用文件验证，所以我们把凭据写到环境变量里面就好。

```bash
alias upyun="/usr/local/bin/upyun"
upyun login {{_UPYUN_SERVICE_NAME}} {{_UPYUN_OPERATOR}} {{_UPYUN_SECRET}}
```

然后上传完成退出就好了。

这个方法非常别扭，但是没办法，这是目前小氯找到的唯一一个能跑起来的方法了。

同样的，老友们可以[自取脚本](https://gist.viento.cc/chlorine/4f9d0a497ca647e5ab35154fb2408693)。

Shell Commands 真的是太强大了，小氯写了若干个脚本，几乎完全替代了 Image Converter、Git 等插件。如果再配合一下 Local REST API 和 Obsidian URI，大概可以把目前小氯的大部分插件都替代掉了。

## 后记

又清掉了一篇草稿，好耶 ～(∠・ω< )⌒☆​