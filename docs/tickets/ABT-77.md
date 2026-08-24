---
id: ABT-77
title: V2.9.0 earbuds 手机显示电池电量不更新
date: 2022/09/05 11:04
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-77
---

# ABT-77 V2.9.0 earbuds 手机显示电池电量不更新

> 📅 2022/09/05 11:04　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-77)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-76](ABT-76.md)　[→ 下一个工单：ABT-78](ABT-78.md)

</div>

## 问题描述

Hi [人名5]，

客户测试到耳机在播放使用中，发现播放到提示音低电了，手机那边显示的电池电量都还是100%，比较概率性10%，还没有抓到log，抓的时候又次次正常，如果有相关补丁，请帮忙提供。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/05 14:42 — [人名5]

Hi @[邮箱已隐藏]，

不清楚客户是怎么测试的，是否有做RHO，左右耳电量是否相差比较大，10%-100%。

</div>

<div class="reply even" markdown="1">

### 2022/09/05 14:45 — [人名5]

可以看看app_hfp_report_battery_to_remote是否有传错的电量到手机

</div>

<div class="reply odd" markdown="1">

### 2022/09/07 17:35 — [人名2]

Hi [人名5]，

是执行RHO 后出现的问题；10:30:53 partner变为agent 之后（COM7），后面 app_hfp_idle_proc_battery_event_group() 处理一直有log，但是跑不进 app_hfp_report_battery_to_remote(); 所以电池电量就没有更新；附件我给了一个正常的；

[附件: 93.zip]

[图片: Snipaste_2022-09-07_17-32-18.png]

[附件: 单耳正常更新电量log.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/09/08 14:13 — [人名5]

Hi @@[邮箱已隐藏]，

看log Logging_COM7_00001_2022[电话已隐藏].pcapng，old partner RHO 成 new agent之后，没有跑app_hfp_idle_proc_battery_event_group，而是跑了app_hfp_idle_porc_app_internal_events，里面已经跑了app_hfp_report_battery_to_remote 更新电量了，但是电量还是没更新成功吗？

[图片: image-2022-09-08-14-13-12-384.png]

[图片: image-2022-09-08-14-13-51-598.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/08 14:32 — [人名5]

Hi @[邮箱已隐藏]，

如微信沟通，把hfp connect 的判断拿掉试试

[图片: image-2022-09-08-14-32-55-567.png]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-76](ABT-76.md)　[→ 下一个工单：ABT-78](ABT-78.md)

</div>
