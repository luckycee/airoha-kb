---
id: ABT-85
title: I2S Audio 信号处理需求
date: 2022/09/16 15:57
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-85
---

# ABT-85 I2S Audio 信号处理需求

> 📅 2022/09/16 15:57　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-85)

## 问题描述

Hi [人名5]，

在 [ABT-67](ABT-67.md)，我提出过I2S 在没有音乐的时候，也需要出0信号，现在客户又提出一个要求，是否存在这样一个接口，即在连接手机音乐播放状态，set 为 true则I2S 输出音乐的状态，set 为false 则 I2S 仅输出0信号，但是像voice prompt 出来时则需要加上；

[客户A]拿AB1565AM 来做音箱，他们支持4个音源：BT，其它2.4G，差分Mono Line In，单端Stereo Line In 。在非BT时，他们希望保持BT的连接，但是不要音乐声，只要0信号的I2S ；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/16 17:33 — [人名5]

Hi @[邮箱已隐藏]，

如电话沟通，把A2DP 音量降到0，I2S还是有输出的。

可以试一下在有line in插入的时候，把A2DP 的音量降到0，VP 的音量保持原来的音量。这样就可以实现Line in 的时候没有A2DP 声音输出，只播VP了。

</div>

<div class="reply even" markdown="1">

### 2022/09/19 15:30 — [人名2]

HI [人名5],

经验证，手机控制音量降到0或者调用 app_smcharger_mute_audio(TRUE)，如果使用的是I2S_MST0，GPIO6(I2S_MST0_MCLK)  \ GPIO8(I2S_MST0_TX) \ GPIO9(I2S_MST0_CK) \ GPIO10(I2S_MST0_WS) \ GPIO11(I2S_MST0_RX) ，GPIO8（音乐data信号）不会有输出了 ，其他GPIO6\GPIO9\GPIO10 仍有输出，voice prompt 不受影响仍可输出。

只要保证在此情况能够输出0信号，那么就能满足客户要求了。

</div>

<div class="reply odd" markdown="1">

### 2022/09/19 17:03 — [人名5]

给力啊！

</div>
