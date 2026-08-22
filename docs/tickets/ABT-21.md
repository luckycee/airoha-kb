---
id: ABT-21
title: AB1565 与AB1565M 的编译区别
date: 2022/02/10 12:08
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-21
---

# ABT-21 AB1565 与AB1565M 的编译区别

> 📅 2022/02/10 12:08　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-21)

## 问题描述

HI [人名1]，

客户有个疑问，加了MFi之后编译生成的固件已经达到2MB了，那么要同时支持OTA的话是不是要使用8M的flash？

但奇怪的是编译使用的feature mk文件时feature_65_evk.mk也没有报错，这个mk文件不是只针对4M flash吗？

如果用8M flash的IC是不是要用feature_65_8m_evk.mk这个mk文件编译？

即 AB1565 AB1565A

./build.sh ab1565_evk earbuds_ref_design ?

AB1565M AB1565AM

./build.sh ab1565_8m_evk earbuds_ref_design ?

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/02/10 12:08 — [人名2]

[图片: image011(02-10-11-41-34).png]

</div>

<div class="reply even" markdown="1">

### 2022/02/11 15:27 — [人名1]

Hi,  

   不同 芯片/硬件 在编译的时候可以选择不同的board, 编译命令和对应的硬件可以参考下面文件中的设置. 

[图片: image-2022-02-11-15-24-36-617.png]

谢谢

</div>
