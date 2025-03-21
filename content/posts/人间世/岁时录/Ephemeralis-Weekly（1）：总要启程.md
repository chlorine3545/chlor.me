---
title: Ephemeralis-Weekly（1）：总要启程
date: 2024-06-30
summary: 浮生散记第一期
description: 本文是作者的博客周报「浮生散记」（Ephemeralis Weekly）的第一期，内容是作者重开周报的考虑、作者本周的生活情况，包括写各种大作业的过程、重启 Hugo 博客的过程，以及与家人分别的不舍和思考。
categories: ["人间世"]
series: 岁时录
tags:
  - 周报
  - 备案
  - 学习
slug: weekly-1
featuredImage: https://img.clnya.fun/cover/weekly-1-cover.webp
draft: false
share: true
---
各位老友们好，我是 Chlorine。

本文是沉寂已久的周报——Ephemeralis Weekly（浮生散记）重启后的第一期，日期范围为公历 2024 年 6 月 24 日至 6 月 30 日。

祝食用愉快。

## 为什么重启？

这件事，说来话长。

许多博客都有「周报」或者是其他时间周期的文章，于是在我刚刚建成博客不久后，我也兴冲冲地开了一个周报栏目，并且起了一个很矫情的名字——浮生散记（Ephemeralis Weekly）。

当时的我是怀着怎样的一番热血，现在我早已经忘却了。剩下的唯有令人尴尬的事实——「浮生散记」只更新了一期，就陷入了「先帝创业未半而还剩大半」的摆烂状态，后面更的一期根本算不上什么「周报」，连流水账都不是，只能算是「为写而写」的垃圾文字。明日复明日，明日何其多。恢复身体的努力，学业的压力，再加上摆复摆之的躺平心态，「浮生散记」无疑成了园子里荒草最多的一块土地。

之后的整个大一下学期，我都是在一个浑浑噩噩的状态中度过的。直接的结果就是期末考试大寄特寄（从而导致了我现在比以往许多次都要严重的口腔溃疡）。优秀的绩点与我有缘无分，徒留我一个人喊着「悟已往之不谏，知来者之可追」的口号麻痹自己，怀着无知者无畏的心态像堂吉珂德挑战风车一般一头撞向瘟锌铀耗的大作业和小学期。

而现在，大作业终于被我急急忙忙地赶完了，无 DDL 一身轻的第二（或者说是第三）天，我就坐上了回北京的高铁，去面对从未学过的 Java。

就是在这个节骨眼，我突然就有些迷茫了：我的生活，到底留下了什么？

毫无记录，精神的和物理的都没有，只有手机上的日期变动提醒我又过了一天，一周，一月，一学期，一年。或许用不了多久，他人口中「美好的大学生活」就将结束，我就会懵懵懂懂地离开我的象牙塔，我的园子，走上一个连我自己也不知道是什么的工作岗位，干着连我自己都不知道是什么的工作，写着连我自己都不知道是什么的文章（也可能不写），走过宏观经济学家和政治家口中「失落」抑或是「繁荣」的年代，最终归于尘土或字节。

这太可怕了。

> Stay Dreaming, Stay Lucid.

清醒地痛苦，也比糊涂地幸福要好得多。

所以我总归还是「想进步」的，心里的那团火，总归还是没有完全熄灭的。

所以，我感觉，我还是应该写点什么，向我自己证明我生活过。

于是我重启了我的周报。名字没换，因为我想不到什么更好的名字。如果你觉得「浮生散记」这个名字太拗口抑或是书卷气，叫它「园子周报」也没问题。我不保证会持续更新，但是有感悟了我一定会写。

