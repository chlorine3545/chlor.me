---
slug: hello-aria2
datetime: 2024-08-12 21:41
summary: 下载！都可以下载！
tags:
  - 下载
  - 折腾
cover_image_url: ""
title: Hello，Aria2
date: 2024-08-12
description: 本文介绍了如何配置 Aria2 作为 macOS 下载工具，涉及安装、设置配置文件、开机自启与自动更新 BT tracker 的步骤，同时感谢了一些教程的贡献者。
categories: ["逍遥游"]
featuredImage: 
draft: false
share: true
---
各位老友们好，我是 Chlorine。

本期讲讲下载神器 Aria2 的配置。网上关于 Aria2 的配置教程已经极为丰富，所以本文主要起一个备份的作用，其教学内容大多还是拾人牙慧。

感谢 GitHub 上的各路大佬，特别感谢博主[月青悠](https://vccv.cc)的教程 [macOS系统配置Aria2](https://vccv.cc/article/aria2-mac.html)。

## 前言

本段接近于自言自语，不想看的老友可以直接跳过。

小氯在用 Windows 时（那大概是半年前，但感觉似乎是很久很久以前了），使用~~开心版的~~IDM（[INTERNET DOWNLOAD MANAGER](https://www.internetdownloadmanager.com/)）作为下载器，用着还挺舒服的。不过换到 macOS 了就没那个好事了，于是我选择了 IDM 的有力竞争者 FDM。

美好的日子就这样一天天过去。FDM 整体虽然看起来有一点点古老，但是用着还可以。不过随着时间的推移，~~闲得发慌的~~我又开始挑毛病了：感觉 FDM 的下载速度不够快，而且没办法用 Firefox 版本的扩展（更正：这个扩展是存在的，但是我的备用浏览器是 基于 Firefox 的 LibreWolf，似乎有适配性问题），而且不是开源的。

于是我接触到了 Motrix。不过 Motrix 很久不更新了，我使用的是 Motrix 的衍生品 Imfile。

Imfile 总体而言还可以，虽然启动时会报出一个莫名其妙的错误提一提我的血压（~~开发者目前对此持摆烂态度~~）。不过最近用 Imfile 的时候，经常动弹不了一点，让我很头痛。而且这软件应该是个 Electron 的，我对这类软件没什么好感（~~但是你现在的主力软件 Obsidian 和 VSCodium 不就是 Electron 的吗~~）。

于是我盯上了据说很出色的~~狗屁下载器~~够快下载器（Gopeed）。具体体验不说了，一言难尽。反正我是没找到正确的打开方式。

思前想后之下我还是决定用之前没搞明白的命令行版 Aria2，反正我不怕耍命令行。经过折腾，现在已经达到了比较良好的效果。

## Aria2 简介

不想看的老友依然可以跳过。

Aria2 是一个跨平台的命令行下载器，具有轻量级、多线程、高速度、多协议支持（HTTP、FTP、BT 等）和高度可定制性（命令行工具基本都这样:）等优点。

不过需要注意：Aria2 并不是 Aria 的第二代。没有叫 Aria 的工具。

（冷知识：aria 的含义是「咏叹调」）

## 安装 Aria2

我们依然使用万能的 Homebrew。

```bash
brew install aria2
```

一般来说 M 芯片的默认下载位置是 `/opt/homebrew/bin/aria2c`，记好这个路径。如果不确定，请使用：

```bash
where aria2c
```

## 设置 `aria2.conf`

注意，以下所有配置，请将 `chlorine` 替换为你的用户名。

我们在你的用户根目录下创建一个配置文件夹 `.aria2`。注意，下面所有的 `<user>` 都需要替换为你的用户名，例如 `chlorine`。

```bash
mkdir -p ~/.aria2 && cd $_
touch aria2.conf aria2.session aria2.log
nano aria2.conf # 或者你的编辑器
```

我的配置文件主要是照抄了博主月青悠的，只不过修改了几个地方：

- 修改端口为 7800：之前这样是因为 6800 被占用了，有可能是因为 Imfile 的缘故。奇怪的是，7800 下载比 6800 快很多。
- 配置了 `all-proxy`，适配某一只会科学技术的小猫的配置。
- 注释掉了通知 hook，因为我们不需要。

为了文章不至于有太长的代码，请在[此处](https://gist.github.com/chlorine3545/b500eed051ca8d7f5977440bacd0aa1b)自取。

你需要做的：

- 将复制的配置粘到文件中。
- 修改 `rpc-secret` 为你自己的密钥。可以自己随便写，但是推荐生成一个长字符串，使用 `openssl rand -base64 32` 即可。
- 你其他的自定义。

## 配置开机自启

这里比较麻烦，所幸万能的开源社区已经替我们做好了一切。

```bash
touch ~/Library/LaunchAgents/aria2.plist
nano ~/Library/LaunchAgents/aria2.plist
```

把这段粘进去：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>KeepAlive</key>
    <true/>
    <key>Label</key>
    <string>aria2</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/aria2c</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>/Users/chlorine/Downloads</string>
</dict>
</plist>
```

如果一切顺利，系统会提示你已经添加了一个开机启动项。

然后检查文件语法：

```bash
plutil ~/Library/LaunchAgents/aria2.plist
```

如果 OK，修改文件权限：

```bash
chmod 644 ~/Library/LaunchAgents/aria2.plist
```

然后加载启动项并启动服务：

```bash
launchctl load ~/Library/LaunchAgents/aria2.plist
launchctl start aria2
```

这样，系统会在后台替你料理好一切。

## 自动更新 BT tracker

这个事情我用不太到，但是还是写上吧。

```bash
touch ~/.aria2/trackers-list-aria2.sh
nano ~/.aria2/trackers-list-aria2.sh
```

写入：

```bash
#!/usr/bin/env zsh
# 如果你的电脑没有 Zsh，请把 zsh 改为 bash，但是我更推荐安装一个
# 文件名 trackers-list-aria2.sh
# aria2 设置文件路径
CONF=${HOME}/.aria2/aria2.conf

# 设置选择的 trackerlist （可选 all_aria2.txt, best_aria2.txt, http_aria2.txt）
trackerfile=all_aria2.txt
# downloadfile=https://raw.githubusercontent.com/ngosang/trackerslist/master/${trackerfile}
downloadfile=https://trackerslist.com/${trackerfile}

list=$(curl -fsSL ${downloadfile})
if ! grep -q "bt-tracker" "${CONF}" ; then
    echo -e "\033[34m==> 添加 bt-tracker 服务器信息......\033[0m"
    echo -e "\nbt-tracker=${list}" >> "${CONF}"
else
    echo -e "\033[34m==> 更新 bt-tracker 服务器信息.....\033[0m"
    sed -i '' "s@bt-tracker.*@bt-tracker=${list}@g" "${CONF}"
fi

## 重启 aria2 服务
echo -e "\033[34m==> 停止 aria2 服务......\033[0m"
launchctl stop aria2
echo -e "\033[34m==> 启动 aria2 服务......\033[0m"
launchctl start aria2
```

然后添加定时任务：

```bash
(crontab -l 2&> /dev/null; echo "0 18 * * * ~/.aria2/trackers-list-aria2.sh") | crontab
```

这会在每天 18 点更新列表。如果希望频率不那么高，可以修改配置，比如每周日一次：

```bash
(crontab -l 2>&1 /dev/null; echo "0 18 * * 0 ~/.aria2/trackers-list-aria2.sh") | crontab
```

如果你希望就算是关机了还能在开机期间执行任务，那可以用 `launchd`。不过这个我没测试过，谨慎使用。

创建服务文件：

```bash
touch ~/Library/LaunchAgents/com.user.trackers-list.plist
nano ~/Library/LaunchAgents/com.user.trackers-list.plist
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.trackers-list</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/sh</string>
        <string>/Users/chlorine/.aria2/trackers-list-aria2.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>86400</integer> <!-- 每24小时执行一次 -->
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

然后按照类似上面的方法加载服务。

## Chrome 扩展

每次都打开命令行下载无疑很痛苦，所幸我们可以通过 Chrome 扩展自动接管浏览器下载事件。

我们选择广受好评的 [Aria2 Explorer](https://chromewebstore.google.com/detail/aria2-explorer/mpkodccbngfoacfalldjimigbofkhgjn)。直接点击安装即可。

安装后需要进行一点配置，这是我的配置，大家可以参考。

![](https://img.clnya.fun/IMG-20240812213211.avif "端口和密钥记得改成你填写的，比如 7800")

然后打开扩展页面。如果显示 Aria2 已连接，那么就大功告成了。

## 最终效果

我们家的宽带大概是百兆的，网络很一般，于是我测试速度的时候吓了一跳。我测试用的是飞书的 `.dmg`，Obsidian 的那个（测试系统代理）只用了两秒钟。

![Aria2 下载飞书安装包时速度达到了 18 M / s|495](https://img.clnya.fun/IMG-20240812213600.avif "你这速度疑似有点太城市化了")

再次感谢伟大的开源社区。祝各位老友资源获取愉快。
