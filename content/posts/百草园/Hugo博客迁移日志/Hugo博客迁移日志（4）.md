---
title: Hugo博客迁移日志（4）
date: 2024-07-01
summary: 真·迁移日志（3）
description: 本文详细介绍了Hugo主题定制过程中的四个主要组件：公告、目录、简历和糖果雨特效。通过具体的代码示例和配置方法，文章指导读者如何实现这些组件的添加和功能扩展。包括了HTML模板的编辑、TOML配置文件的编写、CSS样式的调整以及JavaScript特效的实现。适合希望深入了解Hugo主题开发和自定义功能的读者。
categories: ["百草园"]
series: Hugo博客迁移日志
tags:
  - Hugo
  - 博客
  - Efímero
  - 折腾
slug: migrating-to-hugo-4
featuredImage: https://img.clnya.fun/migrating-to-hugo-4-cover.webp
draft: false
share: true
---
芜湖，各位老友们好啊，我是 Chlorine。接着上一回，继续为您说。

## 公告组件

下面的目标是为主题添加侧边栏组件。经过观察，这部分代码位于 `主题/layouts/partials/sidebar` 和 `主题/layouts/partials/sidebar.html` 中。不过使用循环来简化代码似乎有那么亿点点麻烦，所以还是先不管可扩展性，直接硬上吧。

在 `sidebar` 文件夹下添加一个 `announcement.html`：

```html
{{ $announcement := .Site.GetPage "announcement" }}
{{ with $announcement }}
<div class="markdown-body text-neutral-900 dark:text-neutral-100 text-center">
    {{ .Content | safeHTML }}
</div>
{{ end }}
```

在 `sidebar.html` 下添加：

```html
{{ if .Site.Params.Basic.announcement }}
<widget-layout id="announcement-widget" class="pb-4 card-base">
    <div
        class="font-bold transition text-lg text-neutral-900 dark:text-neutral-100 relative ml-8 mt-4 mb-2 before:content-[''] before:w-1 before:h-4 before:rounded-md before:bg-[var(--primary)] before:absolute before:left-[-16px] before:top-[5.5px]">
        公告
    </div>
    <div id="announcement-content" class="collapse-wrapper px-4 overflow-hidden">
        {{ partial "sidebar/announcement.html" . }}
    </div>
</widget-layout>
{{ end }}
```

这样直接编辑 `announcement.md` 就可以编辑公告了。当然，还需要配置 `.Site.Params.Basic.announcement` 参数。

## 目录组件

目录和公告大差不差：

```html
<div id="toc-container" class="
    toc text-neutral-900 dark:text-neutral-100 
    p-4 rounded-lg shadow-lg overflow-auto max-h-96 
    transition-all duration-300 ease-in-out hover:shadow-2xl
">
    <div id="toc-content" class="transition-all duration-500 ease-in-out">
        {{ .Page.TableOfContents }}
    </div>
</div>
```

就是这个样式不大好看，凑合用吧。

## 简历组件

这个相对麻烦。我不想在 HTML 里硬编码，于是想了半天后，决定使用 TOML 配置，大概就是：

```toml
[[params.social]]
    name = "Home"
    url = ""
    icon = "i-carbon-home"
    enable = true
[[params.social]]
    name = "Email"
    url = "mailto:your@email.com"
    icon = "i-carbon-email"
    enable = true
```

然后改一下 profile 的逻辑：

```html
<div class="card-base">
    <a aria-label="Go to About Page" href="{{ relURL "about/" }}" class="group block relative mx-auto mt-4 lg:mx-3 lg:mt-3 mb-3
       max-w-[240px] lg:max-w-none overflow-hidden rounded-xl active:scale-95">
        <div class="absolute transition pointer-events-none group-hover:bg-black/30 group-active:bg-black/50
        w-full h-full z-50 flex items-center justify-center">
            <div
                class="transition opacity-0 group-hover:opacity-100 text-white text-5xl i-mdi-card-account-details-outline">
            </div>
        </div>
        <div class="mx-auto lg:w-full h-full lg:mt-0 overflow-hidden relative">
            <div class="transition absolute inset-0 dark:bg-black/10 bg-opacity-50 pointer-events-none"></div>
            <img src="{{ relURL "/img/avatar.webp" }}" alt="Profile Image of the Author"
                class="w-full h-full object-center object-cover mx-auto lg:w-full h-full lg:mt-0" />
        </div>
    </a>
    <div class="font-bold text-xl text-center mb-1 dark:text-neutral-50 transition">{{ .Site.Params.Author.name }}</div>
    <div class="h-1 w-5 bg-[var(--primary)] mx-auto rounded-full mb-2 transition"></div>
    <div class="text-center text-neutral-400 mb-2.5 transition">{{ .Site.Params.Author.description }}</div>
    {{/* <div class="flex gap-2 mx-2 justify-center mb-4">
        <a aria-label="Home" href="" target="_blank" class="btn-regular rounded-lg h-10 w-10 active:scale-90">
            <div class="i-carbon-home text-xl"></div>
        </a>

    </div> */}}
    <div class="icons-container">
        {{ range .Site.Params.social }}
        {{ if .enable }}
        <a aria-label="{{ .name }}" href="{{ .url }}" target="_blank"
            class="btn-regular rounded-lg h-10 w-10 active:scale-90">
            <div class="{{ .icon }} text-xl"></div>
        </a>
        {{ end }}
        {{ end }}
    </div>

</div>
```

