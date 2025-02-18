---
title: 瞎折腾MinGW
date: 2024-02-02
slug: how-to-update-mingw
summary: 乱七八糟瞎折腾
description: 这篇文章介绍了作者在更新 MinGW 过程中遇到的各种问题和解决方法。作者首先回顾了自己在学习递归和调试时的困难经历，强调了命令行调试的复杂性。随后，作者分享了自己发现并尝试更新 MinGW 的过程，包括从 GitHub 下载最新版本并替换旧版本的步骤。接着，作者详细描述了如何在 VS Code 中配置可视化调试环境，通过编写和修改配置文件（如 `c_cpp_properties.json`、`launch.json` 和 `tasks.json`）来实现调试功能。尽管成功配置了可视化调试，作者表示自己仍然更习惯使用命令行调试。文章最后感谢了一位学长的教程，并表达了对折腾过程的感慨。
tags: 
    - C++
    - 教程
categories: ["图灵机"]
---

嗨，大家好，我是 Chlorine.

本期的主要内容是讲述我更新 MinGW 的痛苦经历，寄术力不高，大佬轻喷。引用一句[某乎上的话](https://zhuanlan.zhihu.com/p/137332644):

> 知识就是这样的，也许一个问题在老鸟看来是一颗土坷垃，但对于初学者却是一座大山。

## 历史遗留问题

当年我们在学递归之后，老师布置了一个上机作业，要求原文如下:

> 以汉诺塔源程序为对象，参照 PPT 上关于阶乘示例的递归调用与返回过程的示意图，在集成开发环境中，以单步跟踪方式，打开汇编代码和机器代码显示功能，观察函数调用栈（内存）的变化情况，观察程序执行时“当前待执行机器指令”随着单步执行的变化情况。在发生递归调用时，记录函数实参和形参的地址与内容，记录函数调用结束后的返回点指令地址。

这其实是个简单得离谱的任务，更不用提写上机报告一向是我引以为豪的能力（期末成绩，上机报告部分 99.9 分，扣掉的 0.1 是因为第一篇是用 Obsidian 写的，导出的时候标题没居中）。

可是问题是：**我不会单步跟踪调试**。（上课摆烂的后果 qaq）

跟着助教的讲解视频，查网上的教程，甚至是安了好几个其他的 IDE，都是完不成，我好像就和调试有仇。

最后幸好一位好心的 TA 学长教了我一些命令行调试，才让我把报告写出来（最后成绩是满分 q(≧▽≦q)）。

所以以后我在做单步跟踪调试的时候，一直都是在用命令行。不是说命令行不好，但是的确有点复杂。此外，我在写 C++ 教程的时候，总不能上来就往人家脸上糊命令行吧（）.

## 补偿性折腾

最近我发现了一个很好玩的 Github 项目: [Bill-Haku/kawaii-gcc: GCCコンパイラーを可愛くしましょう！Make your GCC compiler kawaii. (github.com)](https://github.com/Bill-Haku/kawaii-gcc)

这里是 B 站解说视频地址: [【中文】杂~鱼♡！人家 GCC 也想变得可爱嘛～】](https://www.bilibili.com/video/BV1gC4y1P7t3?vd_source=b7e941d0715a442723fb5ad229adf1cb)

说实话，我看完之后，真的感觉：好可爱！

然后我忧伤地得知目前只支持 Cygwin。

但是，我折腾的兴奋度已经被挑起来了。不折腾点什么，我是不会罢休的。

## MinGW 的更新

综合以上两段原因，我决定折腾下我的 VS Code + MinGW-w64。

终端里扔个 `gcc -v`, 发现我的 gcc 居然才 8.1.0，于是我决定更新。

MinGW 没有什么一键更新的命令，同时官网上一大堆离奇的布局看得我五彩缤纷。

于是我找到了 [MinGW-64 的 Github 二进制仓](https://github.com/niXman/mingw-builds-binaries)。直接把 release 的最新版本下载下来，解压完事。

*PS: 我下载的是 `x86_64-13.2.0-release-posix-seh-ucrt-rt_v11-rev0.7z`*

解压的时候我图省事，解压到了默认的 download 文件夹，本来想着一会给移到我原本的 D 盘去，结果遇见了这样的擀人速度：

（图片丢了，乐）

好吧，不管怎么样，总算是挪过去了。由于我解压之后的文件夹也叫 `mingw`，因此直接替换了原本的老版本文件，省去了再配一遍环境变量的麻烦。

然后随便开个终端，键入版本检查指令 `gcc -v`, `g++ -v` 和 `gdb -version`，发现更新成功了。

## 可视化调试的配置

其实这也不是什么难事，也就是几个文件的事，但是 VS Code 这厮总是给我闹幺蛾子，于是干脆自己动手写（抄）文件.

把原本 C++ 文件夹的 `.vscode` 子文件夹删空，新建三个文件，把当时留下的代码扔进去：

```json
// c_cpp_properties.json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "compilerPath": "D:\\\\mingw64\\\\bin\\\\gcc.exe",
            "intelliSenseMode": "windows-gcc-x64",
            "cppStandard": "c++23",
            "cStandard": "c23"
        }
    ],
    "version": 4
}

```

```json
// launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++.exe - Build and debug active file",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}\\\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${fileDirname}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "D:\\\\mingw64\\\\bin\\\\gdb.exe",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "C/C++: g++.exe 生成活动文件"
        }
    ]
}

```

```json
// tasks.json
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe 生成活动文件",
            "command": "D:\\\\mingw64\\\\bin\\\\g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "调试器生成的任务。"
        }
    ],
    "version": "2.0.0"
}

```

重启 VS Code，随便写个 C++ 文件，在左侧工具栏尝试可视化调试，完美。

（图片又丢了，乐）

## 后记

就折腾到这吧。尽管说有了可视化调试的方法，但是我可能还是习惯于用命令行。这次折腾大概还是为了解决强迫症的历史遗留问题。

毕竟我还是无法拥有可爱的 GCC qaq

感谢隔壁北大一位学长的教程[用vscode优雅配置c/c++环境！](https://zhuanlan.zhihu.com/p/610895870)。
