---
title: 动手折腾：用SSH解决Oh-my-Zsh的更新错误
date: 2024-05-09T08:14:00
categories: ["图灵机"]
tags:
  - 折腾
  - Zsh
  - 博客
date: 2024-05-09T22:55:00
slug: update-omz-with-ssh
summary: 小小的经验
description: 本文介绍了作者使用 SSH 作为 Oh-my-Zsh 的更新源，用于解决中国大陆更新不畅的问题的过程。
---

Oh my Zsh 的默认更新环境是 HTTPS 的。而由于 GitHub 对国内铀溴的支持，即使是开了科学技术也时常出现访问失败的情况。所幸 GitHub 的 SSH 登录比 HTTPS 靠谱许多，只要有科学技术基本都能成功访问，速度也很好。

所以我们只要设法将 Oh my Zsh 的拉取源改成 SSH 即可。

一般来说，Oh my Zsh 的安装目录是 `~/.oh-my-zsh`，先用 `cd` 进入：

```bash
cd ~/.oh-my-zsh
```

显示一下远程仓库地址：

```bash
git remote -v
```

发现是 HTTPS：

```bash
origin	https://github.com/ohmyzsh/ohmyzsh.git (fetch)
origin  https://github.com/ohmyzsh/ohmyzsh.git (push)
```

直接切换链接：

```bash
git remote set-url origin git@github.com:ohmyzsh/ohmyzsh.git
```

然后再执行一次 `git remote -v` 查看是否更改成功即可。

然后再执行

```bash
omz update
```

就可以成功更新了。

![|590](https://img.clnya.fun/IMG-20240509082331.webp)
