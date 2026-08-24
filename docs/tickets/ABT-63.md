---
id: ABT-63
title: "V2.9.0 IGO 算法 add on【[客户B]】"
date: 2022/07/21 14:28
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-63
---

# ABT-63 V2.9.0 IGO 算法 add on【[客户B]】

> 📅 2022/07/21 14:28　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-63)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-62](ABT-62.md)　[→ 下一个工单：ABT-64](ABT-64.md)

</div>

## 问题描述

Hi [人名6]，

请帮忙提供iGO 算法的add on 包。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/07/21 14:42 — [人名6]

Hi @[邮箱已隐藏]，

65的所有add on 包需要你们找PLM申请

</div>

<div class="reply even" markdown="1">

### 2022/07/21 15:12 — [人名21]

见附件
[附件: IoT_SDK_for_BT_Audio_V2.9.0.ULL_TWS_Headset_ai_nr_premium.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/07/21 15:29 — [人名2]

Hi [人名6]，

请帮忙确认下：
1. 直接拷贝对应内容到文件夹下就可以了吗？ feature.mak 和 Makefile 不用修改？
2. 是否区分像1562 那样分“INTELLIGO 1 + 1 or 2 + 1” ？
3. 如何确认已经添加成功 ？

</div>

<div class="reply even" markdown="1">

### 2022/07/22 10:20 — [人名6]

Hi @[邮箱已隐藏]，

直接复制进去就好了，跟 62一样，在.mk 里面打开就好了

</div>

<div class="reply odd" markdown="1">

### 2022/07/22 14:14 — [人名2]

Hi [人名6]，

这个 MTK_3RD_PARTY_NR = n ？

</div>

<div class="reply even" markdown="1">

### 2022/07/26 09:33 — [人名13]

Hi @[邮箱已隐藏],

请问你编译用的哪个指令

thanks

</div>

<div class="reply odd" markdown="1">

### 2022/07/26 09:47 — [人名2]

Hi [人名13]Huang

./build.sh ab1565_8m_evk earbuds_ref_design

</div>

<div class="reply even" markdown="1">

### 2022/07/26 09:54 — [人名13]

Hi  @[邮箱已隐藏]，

带igo的对应编译./build.sh ab1565_8m_evk earbuds_ref_design_ainr即可

thanks

</div>

<div class="reply odd" markdown="1">

### 2022/07/26 09:59 — [人名2]

Hi Hi [人名13]Huang，

如何确认我添加成功？

</div>

<div class="reply even" markdown="1">

### 2022/07/26 10:15 — [人名13]

Hi @[邮箱已隐藏]，

SDK2.9.0本就有合入igo，只要将add on包合入，option打开即可

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-62](ABT-62.md)　[→ 下一个工单：ABT-64](ABT-64.md)

</div>
