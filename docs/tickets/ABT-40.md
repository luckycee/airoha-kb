---
id: ABT-40
title: "AB1565 中断的使用方式"
date: 2022/04/28 18:30
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-40
---

# ABT-40 AB1565 中断的使用方式

> 📅 2022/04/28 18:30　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-40)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-39](ABT-39.md)　[→ 下一个工单：ABT-41](ABT-41.md)

</div>

## 问题描述

Hi [人名6] / [人名9],

客户使用的SENSOR需要使用外部中断，请帮忙提供一下1565中断注册、设置回调函数等内容的demo code给我参考一下，附件是AB1562x系列的，在1565上有些接口没有。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/28 18:31 — [人名2]

[附件: intr.c]

</div>

<div class="reply even" markdown="1">

### 2022/04/28 18:54 — [人名9]

mcu/doc/ABT_IoT_SDK_for_1565_1568_API_Reference_Manual

这里面有使用说明和sample code

</div>

<div class="reply odd" markdown="1">

### 2022/04/28 20:18 — [人名2]

Hi [人名9]，

看到；

</div>

<div class="reply even" markdown="1">

### 2022/04/29 09:36 — [人名12]

Hi @[邮箱已隐藏]

可参考这个function，里面有GPIO，EINT的配置，谢谢

hal_smart_charger_status_t DRV_SmartCharger_Init_GPIO(hal_gpio_pin_t gpio_index)

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-39](ABT-39.md)　[→ 下一个工单：ABT-41](ABT-41.md)

</div>
