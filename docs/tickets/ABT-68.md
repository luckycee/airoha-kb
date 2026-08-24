---
id: ABT-68
title: 设置硬件IO区分左右声道
date: 2022/08/09 17:17
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-68
---

# ABT-68 设置硬件IO区分左右声道

> 📅 2022/08/09 17:17　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-68)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-67](ABT-67.md)　[→ 下一个工单：ABT-69](ABT-69.md)

</div>

## 问题描述

Hi [人名5]，

在配置工具中设置了硬件区分左右声道（默认GPIO19），虽然TWS能够连接，但是通过声道测试发现左右两边都为L边的声音。通过在 NVKEYID_APP_AUDIO_CHANNEL 这个nvkey相关位置加log，但是都没有显示出来。

如果设置回来软件的模式，则没有问题；请看看这是为什么？

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/08/09 17:17 — [人名2]

[图片: Snipaste_2022-08-09_17-16-26.png]

[图片: Snipaste_2022-08-09_17-16-46.png]

</div>

<div class="reply even" markdown="1">

### 2022/08/09 17:48 — [人名5]

？？？

[图片: image-2022-08-09-17-48-09-098.png]

</div>

<div class="reply odd" markdown="1">

### 2022/08/09 18:27 — [人名2]

Hi [人名5]，

我为了做测试，两边都选为L，没有关系的，实际一边L，一边R也是不行；

</div>

<div class="reply even" markdown="1">

### 2022/08/10 09:32 — [人名5]

Hi @[邮箱已隐藏]，

其他客户这样配置都没说有问题啊

[图片: image-2022-08-10-09-32-00-560.png]

</div>

<div class="reply odd" markdown="1">

### 2022/08/10 11:23 — [人名2]

Hi [人名5],

是我这边的问题，确实是连接并且声道对的，手法需要注意。

每次烧录结束之后，你们的初始化到设置的是“HW mode” GPIO决定声道后，会根据对应的实际的情况获取到值，转为“SW mode”并写入nvkey中，并且只有第一次执行，后面再开机就一直是SW mode了。如果第一次上电没有弄对（一只耳机GPIO 为低，一只耳机GPIO 为高），那么他们的声道就一直是错的。也因为，你们的log必须是开机之后能有，所以第一次上电时没有录制得到，后面再录到也是修改后的SW mode；

[图片: Snipaste_2022-08-10_11-22-39.png]

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-67](ABT-67.md)　[→ 下一个工单：ABT-69](ABT-69.md)

</div>
