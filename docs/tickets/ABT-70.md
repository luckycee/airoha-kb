---
id: ABT-70
title: 1565 独立控制左右声道的音量
date: 2022/08/22 10:31
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-70
---

# ABT-70 1565 独立控制左右声道的音量

> 📅 2022/08/22 10:31　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-70)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-69](ABT-69.md)　[→ 下一个工单：ABT-71](ABT-71.md)

</div>

## 问题描述

Hi [人名5]，

客户想利用TWS来做音箱，问是否能够独立控制左右声道的音量？目前使用的软件，默认是两边同时变大变小的。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/08/24 15:08 — [人名5]

Hi @[邮箱已隐藏],

app_aws_sync_event_send 这个是sync 的api ，可以搜一下在哪里sync 按键的，拿掉就好了，注意要关掉手机绝对音量，不然做不到左右耳大小声不一样

</div>

<div class="reply even" markdown="1">

### 2022/08/25 10:15 — [人名2]

Hi fason，

怎么关闭手机绝对音量？

</div>

<div class="reply odd" markdown="1">

### 2022/08/25 11:47 — [人名5]

[图片: image-2022-08-25-11-47-11-902.png]

rsp.parameter_length = 2; 修改为1

rsp.response_type = BT_AVRCP_RESPONSE_INTERIM;；修改为BT_AVRCP_RESPONSE_NOT_IMPLEMENTED或者BT_AVRCP_RESPONSE_REJECTED

dev->volume_change_status = true; 删除或者修改为false

</div>

<div class="reply even" markdown="1">

### 2022/08/25 15:53 — [人名5]

[图片: image-2022-08-25-15-53-42-454.png]

再加个修改，这些黄色的标注的都不要了，这个函数值做回复response就好

bt_avrcp_send_set_absoulte_volume_response(absolute_volume_event->handle, absolute_volume_event->volume);

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-69](ABT-69.md)　[→ 下一个工单：ABT-71](ABT-71.md)

</div>
