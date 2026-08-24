---
id: ABT-81
title: AB1565 FOTA 问题
date: 2022/09/08 18:50
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-81
---

# ABT-81 AB1565 FOTA 问题

> 📅 2022/09/08 18:50　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-81)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-80](ABT-80.md)　[→ 下一个工单：ABT-82](ABT-82.md)

</div>

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/09 11:30 — [人名10]

hi @[邮箱已隐藏]

请问你是使用什么方式进行FOTA ，谢谢

</div>

<div class="reply even" markdown="1">

### 2022/09/09 11:54 — [人名2]

Hi [人名10] ([人名10])，

使用的手机APP；

</div>

<div class="reply odd" markdown="1">

### 2022/09/09 13:44 — [人名10]

hi @[邮箱已隐藏]

 更新了vp，怎么FOTA到整机上；

----》  APP上不是有升级ROFS的吗，也就是升级fliesystem.bin ,  你那边想要升级的是这部分吧？
更新了 customerized_key_config.c ，FOTA到整机上无效；

----》  customerized_key_config.c 这个文件的改动属于mcu code部分改动，FOTA.bin 默认就包含DSP_FW 和 MCU_FW 两部分，是可以FOTA的，你说FOTA后无效，你具体说明下吗，比如是修改了哪部分内容，升级完之后无效，并附上升级前后的log 看一下，谢谢

</div>

<div class="reply even" markdown="1">

### 2022/09/09 14:14 — [人名2]

Hi [人名10] ([人名10])，

工具上只有生成FOTA.bin , fliesystem.bin 如何生成？

</div>

<div class="reply odd" markdown="1">

### 2022/09/09 14:26 — [人名10]

hi @[邮箱已隐藏]

不好意思，我重新说明下，升级时升级FOTA.bin 就好，可以不管UT APP的ROFS文件 

FOTA Package Tool  上勾选ROFS 的时候，勾选ROFS ，那么FOTA.bin 就包含ROFS 部分了，只要升级FOTA.bin就好，谢谢

