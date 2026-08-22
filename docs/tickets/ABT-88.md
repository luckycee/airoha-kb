---
id: ABT-88
title: adaptive ANC的使用指导
date: 2022/09/26 10:38
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-88
---

# ABT-88 adaptive ANC的使用指导

> 📅 2022/09/26 10:38　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-88)

## 问题描述

HI [人名5]，

请帮忙提供一下 adaptive ANC 的使用指导，客户拿到我提供的AB1565AM V3.3.0 headset的软件后，不知道如何使用。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/26 15:36 — [人名5]

Hi @[邮箱已隐藏]，

headset 只支持ED

[图片: image-2022-09-26-15-36-05-063.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/26 16:11 — [人名2]

Hi [人名5]，

不懂。还是不知道使用。

</div>

<div class="reply odd" markdown="1">

### 2022/09/26 16:16 — [人名5]

Hi @[邮箱已隐藏]，

就是65 headset 支持 adaptive anc 里的 Environment Detect

</div>

<div class="reply even" markdown="1">

### 2022/09/27 19:53 — [人名2]

Hi 帝木，

如沟通，请提供协助；

</div>

<div class="reply odd" markdown="1">

### 2022/09/28 15:21 — [人名4]

@[人名26] @[人名27]

再帮忙评估一下是否可以提供资料给客户参考

谢谢

</div>

<div class="reply even" markdown="1">

### 2022/09/28 17:17 — [人名4]

hi 黄工,

 

PM决定先不支援[客户D] 此项目的Adaptive ANC

谢谢

</div>

<div class="reply odd" markdown="1">

### 2022/09/29 14:26 — [人名4]

hi 黄工,

 

ED 文件如附件

简述之。通过几组ANC 滤波器切换。

每组调节不一样的FB 深度，达到使用者体验不一样的场景

 
[附件: Airoha_Adaptive_ANC_2021_ED_for Mixiu.pdf]

</div>

<div class="reply even" markdown="1">

### 2022/09/29 14:37 — [人名2]

Hi 帝木，

只有三页？里面没有说到adaptive ANC 怎么调试，怎么开启，怎么验证。

</div>

<div class="reply odd" markdown="1">

### 2022/09/30 13:49 — [人名4]

是的，就只有三页。主要内容就是我说的部分，调试几组ANC 

相同的FF 和FB ，然后依靠调节FB不同的gain 达到不一样的场景体验

实际上，这个ED就是只有几组相同的filter ，只是FB gain 不一样

</div>

<div class="reply even" markdown="1">

### 2022/09/30 17:49 — [人名2]

Hi 帝木，

应该是自动切换切换不同的filter，我只需要设置好几组filter 就行了吗？触发条件切换是什么？需要我设定吗？

</div>

<div class="reply odd" markdown="1">

### 2022/09/30 17:54 — [人名2]

另外，[人名25]说需要对接结构和App，这个怎么做？

[图片: Snipaste_2022-09-30_17-54-06.jpg]

</div>

<div class="reply even" markdown="1">

### 2022/09/30 18:06 — [人名4]

*基於耳道及配戴**基於耳道及配戴補償結果**,* *根據**環境躁聲**調整**降躁強度**補償結果**,* *根據**環境躁聲**調整**降躁強度*

*預存適合吵雜**/* *一般* */* *安靜 環境之**三種降躁強度**,* *根據偵*  **  *測到之環境躁聲強弱套用***

</div>

<div class="reply odd" markdown="1">

### 2022/09/30 18:06 — [人名4]

先找客户给3D结构图

</div>

<div class="reply even" markdown="1">

### 2022/10/09 10:08 — [人名2]

Hi 帝木，

客户有几个问题，请帮忙回复：

1，噪声强度是通过FF_MIC侦测还是通过FB_MIC？
2，我们预设进去的滤波器参数后面做量产时怎么调整？三组滤波器都要调整吗？
3，三组滤波器是洛达帮我们调整还是我们自己调整？

3D在同客户确认最终版，确认好后再发给你。谢谢！

</div>

<div class="reply odd" markdown="1">

### 2022/10/11 11:34 — [人名4]

1，噪声强度是通过FF_MIC侦测还是通过FB_MIC？

FFmic
2，我们预设进去的滤波器参数后面做量产时怎么调整？三组滤波器都要调整吗？

因为都是FB不同，所以按照传统的anc校准方式即可（先调FF,再调FB，理论上，针对一组FB校准即可）
3，三组滤波器是洛达帮我们调整还是我们自己调整？

你们自己给客户调，调到客户需要的performance即可，还是像以前一样的调法

</div>
