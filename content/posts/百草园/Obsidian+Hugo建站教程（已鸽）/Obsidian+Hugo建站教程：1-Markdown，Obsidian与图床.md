---
title: Obsidian+Hugo建站教程：1-Markdown，Obsidian与图床
date: 2024-02-16 20:28:25
tags:
  - 博客
  - Obsidian
  - 教程
featuredImage: https://img.clnya.fun/cover/how-to-build-a-blog-1-cover.webp
slug: how-to-build-a-blog-1
categories: ["百草园"]
series: Obsidian+Hugo建站教程（已鸽）
summary: Obsidian + Hugo 建站教程第一期
description: Obsidian + Hugo 建站教程——Markdown 语法介绍，Obsidian 配置，使用缤纷云对象存储搭建图床。
---
各位老友好啊，我是 Chlorine。本期开始，我们进入独立博客建站之旅。

## Markdown 与 Obsidian

我在 [上一期](/Obsidian+Hugo建站教程：0-前言.md) 中曾经说过，搭建博客就像是搭建一座数字博物馆。博物馆中最重要的东西，自然就是展品了。对于我们的博客，展品就是我们的文章。

关于博客文章怎么写、写什么的问题，不是三言两语就能说清楚的，每一位独立博客的博主也都有各自见仁见智的想法。这里我们只讨论一个问题：**用什么写**。

能找到这里的朋友，应该至少都对 Markdown（简称 md）有一定的了解（大概率已经能熟练使用 Markdown 了）。不过为了完整，我们还是简单介绍一下 Markdown。

