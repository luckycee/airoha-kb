---
id: ABT-32
title: "AB1565 是否支持smart case V1/V2"
date: 2022/04/02 15:55
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-32
---

# ABT-32 AB1565 是否支持smart case V1/V2

> 📅 2022/04/02 15:55　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-32)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-31](ABT-31.md)　[→ 下一个工单：ABT-33](ABT-33.md)

</div>

## 问题描述

Hi  [人名6] ,

在feature.mak 中，1wrie的设定需要三个define。

1wire charger

MTK_SMART_CHARGER_ENABLE            = y

MTK_SMART_CHARGER_1WIRE_ENABLE      = y

MTK_SMART_CHARGER_1WIRE_RACE_ENABLE = y

我把后面两个改为n，发现还是无法接受 V1或者V2的pattern，请帮忙确认是否不支持。客户想在已有的项目底座上做耳机软件，不希望改充电仓。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/06 09:51 — [人名6]

Hi @[邮箱已隐藏]

所以目前客户已经做好的仓是 V1 的仓还是 V2 的仓？

可以支持，但是需要确认你们的需求再推进方案。

目前我们主推1wire仓，如果想双向沟通，还是要用1wire 仓。

</div>

<div class="reply even" markdown="1">

### 2022/04/07 18:04 — [人名2]

HI [人名6]，

客户目前已经转到1wire，暂不讨论了。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-31](ABT-31.md)　[→ 下一个工单：ABT-33](ABT-33.md)

</div>
