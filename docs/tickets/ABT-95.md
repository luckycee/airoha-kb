---
id: ABT-95
title: "App 端自定义PEQ调整，LDAC解码无效"
date: 2022/10/09 11:28
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-95
---

# ABT-95 App 端自定义PEQ调整，LDAC解码无效

> 📅 2022/10/09 11:28　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-95)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-94](ABT-94.md)　[→ 下一个工单：ABT-96](ABT-96.md)

</div>

## 问题描述

Hi [人名6]，

之前解决过，在config tool 上调试PEQ， 使用LDAC无效的问题，此问题解决了（见 [ABT-91](ABT-91.md)），现在客户发现使用App 新增自定义PEQ时，也无效；但是使用AAC和SBC有效，请继续指导，如何解决；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/10/10 09:50 — [人名6]

Hi @[邮箱已隐藏]，

麻烦提供一下app 新增不成功过的log

</div>

<div class="reply even" markdown="1">

### 2022/10/10 15:06 — [人名2]

Hi [人名6]，

附件有两个log，LDAC的是无效的，SBC是有效的；

[附件: LDAC问题.rar]

</div>

<div class="reply odd" markdown="1">

### 2022/10/10 17:29 — [人名2]

hi  [人名6],

App设置PEQ101，导出前后的nvkey变化，导入到config tool 是可以看到support 88.2 and 96K是有勾选的；

[附件: all+PEQ.nvr]

[附件: all.nvr]

</div>

<div class="reply even" markdown="1">

### 2022/10/12 11:13 — [人名35]

Hi @[邮箱已隐藏]

Android SDK 的 UI sample 有個變數，可以調整

PeqFragment.java 內 

boolean IS_SUPPORT_LDAC = {color:#d04437}true{color};

將此改為 true，即會生成 88.2 & 96k 的參數
謝謝

</div>

<div class="reply odd" markdown="1">

### 2022/10/12 14:43 — [人名2]

Hi [人名35] ([人名35]),

解决了，问题关闭；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-94](ABT-94.md)　[→ 下一个工单：ABT-96](ABT-96.md)

</div>
