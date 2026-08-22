---
id: ABT-39
title: AB1565 无法退出 APP_STATE_VA
date: 2022/04/28 15:39
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-39
---

# ABT-39 AB1565 无法退出 APP_STATE_VA

> 📅 2022/04/28 15:39　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-39)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-38](ABT-38.md)　[→ 下一个工单：ABT-40](ABT-40.md)

</div>

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/28 15:40 — [人名2]

[附件: Google Pixel 4a  触发语音助手并取消后所有按键无效了-L.pcapng]

[附件: Google Pixel 4a 触发语音助手并取消后所有按键无效了-R.pcapng]

[附件: iOS 触发语音助手并取消后所有按键仍然有效-L.pcapng]

[附件: iOS 触发语音助手并取消后所有按键仍然有效-R.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/04/28 17:34 — [人名8]

@[邮箱已隐藏]

你们现在用的SDK 是什么版本啊？

</div>

<div class="reply odd" markdown="1">

### 2022/04/28 17:46 — [人名2]

Hi [人名8]，

V2.9.0的

</div>

<div class="reply even" markdown="1">

### 2022/04/28 17:49 — [人名8]

@[邮箱已隐藏]

[附件: 5f5192c.diff.zip][附件: ab72805.diff.zip]

请加这个patch修改再验证一下，谢谢

</div>

<div class="reply odd" markdown="1">

### 2022/04/28 19:25 — [人名2]

Hi [人名8],

编译有问题；

[附件: error.txt]

</div>

<div class="reply even" markdown="1">

### 2022/04/29 09:56 — [人名8]

你patch加错位置了吧，加到下一条case去了？

[图片: image-2022-04-29-09-56-43-462.png]

</div>

<div class="reply odd" markdown="1">

### 2022/04/29 10:25 — [人名2]

Hi [人名8],

的确加错位置了；

</div>

<div class="reply even" markdown="1">

### 2022/05/05 17:15 — [人名2]

Hi [人名8],

客户验证了问题解决；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-38](ABT-38.md)　[→ 下一个工单：ABT-40](ABT-40.md)

</div>
