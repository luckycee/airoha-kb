---
id: ABT-83
title: AB1565 回连后profile没有连接
date: 2022/09/13 17:32
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-83
---

# ABT-83 AB1565 回连后profile没有连接

> 📅 2022/09/13 17:32　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-83)

## 问题描述

Hi [人名5]，

客户测试，在音乐播放状态下回连后，发现音乐不会流转到耳机端。在来电状态下回连后（客制化UI，回连后来电状态自动接听），发现话音信号仍在手机端，不会流转到耳机端。概率大约是30次有2次 。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/13 17:32 — [人名2]

[附件: 回连接听电话声音在手机端.rar]

[附件: 苹果12-IOS15.6.1系统-耳机回连手机音乐声音在手机端抓包.rar]

</div>

<div class="reply even" markdown="1">

### 2022/09/14 11:47 — [人名1]

Hi,

这份log "回连接听电话声音在手机端 \ L.pcapng " 中, 根据你标记的时间 : 16点12分.

12分06连上[人名9]P, 12分10就检测到charger, 然后断开了蓝牙. 说的是这个时间点吗?

[附件: 苹果12-IOS15.6.1系统-耳机回连手机音乐声音在手机端抓包.rar]  这份log时间请标记一下, 你也可以检查一下是否有检测充电导致蓝牙断开.

[图片: image-2022-09-14-11-24-52-883.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/15 17:12 — [人名2]

Hi [人名1] ([人名1])，

时间大约在 16:12:29 左右，发送了一个 接听电话的action，但是过了一会出现了BT_[人名9]P_DISCONNECT_IND ，之后每隔5s都会有 BT_[人名9]P_DISCONNECT_IND ，现象就是话音信号在耳机端；

</div>

<div class="reply even" markdown="1">

### 2022/09/15 17:12 — [人名2]

补充图片

[图片: Snipaste_2022-09-15_17-09-51.jpg]

</div>

<div class="reply odd" markdown="1">

### 2022/09/15 17:57 — [人名2]

Hi [人名1] ([人名1])，

"苹果12-IOS15.6.1系统-耳机回连手机音乐声音在手机端抓包.rar"中，时间在 15:12:59 开机后，24777行发起 [A2DP] a2dp_connect_REQ()，我看正常的连接播放只有一次，但是在后面的时间中，a2dp_connect_REQ() 不断有发出来，现象是音乐在手机端播放；

</div>

<div class="reply even" markdown="1">

### 2022/09/21 11:07 — [人名2]

Hi [人名1] ([人名1])，

有继续看吗？

</div>

<div class="reply odd" markdown="1">

### 2022/09/21 14:19 — [人名1]

Hi, @[邮箱已隐藏]

 从你提供的log [附件: 回连接听电话声音在手机端.rar]  耳机连接了2个手机, 

 一个[人名9]P连上了, channel:1422dc3c

 一个[人名9]P没连上. channel:1422dbf0,  

[图片: image-2022-09-21-11-31-21-890.png]

[图片: image-2022-09-21-11-32-49-630.png]

接电话的这台是  1422dc3c .

是SP端主动断掉了eSCO连线，才导致通话声外放.

[图片: image-2022-09-21-13-57-10-539.png]

谢谢.

</div>

<div class="reply even" markdown="1">

### 2022/09/21 14:40 — [人名1]

Hi, @[邮箱已隐藏]

  [附件: 苹果12-IOS15.6.1系统-耳机回连手机音乐声音在手机端抓包.rar]   这个log里面也是看到有2个[人名9]P的连接.  连接两个手机是预期行为吗? 

  建议确认一下客户的测试操作步骤 和 时间点 还有SDK版本 , 并提供完整的log(syslog和HCI log).

谢谢.

</div>

<div class="reply odd" markdown="1">

### 2022/09/27 10:36 — [人名2]

Hi [人名1] ([人名1])，

问题关闭，待客户重新验证；

</div>
