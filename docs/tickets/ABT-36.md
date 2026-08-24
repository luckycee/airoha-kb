---
id: ABT-36
title: "AB1565 修改默认ANC模式"
date: 2022/04/22 12:07
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-36
---

# ABT-36 AB1565 修改默认ANC模式

> 📅 2022/04/22 12:07　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-36)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-35](ABT-35.md)　[→ 下一个工单：ABT-37](ABT-37.md)

</div>

## 问题描述

Hi [人名6]，

你们的demo code（nvkey.xml）默认开机之后，是ANC开启的模式，请指导一下如何设置为默认为关闭的模式；

以及看一下附件的接口，修改的是那个nvkey；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/22 12:07 — [人名2]

[图片: 微信图片_[序列号已隐藏].png]

</div>

<div class="reply even" markdown="1">

### 2022/04/22 15:43 — [人名6]

Hi @[邮箱已隐藏]，

修改的是0xE1E0 这条nvkey，第一个byte 改成 00，就是disable anc ，开机就没有anc 效果了，然后可以通过按键切anc ，切的就是第一个byte。

</div>

<div class="reply odd" markdown="1">

### 2022/04/22 15:55 — [人名2]

Hi [人名6]，

可以了。

如果要默认为通透，那么nvkey改如何修改？

</div>

<div class="reply even" markdown="1">

### 2022/04/22 16:16 — [人名6]

Hi @[邮箱已隐藏]，

最后一个byte 改成 04

[图片: image-2022-04-22-16-16-14-757.png]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-35](ABT-35.md)　[→ 下一个工单：ABT-37](ABT-37.md)

</div>
