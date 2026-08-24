---
id: ABT-79
title: AB1565 5V常在方案满电进入深睡
date: 2022/09/07 11:11
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-79
---

# ABT-79 AB1565 5V常在方案满电进入深睡

> 📅 2022/09/07 11:11　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-79)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-78](ABT-78.md)　[→ 下一个工单：ABT-80](ABT-80.md)

</div>

## 问题描述

HI [人名5]，

5V常在方案，充慢点之后，不会进入深睡，配置工具上没有 deep sleep mode，只有 low power mode，使用了测试都不充电了；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/07 11:11 — [人名2]

[图片: Snipaste_2022-09-07_11-09-18.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/07 11:31 — [人名2]

[附件: 满电后5V端电流有300uA.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/09/07 17:53 — [人名5]

Hi @[邮箱已隐藏]，

麻烦在这里添加这行，让后测试看看：

[图片: image-2022-02-08-10-15-14-475.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/07 17:57 — [人名2]

Hi fason，

看不到你的图片？

</div>

<div class="reply odd" markdown="1">

### 2022/09/07 17:59 — [人名5]

[图片: image-2022-09-07-17-59-09-513.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/07 18:19 — [人名2]

Hi [人名5]，

没有效果；

[附件: 满电不进入deepsleep.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/09/08 10:47 — [人名5]

Hi @[邮箱已隐藏]，

麻烦添加附件patch试试~
[附件: [ABT-79](ABT-79.md).rar]

</div>

<div class="reply even" markdown="1">

### 2022/09/08 18:48 — [人名2]

Hi [人名5]，

还是不行；

</div>

<div class="reply odd" markdown="1">

### 2022/09/14 09:50 — [人名5]

Hi @[邮箱已隐藏]，

麻烦再帮忙提供下log

進不了RTC是因為rtc tick 被打開 上完修正後  應該要看不到這個log

[图片: image-2022-09-14-09-52-38-709.png]
[图片: image-2022-09-14-09-52-38-709.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/14 11:16 — [人名2]

Hi [人名5]，

看到 Charger state已经变到6，但是 tick 仍出现；

[附件: 满电不进入deepsleep-20220914.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/09/14 13:40 — [人名5]

Hi @[邮箱已隐藏]，

这份log没有重头开始的log，没办法确认。

麻烦提供重开机开始到冲满的log

</div>

<div class="reply even" markdown="1">

### 2022/09/14 13:41 — [人名5]

Hi @[邮箱已隐藏]，

麻烦提供一下開機log 裡面需包含正常開機跟短按開機(會直接進RTC mode)

然後提供對應的檔案 : hal_pmu_internal_2565.c

</div>

<div class="reply odd" markdown="1">

### 2022/09/14 14:14 — [人名2]

Hi [人名5]。

上电到，充满的log；

[附件: 满电不进入deepsleep-20220914-2.pcapng]

[附件: hal_pmu_internal_2565.c]

[附件: 单按，但是不开机.pcapng]

[附件: 正常开机.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/09/15 13:42 — [人名5]

Hi @[邮箱已隐藏]，

这边看log，最后charging state都是 5,6，（5：充电过热暂停，6：过充） ，56 可能就是客户充电环境问题了。麻烦确认下充电环境是否有问题。

另外麻烦确认下MTK_BATTERY_EOC_ENTER_RTC是否有打开

[图片: image-2022-09-15-13-42-49-465.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/15 14:40 — [人名2]

Hi [人名5]，

开启  MTK_BATTERY_EOC_ENTER_RTC ，就可以，feature.mak 中默认关闭；

测试环境是正常的，没有过热的情况，但是我看到log停止时 Charger State仍然为 6 ，是否软件仍有问题；

</div>

<div class="reply even" markdown="1">

### 2022/09/15 14:44 — [人名5]

Hi @[邮箱已隐藏]，

没有过热的情况就没问题了，显示4是在前面，前面能进就好了。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-78](ABT-78.md)　[→ 下一个工单：ABT-80](ABT-80.md)

</div>
