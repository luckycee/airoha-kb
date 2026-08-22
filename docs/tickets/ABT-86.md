---
id: ABT-86
title: AB1585 V3.3.0 earbuds_ref_design_ull2 跟dongle配对
date: 2022/09/22 16:00
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-86
---

# ABT-86 AB1585 V3.3.0 earbuds_ref_design_ull2 跟dongle配对

> 📅 2022/09/22 16:00　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-86)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-85](ABT-85.md)　[→ 下一个工单：ABT-87](ABT-87.md)

</div>

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/23 15:11 — [人名5]

Hi @[邮箱已隐藏]，

ULL2.0配对：

1.dongle和earbuds开机之后，设定相同的SIRK：AT+LEULL=SIRK,SET,1,2,3,4,5,6,7,8,9,0,A,B,C,D,E,F

2.分别重启dongle/earbuds，其会再开机之后自动连接，成功时会听到”叮”提示音

默认dongle依旧是两张声卡：

[图片: image-2022-09-23-15-11-29-109.png]

EVK上要拔掉r1306电阻：

[图片: image-2022-09-23-15-11-52-653.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/26 20:25 — [人名2]

Hi [人名5]，

你的截图是1565AM的，应该是1585才对。

</div>

<div class="reply odd" markdown="1">

### 2022/09/27 09:28 — [人名5]

Hi @[邮箱已隐藏]，

85也是一样的，直接测试吧

</div>

<div class="reply even" markdown="1">

### 2022/09/27 19:51 — [人名2]

Hi [人名5]，

可以连接了；但是有问题：

1. 播放音乐就会死机（附件有FW和死机log，时间在19:41:23）；
2. 有没有更加方便，如key的方式来让他们连接起来，客户没法使用logging tool 发送指令；

[附件: Logging220927_194041_COM74.7z]

[附件: dongle_ref_design_ull2.7z]

[附件: earbuds_ref_design_ull2.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/09/28 10:27 — [人名5]

Hi @[邮箱已隐藏]，

我们目前只能通过at cmd 设定 sirk 的方式配对，暂时没办法用key。

</div>

<div class="reply even" markdown="1">

### 2022/09/28 10:59 — [人名2]

Hi [人名5]，

好，死机怎么样？

</div>

<div class="reply odd" markdown="1">

### 2022/09/28 11:30 — [人名5]

Hi @[邮箱已隐藏]，

请咋earbuds端的mcu和dsp两个mk里面开下面的option：

[图片: image-2022-09-28-11-30-21-350.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/28 11:49 — [人名2]

Hi [人名5]，

确认过的，都有打开，code我只修改了customerized_key_config.c的内容，其他没有动。

</div>

<div class="reply odd" markdown="1">

### 2022/09/28 11:50 — [人名2]

Hi [人名5]，

或者把你的FW给我试一试；

</div>

<div class="reply even" markdown="1">

### 2022/09/28 18:26 — [人名2]

Hi [人名5]，

有结果吗？

</div>

<div class="reply odd" markdown="1">

### 2022/09/29 11:23 — [人名5]

Hi @[邮箱已隐藏]，

我这边用附件FW测试播放音乐没有宕机，一切正常

耳机:./build.sh ab1585_evk earbuds_ref_design_ull2
dongle:./build.sh ab1585_evk dongle_ref_design_ull2
[附件: ab158x.rar]

</div>

<div class="reply even" markdown="1">

### 2022/09/29 14:10 — [人名5]

Hi @[邮箱已隐藏]，

上午发错文件了，麻烦用附件软件测试
[附件: ab1585_evk.rar]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-85](ABT-85.md)　[→ 下一个工单：ABT-87](ABT-87.md)

</div>
