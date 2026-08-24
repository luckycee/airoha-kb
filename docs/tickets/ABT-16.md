---
id: ABT-16
title: "ULL dongle连接电脑显示图标"
date: 2022/01/11 20:11
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-16
---

# ABT-16 ULL dongle连接电脑显示图标

> 📅 2022/01/11 20:11　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-16)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-15](ABT-15.md)　[→ 下一个工单：ABT-17](ABT-17.md)

</div>

## 问题描述

Hi [人名1]，

我在eService doc上看到 dongle 连接电脑可以修改图标，但是我的dongle （使用的是EVK）连接电脑却没有东西出来，是驱动还是哪里地方设置不对？

https://eservicedocs.ABT.com.tw/pages/viewpage.action?pageId=61899363

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/01/12 11:07 — [人名1]

Hi,

   尝试在电脑上禁用/卸载设备, 再重新启用设备看看.

谢谢

</div>

<div class="reply even" markdown="1">

### 2022/01/12 15:02 — [人名2]

Hi [人名1]，

在电脑上没有显示dongle应该出现的图标，我使用USB 接的EVK ，是不是有地方不对？

谢谢；

</div>

<div class="reply odd" markdown="1">

### 2022/01/12 15:27 — [人名2]

Hi [人名1]，

使用客户的板子，dongle连接手机使用是没有问题的；

</div>

<div class="reply even" markdown="1">

### 2022/01/13 09:36 — [人名1]

Hi,

       需要禁用/卸载dongle , 再重新启用/插上dongle. (dongle的全部卸载完)

[图片: image-2022-01-13-09-35-22-796.png]

[图片: image-2022-01-13-09-35-44-512.png]

谢谢.

</div>

<div class="reply odd" markdown="1">

### 2022/01/14 15:46 — [人名2]

Hi [人名1]，

接着USB的时候卸载了，拔掉再次接上USB ，什么也没有。

卸载之前我还截图保存了。

[图片: Snipaste_2022-01-14_15-38-29.png]

</div>

<div class="reply even" markdown="1">

### 2022/01/14 15:52 — [人名1]

Hi,

   我这边看SDK2.9.0的dongle代码上, 默认的是已经是修改了相关图标的. 不用再修改了.

   我这边用dongle烧录2.9.0默认程序, 重新删除PC上的设备(我以前是用的老版本程序, 所以电脑上图标不对), 再次插上dongle, PC上的图标就更新过来了.

   如果是老版本的SDK,建议你检查一下修改的地方, 是不是改错了.

谢谢.

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-15](ABT-15.md)　[→ 下一个工单：ABT-17](ABT-17.md)

</div>
