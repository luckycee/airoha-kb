---
id: ABT-33
title: AB1565 race cmd开启ANC 后没有输出
date: 2022/04/07 18:14
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-33
---

# ABT-33 AB1565 race cmd开启ANC 后没有输出

> 📅 2022/04/07 18:14　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-33)

## 问题描述

Hi 帝木，

客户使用附件的指令来做量产测试，发现发完ANC_ON后DSP没有输出，找了log我发现在有5V的时候DSP mute掉，没有输出。

客户希望普通使用的时候，接入5V就mute，通过race cmd控制ANC的时候，DSP不能mute，AB1562上已经验证并通过了的，客户希望AB1565跟AB1562保持一致；

对比1565 和1562的指令，我发现1565 少了两组的，是否这两组影响了？

ENTER_TEST_MODE_CMD =			'055A0400060E0010';

ENTER_TEST_MODE_RESPONSE =		'055B0400060E0010';

EXIT_TEST_MODE_CMD =			'055A0400060E0011';

EXIT_TEST_MODE_RESPONSE =		'055B0400060E0011';

即使加上这两组指令，发现也是不行的。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/07 18:14 — [人名2]

[附件: AB1565_race_cmd.txt]

</div>

<div class="reply even" markdown="1">

### 2022/04/08 09:36 — [人名4]

帮忙把log 抓出来

这题要找SW 看才行

</div>

<div class="reply odd" markdown="1">

### 2022/04/08 11:01 — [人名2]

Hi 帝木，

客户发完指令，掉5V就有输出了，他们认为这样能够解决问题。此题关闭；

</div>
