---
slug: macos-gpg-sign-git-commit
datetime: 2024-07-23 18:28
summary: 太好了，小氯，你可是解决了大问题啊。
tags:
  - Git
  - 折腾
  - GPG
title: macOS配置GPG签名Git提交
date: 2024-07-23
description: 本文详细介绍了如何在macOS上使用GPG签名来验证提交者身份的过程。作者从GPG的历史和功能开始，讲述了其加密和签名的重要性，接着指导读者如何在Mac上安装和配置GPG，包括生成密钥对、在GitHub上设置GPG密钥，以及如何配置Git和VS Code以支持GPG签名。文章还提到了Obsidian Git的配置，并分享了一些解决常见问题的经验。通过这些步骤，用户可以确保他们的Git提交是经过验证的，增强了提交的安全性和可信度。
categories: 图灵机
featuredImage: https://img.clnya.fun/macos-gpg-sign-git-commit-cover.webp
draft: false
share: true
---
各位老友们好，我是 Chlorine。

闲来无事水篇文章，记录一下我刚刚解决的一个心头大患。

## 前言

在咱们看 GitHub 上的 commit 的时候，往往会看到这样的情景：

![](https://static.quail.ink/media/d2ng6hm25r.webp)

那边那个好看的绿色 badge 是怎么来的捏？咱们可以猜一下。Verified，经过验证的，那验证的是什么？自然是提交者的身份，标明这个提交是由仓库的作者亲笔所为，而不是由路边的哪个路人甲或者是不怀好意有 bear 来的攻击者提交的。

那怎么做这种「我是我」的证明呢？方法就是通过咱们今天要讲的 GPG signing。

## What's GPG？

以下内容来自 [Wikipedia](https://zh.wikipedia.org/wiki/GnuPG)：

> GNU Privacy Guard（GnuPG 或 GPG）是一个密码学软件，用于加密、签名通信内容及管理非对称密码学的密钥。GnuPG 是自由软件，遵循 IETF 订定的 OpenPGP 技术标准设计，并与 PGP 保持兼容。

嗯，好像懂了，又好像没懂，听君一席话，如听一席话。

简单来说吧。这个故事要从 1991 年开始讲起。那个时候有一个程序员大神，名叫Phil Zimmermann。PZ 这人呢，是个极其看重隐私的「偏执狂」（注：这个词没有贬义）。为了躲避烦人的监管，他自己写了一个名叫 PGP 的东西。PGP，全称是Pretty Good Privacy，是一个用来给 Email 和各种信息加密的东西。

这玩意有什么用呢？比方说，你给你的朋友写了一封邮件并且使用 GPG 进行了加密，内容是：

> 今天下午天气不错，要不一起去紫荆园吃个饭？听说三楼的酸菜鱼出了新的番茄锅底！

有了加密，即使是你的邮件被截获了，截获者打开一看，由于没有「钥匙」，只能看到里面写的是：

> 玛卡，巴卡，阿卡，哇卡，米卡，玛卡，呣！ 玛卡， 巴卡，阿巴，雅卡，伊卡，阿卡，噢！ 哈姆，达姆，阿卡嗙，咿呀呦~ 玛卡，巴卡，阿卡，哇卡，米卡，玛卡，呣！

监管者：？（`黑人问号.webp`）

但是你拥有「钥匙」的朋友，却能完整地读到你的邮件。这样就保证了隐私的安全。

那这个功能难道不能破解吗？理论上当然可以，但是难度基本相当于让你一粒一粒捡完现在撒哈拉沙漠的沙子。

听起来是个好东西，对吧？很可惜，PGP 是个商业软件。

这就有点坑爹了。所幸，万能的开源社区早就帮我们搓出来了一个完美的替代品，那就是 GNU Privacy Guard，简称 GNUPG 或者 GPG。这中间还有很多困难，但是已经被我们伟大的前辈们一一克服了。咱们这群后备只要坐享其成就可以了。

GPG 的应用极其广泛，包括但是不限于邮件加密、文件完整性验证等。当然了，今天我们只讲 Git commit signing。

## 安装 GPG

OK，废话讲完了，咱们正式开始配置 GPG。

首先我们需要安装 GPG，自然还是用万能的 Homebrew：

```bash
brew update
brew install gpg
brew install pinentry-mac
```

（如果您连 Homebrew 都没安装，或者都不知道是啥，我合理怀疑您是否真的是 Mac 的持有者以及用得到 GPG Git 的人。）

安装完成之后，检测一下安装是否成功：

```bash
gpg --version
# 别的命令也行
```

## 修改配置文件

下面的内容实际上就是写入文件，大家大可以各显神通。

```bash
echo "pinentry-program $(brew --prefix)/bin/pinentry-mac" >> ~/.gnupg/gpg-agent.conf
echo "use-agent" >> ~/.gnupg/gpg.conf
echo 'export GPG_TTY=$(tty)' >> ~/.zshrc # 如果你用的不是 Zsh，请根据你的终端修改
```

然后重启电脑。

## 生成 GPG 密钥对

GPG 的工作需要一对公私钥。重启之后，我们来生成我们所需的密钥。

键入命令：

```bash
gpg --full-generate-key
```

会出现一些交互式命令行选项，大部分按照默认即可。姓名、邮箱和备注按照自己的情况填写（邮箱推荐填写自己用于 Git 提交、且在相关平台——如 GitHub 上绑定过的邮箱）。

注意！关键来了！下一步应该是输入密码，但是你应该看见的是一个**类似这样的 GUI**：

![](https://static.quail.ink/media/3869lueyn0.webp)

而不是一个命令行 UI！

密码随便写，记得一定要勾选「存储在钥匙串中」的选项！

生成密码后，我们键入：

```bash
gpg --list-secret-keys --keyid-format LONG
```

然后应该会输出一串类似这样的东西：

```bash
/Users/chlorine/.gnupg/pubring.kbx
----------------------------------
sec   ed25519/xxxxxxxxx 2024-07-23 [SC]
      yyyyyyyyyyyyyyyyyyyyyyy
uid                   [ 绝对 ] （你的相关信息）
ssb   cv25519/zzzzzzzzzzz 2024-07-23 [E]
```

把 `xxxxxxxxxx` 对应的那一串字符复制下来，这就是你的 Key。

然后键入：

```bash
gpg --armor --export <你的 Key，不带两边的尖角括号，下同>
```

把输出的东西复制一下，注意，`-----BEGIN PGP PUBLIC KEY BLOCK-----` 和 end 的也要复制。

在[这里](https://github.com/settings/keys)配置你的 GPG 密钥，名字随便起，把刚才那一堆粘进去就行。Gitee 和 Codeberg 同理。

## 配置 Git

生成密钥后，我们略略配置一下 Git：

```bash
git config --global commit.gpgsign true
git config --global user.signingkey <你的 Key>
git config --global gpg.program /opt/homebrew/bin/gpg
```

## 配置 VS Code

VS Code 内置了方便的 Git GUI，但是如果不合理配置，就无法对 Git commit 进行签名，从而出现各种奇奇怪怪的问题。

说来也简单，如果你严格地按照我们上面的步骤走的话，直接在设置中搜索 `git.enableCommitSigning` 并启用即可。

## Obsidian Git

不需要任何配置，直接用就行了。因为我们刚在 Git 里面配置了 GPG 程序的位置，应该不会出现找不到 GPG 的错误。

## 结语

GPG 这个事我配了不知道多少次，经常出现 GPG failed to sign the data。我知道应该是在图形界面没法配置密码输入，但是不知道怎么解决，心很累。所幸是搞好了。作文以记之，

## 参考资料

1. https://github.com/microsoft/vscode/wiki/Commit-Signing
2. https://github.com/Vinzent03/obsidian-git/issues/21
