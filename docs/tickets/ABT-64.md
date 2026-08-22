---
id: ABT-64
title: 暂停后立刻播放，发现无法播放
date: 2022/07/22 12:06
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-64
---

# ABT-64 暂停后立刻播放，发现无法播放

> 📅 2022/07/22 12:06　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-64)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-63](ABT-63.md)　[→ 下一个工单：ABT-65](ABT-65.md)

</div>

## 回复记录

<div class="reply odd" markdown="1">

### 2022/07/22 12:06 — [人名2]

[附件: Desktop.7z]

</div>

<div class="reply even" markdown="1">

### 2022/07/22 12:11 — [人名2]

Hi [人名5]，

附件是iPhone 7 的log，也是连续多次发送的0x55，但是播放暂停没有影响；

[附件: iphone log.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/07/25 10:44 — [人名8] [人名19]

hi @[邮箱已隐藏]

请问SDK使用的是哪个版本号呢？

</div>

<div class="reply even" markdown="1">

### 2022/07/25 11:00 — [人名2]

Hi [人名8]huaZhang，

V2.9.0

</div>

<div class="reply odd" markdown="1">

### 2022/07/25 14:59 — [人名8] [人名19]

hi @[邮箱已隐藏]

分析正常的log [附件: iphone log.7z]

^[图片: image-2022-07-25-14-51-57-494.png]^

Agent  端收到Partner Sync 过来的Key event

3304 12:08:36.262399 19 [M:apps C:info F: L: ]: [Music_APP]utils [LEA][BIS] [40] received key action=0x0055

Bt Send PLAY_PAUSE

3361 12:08:36.263168 75 [M:sink_srv C:info F: L: ]: [Sink]bt_sink_srv_send_action, action:0xf8150008, module:0xf8100000

AVRCP  Send operation

3366 12:08:36.263168 80 [M:sink_srv C:info F: L: ]: [sink][avrcp]process_avrcp_action[s]-event: 0xf8150008, base: 0xf8150000

Message Send

3406 12:08:36.348364 113 [M:sink_srv C:info F: L: ]: [sink][avrcp]common_hdr[s]-msg: 0x38000004, status: 0

手机执行AVRCP Operation传回Notification

3424 12:08:36.408253 129 [M:sink_srv C:info F: L: ]: [sink][avrcp]event_notification_ind(changed)--evt_id: 1, status: 2

 

上面的分析是正常的log，正常的大致例程：耳机Send AVRCP Operation 到手机端，手机端执行并返回处理结果

 

分析异常log [附件: Desktop.7z]

^这个问题出现在第一次Key Pause事件^

^[图片: image-2022-07-25-14-50-52-571.png]^

Agent  端收到Partner Sync 过来的Key event

2467 11:50:36.348611 250 [M:apps C:info F: L: ]: [Music_APP]utils [LEA][BIS] [40] received key action=0x0055

Bt Send PLAY_PAUSE

2518 11:50:36.349608 44 [M:sink_srv C:info F: L: ]: [Sink]bt_sink_srv_send_action, action:0xf8150008, module:0xf8100000

AVRCP  Send operation

2523 11:50:36.349608 49 [M:sink_srv C:info F: L: ]: [sink][avrcp]process_avrcp_action[s]-event: 0xf8150008, base: 0xf8150000

Message Send

2559 11:50:36.442256 77 [M:sink_srv C:info F: L: ]: [sink][avrcp]common_hdr[s]-msg: 0x38000004, status: 0

 

但是并没有看到手机回给耳机手机端处理AVRCP Operation的结果，从 sys log 看来应该是手机IOT 问题

听您的描述只有部分手机才会出现的话，应该是手机问题

进一步确认是否是手机问题需要抓Air log

</div>

<div class="reply even" markdown="1">

### 2022/07/25 16:42 — [人名2]

Hi [人名8]huaZhang，

好的，预计明天能收到客户的样机；

收到后，再与你约时间抓Air log；

</div>

<div class="reply odd" markdown="1">

### 2022/07/26 18:02 — [人名2]

Hi [人名8]huaZhang，

收到客户的手机了，明天看那个时间段你方便，我带上手机过去抓Air log；

</div>

<div class="reply even" markdown="1">

### 2022/07/26 18:06 — [人名8] [人名19]

hi @[邮箱已隐藏]

明天早上过来吧，会议室1301

</div>

<div class="reply odd" markdown="1">

### 2022/07/26 18:50 — [人名2]

Hi [人名8]huaZhang，

好的，明天早上10:00 到；

</div>

<div class="reply even" markdown="1">

### 2022/07/27 10:02 — [人名2]

Hi [人名8]huaZhang，

[M:BT_DM_EDR C:info F: L: ]: [BT_DM] Addr type 1, address:0x00:0x00:0x00:0x00:0x09:0x43
[M:BT_DM_EDR C:info F: L: ]: [BT_DM] link key:77,ee,3a,58,  82,dc,f3,a6,  43,86,7e,9d,  72,f1,40,55

我已经在1301

</div>

<div class="reply odd" markdown="1">

### 2022/07/27 10:15 — [人名2]

时间点	2022-07-27 10:12:54.520982	

[附件: Desktop.7z]

</div>

<div class="reply even" markdown="1">

### 2022/07/27 11:23 — [人名8] [人名19]

时间点 2022-07-27 10:12:54.520982

[附件: Desktop.7z]

_匹配的Air log_
[附件: Untitled.btt]

</div>

<div class="reply odd" markdown="1">

### 2022/07/27 14:37 — [人名2]

Hi [人名8]huaZhang，

在高通 3020 ，Realtek 8753 也试到了。

不过还请分析log，需要就原理跟客户说明。

</div>

<div class="reply even" markdown="1">

### 2022/07/28 11:14 — [人名8] [人名19]

hi  @[邮箱已隐藏]

分析 耳机端的HCI log 

图中标示的部分，耳机这边在10:12:54时 已经送一次 AVRCP Operation 出去，10:12:56 的时候也送一次AVRCP Operation 出去

[图片: image-2022-07-28-11-09-29-773.png]

Air log 分析

可以看到耳机发送的两次AVRCP Operation 已经送出去了，至于手机端为什么不响应，可能手机这时候有其他的事情在忙没有及时的去处理，这是手机的问题

[图片: image-2022-07-28-11-11-51-850.png]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-63](ABT-63.md)　[→ 下一个工单：ABT-65](ABT-65.md)

</div>
