---
id: ABT-75
title: 1565 开放dsp的功能需求
date: 2022/08/24 15:57
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-75
---

# ABT-75 1565 开放dsp的功能需求

> 📅 2022/08/24 15:57　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-75)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-74](ABT-74.md)　[→ 下一个工单：ABT-76](ABT-76.md)

</div>

## 问题描述

Hi [人名5]，

这题跟 [ABT-71](ABT-71.md) 相关，同是[客户A]的终端客户提出来的。他们的App想通过利用发送指令的方式，让BT产生一些信号，并且自己播放，为了测试频响用，他们的App想做一些PEQ补偿。

附件pdf是他们详细的功能需求；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/08/24 15:57 — [人名2]

[附件: 5_[序列号已隐藏].pdf]

</div>

<div class="reply even" markdown="1">

### 2022/08/24 17:04 — [人名5]

Hi @[邮箱已隐藏],

他们的App想通过利用发送指令的方式----------->通过什么方式发送指令？race cmd？

让BT产生一些信号--------------->产生什么信号？

并且自己播放--------------->播放音乐？

为了测试频响用，他们的App想做一些PEQ补偿--------------->意思是app 发指令给耳机调节EQ？

</div>

<div class="reply odd" markdown="1">

### 2022/08/25 10:14 — [人名2]

Hi [人名5]，

通过什么方式发送指令？race cmd？
>> 通过BLE 或者是SPP 发送指令的方式；

产生什么信号？
>> 类似1KHz 0dB 这样的正弦波信号，像频点、增益、宽度、间隔都是通过App发指令来控制；（见附件图片）

播放音乐？
>> 对，就是通过播放音乐的方式，从喇叭输出；

意思是app 发指令给耳机调节EQ？
>> 是的；

[图片: Snipaste_2022-08-25_10-12-37.png]

</div>

<div class="reply even" markdown="1">

### 2022/08/25 12:20 — [人名5]

Hi @[邮箱已隐藏]，

所以需要我这边帮忙实现那部分功能呢

</div>

<div class="reply odd" markdown="1">

### 2022/08/25 15:08 — [人名2]

hi  [人名5] ,

需要看，如何产生信号。

</div>

<div class="reply even" markdown="1">

### 2022/08/26 09:16 — [人名5]

Hi @[邮箱已隐藏]，

你这个信号是想通过耳机本身产生还是连接手机由手机产生?

耳机本身就只能通过VP产生，你们存几档符合你们要求的VP ，然后发送cmd push media就好。

</div>

<div class="reply odd" markdown="1">

### 2022/08/26 10:06 — [人名2]

Hi fason，

通过耳机产生。

VP满足不了客户的要求，频点、增益、间隔都要求变化的。而VP只能做固定的。

</div>

<div class="reply even" markdown="1">

### 2022/08/26 13:49 — [人名5]

Hi @[邮箱已隐藏]，

那做不到啊，耳机自身发不了这种声音，只能是连接手机才能发。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-74](ABT-74.md)　[→ 下一个工单：ABT-76](ABT-76.md)

</div>
