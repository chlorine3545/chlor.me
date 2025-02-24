---
title: 解决UnoCSS更新后的奇怪报错
date: 2025-02-24
slug: fix-unocss-66-error
featuredImage: 
categories:
  - 图灵机
tags:
  - 博客
  - UnoCSS
series: 
summary: 偶遇无信息报错，拼尽全力有法战胜
description: 本文讲述了作者在使用UnoCSS过程中因版本更新引发的配置兼容性问题及其解决过程。作者原本沿用旧版配置方案，但在更新依赖包后遭遇构建失败却无明确报错信息，通过逐步排查发现新版UnoCSS对图标预设语法要求更严格。经查阅文档发现原配置中图标集合的手动注册方式已不兼容，转而采用自动检测机制后问题得以解决。最终确认问题根源在于presetIcons模块的调用方式未遵循最新规范。该案例凸显了依赖版本管理的重要性，同时展示了通过最小化测试与官方文档对照排查技术问题的典型思路。
wikilinks:
---

各位老友，晚上好。这里是 Chlorine。

摸鱼了一节计量，终于把这个奇奇怪怪的问题解决了。遂作文以记之。

小氯之前的 UnoCSS 配置是从还在写 Efímero 的时候继承下来的，或者说直接点就是基本从[恐咖兵糖](https://www.ftls.xyz/)大佬那抄下来的。为数不多的改动也就是加了图标导入的 `IconifyJSON` 类型，以及一些对 ALERT 短代码有好处的预制颜色类。在写 Hermeneutics 的时候，也就图省事，除了一个 `IconifyJSON` 之外什么都没改。

同时，虽然说 npm 包的版本问题就像是飞天面条大神给这个宇宙的报应，但是由于小氯实在是太菜了（用得也实在是太简单了），同时由于小氯喜欢一直保持新版本，所以把 `bun update` 当成 `sudo pacman -Syu` 玩几乎是家常便饭，也一直没什么问题。

然而今天事情不一样了。

事情大概是：小氯闲着没事 refactor 了一下 AI Summary 的部分，拿 HTML + CSS 写了个比以前的 JS 版本还顺滑的摘要框。心情非常良好的小氯就更新了一下包版本，就在打算 `bun run build` 之后就交差时，出事了。

当时的截图小氯没有留下来，具体来说，除了一个：

```txt
(node:33920) ExperimentalWarning: Type Stripping is an experimental feature and might change at any time
(Use `node --trace-warnings ...` to show where the warning was created)
```

之外，就只有一个「退出码为 1」的提示。这段话显然不是报错的根源，而退出码 1 等于什么都没说。

按说小氯酱也不是没见过这种场面，加一个参数 debug 一下：

```bash
bun run dev --verbose
```

很好，这下连退出码为 1 都没有了，降本增效了属于是。

然后小氯尝试了很多方法，例如手动指定 config file 等，然而不能说是硕果累累吧，至少可以说是一无所获。

再试一下换个执行方式：

```bash
# 直接使用路径
./node_modules/.bin/unocss "layouts/**/*.html" -o assets/css/uno.css --watch

# 换一个执行器
npx run dev
```

没用。

既然没有信息，那么检查一下是哪个文件的问题呢？

```bash
#!/usr/bin/env zsh

# 配置区
TARGET_GLOB="layouts/**/*.html"
ERROR_LOG="unocss_errors.log"
OUTPUT_CSS="test.css"

rm -f "$ERROR_LOG"

setopt extended_glob
setopt null_glob

# 计数器
total_files=0
error_files=0

echo "Starting UnoCSS batch processing..."
echo "----------------------------------"

for file in ${~TARGET_GLOB}; do
    # 跳过非文件
    [[ -f "$file" ]] || continue

    ((total_files++))

    echo -n "Processing $file ... "

    # 执行UnoCSS并抑制输出
    if npx unocss "$file" --out-file "$OUTPUT_CSS" >/dev/null 2>&1; then
        echo "✅"
    else
        echo "❌"
        echo "$file" >> "$ERROR_LOG"
        ((error_files++))

        # 保留错误现场
        mkdir -p error_dumps
        cp "$file" "error_dumps/$(date +%s)_${file:t}" # 使用 Zsh 的修饰符 :t 获取文件名
    fi
done

echo "----------------------------------"
echo "Processed $total_files files"
echo "Found $error_files problematic files"
[[ $error_files -gt 0 ]] && echo "Error log saved to $ERROR_LOG"

if [[ -f "$ERROR_LOG" ]]; then
    echo "\nError Summary:"
    cat "$ERROR_LOG"
fi
```

执行。非常地漂亮，全报错了。

既然得不到任何有效信息，那么就要秉承着「计算机科学是一门玄学」的理念了。

我们先降级一下。降回 `65.4.0` 自然是可以解决问题的，但是 `65.5.0` 就不行了。去翻 UnoCSS 更新日志，没有任何发现。

按照直觉，下一步我们就该把主意打到 `node_modules` 上了。清掉缓存，清掉已有模块，重装。小氯还顺便发现 Bun 的 lockfile 变 `bun.lock` 了，以前是 `bun.lockb` 来着。不知道为什么。

然而重装没有任何作用。清除其他包，单独安装，没用。

那我们做一个最小化的构建试一下：

```bash
echo '<div class="bg-red-500"></div>' | bun run build --stdin
```

报错。

坏了，这下不得不认真对待了（

看来应该是 UnoCSS config 的问题了。之前小氯一直没怀疑这个，因为从没出过问题嘛。~~但是，以前是以前，现在是现在~~。

看一眼 `uno.config.ts` ……嗯哼？`presetUno`，deprecated。

按理说 deprecated 其实一般也不是不能用，但是我们还是更新一下的好。

换成最新的 `presetWind3`，问题依然存在。

会不会是 `presetUno` 的类名不兼容呢？不太可能。按小氯的经验，不兼容的类名顶多不被识别，不可能导致报错。

那我们就单独找一下每个部分的问题好了。先开个沙盒鼓捣鼓捣：

```bash
mkdir uno-debug && codium $_
bun i unocss
```

写个极简版的 `index.html` 和 `uno.config.ts`：

```html
<div class="bg-red-500"></div>
```


```ts
import { defineConfig } from 'unocss'

export default defineConfig({
  rules: [
    ['m-1', { margin: '1px' }],
  ],
})
```

构建，没问题。这至少说明 UnoCSS 本身没问题（~~废话~~）。

加一个预设：

```ts
import { defineConfig, presetWind3 } from 'unocss'

export default defineConfig({
  presets: [
    presetWind3(),
  ],
})
```

随便找一个 HTML 放进去，构建。成功。

然后小氯开始一点点地把过去的 config 往回加，加到三个图标包，出事了。去掉两个，只留一个最兼容的 carbon，还是报错。

看来就是图标部分的问题了。

这下小氯没办法自己鼓捣了，于是小氯翻开了几乎从没有翻开过的 UnoCSS 文档（

然后在图标部分找到了官方案例：

```ts
import presetIcons from '@unocss/preset-icons/browser'

export default defineConfig({
  presets: [
    presetIcons({
      collections: {
        carbon: () => import('@iconify-json/carbon/icons.json').then(i => i.default),
        mdi: () => import('@iconify-json/mdi/icons.json').then(i => i.default),
        logos: () => import('@iconify-json/logos/icons.json').then(i => i.default),
      }
    })
  ]
})
```

好吧，我改。

结果出现了错误：

```txt
Failed to load custom icon "screen" in "carbon": TypeError [ERR_IMPORT_ATTRIBUTE_MISSING]: Module "file:///Users/chlorine/Dev/Frontend/hermeneutics/node_modules/@iconify-json/carbon/icons.json" needs an import attribute of "type: json"
```

好吧好吧，我加上还不行吗……

```ts
carbon: () => import('@iconify-json/carbon/icons.json', { assert: { type: 'json' } }).then(i => i.default),
```

然而并没有用。

邪了门了（小氯の疑惑）。

再回去看文档……
 
> In `Node.js` the preset will search for the installed iconify dataset automatically, so you don't need to register the `iconify` collections.

Bun 和 Node 应该也差不多，那把 collections 都去了试试……

正常了。

……你人还怪好的嘞。

下面把 mdi 和 simple icons 加回去吧……等会，我 simple icons 呢？我那么大一包 simple icons 呢？

再回去看文档。Icons 其实就是小氯常用的 [Icônes](https://icones.js.org/) 里面的那些，那咱们再去看看吧。

……哦，原来人家叫 `i-simple-icons-xxxx`，不叫 `i-simple-xxxx`。这个别名是之前的写法规定的。

问题解决。

---

总结一下，就是过去不规范的 `presetIcons` 语法和 UnoCSS 的最新标准不兼容，导致 UnoCSS 报错。至于为什么没有报错信息……小氯也不知道哦。