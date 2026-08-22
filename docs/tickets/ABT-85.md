---
id: ABT-85
title: I2S Audio 信号处理需求
date: 2022/09/16 15:57
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-85
---

# ABT-85 I2S Audio 信号处理需求

> 📅 2022/09/16 15:57　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-85)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-84](ABT-84.md)　[→ 下一个工单：ABT-86](ABT-86.md)

</div>

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

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-84](ABT-84.md)　[→ 下一个工单：ABT-86](ABT-86.md)

</div>
