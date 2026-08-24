---
id: ABT-66
title: "关闭POWER KEY 长按10秒的reset"
date: 2022/07/27 18:53
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-66
---

# ABT-66 关闭POWER KEY 长按10秒的reset

> 📅 2022/07/27 18:53　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-66)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-65](ABT-65.md)　[→ 下一个工单：ABT-67](ABT-67.md)

</div>

## 问题描述

Hi [人名6]，

请看一下如何关闭长按power key导致的sys reset，客户需要支持10秒以上的长按功能键；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/07/29 15:04 — [人名6]

Hi @[邮箱已隐藏]，

可以参考pmu_enable_lpsd_lp 这个函数来修改

</div>

<div class="reply even" markdown="1">

### 2022/08/01 10:18 — [人名2]

Hi [人名6],

这个接口是我可以看到的嘛？搜索不出来。

</div>

<div class="reply odd" markdown="1">

### 2022/08/01 11:18 — [人名6]

Hi @[邮箱已隐藏],

在hal_pmu_internal_2565.c文件里面，我搜SDK 也是有的

</div>

<div class="reply even" markdown="1">

### 2022/08/01 11:40 — [人名2]

Hi [人名6],

找到了 V3.2.0 是你写，V2.9.0、V2.11.0 是 void pmu_enable_lpsd_2565(void)；

</div>

<div class="reply odd" markdown="1">

### 2022/08/01 12:10 — [人名2]

Hi  [人名6],

修改了，没有作用；

我添加了部分log，但是init的时候，看不到我的log，这会是什么问题？

[图片: Snipaste_2022-08-01_12-09-25.png]

</div>

<div class="reply even" markdown="1">

### 2022/08/01 16:11 — [人名6]

Hi @[邮箱已隐藏],

开机之后不会跑这里，需要你们开机之后自己调用，我这边调用一下，再长按10s 都不会reset了

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-65](ABT-65.md)　[→ 下一个工单：ABT-67](ABT-67.md)

</div>