再写点美化的 CSS：

```css
.icon svg {
    height: 1em;
    width: 1em
}

.icons-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.icons-container a {
    margin: 5px;
    /* 调整图标之间的间距 */
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* 移动端样式 */
@media (max-width: 600px) {
    .icons-container a {
        margin: 4px;
        width: 30px;
        height: 30px;
    }
}

@media (max-width: 600px) {
    .card-base {
        flex-direction: column;
        padding: 0 1rem;
        gap: 0.5rem;
    }
}
```

就可以渲染社交图标了。

当初整这个的时候费了不少劲，主要的问题居然是我不知道图标不经过重新 UnoCSS 构建是不生效的（因此我安装了 UnoCSS 🤣）。以及，UnoCSS 不能检测没有在 HTML 中直接使用的图标，因此开了个 `utility.html` 来专门引入图标。

## 糖果雨特效

这个我在网上找了许多代码，最终在 Claude 等 AI 伙伴的帮助下写了出来。

新建一个 `candy.js`：

```js
// 糖果雨效果，一定要在 footer 中引入，否则由于页面未加载完成，无法获取到 body 元素

class Circle {
    constructor ({ origin, speed, color, angle, context }) {
        this.origin = origin
        this.position = { ...this.origin }
        this.color = color
        this.speed = speed
        this.angle = angle
        this.context = context
        this.renderCount = 0
    }

    draw() {
        this.context.fillStyle = this.color
        this.context.beginPath()
        this.context.arc(this.position.x, this.position.y, 2, 0, Math.PI * 2)
        this.context.fill()
    }

    move() {
        this.position.x = (Math.sin(this.angle) * this.speed) + this.position.x
        this.position.y = (Math.cos(this.angle) * this.speed) + this.position.y + (this.renderCount * 0.3)
        this.renderCount++
    }
}

class Boom {
    constructor ({ origin, context, circleCount = 10, area }) {
        this.origin = origin
        this.context = context
        this.circleCount = circleCount
        this.area = area
        this.stop = false
        this.circles = []
    }

    randomArray(range) {
        const length = range.length
        const randomIndex = Math.floor(length * Math.random())
        return range[randomIndex]
    }

    randomColor() {
        const range = ['8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        return '#' + this.randomArray(range) + this.randomArray(range) + this.randomArray(range) + this.randomArray(range) + this.randomArray(range) + this.randomArray(range)
    }

    randomRange(start, end) {
        return (end - start) * Math.random() + start
    }

    init() {
        for (let i = 0; i < this.circleCount; i++) {
            const circle = new Circle({
                context: this.context,
                origin: this.origin,
                color: this.randomColor(),
                angle: this.randomRange(Math.PI - 1, Math.PI + 1),
                speed: this.randomRange(1, 6)
            })
            this.circles.push(circle)
        }
    }

    move() {
        this.circles.forEach((circle, index) => {
            if (circle.position.x > this.area.width || circle.position.y > this.area.height) {
                return this.circles.splice(index, 1)
            }
            circle.move()
        })
        if (this.circles.length == 0) {
            this.stop = true
        }
    }

    draw() {
        this.circles.forEach(circle => circle.draw())
    }
}

class CursorSpecialEffects {
    constructor () {
        this.computerCanvas = document.createElement('canvas')
        this.renderCanvas = document.createElement('canvas')

        this.computerContext = this.computerCanvas.getContext('2d')
        this.renderContext = this.renderCanvas.getContext('2d')

        this.globalWidth = window.innerWidth
        this.globalHeight = window.innerHeight

        this.booms = []
        this.running = false
    }

    handleMouseDown(e) {
        const boom = new Boom({
            origin: { x: e.clientX, y: e.clientY },
            context: this.computerContext,
            area: {
                width: this.globalWidth,
                height: this.globalHeight
            }
        })
        boom.init()
        this.booms.push(boom)
        this.running || this.run()
    }

    handlePageHide() {
        this.booms = []
        this.running = false
    }

    init() {
        const style = this.renderCanvas.style
        style.position = 'fixed'
        style.top = style.left = 0
        style.zIndex = '999999999999999999999999999999999999999999'
        style.pointerEvents = 'none'

        style.width = this.renderCanvas.width = this.computerCanvas.width = this.globalWidth
        style.height = this.renderCanvas.height = this.computerCanvas.height = this.globalHeight

        document.body.append(this.renderCanvas)

        window.addEventListener('mousedown', this.handleMouseDown.bind(this))
        window.addEventListener('pagehide', this.handlePageHide.bind(this))
    }

    run() {
        this.running = true
        if (this.booms.length == 0) {
            return this.running = false
        }

        requestAnimationFrame(this.run.bind(this))

        this.computerContext.clearRect(0, 0, this.globalWidth, this.globalHeight)
        this.renderContext.clearRect(0, 0, this.globalWidth, this.globalHeight)

        this.booms.forEach((boom, index) => {
            if (boom.stop) {
                return this.booms.splice(index, 1)
            }
            boom.move()
            boom.draw()
        })
        this.renderContext.drawImage(this.computerCanvas, 0, 0, this.globalWidth, this.globalHeight)
    }
}

const cursorSpecialEffects = new CursorSpecialEffects()
cursorSpecialEffects.init()
```

