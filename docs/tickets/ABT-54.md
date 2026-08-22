---
id: ABT-54
title: AB1565 拒绝回连
date: 2022/06/17 14:27
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-54
---

# ABT-54 AB1565 拒绝回连

> 📅 2022/06/17 14:27　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-54)

## 问题描述

Hi [人名5]，

客户在测试ANC的时候，不希望测试仪对耳机进行回连，在哪里设置可以reject 连接请求。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/06/17 15:36 — [人名5]

Hi @[邮箱已隐藏]，

麻烦试一下在bt_cm_check_connect_request 里面直接return false

</div>

<div class="reply even" markdown="1">

### 2022/06/17 16:12 — [人名5]

Hi @[邮箱已隐藏]，

刚刚的接口ULL 才可用，以下接口可以通杀

[图片: image-2022-06-17-16-12-30-230.png]

</div>
