---
id: ABT-17
title: "ULL dongle测试RF"
date: 2022/01/13 16:47
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-17
---

# ABT-17 ULL dongle测试RF

> 📅 2022/01/13 16:47　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-17)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-16](ABT-16.md)　[→ 下一个工单：ABT-18](ABT-18.md)

</div>

## 问题描述

Hi [人名1]，

客户先要测试一下自己的dongle板子的RF 性能，软件上我开机就触发了 key action (KEY_TEST_MODE_ENTER_DUT_MODE)，并在配置工具上 enable DUT mode，但是触发后就关机了，这个如何测试？

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/01/13 16:47 — [人名2]

[图片: Snipaste_2022-01-13_16-46-52.png]

[附件: ULL dongle DUT mode.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/01/18 10:08 — [人名1]

Hi,

如果你们只想在这次开机进dut mode，下次开机自动退出DUT，可以用下面这种方式:

#include ”bt_device_manager_test_mode.h”

Bt_device_manager_set_test_mode(BT_DEVICE_MANAGER_TEST_MODE_DUT_ONLY);

注意在系统跑起来之后调用.

谢谢

</div>

<div class="reply odd" markdown="1">

### 2022/01/18 11:50 — [人名2]

Hi [人名1]，

按照你的修改后，还是关机了。

[附件: DUT mode.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/01/18 14:37 — [人名1]

Hi, 

     进入DUT mode之后, 你可以用手机搜索看看, 是否能找到一个叫"Bluetooth DUT" 名字的设备, 如果可以看见应该就是正常的.

     此后用蓝牙分析仪测试就可以了.

谢谢

</div>

<div class="reply odd" markdown="1">

### 2022/01/18 15:53 — [人名2]

Hi youwei，

可以了，不过只能在Android 手机上搜索到，iPhone 怎么也搜索不到。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-16](ABT-16.md)　[→ 下一个工单：ABT-18](ABT-18.md)

</div>
