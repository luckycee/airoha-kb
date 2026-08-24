---
id: ABT-78
title: Hi-Res 小金标认证指导
date: 2022/09/06 11:27
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-78
---

# ABT-78 Hi-Res 小金标认证指导

> 📅 2022/09/06 11:27　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-78)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-77](ABT-77.md)　[→ 下一个工单：ABT-79](ABT-79.md)

</div>

## 问题描述

Hi [人名5]，

客户要在日本做LDAC的Hi-Res认证，附件是一些文档，你帮忙看看。附件的文件的黃色部分的資料麻煩提供一下。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/06 11:27 — [人名2]

[附件: Product info_HRAW logo v13_X47.docx]

</div>

<div class="reply even" markdown="1">

### 2022/09/13 10:35 — [人名2]

Hi [人名5]，

这题已经拖了一个星期了，请麻烦处理；

</div>

<div class="reply odd" markdown="1">

### 2022/09/14 10:31 — [人名4]

hi  黄工，

 

这是日本索尼的LDAC的spec阿

你看我们的IC datasheet就有这些内容啦

</div>

<div class="reply even" markdown="1">

### 2022/09/15 14:36 — [人名18]

hi customer,

 请问有从sony 处拿到LDAC codec lib 吗？ 请附上给敝司集成

</div>

<div class="reply odd" markdown="1">

### 2022/09/15 14:51 — [人名2]

Hi jianhua,

在 MIUIX1565-4 已经提供了LDAC codec lib，并且你们已经提供patch 集成，软件测试也没有问题了；

现在客户要做认证，这个ID 下 2022/09/06 11:27 客户要的文档有部分内容需要完善，另外帝木那边有资料需要你的approve 。

</div>

<div class="reply even" markdown="1">

### 2022/09/15 14:58 — [人名4]

hi 黄工,

 

这里认证涉及以下几点

1.LDAC codec要加上去，sdk default是没有包括LDAC的，这部分要软件同仁帮忙

2.SPK单体的频响要可以到40KHz

3.有个标准是40KHz相对1KHz(灵敏度)频响降低不超过20dB

4.5KHz的左右channel的延迟(抖动)不超过±50us（之前用示波器余晖测试过）

5.block diagram如下图

[图片: image-2022-09-14-16-27-25-918.png]

</div>

<div class="reply odd" markdown="1">

### 2022/09/19 13:23 — [人名4]

已提供相关资料，后续有问题再reopen

</div>

<div class="reply even" markdown="1">

### 2022/09/21 15:14 — [人名2]

Hi 帝木，

1. LDAC 990K解码到40K的曲线；
2. 左右耳的时间差（max 227us）;

这两个请帮忙提供一下；

</div>

<div class="reply odd" markdown="1">

### 2022/09/22 11:23 — [人名4]

我们没有这样的现成数据，这个应该是 基于客户的耳机实际测试吧

这是认证公司要求的 吗

</div>

<div class="reply even" markdown="1">

### 2022/09/22 17:26 — [人名2]

Hi 帝木，

是的，要求这个资料；

</div>

<div class="reply odd" markdown="1">

### 2022/09/27 15:47 — [人名4]

这些资料要用客户实际样机测试，我们没有

声学的参数要对标整机才有意义

</div>

<div class="reply even" markdown="1">

### 2022/09/27 16:05 — [人名2]

Hi 帝木，

好的，我叫客户准备好整机，去你那边测试吧。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-77](ABT-77.md)　[→ 下一个工单：ABT-79](ABT-79.md)

</div>
