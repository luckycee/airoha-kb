---
id: ABT-62
title: "AB1565A DUT 模式"
date: 2022/07/18 17:14
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-62
---

# ABT-62 AB1565A DUT 模式

> 📅 2022/07/18 17:14　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-62)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-61](ABT-61.md)　[→ 下一个工单：ABT-63](ABT-63.md)

</div>

## 问题描述

Hi [人名6],

V2.9.0 在config tool上，在RF_Config 上把DUT enable后，开机之后发现系统一直处于 APP_BT_OFF 状态，但是如果关掉则会是 APP_DISCONNECTED，为什么有这个差异？是否DUT 有特别的操作？

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/07/18 17:14 — [人名2]

[图片: Snipaste_2022-07-18_17-13-47.png]

</div>

<div class="reply even" markdown="1">

### 2022/07/19 10:11 — [人名20]

Hi  @[邮箱已隐藏]

关于DUT mode，不建议在configtool上直接将DUT mode enable，这样的话会一直处于DUT mode，建议是要测试的时候用key或者AT CMD去开启。65这部分跟62有差异，请知悉。

</div>

<div class="reply odd" markdown="1">

### 2022/07/19 10:43 — [人名2]

Hi [人名20]，

清楚！

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-61](ABT-61.md)　[→ 下一个工单：ABT-63](ABT-63.md)

</div>
