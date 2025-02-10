---
title: Hugo博客迁移日志（2）
date: 2024-06-29T21:30:00+08:00
summary: 真·迁移日志（1）
description: 本文介绍了作者对于从NotionNext迁移到Hugo的具体过程的简要叙述，包含对项目的总览、友链页面的构建、说说页面的构建等
categories: ["百草园"]
tags:
  - 博客
  - Hugo
  - 浮光
  - 折腾
featuredImage: https://img.clnya.fun/migrating-to-hugo-2-cover.webp
draft: false
share: true
slug: migrating-to-hugo-2
---
芜湖，各位老友们好啊，我是 Chlorine。接着上一回，咱们开始讲我从 NotionNext 迁移到 Hugo 的旅程。

## 项目整体结构

Hugo Landscape 的项目结构没有什么佶屈聱牙的地方，很正常的 Hugo 主题结构……除了 `layouts` 下面有一个单独的 `posts/single.html`？我也不知道这个算不算特别。

这个主题最经典的地方在于：**它使用的是 UnoCSS**。啥是 UnoCSS？行吧我也不是很懂，似乎就是一个高度原子化、依赖于 HTML 对象的 CSS。反正挺 OOP 的。

那就先安装个 UnoCSS 吧。直接在主题文件夹下：

```bash
npm install
```

完事。就安装好了一大堆依赖。

*其实我一开始的时候没有做这个，后续我会讲具体经过。*

为了后续开发方便，我使用 OOP 课程的知识，写了个简单的 Makefile：

```makefile
# 默认目标
all: theme hugo

# Hugo构建
hugo:
hugo server -D

# 主题构建
theme:
cd themes/efimero && npm run build && cd ../..

# 清理构建文件
clean:
rm -rf public
rm -rf resources/_gen
cd themes/efimero && rm -rf node_modules
cd ../..

# 帮助信息
help:
@echo "可用的make目标："
@echo "  all: 默认目标，构建 Hugo 和主题"
@echo "  hugo: 构建 Hugo"
@echo "  theme: 构建主题"
```

这样每次更新功能要预览的时候，直接 `make` 就完事了。

## 友链页面

没错，在不细品项目的情况下，直接开冲，主打一个勇。

~~就算是品了我也品不懂，毕竟我对前端一窍不通。~~

友链页面是我的必需品。还是老办法，用一个 `JSON` 文件存储信息，放在 `主题/static/jsons/friends.json`。格式大概是：

```json
{
    "name": "名字",
    "note": "注释",
    "url": "网址",
    "md5": "邮箱的 MD5 值，用来从 Cravatar 获取头像",
    "des": "描述/签名",
    "ava": "/avatars/头像.webp，在没有 MD5 的情况下用这个"
}
```

然后搬出我的祖传 shortcode：

```html
{{ $friends := getJSON "themes/efimero/static/jsons/friends.json" }}
<div class="friend-link-container">
    {{ range $friends.friend}}
    <div class="friend-link" style="background-image: url('{{ .avatar }}');">
        <a href="{{ .url }}" target="_blank">
            <img src="{{ with .ava }}{{ if ne . "" }}{{ . }}{{ else }}https://cravatar.cn/avatar/{{ .md5 }}{{ end }}{{ else }}https://cravatar.cn/avatar/{{ .md5 }}{{ end }}"
                alt="{{ .name }}" class="friend-link-avatar">
        </a>
        <div class="friend-link-content">
            <h3><a href="{{ .url }}" target="_blank">{{ .note }}（{{ .name }}）</a></h3>
            <p>{{ .des }}</p>
        </div>
    </div>
    {{ end }}
</div>
```

既然是换新主题了，肯定得写个好看的样式。`主题/assets/css` 下新建一个 `addon.css`，扔进去：

```css
.friend-link-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.friend-link {
    width: calc(50% - 10px);
    border: 1px solid #ccc;
    border-radius: 10px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    padding: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    height: auto;
    max-height: 150px;
    background-size: cover;
    background-position: center;
}

@media screen and (max-width: 768px) {
    .friend-link {
        width: 100%;
    }
}

.friend-link-avatar {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    margin-right: 10px;
}

.friend-link-content {
    display: flex;
    flex-direction: column;
}

.friend-link-content h3 {
    margin: 0;
    padding: 0;
    font-size: 20px;
    color: #333;
}

.friend-link-content p {
    margin: 0;
    padding: 0;
    font-size: 16px;
    color: #666;
    word-wrap: break-word;
}
```

当然，不能忘了包含这个 CSS。Landscape 采用的是 `css.html` 专门包含 CSS，嗯，我很喜欢。

