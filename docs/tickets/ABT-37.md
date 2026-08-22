---
id: ABT-37
title: AB1565 dongle获取来电信号状态
date: 2022/04/26 10:56
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-37
---

# ABT-37 AB1565 dongle获取来电信号状态

> 📅 2022/04/26 10:56　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-37)

## 问题描述

Hi [人名5]，

在添加了拒绝电话之后，引起了问题。在earbuds 这端，我是在 APP_CONNECTED 给出了reject指令的，因为客户在 APP_ULTRA_LOW_LATENCY_PLAYING 相同的长按是上下一曲。

客户在连续测试上下曲，在网络环境比较不好的时候，streaming 会停止，state会变为APP_CONNECTED，此时就发送 reject给dongle了，dongle收到后有概率出现earbuds断开连接、earbuds 操作没有反应等奇奇怪怪的问题。

还有什么变量可以区分来电和已连接？不然就没有办法把reject放进去；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/26 10:56 — [人名2]

[附件: dongle.7z]

[附件: 控制之后没有音乐-L.pcapng]

[附件: 控制之后没有音乐-R.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/04/26 10:59 — [人名2]

另外，拒绝来电在一些手机上无法有效。我验证了带线控耳机的逻辑，一些手机的长按2s就能拒绝，一些手机是长按+松手才能拒绝。这个兼容性，能不能解决？

</div>

<div class="reply odd" markdown="1">

### 2022/04/26 11:16 — [人名2]

Hi [人名5]，

附件是code；

[附件: reject.7z]

</div>

<div class="reply even" markdown="1">

### 2022/04/26 16:00 — [人名5]

Hi @[邮箱已隐藏]，

麻烦帮忙提供一下线控耳机可以拒接，我们耳机拒接的log，我们这边需要研究一下怎么实现这个功能~

</div>

<div class="reply odd" markdown="1">

### 2022/04/26 16:00 — [人名5]

另外，我们耳机没有办法区分来电的状态，麻烦跟客户说明~

</div>

<div class="reply even" markdown="1">

### 2022/04/27 10:06 — [人名8]

@[邮箱已隐藏]

线控耳机和 USB audio的耳机是无法对比的，需要同样拿支持USB HID的耳机对比测试.

</div>
