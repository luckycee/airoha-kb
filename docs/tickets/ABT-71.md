---
id: ABT-71
title: 1565 请求race cmd 写PEQ的详细数据格式
date: 2022/08/22 10:56
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-71
---

# ABT-71 1565 请求race cmd 写PEQ的详细数据格式

> 📅 2022/08/22 10:56　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-71)

## 问题描述

Hi  [人名5],

EQ filter的系数数据格式是否和ANC filter的系数系数数据格式相同，如果系数数据格式不相同，能否提供系数数据格式？并且命令格式细节是什么？

[客户A]的田总之前把“通过race cmd写入ANC 参数（滤波、增益等）”调试通了，现在他们想用同样的方式实现机器测试结束后，自动计算合适的PEQ值写到对应的nvkey中。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/08/24 15:35 — [人名5]

Hi @[邮箱已隐藏]，

我们这边是没有PEQ 传参的数据格式的，我们生成那一串nvkey是 app 或者 tool 通过 集成在 SDK 里面的 DSP lib 生成的，app 或者tool 生成之后在发给耳机写进nvkey。

具体app 端实现如以下文档，nvkey格式如下图

[图片: image-2022-08-24-15-35-42-414.png]

</div>

<div class="reply even" markdown="1">

### 2022/08/24 15:36 — [人名5]

[附件: AB156x_Series_PEQ_Coefficient_Update_Application_Note_v1.4_watermark.pdf]

</div>
