---
id: ABT-56
title: AB1585 SDK V3.1.0 DSP编译不过
date: 2022/06/20 16:38
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-56
---

# ABT-56 AB1585 SDK V3.1.0 DSP编译不过

> 📅 2022/06/20 16:38　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-56)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-55](ABT-55.md)　[→ 下一个工单：ABT-57](ABT-57.md)

</div>

## 问题描述

Hi [人名5]，

请看看DSP 为什么编译不过。初始demo，没有做任何修改；

指令 ./build.sh ab1585_evk earbuds_ref_design_ull2 

客户想做earbuds+dongle ；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/06/20 16:38 — [人名2]

[附件: err.log]

[图片: Snipaste_2022-06-20_16-33-26.png]

</div>

<div class="reply even" markdown="1">

### 2022/06/24 15:21 — [人名5]

Hi @[邮箱已隐藏]，

你在MOL 上下载哪版SDK 编译的？

</div>

<div class="reply odd" markdown="1">

### 2022/06/24 16:46 — [人名2]

Hi [人名5]，

这个。

[图片: Snipaste_2022-06-24_16-46-28.png]

</div>

<div class="reply even" markdown="1">

### 2022/06/27 14:56 — [人名5]

Hi @[邮箱已隐藏]，

麻烦下载以下档案，重新安装SDK试试 [图片: image-2022-06-27-14-55-16-345.png]

</div>

<div class="reply odd" markdown="1">

### 2022/06/27 17:57 — [人名2]

Hi [人名5]，

err 是 ./build.sh ab1585_evk earbuds_ref_design 的
err1 是 ./build.sh ab1585_evk earbuds_ref_design_ull2 的

[附件: err2.log]

[附件: err.log]

</div>

<div class="reply even" markdown="1">

### 2022/06/28 15:20 — [人名5]

Hi @[邮箱已隐藏]，

麻烦把google fast pair 关掉试试~

# This option is used to enable fast pair.
AIR_BT_FAST_PAIR_ENABLE = n

</div>

<div class="reply odd" markdown="1">

### 2022/06/29 10:42 — [人名2]

Hi [人名5] ,

还是过不了；

[附件: err.log]

</div>

<div class="reply even" markdown="1">

### 2022/06/29 11:10 — [人名5]

Hi @[邮箱已隐藏]，

麻烦提供一下DSP 的error log。

</div>

<div class="reply odd" markdown="1">

### 2022/06/29 11:25 — [人名2]

Hi [人名5]，

DSP 的；

[附件: err.log]

</div>

<div class="reply even" markdown="1">

### 2022/06/29 13:34 — [人名5]

Hi @[邮箱已隐藏]，

我这边把\dsp\project\ab158x\apps\dsp0_headset_ref_design\XT-XCC\feature_85_earbuds_ull2.mk 里面AMA 相关的feature关掉，然后把mcu\project\ab158x\apps\earbuds_ref_design\GCC\feature_85_evk_ull2.mk里面GFP 相关的feature 关掉之后就编译过了，麻烦试一下~

</div>

<div class="reply odd" markdown="1">

### 2022/06/29 16:04 — [人名2]

Hi [人名5]，

能够直接的code给我对比吗？我还是编译不过

</div>

<div class="reply even" markdown="1">

### 2022/06/29 16:35 — [人名2]

Hi [人名5]，

我的code；

[附件: 1585_V3.1.0.7z.002]

[附件: 1585_V3.1.0.7z.001]

</div>

<div class="reply odd" markdown="1">

### 2022/06/29 16:35 — [人名5]

Hi @[邮箱已隐藏]，

不知道是不是环境问题，麻烦发你的code给我在我这边编译看过不过

</div>

<div class="reply even" markdown="1">

### 2022/07/01 10:52 — [人名2]

Hi [人名5]，

你们MOL上发布了V3.2.0，我会用那个版本试，这题关掉；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-55](ABT-55.md)　[→ 下一个工单：ABT-57](ABT-57.md)

</div>
