---
id: ABT-19
title: ull pairing下关机后指示灯异常
date: 2022/01/19 15:03
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-19
---

# ABT-19 ull pairing下关机后指示灯异常

> 📅 2022/01/19 15:03　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-19)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-18](ABT-18.md)　[→ 下一个工单：ABT-20](ABT-20.md)

</div>

## 问题描述

Hi [人名1]，

TWS状态下自动进入了手机配对，然后在此状态下我触发了Ull pairing，最后通过按键关机；

发现关机之后，LED灯还有几秒钟的异常闪烁；请帮忙看下哪里出了问题，这部分我没有修改源码；

附件有一个未连接状态下的关机，此时LED正常；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/01/19 15:03 — [人名2]

[附件: 在手机配对状态下进行ULL pairing，关机后仍有几秒钟的LED闪烁；.pcapng]

[附件: 正常的关机，LED正常显示；.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/01/28 09:53 — [人名1]

Hi,

   你直接调用关机流程, ULL airpairing 还在进行中, 最后52秒真正才关机(进入RTC mode)之前才退出air pairing.   之前应该只是关机VP而已,并不是真正的关机.

   你可以在关机流程开始的时候, 先手动取消各种配对.

[图片: image-2022-01-28-09-47-26-358.png]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-18](ABT-18.md)　[→ 下一个工单：ABT-20](ABT-20.md)

</div>