再添加 CSS：

```css
.candy {
    position: absolute;
    width: 20px;
    height: 20px;
    background-color: #f00;
    border-radius: 50%;
    pointer-events: none;
}
```

引入即可。以及，点名批评 Hugo 奇葩的构建机制，JavaScript 就摆在那，愣是不加到 `public` 里，我也是没招了。

## 代码一键复制

这个属实是给我整得心力交瘁。好在最后在强大的 Claude 3.5 的帮助下写出来了。

开一个 `clickcopy.js`：

```js
(function () {
    'use strict';
    if (!navigator.clipboard) {
        return;
    }

    function createSVGIcon(iconName) {
        const svgNS = "http://www.w3.org/2000/svg";
        const svg = document.createElementNS(svgNS, "svg");
        svg.setAttribute("viewBox", "0 0 32 32");

        const path = document.createElementNS(svgNS, "path");
        if (iconName === "copy") {
            path.setAttribute("d", "M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z");
            const path2 = document.createElementNS(svgNS, "path");
            path2.setAttribute("d", "M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z");
            svg.appendChild(path2);
        } else if (iconName === "checkmark") {
            path.setAttribute("d", "M13 24L4 15 5.414 13.586 13 21.171 26.586 7.586 28 9 13 24z");
        }
        svg.appendChild(path);
        return svg;
    }

    function flashCopyMessage(el, msg, iconName) {
        var iconContainer = el.querySelector('.copy-icon');
        var msgContainer = el.querySelector('.copy-msg');

        // 更新图标
        iconContainer.innerHTML = '';
        iconContainer.appendChild(createSVGIcon(iconName));

        // 更新消息
        msgContainer.textContent = msg;

        setTimeout(function () {
            // 2秒后清除消息文本和图标变化
            msgContainer.textContent = '';
            iconContainer.innerHTML = '';
            iconContainer.appendChild(createSVGIcon('copy'));
        }, 2000);
    }

    function addCopyButton(containerEl) {
        if (containerEl.querySelector('.highlight-copy-btn')) {
            return;
        }

        var copyBtn = document.createElement("button");
        copyBtn.className = "highlight-copy-btn";
        copyBtn.setAttribute("aria-label", "Copy to clipboard");
        copyBtn.innerHTML = '<span class="copy-icon"></span><span class="copy-msg"></span>';
        copyBtn.querySelector('.copy-icon').appendChild(createSVGIcon('copy'));
        copyBtn.style.display = "none";

        var codeEl = containerEl.querySelector('code') || containerEl;
        copyBtn.addEventListener('click', function () {
            navigator.clipboard.writeText(codeEl.innerText).then(function () {
                flashCopyMessage(copyBtn, 'Copied!', 'checkmark');
            }, function (err) {
                console.error('Unable to copy: ', err);
                flashCopyMessage(copyBtn, 'Failed :\'(', 'copy');
            });
        });

        containerEl.appendChild(copyBtn);
        containerEl.style.position = 'relative';

        containerEl.addEventListener('mouseenter', function () {
            copyBtn.style.display = "block";
        });
        containerEl.addEventListener('mouseleave', function () {
            copyBtn.style.display = "none";
        });
    }

    // 添加复制按钮到所有代码块
    var codeBlocks = document.querySelectorAll('pre');
    Array.prototype.forEach.call(codeBlocks, addCopyButton);
})();
```

写 CSS：

```css
.highlight-copy-btn {
    position: absolute;
    top: 7px;
    right: 7px;
    border: 0;
    border-radius: 4px;
    padding: 5px;
    font-size: 0.8em;
    line-height: 1;
    background-color: transparent;
    /* 移除背景色 */
    color: inherit;
    /* 继承父元素的颜色 */
    cursor: pointer;
    opacity: 0.6;
    transition: opacity 0.3s;
}

.highlight-copy-btn:hover {
    opacity: 1;
}

.copy-icon {
    display: inline-flex;
    /* 使用 flex 布局以更好地控制图标 */
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
}

.copy-icon svg {
    width: 16px;
    height: 16px;
    fill: currentColor;
    /* 使用当前文本颜色填充SVG */
}

.copy-msg {
    margin-left: 5px;
    font-size: 12px;
}
```

然后引入就完事了。不过这个功能有时候需要刷新才能启动。

以及复制之后的按钮和文本有点偏移，但是我没力气调了。