以及，由于我没有[木木老师](https://immmmm.com/)那样庞大而丰富的友链（以及强大的能力），我的周报不会过度涉及我的老友们。

祝愉快。

Chlorine

## 大作业

我一位因病休学，今年高考的初中同学最近找我吃饭，言语间不无好奇地问：DDL 是什么？

我一时语塞。

其实 ddl 就是 deadline（截止日期）的意思，代指有截止日期的任务。想要逼疯一个带学牲，最好用的办法就是问 TA：你还剩几个 DDL/你期末考试怎么样了？

> [!CAUTION]
> 请谨慎使用此类问题，尤其是在考试季。我不为您的生命安全负责。

大概是从什么时候开始学会赶 ddl 的？我也忘了，就像我在吃饭的时候跟娘亲打趣的一样：谈恋爱就像赶 ddl，没赶过 ddl 的人怎么才能学会赶 ddl？到时候就会了。

言归正传。其实考完试我的 ddl 也不算多（指数量），也就三个：图论的 Final Project，中国文明的期末论文，以及 OOP 的阅读报告。

### 图论

计金有一门课程——「面向计算机科学的离散数学」，算是贵系离散数学的超级阉割版本。图论正是这门课的两部分之一。

图论有一个有趣的 Final Project，就是从给定的三个主题中选一个，用图论知识解决（另外有奇思妙想也可以）。这个可以在期末考试上加分，最多 10 分。由于我期末实在不怎么样（88），于是我决定做一下，垂死挣扎（那些考了 95+ 还来卷 proj 的人我不评价）。

我原本有一个想法——「如何吃遍清华所有食堂」，对应旅行商问题。后来我改主意了，选了给定主题的第一个——「北京 985 的公交线路」，知识点就是最小生成树（其余两个是最佳匹配和 GCN）。

项目本身不难，代码很好写，只不过数据很难收集，我和往届的学长学姐要了好几次也没要到，好在我万能的娘亲帮我用缺德地图测出来了 (≧▽≦)。

然后的事情就毫无难度了，照着写就行。我还想了几个延伸方向，像多参数权函数、中心点和 Steiner 树之类的，可惜没找到好的数据源拟合公式。

*PS：图论的加分作业还有一个供题。我写了几道题交上去，包括但不限于特布尔波的城市化建设和铁山靠简笔画的平面性判断之类的（逃）。*

### 中国文明

中国文明的期末论文主题是「XXX 的 XX 思想及其在中国文明中的意义与贡献」。不算是很刁钻的主题，可惜我知识不够，还是得靠学术 AI 帮忙搜集资料。以及，我这个废话大王第一次感受到了凑字数的痛苦 qaq

以及，点名表扬 Typora 的 PDF 导出，非常美观，我整洁漂亮的报告在我的同学们中绝对属于前列水平。

### OOP

终于到 OOP 了。由于我 OOP 考试寄了以及这个作业实在是太难等原因，我把它放到了最后一个。

OOP 的作业是阅读开源项目并且做报告 PPT。给的几个项目都挺阴间的，比方说什么 LiquidFun、Eigen（线性代数库）、glog 之类的。我选的是 TinyXML-2，因为它最小，而且 XML 嘛，也和我的 RSS 有关系。

TinyXML-2 一共两个文件（一个 `.h` 和一个 `.cpp`），加起来四五千行代码吧。由于水平太菜，我看的是挺痛苦的。具体过程就不和大家说了，防止影响大家心情。简而言之就是看完代码用 Marp 和 WPS 做 PPT，用 Obsidian 画白板，再写几个测试样例、Makefile 和 README 就可以交了。最终在 28 号晚上（ddl 的前一天晚上）送走了这尊瘟神。

## Hugo 博客重启

最近我一直在高强度更新我的 Hugo 迁移日志，因为我从 NotionNext 搬回到 Hugo 了。具体的迁移过程大家可以看迁移日志，我就不多说了。

反正也是挺麻烦的，从 shortcode、homepage 到评论系统、搜索这一堆，遇到不会的只能 Google 或者问 AI。从期末考试前折腾到考试后，所幸最终效果还可以。

我对这个主题还是挺喜欢的，后续可能再完善一下，开源成一个完整的主题。

### 备案那些事

在期末考试前，我曾经尝试过备案，但是失败了。在期末后，得知备案期间可以不用暂停 DNS 解析，不肯安分的我又走上了备案之路。

这次备案的流程和上次差不多，由于接到了备案专员的电话，阿里云初审很快过了。

但是吧，在我调查了后续的公安备案流程后，我顿时就不淡定了。非交互式备案简单，但是不能开评论；交互式备案则比较繁琐。

我当初备案就是为了让国内访问更方便，要是起了反作用，我还备个什么案啊……

很可惜，备案订单提交到管局后就不能撤回了，联系了阿里云的工作人员，他们说可以试着处理。算了，大不了就换域名，或者老老实实走流程。

## 聚少离多

下面的内容可能有点煽情，谨慎观看。

或许是时候和各位老友说说我过去的一些经历了。我在准高三那年暑假摔了一跤，导致左股骨颈骨折，在病床上过了大半个高三。在大一上学期的寒假，我和家人深思熟虑后，决定立即做第二次手术，取出当初打在骨头里面的钢钉（事后证明这个决定还是明智的，因为根据手术情况，如果等到这个暑假取钉，很可能就取不出来了）。

二次手术的恢复时间比第一次短，但是也足以让我躺着过了整个寒假，以及在再次开学的时候拄着拐杖。在休学和带病上学之间，我选择了后者。我的娘亲也决定前往北京，照顾我的生活。这一照顾，就是一个学期。

这一个学期的事情不多说了，我从上学期「独自一人」的生活状态，也慢慢重新适应了「有人陪伴」的生活状态。在期末考试后，我和娘亲一起坐车回了家。

但是，随着我身体的好转，我也应该再次脱离照顾，独自面对小学期、暑期实践以及后续的学习生活。这是个很自然的过程，但是实际转换起来，没那么容易。

我们一家人其实都不善言辞。但是在我爹下班回家，和我们闲聊的时候，他说，刚开始还没怎么样，但是就在（原谅我该死的记忆力）的时候，上完夜班回到家，房子空荡荡的，心里特不是滋味。

我听完心里也不是滋味——能让我爹——一个兢兢业业认真负责的班主任，一个沉默寡言到有一点笨嘴拙舌的男人都这么说……

我不是什么坚强的人。刚上大学时，军训的时候，根本没有人教我，作为一个身体不佳半训的学员应该怎么做。和学院持续不断协调宿舍的过程让我们疲于奔命，每天心里都堵得慌。每晚累得半似地回到空荡荡的宿舍，一闭上眼就是在家里的幸福时光。那时候我的泪点低到夸张，随便哪一个刺激，甚至是毫无来由的内心回味都能让我直接破防。我一坐下来就去发微信，看着自己刚印出来的全家福出神，根本不敢听自己以前经常听的歌……现在说起这些也许显得可笑，但是当时的我就是这样的。

转机是什么时候呢？大概是在军训接近尾声的时候，我们的辅导员（科普：清华的辅导员和其他学校不大一样，是学生，例如博士）带着我们几个凑巧在一起的同学（甚至不是一个班级的），拿着偶然找到的吉他，在紫操（紫荆操场）的夜幕下一起唱歌。一首接着一首，想到哪个就现场查谱现场弹唱。记得那天我回去得异常的晚，心里是说不出的快乐和充实，就好像某些东西一下子被填满了。宿舍在我的眼中，也成了微信消息中「温馨的小窝」。

然后，事情就慢慢好起来了。我从高中生到大学生，从不相信自己能上台的社恐分子到一袭正装对着 PPT 侃侃而谈的清华学子，从生活不能自理到生活基本自理，几个月，像梦一样。

我记得，我在刚刚启程上大学的时候，发了一条朋友圈：

![](https://img.clnya.fun/weekly-1-1.webp)

这是一句歌词，出自我很喜欢的一首歌——《向告别飞驰吧》。

> 我躺在忧伤的黄昏
>
> 看光明，正分神
>
> 看每个恍惚的路人
>
> 为虚构，而狂奔
>
> 我经过的地方
>
> 曾看见末日寄来了
>
> 新灵魂
>
> 废墟上的世界
>
> 用它的方式告别你
>
> 的青春
>
> 再见了，爱的人
>
> 再见歌声，你曾经唱起风尘
>
> 再见神的指纹
>
> 我已去往，在未来，新的旅程
>
> 当时光的羽毛落向
>
> 宇宙的，那道门

所以，当我在十一假期第一次自己回家，我会对来接站的泣不成声的妈妈微笑着说：「哭什么？我这不是回来了吗？」在这次临出发之前，我会对家里人说：「别想我，好好玩你们的啊！」

——**因为，即使聚少离多，即使依依不舍，我们也总要启程。**

