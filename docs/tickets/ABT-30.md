---
id: ABT-30
title: "AB1565 dongle + earbuds 咨询"
date: 2022/03/30 15:20
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-30
---

# ABT-30 AB1565 dongle + earbuds 咨询

> 📅 2022/03/30 15:20　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-30)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-29](ABT-29.md)　[→ 下一个工单：ABT-31](ABT-31.md)

</div>

## 问题描述

Hi [人名6]，

请帮忙回复以下客户问题，有一些我知道，但是大部分都是不清楚的；  

1. TX   AB1565D 到 RX   AB1565AM 之间延时可以做到多少MS?  全链路传输低延时是否能做到小于50MS（含PC端编解码与耳机接收端编解码时间）

  2. TX   AB1565D 到 RX   AB1565AM 之间传输用的多少G频率？用的什么音频编解码传输协议？

  3. RX   AB1565AM 与手机蓝牙连接，开启低延时模式时，低延时可以多到多少MS? 用的什么音频编解码传输协议？有什么特殊要求？全链路传输低延时是否能做到小于100MS

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/03/30 17:05 — [人名6]

Hi @[邮箱已隐藏]，
 # PC端编解码到PC从USB 丢数据出去的延时，我们没有数据。我们只保证PC USB output 到 Headset output output之间latency < 25ms

 # BT2.4G. Airoho 自己的codec

</div>

<div class="reply even" markdown="1">

### 2022/03/31 11:16 — [人名6]

Hi !@[邮箱已隐藏],

3、默认情况下， SBC 低延时模式是160ms 左右，AAC 是220ms。全链路可以做到100ms ，但是可能会有jumpness，或者需要手机配合。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-29](ABT-29.md)　[→ 下一个工单：ABT-31](ABT-31.md)

</div>
