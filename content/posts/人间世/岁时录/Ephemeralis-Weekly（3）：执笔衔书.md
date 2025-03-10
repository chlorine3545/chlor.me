---
slug: weekly-3
datetime: 2024-07-22 19:17
summary: 浮生散记第三期
series: 岁时录
tags:
  - 博客
  - 周报
  - 开源
  - 日常
cover_image_url: https://img.clnya.fun/cover/weekly-3-cover.webp
title: Ephemeralis-Weekly（3）：执笔衔书
date: 2024-07-22
description: 本文是作者周报的第三期，作者分享了他参与小学期课程的大作业开发新闻客户端的经历。他通过学习教程、魔改代码，克服了时间紧迫和自身知识短缺的困难，最终成功完成了作业。此外，作者还谈到了他的梦想是成立一个自己的开源基金会，并介绍了自己最近想学习的新的编程语言Rust以及他喜欢的美食烤冷面。
categories: ["人间世"]
featuredImage: https://img.clnya.fun/cover/weekly-3-cover.webp
draft: false
share: true
---
各位老友们好，我是 Chlorine。

本文为园子周报——Ephemeralis Weekly（浮生散记）的第三期，日期范围为公历 2024 年 7 月 15 日至 7 月 21 日。祝食用愉快。

## 「衔书」

这个标题听起来蛮有诗意的，但是实际过程没那么有诗意。

简单来说，我们的「小学期」课程——《程序设计训练》的大作业，要求是使用 Java 开发一个新闻客户端，要求实现新闻爬取、列表展示、详情页面、图片/视频展示、AI 摘要、历史记录、收藏功能、上拉获取、下拉刷新、本地缓存和搜索等功能。

听上去有那么亿点可怕，更何况我们从结课到交作业只有十天左右的时间，而课程本身也只有十天。十天，要讲明白最受欢迎的企业级编程语言之一，谈何容易？就算是老师尽力输出，也只能带我们浮光掠影地看个大概。

更何况，我是个上课从来不听的摆子人。

---

