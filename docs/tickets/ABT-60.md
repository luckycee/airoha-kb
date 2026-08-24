---
id: ABT-60
title: "切换通透问题的问题"
date: 2022/07/04 18:09
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-60
---

# ABT-60 切换通透问题的问题

> 📅 2022/07/04 18:09　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-60)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-59](ABT-59.md)　[→ 下一个工单：ABT-61](ABT-61.md)

</div>

## 问题描述

Hi [人名6]

可以个性化软件，ANC的切换顺序为 降噪>通透>风声抑制>关闭，切换顺序和使用的参数见图片。另外客户，加入了光感，要求双耳佩戴时，一个出耳需要直接切换到通透。

在实际测试的光感控制的过程中，从ANC到通透，效果不明显；从风声抑制到通透，效果明显，调用的接口都是一样的，不明白为什么有这样的区别；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/07/04 18:09 — [人名2]

[附件: ANC-通透，通透无效.pcapng]

[图片: Snipaste_2022-07-04_18-07-53.png]

[图片: Snipaste_2022-07-04_18-08-33.png]

[附件: WNR-通透，通透有效.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/07/05 09:44 — [人名6]

Hi @[邮箱已隐藏]，

你是用哪版软件测试的？

</div>

<div class="reply odd" markdown="1">

### 2022/07/05 10:11 — [人名2]

Hi [人名6]，

V2.9.0

</div>

<div class="reply even" markdown="1">

### 2022/07/05 14:59 — [人名6]

Hi @[邮箱已隐藏]，

麻烦替换dsp\prebuilt\middleware\MTK\dspfw\anc\ab156x 这个路径下附件.a文件试试~
[附件: libanc_protected.a]

</div>

<div class="reply odd" markdown="1">

### 2022/07/05 16:32 — [人名2]

Hi [人名6],

测试有效，给客户验证看看。

</div>

<div class="reply even" markdown="1">

### 2022/07/05 16:50 — [人名6]

OK~

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-59](ABT-59.md)　[→ 下一个工单：ABT-61](ABT-61.md)

</div>
