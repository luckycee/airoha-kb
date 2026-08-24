---
id: ABT-29
title: "SDK V2.7.1 AB1565A earbuds_ref_design 使用hex文件播放异常 "
date: 2022/03/15 15:07
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-29
---

# ABT-29 SDK V2.7.1 AB1565A earbuds_ref_design 使用hex文件播放异常 

> 📅 2022/03/15 15:07　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-29)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-28](ABT-28.md)　[→ 下一个工单：ABT-30](ABT-30.md)

</div>

## 问题描述

Hi [人名6]，

客户参考了你们代码中播放hex 文件使用方法，发现在SDK V2.7.1 播放的声音失真的问题，相同的代码在SDK V2.9.0 中我试了OK，请帮忙看看为什么，比较奇怪；

附加有参考代码，可以自行添加测试验证；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/03/15 15:07 — [人名2]

[附件: code.c]

[图片: Snipaste_2022-03-15_15-03-58.png]

[图片: Snipaste_2022-03-15_15-04-32.png]

</div>

<div class="reply even" markdown="1">

### 2022/03/15 15:08 — [人名2]

这个 48K.mp3.hex 是“三声嘟嘟嘟”，开机后进入配对就能触发听到；

</div>

<div class="reply odd" markdown="1">

### 2022/03/15 15:11 — [人名2]

参考的地方在这里；

[图片: Snipaste_2022-03-15_15-11-09.png]

</div>

<div class="reply even" markdown="1">

### 2022/03/17 16:34 — [人名2]

Hi  [人名6],

长按开机之后，短按一下power_key，就能听到三声失真的提示音；

[附件: AB1565A_earbuds_ref_design.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/03/17 18:44 — [人名6]

Hi @[邮箱已隐藏]，

麻烦把prompt_control_play_tone_internal换成prompt_control_play_sync_tone试试。

</div>

<div class="reply even" markdown="1">

### 2022/03/17 20:59 — [人名2]

Hi [人名6]，

一样失真；

</div>

<div class="reply odd" markdown="1">

### 2022/04/01 17:20 — [人名6]

Hi @[邮箱已隐藏]，

这题可以升级SDK 使用吗？

2.7.1已经很旧了。而且hex文件我们不推荐使用！

可以转换成MP3试试？

</div>

<div class="reply even" markdown="1">

### 2022/04/01 17:43 — [人名2]

Hi [人名6]，

直接使用MP3 吗？怎么直接使用？

</div>

<div class="reply odd" markdown="1">

### 2022/04/06 09:59 — [人名6]

Hi @[邮箱已隐藏],

FYI

[附件: VP.wmv]
[附件: VP.pdf]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-28](ABT-28.md)　[→ 下一个工单：ABT-30](ABT-30.md)

</div>
