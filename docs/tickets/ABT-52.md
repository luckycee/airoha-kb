---
id: ABT-52
title: "AB1565 uart0需改波特率"
date: 2022/05/30 11:16
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-52
---

# ABT-52 AB1565 uart0需改波特率

> 📅 2022/05/30 11:16　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-52)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-51](ABT-51.md)　[→ 下一个工单：ABT-53](ABT-53.md)

</div>

## 问题描述

Hi [人名4]，

客户做的headset，支持ANC的。他们想把TWS那一套调试ANC的设备和指令放到headset上，但是TWS是1wire，headset是5V常在。他们想用uart0来发送接收指令，uart1和uart2都被他们的key用去了；

1. 把uart0的波特率改为115200；

2. 把syslog不要，但是发送指令后要有指令的返回；

请看看如何实现；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/05/30 16:46 — [人名6]

Hi @[邮箱已隐藏]，

如电话沟通，客户上位机可以通过发送cmd的方式把log暂时关掉

RACE_SLEEP_CONTROL
055A0300200201 ：让耳机退出sleep
055B0300200200

 

DisableCpuLog （两条cmd对应两颗mcu，可以都试一下看哪个有用）
055A0600200F00090D0A ：暂时关闭log，reset后恢复
055D0300200F00
055A0600200F01090D0A：暂时关闭log，reset后恢复
055D0300200F00

可以用hal_uart_set_baudrate这个api改波特率

</div>

<div class="reply even" markdown="1">

### 2022/05/30 17:32 — [人名2]

Hi [人名6]，

关不掉，还是会有出来；

</div>

<div class="reply odd" markdown="1">

### 2022/05/30 17:36 — [人名2]

Hi [人名6]，

准确来说应该是可以了，关了部分的log（MCU的？），但是仍有一些出来（DSP的？）。

[附件: log.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/05/30 17:56 — [人名2]

Hi [人名6]，

本次开机有效
AT+SYSLOG=0,0,1,1 关mcu log
AT+SYSLOG=0,1,1,1 关dsp log

AT+SYSLOG=2 将关log设定存到nvdm，下次开机也生效

上面的内容是客户咨询你们RD还是其他人获取到的信息，我试了有效；但是客户的上位机怎么发送 AT cmd ？

</div>

<div class="reply odd" markdown="1">

### 2022/05/30 18:20 — [人名9]

@[邮箱已隐藏]

 AT CMD 是我回复给客户的， 上位机怎么发AT ，这是不是要问客户了啊？哈哈

</div>

<div class="reply even" markdown="1">

### 2022/05/31 09:33 — [人名6]

Hi @[邮箱已隐藏]，

发送055A0600200F00090D0A （cm4） 后再发送 055A0600200F01090D0A （DSP）就可以了~

</div>

<div class="reply odd" markdown="1">

### 2022/05/31 09:55 — [人名2]

hi  [人名6],

可以了！

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-51](ABT-51.md)　[→ 下一个工单：ABT-53](ABT-53.md)

</div>
