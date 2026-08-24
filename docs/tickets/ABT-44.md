---
id: ABT-44
title: "1565 中断使用VP或者timer会导致死机"
date: 2022/05/06 18:21
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-44
---

# ABT-44 1565 中断使用VP或者timer会导致死机

> 📅 2022/05/06 18:21　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-44)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-43](ABT-43.md)　[→ 下一个工单：ABT-45](ABT-45.md)

</div>

## 问题描述

Hi [人名6]，

外加的光感控制器，使用的中断、回调函数处理，客户要求，光感检测到入耳之后，播放一个提示音。但是你们的eService Docs 中提示，在中断中加入vp会导致死机；实测不单加vp会死机，加timer也会死机。有方法可以规避死机吗？

加timer，主要是为了做消抖，防止客户快速出入耳导致功能错乱；

https://eservicedocs.ABT.com.tw/pages/viewpage.action?pageId=54035258

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/05/07 14:26 — [人名13]

Hi @[邮箱已隐藏]，
 # 防抖可以用eint 本身的sw deounce timing, 具体参考bsp_gsensor_platform_eint_init 这个func
 # 中断播vp死机 ，一般做法则是中断通过ui_shell_send_event 到APP层去播放vp,具体参考该func在code中的使用

thanks

</div>

<div class="reply even" markdown="1">

### 2022/05/07 16:27 — [人名2]

hi  [人名13]Huang,

使用 ui_shell_send_event  也会导致死机；

Miuix_SendKeyAction() 参考的bt_race_key_app_event_callback() 来写；

[图片: Snipaste_2022-05-07_16-11-25.png]

[图片: Snipaste_2022-05-07_16-22-21.png]

[附件: 中断中使用ui_shell_send_event会死机.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 17:05 — [人名13]

Hi @[邮箱已隐藏]，

你已经在那个event那里做了播放vp的处理了对吧？

518 2022-05-07 16:09:21.452880 [M:ui_shell C:info F: L: ]: ui_shell_send_event: 0x2, 0xffff, delay:0

我看这里的delay是0，延长一下也会死机吗？

</div>

<div class="reply even" markdown="1">

### 2022/05/07 17:19 — [人名2]

hi [人名13]Huang,

你已经在那个event那里做了播放vp的处理了对吧？
>> 还没有加vp，只是发一个key event出去，希望入耳播放音乐；

我看这里的delay是0，延长一下也会死机吗？
>> 没有延时，0不就是没有延时了吗？这个0也是参考bt_race_key_app_event_callback() 的

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 18:18 — [人名2]

Hi [人名13]Huang,

附件是我使用的中断及sendKeyEvent的接口，应该你也能复现问题；

[附件: Interrupt.c]

</div>

<div class="reply even" markdown="1">

### 2022/05/10 11:03 — [人名2]

Hi [人名13]Huang,

此题有解决方法了吗？

</div>

<div class="reply odd" markdown="1">

### 2022/05/10 16:49 — [人名13]

Hi  @[邮箱已隐藏],

麻烦按照下图修改再测试下

[图片: image-2022-05-10-16-49-35-327.png]

</div>

<div class="reply even" markdown="1">

### 2022/05/10 18:06 — [人名2]

Hi [人名13]Huang,

问题解决了；

</div>

<div class="reply odd" markdown="1">

### 2022/05/10 18:11 — [人名2]

Hi [人名13]Huang,

好奇问一下，在内部处理，from_isr 这个参数true 和false，处理上有什么不同？

</div>

<div class="reply even" markdown="1">

### 2022/05/10 18:15 — [人名13]

Hi @[邮箱已隐藏]，

在中断中调用true,非中断调用false,

freertos 操作系统里面中断和非中断中调用使用的API有些是不同的，比如此题用的信号量这个API

[图片: image-2022-05-10-18-14-07-865.png]

</div>

<div class="reply odd" markdown="1">

### 2022/05/10 19:37 — [人名2]

Hi [人名13]Huang,

是不是在中断状态下，左右耳不能sync data，我希望把所有的入耳处理放到agent做处理，在partner入耳时，把data给到agent，让agent来控制。但是我又发现死机了。

平常用没有发现问题；

[附件: syncData.c]

</div>

<div class="reply even" markdown="1">

### 2022/05/11 09:00 — [人名13]

Hi @[邮箱已隐藏]，

中断下请不要处理任何太复杂或者耗时长的问题，有什么action，shell event 到上层处理

中断下不能播vp是因为app_voice_prompt_play中拿了mutex，按照这个方式，只要拿了mutex,都会assert在同一位置，

[图片: image-2022-05-11-09-01-48-207.png]
thanks

</div>

<div class="reply odd" markdown="1">

### 2022/05/11 11:22 — [人名2]

Hi [人名13]Huang,

好的，我知道如何实现想要的功能了。

感谢支持；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-43](ABT-43.md)　[→ 下一个工单：ABT-45](ABT-45.md)

</div>
