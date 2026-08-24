---
id: ABT-27
title: AB1565 添加第三方算法和空间问题
date: 2022/03/11 12:01
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-27
---

# ABT-27 AB1565 添加第三方算法和空间问题

> 📅 2022/03/11 12:01　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-27)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-26](ABT-26.md)　[→ 下一个工单：ABT-28](ABT-28.md)

</div>

## 问题描述

Hi [人名5]，

因为现在ABT 的方案还不支持空间音频，所以客户想使用第三方算法来实现，但是第三方算法消耗的RAM资源预计超过300KB。

客户计算过SDK 2.10.1版本CM4剩余RAM约86KB，DSP DRAM剩余约428KB，第三方算法如果单独使用CM4的RAM肯定不能满足，因此唯一的方法就是只将陀螺仪的驱动部分放到CM4，其它部分放DSP。目的就是想使用DSP部分的ROM/RAM资源，不知是否可行？

客户有看到ABT DSP是可用导入第三方的声音算法，但是空间音频算法应该属于一般控制算法，所以不确定能否导入到DSP FW。

1. 能导入的话该如何导入？导入后CM4如果跟DSP算法进行交互？

2. 不能导入的话DSP内部的DRAM能不能share出来给CM4使用？

3. 如果都可以，请提供方法；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/03/11 13:47 — [人名5]

Hi @[邮箱已隐藏]，

你们用的是A还是AM？

</div>

<div class="reply even" markdown="1">

### 2022/03/11 13:50 — [人名5]

86KB 你们怎么算的？

</div>

<div class="reply odd" markdown="1">

### 2022/03/11 14:22 — [人名5]

Hi @[邮箱已隐藏]，

这个需求很难实现，我们DSP RAM 剩余也就200多KB ，你们算法假如300多KB 不能缩减的话，很难移植进去了。

</div>

<div class="reply even" markdown="1">

### 2022/03/11 14:27 — [人名2]

Hi [人名5]，

AB1565AM参考这个链接方法得出
https://eservicedocs.ABT.com.tw/pages/viewpage.action?pageId=32606040

</div>

<div class="reply odd" markdown="1">

### 2022/03/11 14:32 — [人名5]

Hi @[邮箱已隐藏]，

很困难啊，而且空间音频基本都是A2DP 跟 VP 同时存在，还有耳机其他功能也在跑，影响很大的。

</div>

<div class="reply even" markdown="1">

### 2022/03/11 17:39 — [人名2]

Hi [人名5]，

那我这边回复客户做不了？？

</div>

<div class="reply odd" markdown="1">

### 2022/03/14 09:34 — [人名5]

Hi @[邮箱已隐藏]，

假如客户空间音频包300多K 缩减不了，就回复做不了吧。

</div>

<div class="reply even" markdown="1">

### 2022/03/16 14:43 — [人名7]

Dear all,

先回 1565AM 不支持, 我在跟客戶解釋

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-26](ABT-26.md)　[→ 下一个工单：ABT-28](ABT-28.md)

</div>
