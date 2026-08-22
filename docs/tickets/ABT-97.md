---
id: ABT-97
title: AB1565 V2.9.0 回连接听电话问题
date: 2022/10/11 18:22
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-97
---

# ABT-97 AB1565 V2.9.0 回连接听电话问题

> 📅 2022/10/11 18:22　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-97)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-96](ABT-96.md)　[→ 下一个工单：ABT-98](ABT-98.md)

</div>

## 回复记录

<div class="reply odd" markdown="1">

### 2022/10/11 18:23 — [人名2]

[附件: 通话声音在手机端.rar]

</div>

<div class="reply even" markdown="1">

### 2022/10/12 11:16 — [人名17]

Hi @[邮箱已隐藏]

你自动接听的功能是怎么做的？麻烦提供一下修改。

</div>

<div class="reply odd" markdown="1">

### 2022/10/12 14:47 — [人名2]

Hi Tony，

客户提出一个设想，仍然开启EMP ，回连的时候能否只回连一只手机？像没有开启EMP那样。要连接第二手机，用户可以在手机端点击名字连接。

</div>

<div class="reply even" markdown="1">

### 2022/10/12 15:21 — [人名17]

Hi  @[邮箱已隐藏]

可以只回连一个设备。

你可以修改成只回连最后一支设备

[图片: image-2022-10-12-15-20-47-009.png]

</div>

<div class="reply odd" markdown="1">

### 2022/10/13 14:04 — [人名17]

HI @[邮箱已隐藏]

补充一下，图片红框要拿掉，不然当回连失败两次后，会将倒数第二支手机的记录跟最后一支手机的记录互换。

[图片: image-2022-10-13-14-03-53-435.png]

</div>

<div class="reply even" markdown="1">

### 2022/10/14 14:28 — [人名2]

Hi [人名17]，

修改了测试只会回连最后一个手机；客户需要继续测试，和考虑是否关闭EMP ；

</div>

<div class="reply odd" markdown="1">

### 2022/10/14 19:13 — [人名2]

Hi [人名17]，

看客户测试流程：
1. 连接了手机A，关闭手机A蓝牙；
2. 耳机入仓（关机），出仓开机（log开始录制），回连不上进入配对；
3. 手机B搜索到耳机，并连接，先接连接上A2DP，直到30多秒后才连接上[人名9]P ；

我看到，在连接手机B的过程，耳机还在不停发起对手机A的连接，并且最终手机B的[人名9]P也连接上了，对手机A仍发起连接请求，会不会导致了手机慢？是不是仍有地方需要修改为连接一个手机后，不再发起回连？

[附件: 连接慢-R.pcapng]

[附件: 连接慢-L.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/10/17 09:48 — [人名17]

Hi @[邮箱已隐藏]

这样的话，你就要在连上一支设备的ACL的时候，就要将reconnect给cancel掉才行。

</div>

<div class="reply odd" markdown="1">

### 2022/10/17 10:53 — [人名2]

Hi [人名17]，

我在手机回连之后，调用了 bt_cm_cancel_connect(NULL); ，没有看到之前的连接请求，但是一直有 8782	10:49:25.633513	 [M:BTGAP C:info F: L: ]: [GAP] enter bt_gap_connection_sniff_timeout() 这个timeout的log，关闭时是没有的，应该是我没有改好？请提供不会引起 side effect的方法。

[附件: 连接的手机取消其他回连-L.pcapng]

[附件: 连接的手机取消其他回连-R.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/10/17 11:11 — [人名17]

Hi  @[邮箱已隐藏]

麻烦重新抓一下log，从开机开始抓，然后列一下测试手机的address，跟描述一下测试具体步骤，方便分析。

</div>

<div class="reply odd" markdown="1">

### 2022/10/19 11:07 — [人名2]

Hi [人名17]，

加入阻止回连的请求后，客户接受了目前效果。问题先关闭，等他们继续反馈，我处理不好再请教，感谢。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-96](ABT-96.md)　[→ 下一个工单：ABT-98](ABT-98.md)

</div>
