---
title: Hugo博客link更改后如何修改Twikoo评论位置
date: 2024-02-21T10:29:40
location: 辽宁，东港
categories: 百草园
tags:
  - Twikoo
  - Hugo
  - 折腾
slug: link-modifying-of-twikoo
summary: 数据库可爱捏
description: 本文介绍了如何在更改 Hugo 博客的文章链接后，更新 Twikoo 评论系统以匹配新的链接。文章首先说明了更改链接的必要性和方法，然后详细描述了如何通过 MongoDB CLI 工具导出、修改并重新导入 Twikoo 的评论数据，以确保评论能够正确地与文章关联。作者提供了具体的步骤，包括获取 MongoDB URI、下载并使用 MongoDB CLI 工具进行数据操作。最后，文章还给出了参考资料，供读者进一步了解相关操作。
---
各位老友们好，我是 Chlorine。

本期是一个小事情，就是在 Hugo 博客文章的 link 被修改之后，如何使 Twikoo 评论也跟到正确的位置。

不仅是 Hugo，任何使用 Twikoo 的静态博客都适用这个方法。

## 前言

我的博客之前的链接大致都是 `https://yoghurtlee.com/posts/<link>`，感觉加一个 `posts` 属实是有点多余。这个好办，改一下 `config.toml` 就好。

```toml
[permalinks]
  # posts = "/posts/:slug/" 这是改之前
  posts = "/:slug/"
```

但是再上网站上一看，Twikoo 面板里的评论还在，然而点击查看是 404.

短暂懵了一下后，联想到我从 NotionNext 换到 Hugo 的时候，明明没有做任何迁移，我的 now 页面的评论却还在，我瞬间想到了一种可能：

> Twikoo 后台的数据是按照文章链接进行对应的，只要链接不变，文章的评论就在，否则就找不到。

那只要能修改 Twikoo 后台的数据，就可以完成迁移了。

## 获取 MongoDB URI

去 Vercel 里找到你的项目，在项目设置-环境变量中找到 `MONGODB_URI` 把值复制下来备用，它应该具有这样的形式：

```txt
mongodb+srv://<某些字符>:<某些字符>@<某些字符>.mongodb.net/<后面的东西>
```

把 `net/` 后面带问号的那一堆删了，我们用不着。

## 下载 MongoDB CLI

Twikoo 的背后是 MongoDB 数据库。我对操控数据库一窍不通，所幸官方提供了可以操控数据库的 CLI 套件。

由于在 macOS 上尝试之后遇到了不可名状的错误，因此我启动了我的 Windows 备用机（所以，真心推荐每一个喜欢 macOS 的计算机类学生准备一台备用机，指不定什么时候能救命 awa）。

在[这里](https://www.mongodb.com/try/download/database-tools)下载相应套件，直接解压就好。

然后进入解压后的文件夹，找到 `bin` 子文件夹，点进去，会发现一堆二进制文件。

右键-更多-打开终端，把这段命令粘进去（注意，URI 是没有尖括号包裹的，用尖括号只是表示变量的习惯🤣）

```bash
./mongoexport --uri <你的URI> --collection comment --type json --out twikoo-comments.json
```

> **瘟锌锑逝**
> 有些教程不会带前面的 `./`，但是由于我们没有配环境变量，这样会报错。所以我们直接加 `./`，方便。

回车执行。一切顺利的话，你应该可以在 `bin` 文件夹下看到 `twikoo_comments.json` 文件。

打开这个文件，就可以进行修改了。由于我的需求比较简单，因此使用 VS Code 的查找替换功能，两步就完成了：将 `` 替换为空，将 `bulid` 替换为 `build`。如果需求比较复杂，可能需要结合正则表达式进行食用。

改完之后保存，执行这段代码：

```bash
./mongoimport --uri "<你的URI>" --collection comment --type json --mode merge --file twikoo-comments.json
```

就可以覆盖原本的数据。

将来，如果更改域名或者别的链接修改，都可以照葫芦画瓢地使用。

参考资料：

1. [静态博客永久链接变更后修改twikoo评论地址 | AppSnitch (readfere.com)](https://www.readfere.com/twikoo_url_modified)
2. [Twikoo 评论数据导出教程 - iMaeGoo&#39;s Blog](https://www.imaegoo.com/2022/twikoo-data-export/)
