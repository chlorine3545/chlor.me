---
title: Hello，VSCodium
date: 2024-05-19T19:52:00
slug: hello-vscodium
summary: 一次简简单单的换编辑器之旅
categories: 逍遥游
description: 本文介绍了 VSCodium，这是一个完全开源且不包含数据收集的 VS Code 替代品。作者讨论了转向 VSCodium 的原因，包括对开源软件和隐私的关注，并提供了安装、设置迁移和扩展换源的指南。最后，作者指出 VSCodium 和 VS Code 在界面和使用上非常相似。
showTableOfContents: true
featuredImage: https://img.clnya.fun/hello-vscodium-cover.webp
---
# Hello，VSCodium

各位老友们好，我是 Chlorine。

## 前言

从高考暑假接触 Python 开始，我就一直使用蟒蛇书推荐的 VS Code 作为我的代码编辑器，其美观和高度可扩展性深得我心。即使是换用 MacBook 后我也没有考虑过别的编辑器。

不过，随着见识的增长，我对自由开源软件（FLOSS）和隐私保护的渴求越来越强。这倒不是什么关乎（软件方面的）意识形态的问题，也不是说非 FLOSS 就如何如何，只是单纯的个人感觉而已。

## VS Code——开源的代码编辑器……吗？

可能有人会问，VS Code 难道不是 FLOSS 吗？VS Code 的全部源码都在[这个仓库](https://github.com/microsoft/vscode)，并且遵循 MIT 许可证开源。

对此，我的答案是：确实，您说的大部分正确。

但是我们需要注意： **无论是从 VS Code 的官网还是从 GitHub release 进行下载，我们获取的都是一个二进制包，而不是 VS Code 的源码** 。

这有什么区别吗？

当然有。

我们看一下 VS Code 的官方网站：

![](https://img.clnya.fun/IMG-20240519120024.webp)

注意到了吗？VS Code 的说明中，不是「open source」，而是「build on open source」。

我们来复习一下 MIT 许可证的内容：

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

如各位所见，MIT 许可证允许任何人使用、复制、修改、合并、发布、分发、再授权和销售软件副本。**这里的「任何人」，自然也包括 Microsoft。**

那么 Microsoft 到底做了什么？简而言之，微软的工程师们将自家的源码进行了打包，构成了我们平时看到的 Visual Studio Code。但是，**这份 Visual Studio Code 的成品包是在一个[非FLOSS的许可证](https://code.visualstudio.com/license)下发布的，并且包含了微软的遥测和数据收集**。

下面是微软的一位工程师 [Chris Dias](https://github.com/chrisdias) 在 VS Code 源码的 GitHub 仓库中 issue #60 的解释：

> Thanks for the interest in this topic and I apologize for not commenting sooner, I’ve been on vacation and just getting through my backlog. Let me try to provide more details behind our thinking here.
>
> When we set out to open source our code base, we looked for common practices to emulate for our scenario. We wanted to deliver a Microsoft branded product, built on top of an open source code base that the community could explore and contribute to.
>
> We observed a number of branded products being released under a custom product license, while making the underlying source code available to the community under an open source license. For example, Chrome is built on Chromium, the Oracle JDK is built from OpenJDK, Xamarin Studio is built on MonoDevelop, and JetBrains products are built on top of the IntelliJ platform. Those branded products come with their own custom license terms, but are built on top of a code base that’s been open sourced.
>
> We then follow a similar model for Visual Studio Code. We build on top of the `vscode` code base we just open sourced and we release it under a standard, pre-release Microsoft license.
>
> The cool thing about all of this is that you have the choice to use the Visual Studio Code branded product under our license *or* you can build a version of the tool straight from the `vscode` repository, under the MIT license.
>
> Here's how it works. When you [build](https://github.com/Microsoft/vscode/wiki/How-to-Contribute#build-and-run-from-source) from the `vscode` repository, you can configure the resulting tool by customizing the [`product.json`](https://github.com/Microsoft/vscode/blob/master/product.json) file. This file controls things like the Gallery endpoints, “Send-a-Smile” endpoints, telemetry endpoints, logos, names, and more.
>
> When we build Visual Studio Code, we do exactly this. We clone the `vscode` repository, we lay down a customized `product.json` that has Microsoft specific functionality (telemetry, gallery, logo, etc.), and then produce a build that we release under our license.
>
> When you clone and build from the `vscode` repo, none of these endpoints are configured in the default `product.json`. Therefore, you generate a "clean" build, without the Microsoft customizations, which is by default licensed under the MIT license (note, i made [this commit](https://github.com/Microsoft/vscode/commit/9dd095c27ea79f526b054f741bb52fa62fae80a9) to help make this more clear).
>
> I hope this helps explain why our Microsoft branded Visual Studio Code product has a custom product license while the `vscode` open source repository has an MIT license. Last, I apologize for the fact that the naming of “Visual Studio Code”, “VS Code” and the `vscode` repository are so similar, I think it contributed to the confusion.

这样做有问题吗？

完全没有。Microsoft 严格地遵循了他们自己制定的开源规则：他们使用自己开源的代码构建了一份属于 Microsoft 的发行版本。他们也没有欺骗用户，在显眼的位置写着 「build on open source」，甚至还告诉你：你可以通过一些方式关闭遥测。姑且不论这样做是否符合实质正义，但是在我看来，这已经足够坦荡。

但是，用户很可能不会愿意被收集数据，尤其是那些极其看重隐私的用户。虽然微软给出了关闭遥测的方法，但是他们也堂而皇之地说：

> The software may collect information about you and your use of the software, and send that to Microsoft. Microsoft may use this information to provide services and improve our products and services. **You may opt-out of many of these scenarios, but not all,** as described in the product documentation located at [https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting](https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting).

那难道我们真要自己从头编译 VS Code 的源码吗？毫无疑问，99%的人是做不到这一点的。

**于是，VSCodium 应运而生。**

## An Introduction to VSCodium

VSCodium 的官网上如是介绍自己：

> VSCodium is a community-driven, freely-licensed binary distribution of Microsoft’s editor VS Code.

好的，已经把事情说清楚了。

VSCodium 就是通过 VS Code 的源码构建出来的另一份发行版。其不同之处在于：它是一个完全的 FLOSS，**不包含任何遥测和数据收集的部分**。

那如果我也没办法相信 VSCodium 呢？

对此我只能说：那您就自己编译一份发行版，然后比较 Hash 值吧。

## 我需要切换吗？

简而言之，你需要满足以下条件，否则请继续 VS Code：

- 不能忍受 Microsoft 的数据收集/FLOSS 的信仰者
- 不是绝对需要 Microsoft 的专属插件

## 安装

在 macOS 上，可以使用 Homebrew 安装 VSCodium：

```bash
brew install --cask vscodium
```

## 设置迁移

运行以下命令：

```bash
cp ~/Library/Application\ Support/Code/User/settings.json ~/vscode-settings.json
cp ~/Library/Application\ Support/Code/User/keybindings.json ~/vscode-keybindings.json
```

然后运行：

```bash
mv ~/vscode-settings.json ~/Library/Application\ Support/VSCodium/User/settings.json
mv ~/vscode-keybindings.json ~/Library/Application\ Support/VSCodium/User/keybindings.json
```

## 扩展换源

VSCodium 使用[https://open-vsx.org/](https://open-vsx.org/)作为扩展源，但是这个源的扩展不太全。我们可以使用微软市场作为扩展源。

在访达-应用程序中，双击 VSCodium ，显示包内容，然后进入 `/resources/app/product.json`，编辑 `extensionsGallery` 键：

```json
"extensionsGallery": {
    "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
    "itemUrl": "https://marketplace.visualstudio.com/items"
}
```

重启即可。

## 扩展迁移

个人觉得，最方便的方法就是直接复制所有扩展文件。

在 `~/.vscode` 中，复制整个 `extensions` 文件夹，粘贴到 `~/.vscode-oss` 即可。

下面是一些我测试之后有问题的扩展：

### Pylance

Pylance 是 Python 的一个语言服务器。这个服务器属于微软专有，不能在 VSCodium 上运行。可以改用 Jedi。

### GitHub Copilot

GitHub 是微软的一部分，所以 GitHub Copilot 在 VSCodium 上运行不了也不奇怪。

这里没有什么很好的方案，推荐的方法就是使用替代品，例如同样受欢迎的 Codeium，以及我带清的几位学长开发的 Fitten code 等。

> 更新：是可以使用的，方法见[https://github.com/VSCodium/vscodium/discussions/1487](https://github.com/VSCodium/vscodium/discussions/1487)

## 结语

然后，基本上就可以无缝衔接到 VSCodium 进行开发了。祝愉快。

![二者的样式几乎一模一样](https://img.clnya.fun/IMG-20240519124202.webp)
