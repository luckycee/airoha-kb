---
id: ABT-87
title: "1565 断开连接后提示音不同步"
date: 2022/09/26 10:35
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-87
---

# ABT-87 1565 断开连接后提示音不同步

> 📅 2022/09/26 10:35　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-87)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-86](ABT-86.md)　[→ 下一个工单：ABT-88](ABT-88.md)

</div>

## 问题描述

Hi [人名6]，

断开手机连接后，发现disconnect 有概率性出现差3秒的情况，问题出现在17:21:08 附近，这会和什么有关系？如何改善？

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/26 10:36 — [人名2]

[附件: 断开连接提示音播报不一致-L.pcapng]

[附件: 断开连接提示音播报不一致-R.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/09/26 15:13 — [人名6]

Hi @[邮箱已隐藏]，

概率多少啊，你们怎么测试的啊，我测试3.3.0测了n次都没问题啊

</div>

<div class="reply odd" markdown="1">

### 2022/09/26 15:34 — [人名2]

Hi [人名6]，

用的是V2.9.0 ，手法是连接手机后走远 link loss，不是直接在手机上断开的。

</div>

<div class="reply even" markdown="1">

### 2022/09/27 14:37 — [人名17]

hi @[人名28]

请帮忙看看这个现象是正常的吗？link loss 后agent 断开手机和 partner 断开agent 的时间差了3s

[图片: image-2022-09-27-14-37-30-037.png]

[图片: image-2022-09-27-14-37-53-145.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/27 16:40 — [人名6]

Hi @[邮箱已隐藏]，

可以确认两只耳机是同时拉远吗？

log看起来是有一只耳机先拉远导致先收不到手机包了。

这个问题是无法避免的。

</div>

<div class="reply even" markdown="1">

### 2022/09/27 17:14 — [人名2]

Hi [人名6]，

是的，两个耳机在桌上抓log，手机走远。

开始一两次正常的，第三次或者之后就容易出现；

</div>

<div class="reply odd" markdown="1">

### 2022/09/27 17:42 — [人名6]

Hi @[邮箱已隐藏]，

这种情况也是会出现一只耳机先收不到包的概率的。属于正常现象，无法避免

</div>

<div class="reply even" markdown="1">

### 2022/09/30 18:17 — [人名2]

Hi [人名6]，

客户接受，问题关闭；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-86](ABT-86.md)　[→ 下一个工单：ABT-88](ABT-88.md)

</div>
