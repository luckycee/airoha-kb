---
id: ABT-43
title: "1565 dongle兼容性问题"
date: 2022/05/06 14:26
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-43
---

# ABT-43 1565 dongle兼容性问题

> 📅 2022/05/06 14:26　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-43)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-42](ABT-42.md)　[→ 下一个工单：ABT-44](ABT-44.md)

</div>

## 问题描述

Hi [人名6]，

客户在使用dongle时，遇到几个兼容性问题，我这边看了发送的内容都是正确的，是手机识别的问题，但客户不接受我的解释，请帮忙看看；

5. dongle连接了小米MIX 2X，上下曲变成音量加减，但是实际上的音量并没有变化。

6. dongle连接了小米MIX 2X，通话过程中单击没有结束电话，而是变成了静音，在单击就是取消静音。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/05/06 14:26 — [人名2]

[附件: 5Dongle,用小米连接Dongle测试，长按调出上下曲变成音量加减，但是实际上的音量并没有变化.pcapng]

[附件: 5L，用小米连接Dongle测试，长按调出上下曲变成音量加减，但是实际上的音量并没有变化.pcapng]

[附件: 5R，用小米连接Dongle测试，长按调出上下曲变成音量加减，但是实际上的音量并没有变化.pcapng]

[附件: 6Dongle，小米手机连接Dongle测试，通话过程中单击没有结束电话，而是变成了静音，在单击就是取消静音.pcapng]

[附件: 6L，小米手机连接Dongle测试，通话过程中单击没有结束电话，而是变成了静音，在单击就是取消静音.pcapng]

[附件: 6R，小米手机连接Dongle测试，通话过程中单击没有结束电话，而是变成了静音，在单击就是取消静音.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/05/07 11:37 — [人名14]

Hi @[邮箱已隐藏]，

    看到上下曲发送给手机的HID没有问题，手机自己不做音量处理我们也没办法。

    如果客户不接受，可以拿对比耳机测试看看其它产品在这个手机上的表现是否也是不正常的。

!image-2022-05-07-11-28-52-281.png|width=702,height=343!

Thanks.

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 11:43 — [人名14]

Hi @[邮箱已隐藏],

    HID做挂断电话是用的hold play/pause 2sec，spec并没有直接规定有挂断电话的操作，手机收到2秒长按完全看手机自己怎么处理。

Thanks.

</div>

<div class="reply even" markdown="1">

### 2022/05/07 18:12 — [人名2]

Hi [人名14],

好的，我已经将你的回复转给客户了，确认客户接受后，再关闭问题；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-42](ABT-42.md)　[→ 下一个工单：ABT-44](ABT-44.md)

</div>
