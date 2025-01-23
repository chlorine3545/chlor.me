---
slug: hello-shiki
datetime: 2024-08-18 11:39
summary: 这代码高亮，多是一件美事啊
tags:
  - 博客
  - 折腾
cover_image_url: https://img.clnya.fun/hello-shiki-cover.webp
title: Hello，Shiki
date: 2024-08-18
description: 本文介绍了如何在Hugo中使用Shiki进行代码高亮，Shiki在服务端执行，提供了更好的性能和样式，适合构建静态网站，需满足特定前置条件和安装依赖，步骤包括配置Hugo、创建rehyperc文件和修改CSS等。
categories: 逍遥游
featuredImage: https://img.clnya.fun/hello-shiki-cover.webp
draft: false
share: true
showTableOfContents: true
---
各位老友们好，我是 Chlorine。继续高强度水文。

本期的主题是 Hugo 的代码高亮，主要参考了[蜗牛大神](https://www.eallion.com)的教程：[在 Hugo 中使用 Shiki](https://www.eallion.com/hugo-syntax-highlight-shiki/)。感谢前辈的付出。

## 前言

Hugo 的代码高亮基于 Chroma。这是个用 Go 语言写的库，好处是性能极高，坏处是不太聪明。比如我之前的文章 [Hello，SearXNG]({{< relref "Hello，SearXNG.md" >}})，里面有一段 PowerShell 脚本，结果：

![](https://img.clnya.fun/IMG-20240818100304.avif)

嗯……这个效果不能说是尽善尽美吧，至少也可以说是聊胜于无。

其他的部分，像 `docker-compose`、`git` 之类的命令高亮不了，已经是紫荆园的麻辣香锅——家常便饭了。

那怎么修复？无非两个招：自己写 Lexer[^1]，或者引入第三方库。

不清楚哪位勇士有第一项所需的娴熟的专业技能、大把的闲暇时间和超人的折腾勇气，反正小氯自认为没有。

Hugo 的第三方代码高亮库很多，比方说 `Highlight.js` 和 `Prime.js`，其优缺点可谓各有千秋。但它们都有一个致命的缺点：**都需要在客户端执行大量的 JavaScript 代码**。这就势必会对性能造成可怕的影响。如果大家没有什么感知的话，请参考下面的 Twikoo 的加载需要多久。

那有没有办法在服务端执行代码，把压力放在网站构建过程中呢？

有，方法就是我们今天的主角——Shiki。

## Shiki 简介

Shiki 这个名字来自于日语的「式」（しき），意思就是「样式」。此外如果我记得没错，Shiki 应该还有季节、四季的意思，当然这不重要。

[Shiki](https://shiki.style) 是一个基于 VS Code 语法高亮引擎（没错，就是那个 VS Code）的代码高亮库。其基于 TextMate 语法定义文件和 WebAssembly 技术提供快速精确的代码高亮。

Shiki 很特别的一点在于：**它在执行时会扫描指定路径的 HTML 文件，并且将各种语法 token 附加上内联样式**。这使得 Shiki 非常适合用来为 Hugo 这样的静态网站构建工具添加高亮，无它，扫一遍 `public` 就行了。

顺便说一句：Shiki 是 Pine Wu 和 Anthony Fu 等前端大神的力作 :)

## 前置要求

请注意，如果您的已有条件和需求不满足下面所述，那小氯推荐您还是先别看文章了，还是先去紫荆公寓的公共空间喝杯茶更能体现对您生命的尊重。~~没错我是直接从上一篇文章复制过来的~~

条件：

- 已经能用 Hugo 构建静态网站
- 对 GitHub Actions 和 Vercel 等自动构建的流程有一定了解
- 本地已经配置了一个 JavaScript 运行时及包管理器，例如 `Node.js` 或者 `Bun.js`。我们以下均使用 `Bun.js` 进行演示。

要求：

- 对 Chroma 的高亮表现不满
- 不希望使用 `Highlight.js` 等客户端高亮器

## 安装相关依赖

进入你的博客根目录，运行命令：

```bash
bun i shiki @shikijs/rehype rehype-cli
```

这应该会自动为你创建 `node_modules`、`bun.lockb` 和 `package.json`。记得把 `node_nodules` 文件夹加到  `.gitignore` 里面——如果没有自动添加的话。

## 配置 Hugo

修改 `hugo.toml` 或者你其他名字的配置文件，将 `codeFences` 改为 `false`。如果没有请自行创建，像这样：

```toml
[markup]
    [markup.highlight]
      codeFences = false
```

## 创建 `.rehyperc`

如果我没猜错的话，这应该是 rehype 的配置文件了。看起来跟个 `JSON` 似的。

```json
{
  "plugins": [
    [
      "@shikijs/rehype",
      {
        "themes": {
          "light": "你的日间主题",
          "dark": "你的夜间主题"
        }
      }
    ]
  ]
}
```

主题列表在[这里](https://shiki.style/themes)，挑个自己喜欢的吧。效果没必要像我一样每次都重新构建，在 VS Code 里面搜索同名主题看就行了。我比较选综，就用了 One Dark Pro 系列的。

rehype 这东西很神奇，可以对 HTML 各种爆改。当然，咱们这里用的就是其中一个插件，如果想进一步探索请看[这里](https://github.com/rehypejs/rehype/blob/main/doc/plugins.md)，如果有什么好的创意也可以和我分享，小氯洗耳恭听。

## 修改 Hugo CSS

找到你主题的 CSS。我们要做一下样式适配。我原本的样式大概是：

```css
code {
    font-family: "Fira Code Light", "LXGW WenKai Lite", monospace;
}

code[class*="language-"],
pre[class*="language-"] {
    white-space: pre-wrap;
    /* 或 pre-line */
    word-break: break-all;
}
```

现在改成：

```css
code {
    font-family: "Fira Code Light", "LXGW WenKai Lite", monospace;
}

html .shiki,
html .shiki span {
    white-space: pre-wrap;
    word-break: break-all;
    overflow-wrap: break-word;
    font-family: "Fira Code Light", "LXGW WenKai Lite", monospace;
}

html.dark .shiki,
html.dark .shiki span {
    color: var(--shiki-dark) !important;
    white-space: pre-wrap;
    word-break: break-all;
    overflow-wrap: break-word;
    font-family: "Fira Code Light", "LXGW WenKai Lite", monospace;
}
```

大家照猫画虎即可。

## 配置脚本命令

在根目录的 `package.json` 下面添加这样的脚本命令：

```json
"scripts": {
    "shiki": "bunx rehype-cli public -o"
}
```

大体而言改完之后你的文件应该看起来像是：

```json
{
    "dependencies": {
        "@shikijs/rehype": "^1.13.0",
        "rehype-cli": "^12.0.0",
        "shiki": "^1.13.0"
    },
    "scripts": {
        "shiki": "bunx rehype-cli public -o"
    }
}
```

当然，shiki 这个名字你可以随便起，然后就可以在根目录下运行 `bun run shiki` 对构建产物进行替换了。如果报错，大概率是因为你使用了不支持的语言或者错误的语言代码（比方说，`html` 写成 `HTML`）。可以在[这里](https://shiki.style/languages)查看标准化的代号表。

## Vercel 构建命令

GitHub Actions 版本的可以看上面蜗牛大神的教程。

```bash
cd themes/efimero && bun install && bun run build && cd ../.. && hugo --gc --minify && bun install && (bun run shiki || true)
```

这大概就是完整的构建命令了。最后的 `|| true` 是为了防止报错导致的构建失败。

## 自动化

大家知道，小氯是个被 C++ ~~荼毒~~熏陶过的计算机系学生，因此习惯使用 Makefile 整合所有构建过程。

不过 Makefile 有个致命的缺点：**只能一步一步执行命令**。而 `bun run shiki` 应该在 `hugo server -D` **构建 public 文件夹完成，但是未结束（只有我们手动停止这个命令才能结束）** 时执行。使用后台运行的指令的话，又没办法准确把控时机。唯一的方法可能就是使用 `fswatch` 了，但是这样又会造成不必要的性能开销。

对于不经常折腾主题，只是发布内容的老友来说，这其实不是问题，主要对于小氯这样的喜欢折腾主题的人比较麻烦。现在只能是每次手动执行下，或者干脆只 `make`，缺点就是高亮没了。

## 去掉行号

在本地测试的时候我发现 Hugo 代码块的行号变得非常抽象，具体来说，10 居然会换行变成 1 和 0。改 `hugo.toml` 不管用，于是采取最简单粗暴的方法：CSS 隐藏。

```css
.custom-md code span.line:before {
    display: none;
}
```

## 结语

又水了篇文章，内心毫无~~波兰~~波澜。

Shiki 的效果确实出挑，虽然会显著加长构建时间，但是也算可以接受。这样代码高亮看起来就好看多了。

以及一个新消息：我准备为主域名重新备案啦！这期间网站评论可能会关闭（看侧边栏的公告即可），但是其他功能不受影响。可以给我发邮件来互动~

[^1]: Lexer，即词法分析器或扫描器，是编译器的第一阶段。其任务是读取源代码文本，并将其分解成一系列的标记（tokens）。每个标记代表了源代码中的一个有意义的片段，比如关键字、标识符、字面量、运算符等。Lexer 的输出是源代码的抽象表示，它为后续的语法分析（parser）提供了基础。
