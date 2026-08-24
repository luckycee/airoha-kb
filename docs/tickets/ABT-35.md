---
id: ABT-35
title: "AB1565 设置按键开机"
date: 2022/04/15 19:45
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-35
---

# ABT-35 AB1565 设置按键开机

> 📅 2022/04/15 19:45　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-35)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-34](ABT-34.md)　[→ 下一个工单：ABT-36](ABT-36.md)

</div>

## 问题描述

Hi [人名6]，

软件的 customerized_key_config.c 没有开机的时长设置，每次按键开机都是差不多1s就起来了。客户希望跟之前的UI保持一致，改为长按3s才能开机，请帮忙看看如何实现；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/16 16:17 — [人名6]

Hi @[邮箱已隐藏]，

可以按照这个试一下~
[附件: AB1565_key_setting.wmv] [附件: AB1565_key_setting.pptx]

</div>

<div class="reply even" markdown="1">

### 2022/04/19 14:30 — [人名2]

Hi [人名6]，

我试过了，即使关闭1wire也是一样的开机时间。

我用V2.11.0 的code，生成的FW也是1s开机。

编译指令如下：
 ./build.sh ab1565_evk earbuds_ref_design

附件是FW，你也可以测试一下；

[附件: V2.11.0_earbuds_ref_design.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/04/19 15:12 — [人名6]

Hi @[邮箱已隐藏]，

这边测试刚好3s啊

[图片: image-2022-04-19-15-12-04-340.png]

</div>

<div class="reply even" markdown="1">

### 2022/04/19 15:57 — [人名2]

Hi [人名6]，

请使用电池测试；

</div>

<div class="reply odd" markdown="1">

### 2022/04/19 16:54 — [人名6]

Hi [人名11]，

我们耳机在充电状态下，耳机已经唤醒，所以会跑key 开机。

假如没有充电，这时候按power key 1s 钟，就会触发硬件开机。这部分功能是硬件控制的，软件已经改不了了，麻烦跟客户解释，感谢~

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-34](ABT-34.md)　[→ 下一个工单：ABT-36](ABT-36.md)

</div>
