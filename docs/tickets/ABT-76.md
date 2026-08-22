---
id: ABT-76
title: dongle测试DUT mode
date: 2022/09/02 10:48
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-76
---

# ABT-76 dongle测试DUT mode

> 📅 2022/09/02 10:48　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-76)

## 问题描述

Hi [人名5]，

你们之前给过dongle的测试方式（[ABT-17](ABT-17.md)），但是现在客户的产品是没有按键的，是否可以通过5V 发码的方式让它进入DUT mode，或者已经量产的客户怎么做。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/02 12:33 — [人名5]

Hi @[邮箱已隐藏]，

Dongle 可以通过USB 连接电脑，然后在logging tool上把设置改成USB-HID。串口选择USB-HID，连接dongle就可以发送race cmd了。

注意PID 跟 VID 要跟code里对应上：
 * File : \mcu\middleware\MTK\usb\src\_common\usb_custom.c
 * VID 
 * #define CUSTOM_VID 0x0E8D
 * PID
 * #ifdef AIR_USB_DONGLE_PROJECT_ENABLE
 * #define CUSTOM_PID 0x0808

[图片: image-2022-09-02-12-30-51-046.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/02 12:55 — [人名2]

Hi [人名5]，

race cmd发哪个指令？还是需要自己写？

</div>

<div class="reply odd" markdown="1">

### 2022/09/02 13:38 — [人名5]

Hi @[邮箱已隐藏]，

就key 的race cmd 就可以啊，之前你们不是实体按键触发吗？现在改成race cmd跑key对应的功能函数。

</div>
