---
title: 离散数学——Bell数
date: 2024-04-27T07:12:00
slug: bell-number
categories: ["九章术"]
summary: 算点东西
description: 本文介绍了离散数学中的 Bell 数。作者介绍了集合的划分，然后引出了 Bell 数的定义并指出其比想象中复杂，并给出了一个递归表达式。最后作者给出了一份计算 Bell 数的 C++ 代码。
tags:
  - 离散数学
math: true
---
# 离散数学——Bell数

最近复习离散数学的时候想到一个问题，记录一下。

首先科普一下 **集合的划分** 的知识：

对于集族 $\pi =\{ x \mid x \ \text{is a subset of A and satisfies some conditions} \}$ （奇妙定义法），如果其满足以下条件：

1. 不含空集： $\emptyset \notin \pi$
2. 装住 A： $\cup \pi = A$
3. 元素彼此不交： $(\forall x)(\forall y)(x \in \pi  \land y \in \pi)\to(x \cap y = \emptyset)$

那么称 $\pi$ 为 A 的一个 **划分** 。

我想到的问题是：对于一个含有 n 个元素的有限集合，其有多少种划分？

也可以表述成一个更加接地气的形式：n 个不同的球，随便分，有多少种分法？

这道题目的结果称为 **Bell 数** 。看起来是一个简单的排列组合问题，但实际上比我们想象中复杂许多。利用现在的知识甚至难以给出一个显式的序列表达式，只能给出一个递归表达式：

$$
B_{n + 1} = \sum_{k=0}^{n}\binom{n}{n-k}B_{k} = \sum_{k=0}^{n}\binom{n}{k}B_{k}
$$

直观意义就是将多出来的那个元素单独一类，和某一个元素一类，和某两个元素一类……和剩下 n 个元素一类。

此外我去查阅了一些资料，由于知识浅薄，不敢卖弄，想了解更多的老友可以参考[这里](https://oi-wiki.org/math/combinatorics/bell/)。

最后附上一个我闲着没事写的 Bell 数计算代码（`千村万落生荆杞的动态规划.webp`）。

```cpp
#include <iostream>

using namespace std;

int dp_1[1000][1000] = {0}; // 二项式系数
int dp_2[1000] = {0};       // 贝尔数

int binary(int n, int k)
{
    if (k == 0 || k == n)
    {
        return 1;
    }
    if (dp_1[n][k] != 0)
    {
        return dp_1[n][k];
    }
    int ret = binary(n - 1, k - 1) + binary(n - 1, k);
    dp_1[n][k] = ret;
    return ret;
}

int bell(int N)
{
    if (N == 1)
    {
        return 1;
    }
    if (dp_2[N] != 0)
    {
        return dp_2[N];
    }
    int ret = 0;
    for (int i = 1; i < N; i++)
    {
        ret += binary(N - 1, i - 1) * bell(i);
    }
    dp_2[N] = ret;
    return ret;
}
```
