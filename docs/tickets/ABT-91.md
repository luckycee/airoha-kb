---
id: ABT-91
title: LDAC下调试PEQ无效
date: 2022/09/27 11:15
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-91
---

# ABT-91 LDAC下调试PEQ无效

> 📅 2022/09/27 11:15　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-91)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-90](ABT-90.md)　[→ 下一个工单：ABT-92](ABT-92.md)

</div>

## 回复记录

<div class="reply odd" markdown="1">

### 2022/09/27 18:24 — [人名29]

@[邮箱已隐藏] 麻烦提供FW & ATK版本号

</div>

<div class="reply even" markdown="1">

### 2022/09/27 18:42 — [人名2]

Hi Sanmuel,

config tool 2.11.4, FW是AB1565AM

[附件: debug.7z]

[附件: AB1565AM_V2.9.0_D86_V20_20220926_V0.25_L.7z]

[附件: AB1565AM_V2.9.0_D86_V20_20220926_V0.25_R.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/09/27 20:08 — [人名4]

code里面默认是没开LDAC的哦

你要先确认code里面是否有正确配置了

可以找SW AE  确认一下

</div>

<div class="reply even" markdown="1">

### 2022/09/28 11:02 — [人名2]

Hi 帝木，

LDAC 是后面加的，LDAC也起效了，就是PEQ使用是没有用。

</div>

<div class="reply odd" markdown="1">

### 2022/09/28 11:30 — [人名2]

Hi [人名5]，

使用SBC时：
1283	2022-09-28 11:20:13.058921	 [M:dsp_mw C:info F: L: ]: peq mxing finish, status: 1 0\n

使用功能LDAC 时：
1898	2022-09-28 11:22:53.882685	 [M:dsp_mw C:error F: L: ]: [0] peq_get_inter_param fail, rate:96 \n

[附件: SBC能够使用PEQ.pcapng]

[附件: LDAC不能使用PEQ.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/09/28 15:22 — [人名4]

这看起来是SW bug

再帮客户处理一下

</div>

<div class="reply odd" markdown="1">

### 2022/09/28 17:32 — [人名30]

Dear Customer,

请先检查下feature是否有正确打开：

MCU:

MTK_BT_A2DP_VENDOR_ENABLE = y
 FIXED_SAMPLING_RATE_TO_48KHZ = n
 AIR_FIXED_DL_SAMPLING_RATE_TO_96KHZ_ENABLE = y

DSP:

MTK_BT_A2DP_VENDOR_1_ENABLE = y
 MTK_BT_A2DP_VENDOR_1_USE_PIC = y
 FIXED_SAMPLING_RATE_TO_48KHZ = n
 AIR_FIXED_DL_SAMPLING_RATE_TO_96KHZ_ENABLE = y

另外，要勾选88和96K

[图片: image-2022-09-28-17-33-41-987.png]

调整MTU size:

[图片: image-2022-09-28-17-32-46-597.png]
[图片: image-2022-09-28-17-33-41-987.png]

</div>

<div class="reply even" markdown="1">

### 2022/09/29 10:29 — [人名2]

Hi [人名30] ([人名30])，

我使用的是V2.9.0 ，AIR_FIXED_DL_SAMPLING_RATE_TO_96KHZ_ENABLE 没有找到这个define，我找V3.2.0 也是没有。直接加在feature.mak 和dsp中可以吗？

</div>

<div class="reply odd" markdown="1">

### 2022/09/29 19:19 — [人名30]

Hi @[邮箱已隐藏],

AIR_FIXED_DL_SAMPLING_RATE_TO_96KHZ_ENABLE 

这个feature需要在贵司project对应的feature_xx.mk里面打开

谢谢！

</div>

<div class="reply even" markdown="1">

### 2022/09/30 11:27 — [人名2]

Hi [人名30] ([人名30])，

有的， ./build.sh ab1565_8m_evk earbuds_ref_design , 找到了 feature_65_8m_evk.mk ，的确没有 AIR_FIXED_DL_SAMPLING_RATE_TO_96KHZ_ENABLE 此define， 只有 FIXED_SAMPLING_RATE_TO_48KHZ ；

除了这点，其他按照指导，LDAC下PEQ也能够起效了，是否有问题？

</div>

<div class="reply odd" markdown="1">

### 2022/09/30 11:51 — [人名30]

Hi @[邮箱已隐藏],

按照我上面贴出来的配置就好，其他没有要注意的了。

Thanks！

</div>

<div class="reply even" markdown="1">

### 2022/09/30 16:09 — [人名30]

Hi @[邮箱已隐藏]，

该题如果没有其他疑问就先关掉了，后续有问题再提jira分析

Thanks！

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-90](ABT-90.md)　[→ 下一个工单：ABT-92](ABT-92.md)

</div>
