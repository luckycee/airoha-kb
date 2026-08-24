---
id: ABT-89
title: 去掉了PEQ后无法保存
date: 2022/09/26 20:07
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-89
---

# ABT-89 去掉了PEQ后无法保存

> 📅 2022/09/26 20:07　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-89)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-88](ABT-88.md)　[→ 下一个工单：ABT-90](ABT-90.md)

</div>

## 问题描述

Hi 帝木，

发现去掉PEQ频点之后，无法保存到软件中；

使用V2.5.4，V2.11.2，V2.11.4都验证过，有次问题；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/26 20:07 — [人名2]

[图片: 修改之前.jpg]

[图片: 修改之后.jpg]

</div>

<div class="reply even" markdown="1">

### 2022/09/27 18:27 — [人名29]

@[邮箱已隐藏] 如果不需要EQ又想保存FW，先开一组PEQ，gain都设0 就好了.

</div>

<div class="reply odd" markdown="1">

### 2022/09/27 18:40 — [人名2]

Hi Sanmuel,

config tool 2.11.4, FW是AB1565AM

[附件: AB1565AM_V2.9.0_D86_V20_20220926_V0.25_L.7z]

[附件: AB1565AM_V2.9.0_D86_V20_20220926_V0.25_R.7z]

[附件: debug.7z]

</div>

<div class="reply even" markdown="1">

### 2022/09/30 18:16 — [人名2]

Hi [人名29]，

确认了问题在第一个频点上，把这个频点去掉就无法保存了，即使再勾选回来还是无法保存软件；

[图片: Snipaste_2022-09-30_18-15-03.jpg]

</div>

<div class="reply odd" markdown="1">

### 2022/10/11 11:29 — [人名4]

未勾選頻點算出來的NV長度為0,

nvdm driver不允許寫入長度為0的nv key

 

之後再勾選無法存檔的問題TW还要再查一下

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-88](ABT-88.md)　[→ 下一个工单：ABT-90](ABT-90.md)

</div>