搬运 [Wiki](https://zh.wikipedia.org/wiki/Markdown)：

> Markdown 是一种轻量级标记语言，创始人为约翰·格鲁伯。它允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的 XHTML（或者 HTML）文档。这种语言吸收了很多在电子邮件中已有的纯文本标记的特性。

说白了，Markdown 就是一种使用特殊记号对文本进行样式标记（给文本赋予特定的样式，例如斜体、粗体等）的语言。

下面的优点由 Kimi AI 进行概括总结：

1. **易读性**：Markdown 的语法简单直观，即使没有编程背景的用户也能快速理解和使用。它的设计哲学是“所见即所得”，即最终的输出格式在编辑时就能直观地看到。
2. **易写性**：Markdown 的语法规则很少，这使得编写文档变得快速且不繁琐。它避免了传统 HTML 的复杂标签，使得内容创作者可以专注于内容本身，而不是格式。
3. **跨平台兼容性**：Markdown 文件可以在多种平台和应用程序中使用，包括 GitHub、Reddit、Stack Overflow 等，这使得内容可以在不同的环境中保持一致性。
4. **可扩展性**：虽然 Markdown 本身是固定的，但它可以通过扩展插件或工具链来增加额外的功能，如表格、脚注、数学公式等。
5. **版本控制友好**：Markdown 文件通常是纯文本格式，这使得它们非常适合版本控制系统（如 Git），可以轻松地追踪文档的变更历史。
6. **转换灵活性**：Markdown 文件可以轻松转换为 HTML、PDF、Word 等其他格式，这为内容的发布和分享提供了便利。
7. **社区支持**：由于 Markdown 的流行，有许多工具和编辑器支持 Markdown，如 Typora、Mark Text、Visual Studio Code 等，这些工具提供了丰富的功能和良好的用户体验。
8. **适合快速草稿和笔记**：Markdown 的简洁性使得它成为快速记录想法和草稿的理想选择，尤其是在需要快速整理思路时。
9. **减少视觉干扰**：Markdown 的编辑器通常提供简洁的界面，减少了视觉干扰，有助于提高写作效率。
10. **易于维护**：由于 Markdown 文件是纯文本，它们不需要特定的软件来打开，也不需要担心文件格式的兼容性问题。

后面我们会讲到，我们的博客文章需要借助博客框架转换为可展示的 HTML 页面，借助 Git 进行版本控制和提交。那很明显，用 Markdown 再合适不过了。

如果你想快速入门 Markdown，可以参考以下资料：

1. [Markdown 官方教程](https://markdown.com.cn/)
2. [Markdown 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/markdown/md-tutorial.html)
3. [基本撰写和格式语法 - GitHub 文档](https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
4. [MarkDown超级教程 by 成雙醬 - Obsidian中文教程 - Obsidian Publish](https://publish.obsidian.md/chinesehelp/01+2021%E6%96%B0%E6%95%99%E7%A8%8B/MarkDown%E8%B6%85%E7%BA%A7%E6%95%99%E7%A8%8B+by+%E6%88%90%E9%9B%99%E9%86%AC)

注意，由于我们后续要使用 Hugo 作为框架，我强烈推荐在写作时严格遵循 GitHub- favored Markdown（GFM）格式标准。

言归正传。既然要用 Markdown 写文章，那就需要一个称手的编辑器。市面上的 md 编辑器极多，代表如 Obsidian、Typora、VS Code（是的，你用来写代码的 VSC 可以当做 Markdown 编辑器，毕竟人家是 code editor 而不是 IDE）等。这里我们重点讲 Obsidian。

[Obsidian](https://obsidian.md)，中文名为“黑曜石”，是一款免费的跨平台笔记软件，以其完善的 Markdown 支持、双链、关系图谱、本地化存储、强大的可扩展性、良好的社区生态和多样的主题等受到广泛好评。Obsidian 完善的语法支持和丰富的插件会给我们后续的写作带来极大的便利。


能找到这篇文章，相信多少也对 Obsidian 有了解。如果不是，那我强烈推荐你尝试一下这款笔记神器。以下是一些教程：

1. [清单控沙牛的个人空间-清单控沙牛个人主页-哔哩哔哩视频 (bilibili.com)](https://space.bilibili.com/443605967?spm_id_from=333.337.0.0)
2. [由此开始 - Obsidian 中文帮助 - Obsidian Publish](https://publish.obsidian.md/help-zh/%E7%94%B1%E6%AD%A4%E5%BC%80%E5%A7%8B)
3. [Ob新手入门必读——常见Q&amp;A（持续建设ing...请勿在此回复及提问） - 疑问解答 - Obsidian 中文论坛](https://forum-zh.obsidian.md/t/topic/3222)
4. [想一小时上手obsidian？这一篇就够了。【玩转Obsidian的保姆级教程】 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/428519519)

## 图床的搭建

OK，现在我们似乎已经可以开始进行愉快的创作了，但是让我们先行思考一个问题。

我们知道 Markdown 是纯文本语言，那我们怎么插入图片呢？

事实上，Markdown 的图片是通过链接引用的形式插入的，典型的链接格式为 `![图片注释](图片链接，本地或者网络)`。Obsidian 还支持在方括号内的注释后面添加 `|图片大小` 来调整宽度。

那看来我们只需要将图片放在适当的位置进行引用就好了。问题是：**放在哪呢？**

如果你的图片不多，你可以将其放置于静态资源文件夹下（后面会讲）。但是我更推荐另一种方式：使用图床。

简单点说，图床（Image Hosting Service，IHS）就是一个能存储图片的服务器。与一般的服务器不同, 它允许将图片以 URL 链接的形式插入文章并展示图片内容。使用图床管理文件可以节省仓库空间，并避免乱七八糟的文件堆积，同时使 Markdown 仓库完全文本化，便于导出和迁移；当然也有缺点，例如隐私性较低，可能跑路（因此要做好备份）等。

图床有很多种，免费的包括 SMMS，路过图床，聚合图床，Imgur 和新浪微博图床（已经无法使用）等，甚至 GitHub 和 Gitee 的仓库也可以当图床（Gitee 已经无法使用，GitHub 需要借助特殊手段）；付费图床主要是各大厂商的对象存储，例如阿里云 OSS，腾讯云 COS 等，一般都很便宜。

这里推荐一些个人觉得比较靠谱的方案：

- [SMMS](https://smms.app/)：老牌免费图床，免费用户有 5G 的空间，够用很久了。至于速度嘛，只能说中规中矩。
- GitHub+jsDelivr：jsDelivr 专门帮 GitHub 仓库做 CDN，大陆速度比较稳。不过每次都得创建一个 release，怪麻烦的。
- [又拍云](https://www.upyun.com/)：加入又拍云联盟（在网站底下放他们的 logo）可以薅不少的免费额度，用来当图床和全站 CDN 都挺好，可惜需要 ICP 备案。
- [七牛云](https://www.qiniu.com/)：不少大佬的推荐，免费额度较充足，可惜也需要备案。
- 对象存储：现在的大厂基本都有，价格和质量都差不多，随便挑一个就可以。
- 不用：没错，不用图床。如果你的图片不多且体积不大，那放在 `static` 文件夹里面完全没毛病，后续会有讲解。

我曾经先后使用 SMMS 和阿里云 OSS，目前使用的方案是缤纷云对象存储，有 50G 免费存储，每个月前 30G 流量免费（S4 出口流量、内置 CDN 回源、内置 CDN 出口流量各 10GB/月），不出意外够我用了。下面以这个图床为例讲解图床的搭建。

### 缤纷云对象存储创建

首先进入[缤纷云官网](https://bitiful.com)，完成注册和实名认证，这个略过。

然后进入控制台，点击新建存储桶：

![|600](https://img.clnya.fun/IMG-20240216202825-1.webp)

新建存储桶后，在左侧选择 accesskey，添加一个子用户并获取对应的 accesskey 和 secretkey，这个很重要，找个地方保存好。权限就选择我们刚才的桶就可以。

然后我们就可以上传图片了。

### PicList 的配置

可以上传图片还不够，总不能每次都进去传一遍，太不优雅了。

我们可以使用一些工具，使得我们在 Obsidian 中写作时就直接可以上传图片。

PicList 是一个图床管理工具，基于著名的 PicGo 进行二次开发而成，有更加强大的功能。

[这里](https://piclist.cn/)是 PicList 的官网，大家可以进去选择对应版本进行安装。

安装后打开主窗口，在右边栏中选择 AWS S3，在设置中配置并保存。两个 key 写刚才保存的那一串，bucket 写桶的名字，自定义节点填 `https://<你的桶名>.s3.bitiful.net`。

![|600](https://img.clnya.fun/IMG-20240216202825-2.webp)

### image auto upload 插件配置

进入 Obsidian 插件市场，搜索 image auto upload 并安装。访问 GitHub 不顺畅的老友可以自行百度搜索 PKMer 插件进行辅助。

安装后启用，进行如下配置：

![|600](https://img.clnya.fun/IMG-20240216202825-3.webp)

然后就可以做到粘贴图片自动上传了。

此外还有一些进阶的用法，这个我们留到后面讲。