一开始我基本上毫无头绪，有一种即将入土为安的美感。我甚至连 Android Studio 都不会用。所幸，我的一位同学告诉我：可以去 B 站上找相关的教程（B 站真的是个学习网站呐 :D）。然后我就去找了，嘿，您猜怎么着？真找到了，而且是手把手的教程！（这里感谢一下教程的作者 [@浩宇软件开发](https://space.bilibili.com/492354901)，如果没有他的教程我必 4 无疑）。

事实证明：面对一门你完全不熟悉的语言的时候，照葫芦画瓢加魔改永远是最好的方法。就像我们写 C++ 代码的时候：

```cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
```

刚开始谁又能说清楚什么是预处理指令、命名空间、流运算符？还不是先「当成八股文写下来」（来自我的程序设计基础课程老师），然后再一点点理解？

继续。我照着教程的代码一点点敲下来，中间不断地魔改，来适应作业的要求和我自己的审美。随着作业进程的推进，我写得越发得心应手，常常一天更新四五个功能，很多部分实际上已经完全是自己在独立开发了。用我报告的话来说，就是：

> 从看着什么都没有的用户界面直龇牙，到开始细致地考虑美工和设计；从什么都需要翻 CheatSheet、查教程、问 AI，到能为别人解惑答疑；从「做出来就行」到「做个还行的就行」到「必须得做个好的」

最终，我花了六天左右的时间，完成了这份看起来极其恐怖的作业，以及用心到让人无法直视的报告（上万字，导出为 PDF 整整一百页，这个长度在整个 Java 课程历史上应该可以空前绝后了）。我将最终的产品取名为「衔书」（Xianshu 或 Tsira News）。

不过其实我最想说的还不是产品开发的过程本身，而是我这几天的状态。

刚开始时，为了学习效率，我尝试去三教自习。找了一圈没找到空教室，只好随便找了个人少的地方。此后几天，如果没有特殊情况，我一直都在这个位置。

架好电脑，戴上耳机，平心静气地不停地敲着。一个功能，一个功能，又是一个功能。我就这么一点点解决遇到的问题，兵来将挡，水来土掩，顺滑得行云流水，道法自然。

这种美好的学习状态，上次还是在我高中的时候。我感觉那个工作效率爆表的我又回来了。

口说无凭。在这六天的时间里，我写完了包含几千行（估计的）代码的 Android 应用，完成了数万字的报告，还顺带着帮班级的思政实践写好几千字的预调研报告，还顺带着帮几个同学答了下疑。

有人可能会将这看成「DDL 是第一生产力」，但是就我个人的感觉来看，这就是这几天的状态的优越。

总而言之，这几天是卷得神清气爽，果然我的学习血脉还是在的~

## I Have A Dream

「I have a dream」，我有一个梦想，简单的英语句子，因美国黑人平权运动先驱马丁·路德·金（Martin Luther King Jr.）于 1963 年在华盛顿特区林肯纪念堂前发表的演讲而举世闻名。

金是一位杰出的社会活动家，他的梦想就是实现社会的正义与平等。我没有如此的社会责任、胸怀与热忱，但是我也有一个梦想：成立一个自己的开源基金会。

容我多说几句吧。

我一直是一个典型的「没什么理想」的人，具体来说，我没有什么明确的目标和方向。就连当初选择计金，也可以算是一个「一时兴起」的决定。

但是我也做过梦，一个听起来挺中二的梦——「追逐人类心智的荣耀」。

我对科研的兴趣应当起源于我初三和高一的时候。我们初三开始学化学，至少在考试方面，我展现出了相当出色的化学天赋，以至于初三后期老师开始明令禁止我听课（她认为这样是在浪费我的时间 LOL）。高中时期，我的班主任就是化学老师。我曾经在刚开学的时候——他刚刚注意到我的时候对他说，我想学化学。他说，好，那就报北大的化学系（准确来说应该是「化学与分子工程学院」，我对北大许久的好感就是从这一刻开始的。当然，那是另一个故事了）。

于是乎我有了自己的第一个梦——化学，做最顶尖的化学家。我当时不在乎什么冷门热门，只是感觉自己喜欢（毕竟，清北的学生——我当时多少是带点自傲的，觉得自己能在三年后稳拿清北——还能饿死不成？多天真的想法啊）。有喜欢的事情，就是幸福啊。

请允许我省略中间的故事。我的梦几度变易，从化学，到物理，到数学，到统计。唯一没变的，就是我那份中二的科学家的心。

后来，我的中二又有了新的高度。我不再满足于「做科研就完事了」，我希望我能「追逐人类心智的荣耀」——用自己的努力，为人类知识的边界开疆拓土，将有限的一生奉献于无限的探索中。

听上去……确实挺好的。

然后这么梦在高考后醒了。

不是说我发挥失常，我考得还不错，已经可以在清北随便选专业了。我曾经一度想报考我梦想的地方——北大元培，但是最终我去了清华电子，后来又去了计金，读了两个我曾经最不喜欢的专业。

个中曲折，我也不希望在此细说了。总而言之，我收获了许多，唯独把我曾经中二而热烈的梦想丢掉了。

一件事如果不喜欢，又没有长久的目的，是很难做下去的。我在计金的学业并不突出，可能也有这个原因（~~不要把自己的弱鸡归因于其他~~）。

然而，作为一个从没接触过计算机的小镇做题家，在我高强度（迫真）写了一年代码后，我反而感觉这门学科还是蛮有意思的。以及在不断的不务正业中，我接触到了另一个奇妙的世界——开源宇宙。

开源宇宙确实是个奇妙的地方。各路精英大佬各显神通，做出令人惊艳的产品，然后把源代码交给社区。而开源社区的精神，也是极为具有感染性的：自由，开放，协作，探索，行动。

恍惚之间，我感觉当年离我而去的梦，又以另一种形式回来了。

一个是贡献理论知识，一个是贡献代码和产品，都是崇高的事业，值得人奉献一生的事业。

于是，我想着，将来是否有这个机会，成立一个自己的开源基金会？

这个设想基本和成为世界级科学家一个难度，而且我对开源团体的运作机制完全不了解。可能我更想表达的是一个社团，一群志同道合的人合作开发令人惊艳的产品，依靠社区的支持完成运作和对成员生活的补益。

但是我就是这么想了，甚至还给「基金会」起了一个名字，叫「青若」（Tsira）。这个词汇没什么特别的含义，就是我一拍脑袋想出来的。硬要说，就是致敬我的母校清华大学（Tsinghua University）。

这个新闻客户端，也是第一个还算能叫「产品」的产品。我为它冠上了 Tsira 的词头，并且在签名证书的单位上郑重地写下：Tsira Open Source Foundation。

我不知道这是不是又会成为我无数个胎死腹中的梦想之一，咱们暂且先看着吧。

## 学门新语言？

最近相对比较闲，就想着学门现代化的语言，来满足自己开（zhē）发（teng）的欲望。环顾一圈，现代化，高性能，还能写美观的跨平台应用，那首选应该就是开源世界的新宠——Rust 了。

![](https://img.clnya.fun/weekly-3.avif)

于是我准备试一试 Rust。然后我就疯了。

都说 Rust 在所有权、生命周期这块难，但是从一开始我就觉得，Rust 的语法怎么看怎么别扭……

都变量了，为什么还要显式声明可变？为什么打印是宏？这导入用的什么格式？为什么变量可以自动类型推导常量就不行？为什么……

行吧，Rust 有自己的美，但是目前我是理解不了一点。

所以现在还剩下 Swift（需要烦人的 Xcode）、Go、Dart、Kotlin 等这些。要是各位知道什么语法和 C++ 相似（但是更简单），同时还比较优雅的现代语言，可以给我推荐一下。

## 烤冷面

作为辽宁人，烤冷面属于一个我不常吃但是挺喜欢的美食。来了北京之后很少吃，一般都是去 C 楼地下买。后来尊敬的崔博士（我在协和读临床本博八年的同学）带我去桃李园吃了一次，只能说过得去，但是胜在便宜实惠。

最近我在饿~~似~~了么发现了一家烤冷面，做得相当好吃，于是这周点了好几份。虽说贵了点，但是人家好吃啊~