最终出来的效果还是很好看的，详见我的友链页面。哦，别忘了新建一个 Markdown 文件，包含这个短代码。

## 说说

关于怎么搞说说，我属实是折腾了 N 多天，最终还是靠着[恐咖兵糖](https://www.ftls.xyz/)大佬的方案，经过一顿折腾之后得到的还算满意的 solution。

首先，让我们科普一个概念：**联邦宇宙**。

搬运 Wiki：

> 联邦宇宙（英语：Fediverse，简称Fedi）在英文中是“联邦”（Federation）和“宇宙”（Universe）的混成词。联邦宇宙由一系列自由软件组成，有一组互联的服务器（用户自建或第三方托管），一起提供网络发布（如社交媒体、微博、博客或者网站）或者文件托管功能。虽然各个服务器是独立运行的，且各个实例繁多，内容多样， 但服务器之间可以彼此互通。在不同的服务器（实例）上，用户可以创建不同帐号。这些帐号能够跨越实例边界而通信，因为服务器上运行的软件支持一种或多种遵循开放标准的通信协议。 用户通过联邦宇宙中的帐号，可以发布文本或者其他媒体文件，也可以关注其他用户。在某些情况下，用户可以公布或分享数据（如音频、视频、文本文件等），使其对所有或部分人开放并允许他们共同编辑内容（例如日历和黄页）。
>
> 联邦宇宙的目的是建立在网络社交巨头公司之外， 提供另一种交流方式。与在单一服务器上运行的传统社交网络相比，联邦宇宙的运行方式更开放。 其服务器的分散性，使联邦宇宙更安全可靠。

简单来说，就是一系列去中心化（准确来说应该算是联邦化或者多中心化）的自由软件组成的庞大社交网络。我对去中心化网络非常感兴趣，后续如果系统学习，会把心得分享出来（`画大饼.webp`）。

联邦宇宙主要由四大通讯协议支持：

- ActivityPub
- Diaspora Network
- OStatus
- Zot & Zot/6

我们要用的是第一个。ActivityPub 协议的代表软件是 [Mastodon](https://mastodon.social/)（中文名：长毛象/乳齿象），简单来说就是联邦宇宙的 Twitter（𝕏）。Mastodon 虽然成熟，但是比较笨重，不利于自托管（虽然说咱们也不用自托管就是了），而且国内可用的实例比较少。所以，我们选择 ActivityPub 协议的另外一个实践者—— [GoToSocial](https://gotosocial.org/)。

GoToSocial 不多介绍。直接上解决方案：

1. 注册一个国内的 GTS 实例，例如我用的 [https://scg.owu.one](https://scg.owu.one)。
2. 获取鉴权 Token，直接在[这里](https://takahashim.github.io/mastodon-access-token/)操作即可。

好的，下面开始爆改。具体的操作步骤等我专门写一个说明文档（或许是主题的说明文档？）。

上一个 shortcode：

```html
<style>
    .toots-container {
        margin: 0 auto;
        max-height: fit-content;
    }

    .toot {
        margin-bottom: 10px;
    }

    .toot .avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin-right: 15px;
    }

    .toot-info {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }

    .toot-stats {
        display: flex;
        justify-content: flex-end;
        /* 将元素靠右对齐 */
    }

    .toot-stats i {
        margin-right: 3rem;
    }

    .basic-field-status {
        border: 1px solid #2d97bd86;
        border-radius: 30px;
        background-color: rgba(255, 255, 255, 0.05);
    }

    .basic-avatar img {
        position: absolute;
        z-index: 2;
        object-fit: cover;
        width: 100px;
        height: 100px;
        left: calc(50% - 50px);
    }

    .basic-avatar img {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        top: 0;
        z-index: 1;
        overflow: hidden;
        object-fit: cover;
    }

    .basic-avatar img:hover {
        position: absolute;
    }

    .basic-avatar {
        height: 120px;
    }

    /* Media Query for Mobile Devices */
    @media only screen and (max-width: 600px) {
        .header {
            height: 150px;
            padding: 10px;
        }

        .toots-container {
            padding: 10px;
        }

        .toot .avatar {
            width: 40px;
            height: 40px;
        }

        .avatar {
            width: 100px;
            height: 100px;
        }

        .basic-info {
            margin-left: 2px;

        }
    }

    @media only screen and (max-width: 430px) {

        .basic-avatar::before,
        .basic-avatar::after {
            display: none;
        }

        .basic-text {
            margin-top: 100px;
            margin-left: -25px;
        }

        .basic-avatar img {
            margin-right: 10px;
            display: none;
        }
    }

    .mdi--reply {
        display: inline-block;
        width: 1.3em;
        height: 1.3em;
        --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M10 9V5l-7 7l7 7v-4.1c5 0 8.5 1.6 11 5.1c-1-5-4-10-11-11'/%3E%3C/svg%3E");
        background-color: currentColor;
        -webkit-mask-image: var(--svg);
        mask-image: var(--svg);
        -webkit-mask-repeat: no-repeat;
        mask-repeat: no-repeat;
        -webkit-mask-size: 100% 100%;
        mask-size: 100% 100%;
    }

    .mdi--star {
        display: inline-block;
        width: 1.3em;
        height: 1.3em;
        --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.62L12 2L9.19 8.62L2 9.24l5.45 4.73L5.82 21z'/%3E%3C/svg%3E");
        background-color: currentColor;
        -webkit-mask-image: var(--svg);
        mask-image: var(--svg);
        -webkit-mask-repeat: no-repeat;
        mask-repeat: no-repeat;
        -webkit-mask-size: 100% 100%;
        mask-size: 100% 100%;
    }

    .mdi--twitter-retweet {
        display: inline-block;
        width: 1.3em;
        height: 1.3em;
        --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M6 5.75L10.25 10H7v6h6.5l2 2H7a2 2 0 0 1-2-2v-6H1.75zm12 12.5L13.75 14H17V8h-6.5l-2-2H17a2 2 0 0 1 2 2v6h3.25z'/%3E%3C/svg%3E");
        background-color: currentColor;
        -webkit-mask-image: var(--svg);
        mask-image: var(--svg);
        -webkit-mask-repeat: no-repeat;
        mask-repeat: no-repeat;
        -webkit-mask-size: 100% 100%;
        mask-size: 100% 100%;
    }
</style>

<body>
    <br>
    <div id="toots-content" class="toots-container">
        <div class="toot" id="toots">
        </div>
        <i id="toots-loading" class="fa fa-spinner fa-pulse fa-3x fa-fw" style="display: none;place-items: center;">
            <svg xmlns="http://www.w3.org/2000/svg" width="5em" height="5em" viewBox="0 0 256 256">
                <path fill="currentColor"
                    d="M128 24a104 104 0 1 0 104 104A104.11 104.11 0 0 0 128 24m39.11 25.19C170.24 83.71 155 99.44 135 113.61c-2.25-24.48-8.44-49.8-38.37-67.82a87.89 87.89 0 0 1 70.5 3.4ZM40.18 133.54c28.34-20 49.57-14.68 71.87-4.39c-20.05 14.19-38.86 32.21-39.53 67.11a87.92 87.92 0 0 1-32.34-62.72m136.5 67.73c-31.45-14.55-37.47-35.58-39.71-60c12.72 5.86 26.31 10.75 41.3 10.75c11.33 0 23.46-2.8 36.63-10.08a88.2 88.2 0 0 1-38.22 59.33" />
            </svg>
        </i>
        <button id="toots-moreButton" onclick="tootsShowMore()"><a>更多</a></button>
    </div>
</body>

<script type="text/javascript" src="/js/time-fmt.min.js"></script>
<script>
    let maxId = null; // 初始值为 null，表示第一页
    let isFirst = true; // 首次加载
    const tootsDiv = document.getElementById('toots');
    const tootsMoreButton = document.getElementById('toots-moreButton');
    const tootsLoading = document.getElementById('toots-loading');
    const urlObject = new URL(window.location.href);
    const idValue = urlObject.searchParams.get("id");

    // 获取 Mastodon 用户公开Toots 限制条数 默认5 排除回复 toot
    async function getPublicToots() {
        let limit = "{{ .Get 2 | default 5 }}";

        if (idValue != null && isFirst) {
            isFirst = false;
            const response = await fetch("{{ .Site.Params.Whisper.instance }}/api/v1/statuses/" + idValue, {
                headers: {
                    'Authorization': "Bearer {{ .Site.Params.bot_token }}"
                }
            })
            const toot = await response.json();
            return [toot];
        }

        const queryParams = maxId ? (`?limit=${limit}&max_id=${maxId}`) : "?limit=" + limit;
        const response = await fetch("{{ .Site.Params.Whisper.instance }}/api/v1/accounts/{{ .Site.Params.Whisper.user_id }}/statuses" + queryParams + "&exclude_replies=true", {
            headers: {
                'Authorization': "Bearer {{ .Site.Params.Whisper.bot_token }}"
            }
        })
        const toots = await response.json();
        return toots;
    }

    // 解析ULID
    function parseULID(ulid) {
        const base32Chars = '0123456789ABCDEFGHJKMNPQRSTVWXYZ';
        const timestamp = parseInt(ulid.slice(0, 10).split('').map(char => base32Chars.indexOf(char)).map(index => index.toString(2).padStart(5, '0')).join(''), 2);
        const randomPart = ulid.slice(10);

        return {
            timestamp: new Date(timestamp),
            randomPart: randomPart
        };
    }

    // 将Toots显示在页面上
    async function displayToots() {
        try {
            tootsLoading.style.display = "grid";
            tootsMoreButton.style.display = 'none';
            const toots = await getPublicToots();
            if (toots && toots.length > 0) {
                displayBioProfile(toots[0]);
                toots.forEach(toot => {
                    // console.log(parseULID(toot.id)); // 解析 ULID
                    const tootDiv = document.createElement("div");

                    tootDiv.classList.add("toot");

                    const tootInfoDiv = document.createElement("div");
                    tootInfoDiv.classList.add("toot-info");

                    const tootAvatar = document.createElement("div");
                    tootAvatar.classList.add("toot-avatar");

                    const profileImage = document.createElement("img");
                    profileImage.src = "{{ .Site.Params.Author.avatar }}";
                    profileImage.classList.add("avatar");
                    profileImage.alt = toot.account.display_name;

                    const tootProfileDiv = document.createElement("div");
                    tootProfileDiv.innerHTML = `<strong>${toot.account.display_name}</strong> <a href="${toot.url}" target="_blank">@${toot.account.acct}</a><br><small>${formatTime(toot.created_at)}</small>`;

                    tootAvatar.appendChild(profileImage);
                    tootInfoDiv.appendChild(profileImage);
                    tootInfoDiv.appendChild(tootProfileDiv);

                    const contentDiv = document.createElement("div");
                    contentDiv.classList.add("toot-content");
                    contentDiv.innerHTML = toot.content.replace(/<img/g, '<img loading="lazy" class="toot-img"');
                    // contentDiv.innerHTML = toot.content;

                    // media  loading="lazy"
                    for (let i = 0; i < toot.media_attachments.length; i++) {
                        const media = toot.media_attachments[i];
                        contentDiv.innerHTML += `<img loading="lazy" src="${media.url}">`;
                    }

                    const tootStats = document.createElement("a");
                    tootStats.href = toot.url;
                    tootStats.target = "_blank";
                    {
                        {/*  tootStats.className = "toot-stats";
                    if (toot.replies_count + toot.favourites_count + toot.reblogs_count != 0) {
                        tootStats.innerHTML += `<span class="mdi--reply"></span> ${toot.replies_count}  `;
                        tootStats.innerHTML += `<span class="mdi--star"></span> ${toot.favourites_count}  `;
                        tootStats.innerHTML += `<span class="mdi--twitter-retweet"></span> ${toot.reblogs_count}`;
                    }  */}
                    }

                    const statsDiv = document.createElement('div');
                    statsDiv.classList.add('toot-stats');
                    statsDiv.innerHTML = `
                    <span class="mdi--reply"></span> ${toot.replies_count}  
                    <span class="mdi--star"></span> ${toot.favourites_count}  
                    <span class="mdi--twitter-retweet"></span> ${toot.reblogs_count}
                `;

                    const hr = document.createElement("hr");
                    hr.style = "margin: 0.4rem 0;"

                    // 评论锚点
                    // const commentAnchor = document.createElement("div");

                    tootDiv.appendChild(tootInfoDiv);
                    tootDiv.appendChild(contentDiv);
                    tootDiv.appendChild(tootStats);
                    tootDiv.appendChild(statsDiv);
                    tootDiv.appendChild(hr);

                    tootsDiv.appendChild(tootDiv);
                    maxId = toot.id; // 更新最大 ID
                    // 如果 只有一个 自动打开评论区
                    if (toots.length == 1) {
                        initArtalk(commentAnchor, toot);
                    }
                });
                tootsMoreButton.style.display = 'block';
            } else {
                tootsMoreButton.style.display = 'none';
            }
        } catch (error) {
            console.error('获取 Toots 时出错：', error);
            tootsDiv.innerHTML += error.message;
        }
        tootsLoading.style.display = "none";
    }

    function tootsShowMore() {
        displayToots();
    }

    function displayBioProfile(statuse) {
    }

    displayToots();
    // 页面加载时调用显示Toots函数
    // window.onload = displayToots;
    window.ViewImage && ViewImage.init('.toot-img');
</script>
```

在站点配置 TOML 中加入相关数据：

```toml
# 联邦宇宙的说说参数
[params.whisper]
    instance = "你的实例名称"
    user_id = "你的 ID"
    bot_token = "你的 Token"
```

开一个 Markdown，加入短代码，完事。

别看我现在说得轻巧，当初折腾的时候不知道费了多少劲。

今天先说这两个，剩下的明天再说。
