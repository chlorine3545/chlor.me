---
title: 如何为NotionNext Hexo主题添加文章封面图
date: 2024-02-09 12:00:00
categories: 百草园
tags:
  - 教程
  - 博客
  - Javascript
  - NotionNext
summary: 为 NotionNext 的 Hexo 主题添加头图。
description: 本文记录了作者为 Hexo 主题 NotionNext 添加文章详情页封面图的过程。受 Matery 主题启发，作者通过修改 PostHeader.js 文件，成功实现了封面图的显示，并调整了背景透明度和样式。为优化性能，作者还关闭了 Live2D 看板功能。最终，作者通过多次尝试解决了封面图加载问题，实现了美观的文章详情页设计。
slug: how-to-add-header-img-to-notionnext-hexo
---
嗨，大家好，我是 Chlorine.

先行给大家拜个年🎉晚上我会发完整的拜年公告的~

本期依然是寄术力不高的瞎折腾，内容是为 NotionNext 的 Hexo 主题文章详情页添加封面图。如果您是精通 JS 的大佬，请略过.

在刚开始使用 NotionNext 的时候，我最喜欢的是 Matery 主题，有着很漂亮的 Hero 图和文章卡片。但是随着时间的推移，能显示作者介绍，整合类 Algolia 搜索的 Hexo 主题开始渐渐更得我心，更别提 Matery 每次进入文章页面文章内容还会灵性地左移一下，于是我把主题换成了 Hexo.

但是我很快发现了一个问题:**Hexo 主题没有文章封面图**.

容我解释一下: 文章卡片两个主题都是有的，但是在文章详情页，二者的表现有所不同:

![](https://img.clnya.fun/IMG-20240209120000-1.webp)
![](https://img.clnya.fun/IMG-20240209120000-2.webp)

显然是有封面图显示更漂亮.

而加封面图这种小事也不好意思去麻烦人家开发大大，于是我决定自力更生.

我们进入 Github, 找到 `themes/hexo` 文件夹，这里就是 Hexo 主题的配置文件夹.

我一向不喜欢 Hexo 显示 categories 的功能，因此在一顿试探之后，我发现了控制这个功能的代码，位于 `config.js` 中:

```js
HEXO_HOME_NAV_BUTTONS: true, // 首页是否显示分类大图标按钮
  // 已知未修复bug, 在移动端开启true后会加载不出图片； 暂时建议设置为false。
  HEXO_HOME_NAV_BACKGROUND_IMG_FIXED: false, // 首页背景图滚动时是否固定，true 则滚动时图片不懂动； false则随鼠标滚动 ;
  // 是否显示开始阅读按钮
  HEXO_SHOW_START_READING: true,
```

好好好，更有理由改成 false 了🤣

我猜测，加入头图之后很可能加重加载负担，因此我把 live2D 的看板关了.

在我们的中心配置文件 `blog.config.js` 中第 205 行左右的位置找到:

```js
// 悬浮挂件
  WIDGET_PET: process.env.NEXT_PUBLIC_WIDGET_PET || true, // 是否显示宠物挂件
  WIDGET_PET_LINK:
        process.env.NEXT_PUBLIC_WIDGET_PET_LINK ||
        'https://cdn.jsdelivr.net/npm/live2d-widget-model-wanko@1.0.5/assets/wanko.model.json', // 挂件模型地址 @see https://github.com/xiazeyu/live2d-widget-models
  WIDGET_PET_SWITCH_THEME: process.env.NEXT_PUBLIC_WIDGET_PET_SWITCH_THEME || true, // 点击宠物挂件切换博客主题
```

把 `WIDGET_PET: process.env.NEXT_PUBLIC_WIDGET_PET` 那行改成 false 即可.

下面正式进入魔改环节。作为不会 JavaScript 的小杂鱼，我采取的依然是 [blog&amp;随笔/如何在不懂CSS的情况下魔改Typora主题|魔改 Typora 主题时](blog&随笔/如何在不懂CSS的情况下魔改Typora主题|魔改%20Typora%20主题时)的方法: 瞪眼法.

我仔细观察了整个 hexo 文件夹的结构，最后从名字上猜测 `components/PostHeader.js` 很可能与这件事有关.

点进去，发现 21 行左右这块很可能和头图有关:

```js
const headerImage = post?.pageCover ? post.pageCover : siteInfo?.pageCover

  return (
    <div id="header" className="w-full h-96 relative md:flex-shrink-0 z-10" >
      <LazyImage priority={true} src={headerImage} className='w-full h-full object-cover object-center absolute top-0'/>

      <header id='article-header-cover'
            className="bg-black bg-opacity-70 absolute top-0 w-full h-96 py-10 flex justify-center items-center ">
```

嗯，从字面上就能猜出来，这块设置了一个透明度是 70%的黑色背景，那能显示头图就出鬼了.

我们找到 Matery 的相应文件，发现这里是:

```js
import LazyImage from '@/components/LazyImage'
import NotionIcon from '@/components/NotionIcon'

/**
 * 文章背景图
 */
export default function PostHeader({ post, siteInfo }) {
  const headerImage = post?.pageCoverThumbnail ? post?.pageCoverThumbnail : siteInfo?.pageCover
  const title = post?.title
  return (
        <div id='header' className="flex h-96 justify-center align-middle items-center w-full relative bg-black">
            <div className="z-10 leading-snug font-bold xs:text-4xl sm:text-4xl md:text-5xl md:leading-snug text-4xl shadow-text-md flex justify-center text-center text-white">
                <NotionIcon icon={post?.pageIcon} />{title}
            </div>
            <LazyImage alt={title} src={headerImage} className='pointer-events-none select-none w-full h-full object-cover opacity-30 absolute'
                placeholder='blur' blurDataURL='/bg_image.jpg' />
        </div>
  )
}
```

这里明显就是有头图的.

在经过锲而不舍的~~胡乱~~尝试+询问 AI 之后，我发现了正确的改动方法:

```js
// 文章全屏隐藏标头
  if (fullWidth) {
    return <div className='my-8'/>
  }

  const headerImage = post?.pageCoverThumbnail ? post.pageCoverThumbnail : siteInfo?.pageCover

  return (
    <div id="header" className="w-full h-96 relative md:flex-shrink-0 z-10" >

      <div className="absolute inset-0 bg-black bg-opacity-70"></div>
      <LazyImage alt={post?.title} src={headerImage} className='w-full h-full object-cover absolute top-0 opacity-30'/>
  
      <header id='article-header-cover'
            className="absolute top-0 w-full h-96 py-10 flex justify-center items-center ">
```

这样就可以在 Hexo 主题也显示好看的封面了捏~

PS: 列一下我踩过的愚蠢的坑:

1. 直接拷贝 Matery 的代码
2. 不会加黑色蒙版
3. 乱改模糊加载导致错误
4. 以下省略 114514 条 ()
