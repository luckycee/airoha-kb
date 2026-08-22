---
id: ABT-41
title: AB1565 读写nvkey的地址
date: 2022/04/28 20:23
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-41
---

# ABT-41 AB1565 读写nvkey的地址

> 📅 2022/04/28 20:23　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-41)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-40](ABT-40.md)　[→ 下一个工单：ABT-42](ABT-42.md)

</div>

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/29 10:57 — [人名11]

Hi @[邮箱已隐藏],

1565 系列 0xFE00之后的也是都可以自由使用, 请问是有遇到什么问题了吗？

thanks

</div>

<div class="reply even" markdown="1">

### 2022/04/29 11:13 — [人名2]

Hi [人名11]Huang,

暂时没有遇到问题，就是确认这个其实地址。

</div>

<div class="reply odd" markdown="1">

### 2022/04/29 20:32 — [人名2]

Hi [人名11]Huang,

新增的0xFE00 放在什么地方，如果放在 ..\mcu\project\ab1565_ab1568_evk\apps\earbuds_ref_design\config_bin\ab1565_evk\nvkey.xml 编译不过；

如果放在 \out\ab1565_evk\earbuds_ref_design_ull\download\syskey.xml 中，读取的时候提示 NVKEY_STATUS_ITEM_NOT_FOUND；

</div>

<div class="reply even" markdown="1">

### 2022/05/05 08:59 — [人名11]

Hi  @[邮箱已隐藏],

放在即可：..\mcu\project\ab1565_ab1568_evk\apps\earbuds_ref_design\config_bin\ab1565_evk\nvkey.xml 

你是怎么加的，我这边可以编译通过

thanks

[图片: image-2022-05-05-08-59-13-489.png]

</div>

<div class="reply odd" markdown="1">

### 2022/05/05 10:40 — [人名2]

Hi [人名11]Huang,

可以编译pass了；

但是提示没有这个ID ；

[图片: Snipaste_2022-05-05_10-40-01.png]

[图片: Snipaste_2022-05-05_10-39-42.png]

[图片: Snipaste_2022-05-05_10-39-16.png]

[图片: Snipaste_2022-05-04_10-55-42.png]

[附件: 读取不到.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/05/05 13:29 — [人名11]

Hi @[邮箱已隐藏]，

麻烦参照这份文档再验证下，

[附件: NVKey User Guide.pptx]

</div>

<div class="reply odd" markdown="1">

### 2022/05/05 15:05 — [人名2]

Hi [人名11]Huang,

可以了，代码没有问题；

我一直保留着 filesystem.bin、nvdm.bin、syskey.xml 这个三个文件（包含了voice prompt、LED 等设置），编译出来之后就用旧的覆盖编译出来的内容，导致了新增的nvkey始终不在FW中。

为了使用新增的nvkey内容，不能使用之前保留的三个文件，有什么方法可以快速添加以前的内容？

</div>

<div class="reply even" markdown="1">

### 2022/05/05 15:49 — [人名11]

Hi  @[邮箱已隐藏],

不好意思，请以这份资料为准

[图片: image-2022-05-05-15-43-43-527.png]

 

为了使用新增的nvkey内容，不能使用之前保留的三个文件，有什么方法可以快速添加以前的内容？

==》 这个问题我再看下， 另外，1. 使用新的三个文件，导入相应的led_index_list.h,以及vp之类的，2. 导入之前旧的 nvr （之前62的方式），按照这个步骤下来是否有问题？

thanks
[附件: Customize NVKeys.pdf] [图片: image-2022-05-05-15-40-17-868.png] [图片: image-2022-05-05-15-43-43-527.png]

</div>

<div class="reply odd" markdown="1">

### 2022/05/06 10:24 — [人名11]

Hi  @[邮箱已隐藏],

修改NVKEY.XML 编译后改到的只有nvdm.bin, 只更新nvdm.bin 应该就可以了，麻烦测试看看

(filesystem.bin是用于vp保存的，只有vp有增删才会改到，system.xml这是什么路径下的文件呢）

thanks

</div>

<div class="reply even" markdown="1">

### 2022/05/06 11:47 — [人名2]

Hi [人名11]Huang,

在config tool上选择“save file”在对应的目录下，就会有一个 system.xml

[图片: Snipaste_2022-05-06_11-47-42.png]

</div>

<div class="reply odd" markdown="1">

### 2022/05/06 16:57 — [人名11]

Hi  @[邮箱已隐藏],
 # 编译后我们会得到一个新的nvdm.bin，
 # 在config tool打开新的nvdm.bin所在的文件夹后， 导入原本的nvr,
 # 因为vp这些你没有改动，所以直接用旧的filesystem.bin，这时候保存会得到新的nvdm.bin 和system.xml 

经过以上就会得到原本led ,vp的设置

</div>

<div class="reply even" markdown="1">

### 2022/05/06 17:04 — [人名2]

Hi Hi [人名11]Huang,

是的，已经解决；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-40](ABT-40.md)　[→ 下一个工单：ABT-42](ABT-42.md)

</div>
