---
slug: swup-modifying
datetime: 2024-07-26 22:41
summary: 解题方法：瞪眼法（确信）
tags:
  - 博客
  - 折腾
cover_image_url: ""
title: 解决Swup导致的JavaScript加载失效问题
date: 2024-07-26
description: 本文记录了作者修复 Swup 下 JavaScript 加载问题的过程。作者发现页面功能如评论和代码复制无法正常加载，经过排查发现 Swup 仅替换页面的 HTML 内容，而未加载新页面的 JavaScript。作者随后找到了解决方案，使用 Swup 的 Script Plugin 来确保 JavaScript 被正确加载。最后，作者针对评论功能做了额外处理，确保 Twikoo 评论系统可以正常工作。虽然该方案还未完全完善，但已基本解决问题。
categories: ["百草园"]
featuredImage: 
draft: false
share: true
---

各位老友们好，我是 Chlorine。本期又是前端小白的魔改历险记。

## 前言

我目前使用的主题 Efímero 是我基于 [Hugo Landscape](https://github.com/kkbt0/Hugo-Landscape) 的魔改版本。Landscape 使用 Swup 作为页面的过渡，平滑的效果深得我心。

但是在我的网站使用过程中遇到了一个很烦人的问题：有一些功能常常加载不出来，比方说说说页面、代码一键复制、评论等等。奇怪的是，刷新一次就好了。

之前我并没怎么在意这件事。但是由于今天太闲且强迫症作祟，我就想着修复一下。

## 踩坑

我的切入点是我的说说页面 `whisper.html`。我相当肯定问题在 JavaScript 部分（毕竟 HTML 和 CSS 能有什么坏心思捏），然而凭借我有限的知识看了半天还是无果，AI 也不行。

我打开了控制台，发现在初次加载的时候，报出了错误：

```bash
Hooks.ts:435 Error in hook 'page:view': ReferenceError: init is not defined
    at VM35:6:36
    at index.ts:37:2
    at new Promise (<anonymous>)
    at Hooks.ts:433:8
    at index.ts:37:31
    at Hooks.ts:435:26
    at t (Hooks.ts:438:6)

whisper/:1385 Uncaught ReferenceError: init is not defined
    at HTMLDocument.<anonymous> (whisper/:1385:101)
```

看起来有一个神秘的 `init` 没有定义。我相当肯定我的 `whisper` 中没有什么 `init`，但是问题都摆在眼前了，总不能摆烂（~~还真能~~）。

前往定义，在挖呀挖呀挖了半天后，终于发现了一个所谓的 `init`：

```js
const swup = new Swup({
        plugins: [new SwupPreloadPlugin()]
    });
document.readyState === "complete" ? init() : document.addEventListener("DOMContentLoaded", ()=>init()),
swup.hooks.on("page:view", ()=>init())
```

嘶，好像有点熟，但是也就是有点熟，然后就没有然后了。

试着在项目里搜索这段代码，还真有，在 `baseof.html` 中。这看起来是创建了一个 JavaScript 的 `swup` 实例。把 `init` 去掉，发现不报错了，但是还是不行；随便写一个 `init`，发现还是没用。

中间经过了多少稀奇古怪的尝试我已经忘了。不过我是一点不慌，别问，问就是 Git 配享太庙。

## 福至心灵

一筹莫展之际，我又仔细翻了翻代码，发现了个正常到不能再正常的事情，就是 `document.addEventListener`。我不太了解 JavaScript，但是前几天写 Java+XML 的经验让我大致能猜出其意思。二者的绑定方式还有点像。

嗯？既然 `document.addEventListener` 是在页面加载完的时候进行，**那如果页面没加载完呢？更进一步，如果根本没加载呢？**

听上去荒谬，但是我瞬间来精神了。Swup 能做到切换这么丝滑，难道是根本没加载新的页面，只是做了点替换？

说干就干，我在我的 HTML 顶端加了条测试语句：

```html
<script>
    console.log("whisper.html");
</script>
```

然后重启本地服务器，打开控制台……果然没打印！

破案了家人们，这个 Swup 根本没加载新的页面——至少是没加载新页面的 JavaScript。而刷新会强制加载这个页面，所以就好使了；而前面的 `baseof` 的代码，就是让 Swup 接管这些加载活动。

那下面就想办法解决好了。我翻了半天，在[这里](https://swup.js.org/getting-started/reloading-javascript/)找到了解决方法（准确来说是被 issue 引过去的）。琢磨了一会儿，我决定采取省事的 Script Plugin。至于内存泄漏，算了先不管了。

```html
<script src="https://unpkg.com/@swup/scripts-plugin@2"></script>
{{/* ... */}}
<script data-swup-ignore-script>
    document.addEventListener('DOMContentLoaded', function() {
        const swup = new Swup({
            plugins: [
                new SwupPreloadPlugin(),
                new SwupScriptsPlugin()
            ]
        });
    });
</script>
```

速度慢的话可以自己去找镜像。

## 评论

其他部分都好了，就是这个评论还是不行。找了半天，发现是按钮本身绑定的 JavaScript 的事情。

首先把 Twikoo 的 CDN JavaScript 单独拎出来加载，然后再加一个钩子：

```js
swup.hooks.on('page:view', () => {
    const loadCommentsBtn = document.getElementById('load-comments-btn');
    if (loadCommentsBtn) {
        loadCommentsBtn.addEventListener('click', function () {
            const container = document.getElementById('comments-container');
            if (container) {
                container.style.display = 'block'; // 显示评论容器
                this.style.display = 'none'; // 隐藏按钮
            }
        });
    }
});
```

目前这个方案虽然还不完善，但是已经可以用了。

## 结语

本来打算明天在高铁上写的，但是太过激动，今天就写出来了。

明天大作业验收啦……祝我好运！