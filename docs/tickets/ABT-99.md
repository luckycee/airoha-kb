---
id: ABT-99
title: FOTA 版本的设置
date: 2022/10/14 18:28
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-99
---

# ABT-99 FOTA 版本的设置

> 📅 2022/10/14 18:28　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-99)

## 问题描述

Hi [人名5]，

1. 有像1562x那样，在配置工具上的FW_Information 那样设置版本的地方吗？

2. 我尝试通过 fota_version_write() 直接写版本，但是通过Flash Tool 甚至MP Tool 烧录之后，再去读取居然写的内容还保持着，这是为什么？

3. 通过 FOTA Package Tool 生产的升级文件，升级后，再用Flash Tool 和MP Tool 烧录，读取到的还是 FOTA中设置的版本，这是为什么？

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/10/14 18:28 — [人名2]

[图片: 1.jpg]

[图片: 2.jpg]

[图片: 3.jpg]

</div>

<div class="reply even" markdown="1">

### 2022/10/18 18:11 — [人名32]

Dear customer,

        FOTA version是放在FOTA partition里面的，用Flash Tool 选择升级partition的时候，FOTA partition没有包含在.cfg文件里面，所以 FOTA version不会被擦除，thanks。

</div>

<div class="reply odd" markdown="1">

### 2022/10/18 18:27 — [人名2]

Hi [人名32] ([人名32]),

好的，明白了。同理MP 烧录也是调用的是 .cfg ，FOTA version也不会被擦除。

客户的需求是编译出来的软件有一个初始版本，FOTA时版本会进行更新。这个如何实现。

</div>

<div class="reply even" markdown="1">

### 2022/10/18 19:16 — [人名32]

hi @[邮箱已隐藏]

   1、  FOTA version有初始值，是放在如下的文件中。 [图片: image-2022-10-18-19-13-07-382.png]

  

   2、用fota package tool生成fota bin的时候，tool里面有个version的框，填入version value，fota完成的时候，fota version就会更新成新的version。

[图片: image-2022-10-18-19-14-39-995.png]

</div>

<div class="reply odd" markdown="1">

### 2022/10/19 10:49 — [人名2]

Hi [人名32] ([人名32]),

关于#1 通过修改你提供的地方，使用Flash Tool和MP Tool 烧录，版本并不会发生改变；关于#2 验证是OK的；

</div>

<div class="reply even" markdown="1">

### 2022/10/20 09:14 — [人名32]

hi @[邮箱已隐藏]

     FOTA version是放在FOTA  partition的最后4K中，请确认使用Flash Tool和MP Tool 烧录时是否有包含到最后4K的位置， thanks。

</div>

<div class="reply odd" markdown="1">

### 2022/10/20 10:33 — [人名2]

Hi [人名32] ([人名32]),

见附件图片；

左边是 ab156x_flash_8m.ld 右边是Flash Tool 导入 flash_download.cfg 后的；其中绿色部分是两边都对应上的，黄色是FOTA 部分，右边没有包含，所以这就是版本号不会改变的原因吗？红色部分内容有4K，是不是跟你说的4K相关？

再明确一下需求：编译出来的软件有一个初始版本（连接了App可用正确读取），FOTA时版本会进行更新。

请帮忙指导如何实现。

[图片: Snipaste_2022-10-20_10-27-15.jpg]

</div>

<div class="reply even" markdown="1">

### 2022/10/20 10:59 — [人名32]

hi  @[邮箱已隐藏]

      1、FOTA partition是这个，FOTA version是放在这个partition的最后4K位置。

      [图片: image-2022-10-20-10-42-15-970.png]

    2、其中绿色部分是两边都对应上的，黄色是FOTA 部分，右边没有包含，所以这就是版本号不会改变的原因吗？

         >是的。

   3、再明确一下需求：编译出来的软件有一个初始版本（连接了App可用正确读取），FOTA时版本会进行更新。

        >请问这个版本是什么版本？如果不是FOTA版本， 这个版本就不是放在FOTA partition的最后4K。

        >如果是FOTA 版本，如前面的回答，FOTA version有默认值是 [图片: image-2022-10-20-10-55-21-845.png] ，正常做完FOTA的时候，版本            会更新成用tool做FOTA package时填入的版本，比如 [图片: image-2022-10-20-10-57-49-078.png] 。

</div>

<div class="reply odd" markdown="1">

### 2022/10/20 11:20 — [人名2]

Hi [人名32] ([人名32]),

请问这个版本是什么版本？
>> 综合来看，应该是FOTA的版本了，连接了你们提供的Android App之后会获取（见附件图片），在制作FotaPackage.bin 时，修改“Version”，FOTA成功后，这个地方也会发生改变；

我想明白了，是不是这样？因为我使用的是EVK，被我多次使用并FOTA更新，“FOTA partition”里面已经包含了data（最后一FOTA设置的VERSION 值），而“FOTA_DEFAULT_VERSION”这个初始值，只会在 “FOTA partition”没有data才会使用，而且使用Flash tool或者MP 烧录时这部分不会被更新；

正确的做法，是不是应该在Flash tool或者MP 烧录时，把这部分擦除掉，这样 FOTA_DEFAULT_VERSION 就会起作用了？是否可以这么做？怎么修改 flash_download.cfg ？

[图片: 微信图片_[序列号已隐藏].jpg]

</div>

<div class="reply even" markdown="1">

### 2022/10/20 11:52 — [人名2]

Hi [人名32] ([人名32]),

之前我尝试修改过version，也修改成功了，做法就是每次开机的时候都往存版本号的地方，写入一个固定值。

我不采用这个方式，因为只能在code更改，生成 FotaPackage.bin 时的 Version 写的就没用了。如果客户只是修改VP，其实是不用变动code，生成 FotaPackage.bin 时的 Version 写的就能够实现版本的更新。

[图片: 3.jpg]

</div>

<div class="reply odd" markdown="1">

### 2022/10/20 14:04 — [人名5]

Hi @[邮箱已隐藏]，

可以在config tool 上找一个用不到的nvkey 做版本号，耳机初始化的时候先读取该nvkey，然后再把这个值写进fota patition。这样就可以只改config tool，不用改code了

[图片: image-2022-10-20-14-02-15-201.png]

</div>

<div class="reply even" markdown="1">

### 2022/10/20 14:26 — [人名2]

Hi [人名5]，

好的，搞清楚原理就知道怎么弄了。问题关闭。

</div>
