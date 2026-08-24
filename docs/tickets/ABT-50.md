---
id: ABT-50
title: "AB1565A dongle回连不成功"
date: 2022/05/27 17:27
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-50
---

# ABT-50 AB1565A dongle回连不成功

> 📅 2022/05/27 17:27　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-50)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-49](ABT-49.md)　[→ 下一个工单：ABT-51](ABT-51.md)

</div>

## 问题描述

Hi [人名6]，

请帮忙看看，开机后TWS连接上，进入手机配对，此时插入dongle，出现了连接失败的情况；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/05/27 17:27 — [人名2]

[附件: AGENT.7z]

[附件: DONGLE.7z]

[附件: PARTNER.7z]

</div>

<div class="reply even" markdown="1">

### 2022/05/30 09:23 — [人名6]

Hi @[邮箱已隐藏]，

你们spp 改了什么吗？

</div>

<div class="reply odd" markdown="1">

### 2022/05/30 10:00 — [人名2]

Hi  [人名6],

没有，spp还没有加入我的代码，是demo状态

</div>

<div class="reply even" markdown="1">

### 2022/06/01 19:21 — [人名18]

Dear @[人名19] and @[人名16]

\src\apps\app_ull\app_ull_idle_activity.c里面, 有一段app_ull_proc_bt_cm_group函数 中
case BT_CM_EVENT_REMOTE_INFO_UPDATE: \{
部分
{code:java}
} else if ((BT_CM_ACL_LINK_CONNECTED <= remote_update->pre_acl_state && BT_CM_ACL_LINK_CONNECTED > remote_update->acl_state)
                        || (BT_CM_ACL_LINK_DISCONNECTING == remote_update->pre_acl_state && BT_CM_ACL_LINK_DISCONNECTED == remote_update->acl_state)) {
{code}
改成
{code:java}
} else if ((BT_CM_ACL_LINK_CONNECTED <= remote_update->pre_acl_state && BT_CM_ACL_LINK_CONNECTED > remote_update->acl_state)
                        || (BT_CM_ACL_LINK_DISCONNECTING == remote_update->pre_acl_state && BT_CM_ACL_LINK_DISCONNECTED == remote_update->acl_state && BT_HCI_STATUS_UNKNOWN_CONNECTION_IDENTIFIER != remote_update->reason)) {
{code}

</div>

<div class="reply odd" markdown="1">

### 2022/06/02 08:56 — [人名6]

Hi @[邮箱已隐藏]，

\src\apps\app_ull\app_ull_idle_activity.c里面, 有一段app_ull_proc_bt_cm_group函数 中
case BT_CM_EVENT_REMOTE_INFO_UPDATE: \{
部分
{code:java}
} else if ((BT_CM_ACL_LINK_CONNECTED <= remote_update->pre_acl_state && BT_CM_ACL_LINK_CONNECTED > remote_update->acl_state)
                        || (BT_CM_ACL_LINK_DISCONNECTING == remote_update->pre_acl_state && BT_CM_ACL_LINK_DISCONNECTED == remote_update->acl_state)) {
{code}
改成
{code:java}
} else if ((BT_CM_ACL_LINK_CONNECTED <= remote_update->pre_acl_state && BT_CM_ACL_LINK_CONNECTED > remote_update->acl_state)
                        || (BT_CM_ACL_LINK_DISCONNECTING == remote_update->pre_acl_state && BT_CM_ACL_LINK_DISCONNECTED == remote_update->acl_state && BT_HCI_STATUS_UNKNOWN_CONNECTION_IDENTIFIER != remote_update->reason)) {{code}

</div>

<div class="reply even" markdown="1">

### 2022/06/06 17:54 — [人名2]

Hi [人名6]

还是有问题；

问题出现在com7 的17:33:55 左右；
com7 主机
com5 dongle
com11 副机

[附件: log.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/06/07 10:10 — [人名18]

Dear @[邮箱已隐藏]

17:33:55有成功连上Dongle, 你说的问题是什么现象.

Dongle开机:
10260 17:33:51.417703 160 MCU 12 [M:hal C:warning F: L: ]: rtc use iner eosc-32k
开启BT:
11794 17:33:54.787436 3542 MCU 28 [M:apps C:info F: L: ]: [app_bt_state_service] app_bt_state_service_set_bt_on_off ? 1, classic_off: 0, try_rho : 1, for_system_off: 0
连上
12767 17:33:55.371481 4137 MCU 12 [M:apps C:info F: L: ]: [app_bt_state_service] Agent ACL Connected
13087 17:33:55.751221 4533 MCU 12 [M:apps C:info F: L: ]: [app_bt_state_service] Agent Connected



COM17耳机端:

开机回连Dongle
35246 17:33:45.726728 1014 MCU 16 [M:apps C:info F: L: ]: [ULL_activity], power on reconnect dongle:0
38366 17:33:55.526962 10834 MCU 16 [M:apps C:info F: L: ]: [ULL_activity], Dongle connected, link_mode: 0

这里发生了断线event: 应该是拔掉了dongle导致的.
42343 17:34:20.265253 35565 MCU 16 [M:apps C:info F: L: ]: [ULL_activity], Dongle disconnected, link_mode: 0

</div>

<div class="reply even" markdown="1">

### 2022/06/08 10:20 — [人名2]

Hi [人名18] ([人名18])，

昨天的客户有多余的操作，请看这一份；

问题在com5 10:06:36 左右，客户在手机上播放音乐，耳机上没有声音；

com5 主机
com7 dongle
com10 副机；

[附件: log_0608.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/06/10 14:33 — [人名2]

Hi [人名18] ([人名18])，

的确，我使用的是SDK V2.9.0 ，没有这个API ；如何添加？在哪里调用？

</div>

<div class="reply even" markdown="1">

### 2022/06/13 13:43 — [人名17]

hi @[人名16]

请帮忙整理这份patch 与上层app 的patch 提供给客户测试

感谢

[附件: bt_connection_manager.diff]

</div>

<div class="reply odd" markdown="1">

### 2022/06/13 15:23 — [人名6]

Hi @[邮箱已隐藏]，

麻烦添加附件patch，然后APP 层 bt_cm_get_reconnect_profile 这个接口 参考 V2.11.0 直接copy 整个函数定义过去就好了~

[附件: bt_connection_manager.diff]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-49](ABT-49.md)　[→ 下一个工单：ABT-51](ABT-51.md)

</div>
