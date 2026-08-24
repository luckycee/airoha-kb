---
id: ABT-98
title: dongle跟BT输出有差异
date: 2022/10/14 10:28
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-98
---

# ABT-98 dongle跟BT输出有差异

> 📅 2022/10/14 10:28　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-98)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-97](ABT-97.md)　[→ 下一个工单：ABT-99](ABT-99.md)

</div>

## 问题描述

Hi [人名5]，

相同的手机，用dongle和蓝牙连接输出（音量最大，播放1KhZ信号， AP测的），有差异，dongle输出的声音小，如何调整到一致？

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/10/14 10:28 — [人名2]

[图片: 0a2580e9893df54db37f8ae40b82a16.jpg]

[图片: 9d76a5737c3fb78e30058d35d2def85.jpg]

</div>

<div class="reply even" markdown="1">

### 2022/10/14 10:31 — [人名2]

不够清晰用这个

[附件: ap.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/10/14 11:35 — [人名2]

Hi 帝木，

我这边有调试dongle的配置 A2DP gain setting 到-5（默认是-15.5），但是没有作用。

</div>

<div class="reply even" markdown="1">

### 2022/10/14 11:38 — [人名4]

你能抓一下log吗

分别抓BT下耳机的log及dongle的log+耳机log

3份log ，再丢过来找SW看看

</div>

<div class="reply odd" markdown="1">

### 2022/10/14 15:07 — [人名2]

Hi 帝木 / fason，

com56 耳机右边；
com74 耳机左边；
com24 dongle;

[附件: 连接手机.7z]

[附件: donge+耳机.7z]

</div>

<div class="reply even" markdown="1">

### 2022/10/17 09:14 — [人名4]

@[人名13]

麻烦先帮美优看log对比一下

应该是dongle FW影响了

</div>

<div class="reply odd" markdown="1">

### 2022/10/17 09:31 — [人名4]

@[邮箱已隐藏]

hi 黄工，

再麻烦告知一下这个客户的名称

谢谢

</div>

<div class="reply even" markdown="1">

### 2022/10/17 09:33 — [人名4]

另外，你调过gain，是调Again 还是 D gain？

可以调一下Analog gain看看

</div>

<div class="reply odd" markdown="1">

### 2022/10/17 09:53 — [人名2]

Hi 帝木，

客户是[客户A]，调整的是附件位置，应该是digital gain ；

[图片: Snipaste_2022-10-17_09-52-18.jpg]

</div>

<div class="reply even" markdown="1">

### 2022/10/17 10:53 — [人名4]

ok 你再调一下A gain 看看

</div>

<div class="reply odd" markdown="1">

### 2022/10/17 15:33 — [人名2]

Hi 帝木，

调了这里，没有效果；

[图片: 微信图片_[序列号已隐藏].jpg]

</div>

<div class="reply even" markdown="1">

### 2022/10/17 18:01 — [人名4]

貌似内部有一题相似，我找同事讨论一下

晚些更新一下

</div>

<div class="reply odd" markdown="1">

### 2022/10/18 10:38 — [人名2]

Hi 帝木，

讨论到结果吗？

</div>

<div class="reply even" markdown="1">

### 2022/10/18 10:56 — [人名4]

内部的是[人名9]P uplink的，我再跟内部对一下

</div>

<div class="reply odd" markdown="1">

### 2022/10/18 11:01 — [人名4]

@[人名13]

请找SW RD帮忙看一下，上面记录有log

</div>

<div class="reply even" markdown="1">

### 2022/10/18 11:35 — [人名4]

!image-2022-10-18-11-35-07-448.png|width=533,height=320!

</div>

<div class="reply odd" markdown="1">

### 2022/10/18 14:14 — [人名2]

Hi 帝木，

客户改到了15，问题解决；

[图片: 微信图片_[序列号已隐藏].jpg]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-97](ABT-97.md)　[→ 下一个工单：ABT-99](ABT-99.md)

</div>