[图片: image-2022-09-09-14-23-46-896.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/09 14:34 — [人名2]

Hi [人名10] ([人名10])，

看文档，FOTA.bin 和 FileSystem.biin 是不是独立分开升级的意思?

[图片: Snipaste_2022-09-09_14-30-33.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/09 16:35 — [人名2]

Hi [人名10] ([人名10])，

可以解答一下上个问题吗？

</div>

<div class="reply even" markdown="1">

### 2022/09/09 18:07 — [人名10]

Hi @[邮箱已隐藏]

这要看flash layout

你使用的是1565AM的吧 8M

因为 fota.bin  经过 LZMA 压缩之后的 ，压缩率在70%左右，fota buffer flash 大小可以够存 dsp + mcu + rofs 的

[图片: image-2022-09-09-18-04-49-108.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/09 19:13 — [人名2]

Hi [人名10] ([人名10])，

如果勾选上ROFS之后，FOTA结束后系统再也不能开机了；

</div>

<div class="reply even" markdown="1">

### 2022/09/13 10:34 — [人名10]

Hi @[邮箱已隐藏]

我再EVK上验证，可以FOTA success

你那边可以提供下log看下吗，log从升级前开始录，谢谢

</div>

<div class="reply odd" markdown="1">

### 2022/09/13 10:47 — [人名2]

Hi [人名10] ([人名10])，

见附件log；

[附件: FOTA 后无法开机.7z]

</div>

<div class="reply even" markdown="1">

### 2022/09/13 18:13 — [人名2]

Hi [人名10] ([人名10])，

今天会给解决方案试一试吗？

</div>

<div class="reply odd" markdown="1">

### 2022/09/13 18:19 — [人名10]

Hi @[邮箱已隐藏]

可以把你那边的原始固件Out 文件夹和你那边制作后的fota.bin 发过来吗，我再EVK上验证看看

</div>

<div class="reply even" markdown="1">

### 2022/09/13 19:00 — [人名2]

Hi [人名10] ([人名10])，

原始固件的out文件没有保留，附件是用来Fota 的 FW，生成的FotaPackage.bin 时修改了version，也会死机；我升级的时候，选择单个耳机升；

[附件: download.7z]

[附件: AB1565AM_V2.9.0_D86_V19_20220908_L.7z]

[附件: AB1565AM_V2.9.0_D86_V19_20220908_R.7z]

[附件: debug.7z]

[附件: V0020_FotaPackage_L.bin]

[附件: V0020_FotaPackage_R.bin]

[附件: FOTA 后无法开机-2.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/09/14 15:21 — [人名2]

Hi [人名10] ([人名10])，

看到为什么死机吗？

</div>

<div class="reply even" markdown="1">

### 2022/09/14 15:31 — [人名10]

Hi @[邮箱已隐藏]

还在分析中，我这边使用原生SDK验证是好像没有遇到你的那种问题，你也可以验证下看是不是这样，看下是不是改了什么东西导致的，谢谢

</div>

<div class="reply odd" markdown="1">

### 2022/09/14 15:50 — [人名2]

Hi [人名10] ([人名10])，

SDK 中加了AINR、LDAC、ECMP patch等等，demo 是没有这部分的。

</div>

<div class="reply even" markdown="1">

### 2022/09/14 16:27 — [人名10]

Hi @[邮箱已隐藏]

使用你发过来的

[附件: AB1565AM_V2.9.0_D86_V19_20220908_L.7z]

[附件: AB1565AM_V2.9.0_D86_V19_20220908_R.7z]

修改蓝牙地址保存会出现fail, 你那边不会出现这个问题吗

另外FOTA ROFS 也是可以单独升级的，生成ROFS.bin 和 FOTA.bin 方式是一样的，只要勾选对应的选项就好，然后点击生成FOTA包，你可以分开FOTA看看是否OK，谢谢

[图片: image-2022-09-14-16-22-54-579.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/14 16:39 — [人名2]

Hi [人名10] ([人名10])，

我使用的是V2.11.4的config tool，修改蓝牙地址后保存没有问题，使用V2.5.4 确实会fail，是所以使用V2.11.4 是因为后面V2.9.0 没有power detect 这个选项，单独升级ROFS试过的，也会fail；

</div>

<div class="reply even" markdown="1">

### 2022/09/15 10:25 — [人名10]

帮忙使用附件的固件验证下，谢谢
[附件: earbuds_ref_design.rar]

</div>

<div class="reply odd" markdown="1">

### 2022/09/15 11:25 — [人名2]

Hi [人名10] ([人名10])，

问题找到原因，我修改了 filesystem.bin 语音包的大小（320K），但是 ab156x_flash_8m.ld （AB1565AM）中 ROM_ROFS 的大小只有 264K，空间是不够的， 占用一些ROM_LM的空间，把ROM_ROFS 修改到320K，就可以FOTA了。

我再确认多几次，今天晚点会关闭问题。

</div>

<div class="reply even" markdown="1">

### 2022/09/16 15:28 — [人名2]

Hi [人名10] ([人名10])，

1. 更新nvkey OK；
2. 更新ROFS OK ；
3. 更新如 app_battery_idle_activity.c apps_events_battery_event.c OK ；
4. 更新 customerized_key_config.c， fail；

#4 修改后的内容FOTA 不到耳机中。

</div>

<div class="reply odd" markdown="1">

### 2022/09/16 18:20 — [人名2]

Hi [人名10] ([人名10])，

如沟通，更新 customerized_key_config.c，FOTA 不到耳机中，是因为我使用的key table会保留在 nvkey 中，下次初始化会从nvkey获取，不是在  customerized_key_config.c 的设定中。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-80](ABT-80.md)　[→ 下一个工单：ABT-82](ABT-82.md)

</div>
