---
id: ABT-42
title: "AB1565 连接dongle使用联系操作后导致link loss"
date: 2022/04/29 10:50
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-42
---

# ABT-42 AB1565 连接dongle使用联系操作后导致link loss

> 📅 2022/04/29 10:50　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-42)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-41](ABT-41.md)　[→ 下一个工单：ABT-43](ABT-43.md)

</div>

## 问题描述

Hi [人名9]，

客户连接了dongle后，手机播放音乐，连续操作执行上一曲，大约十多次就有一次出现link loss，单纯的partner 断开手机，操作主机能让partner回连，时间比较长。请看看是什么问题。

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/29 10:50 — [人名2]

[附件: 1L-持续长按左耳调出上一曲，耳机没有音乐，手机音乐正常在播放，有时候单击可以恢复正常.pcapng]

[附件: 1R-持续长按左耳调出上一曲，耳机没有音乐，手机音乐正常在播放，有时候单击可以恢复正常.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/04/29 11:16 — [人名9]

@[邮箱已隐藏]

请详细描述一下测试步骤以及出现问题的时间点（精确到s）： dongle 插在手机上吗？是在手机上切换下一首还是在耳机上？

单纯的partner 断开手机，操作主机能让partner回连==》这个操作是指什么操作？

</div>

<div class="reply odd" markdown="1">

### 2022/04/29 11:28 — [人名2]

Hi [人名9]，

1. 附件是log，看到的内容；
2. dongle插在手机上，在耳机上操作上一曲；
3. 发现没有声音尝试在主机上操作，看看是否有反应，实测能够播放，一会儿后partner回连；

[图片: Snipaste_2022-04-29_11-26-36.png]

[图片: Snipaste_2022-04-29_11-24-56.png]

</div>

<div class="reply even" markdown="1">

### 2022/05/05 11:46 — [人名14]

Hi @[邮箱已隐藏]，

    请问可以把dongle log和HCI log一起提供吗？也麻烦标注一下测试的具体步骤和时间点。

Thanks.

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 09:21 — [人名14]

Hi @[邮箱已隐藏],

    请问这题可以麻烦帮提供dongle earbuds syslog和HCI log吗？

Thanks.

</div>

<div class="reply even" markdown="1">

### 2022/05/07 09:51 — [人名2]

Hi [人名14] ，

客户只有抓到agent 和dongle的log，看看这些能不能看到问题；

还想抓，不过又没有复现到问题了；

在11:54:19 之后，无论怎么操作都没有反应了；

[附件: 7Dongle，连接Dongle模式持续长按调出上一曲，手机还在正常播放音乐，耳机也有音乐，但是按键除了左耳的双击都没有反应，俩个开发板都按复位键才恢复正常.pcapng]

[附件: 7L，连接Dongle模式持续长按调出上一曲，手机还在正常播放音乐，耳机也有音乐，但是按键除了左耳的双击都没有反应，俩个开发板都按复位键才恢复正常.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 09:54 — [人名14]

Hi @[邮箱已隐藏],

    log麻烦提供完整一点，请到ATK log目录下面把对应的log传上来，另外你传的log是左耳还是右耳？那一份是有问题的？可否帮标注清楚？不然不好排查问题。

    如果和本题无关的问题，请另外提一笔JIRA，这题用来关注link loss出现的原因，其它问题请不要混在一起。

Thanks.

</div>

<div class="reply even" markdown="1">

### 2022/05/07 10:20 — [人名2]

Hi [人名14] ，

1. 无论今天提供的log，还是第一次提供的log，都是基于相同的操作手法，最终表现为按键无效。link loss是我在第一份log，我看到的判断，当然这个判读不一定是正确的，你们更加专业。因为是手法和结果都一致的，所以今天的log我放在了这里；
2. 文件名字，“7Dongle”表示这个dongle log，“7L”表示左边，“7R”表示右边（log bin文件没有选择对，导致全是LOG ERROR）没有上传，根据客户描述，实际过程没有操作右边；
3. 两份log都找到11:54:19 就能看到，之后“7L”的key 动作，在“7Dongle”都没有体现出来；

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 10:23 — [人名14]

Hi @[邮箱已隐藏]，

    “[附件: 7Dongle，连接Dongle模式持续长按调出上一曲，手机还在正常播放音乐，耳机也有音乐，但是按键除了左耳的双击都没有反应，俩个开发板都按复位键才恢复正常.pcapng]”，你们没有传R的log，无法知道右耳按键发生了什么，请提供完整的log并另外开一笔JIRA。

    这题出现link loss的问题请继续测试并提供完成的log（包括dongle和耳机的syslog以及HCI log）

Thanks.

</div>

<div class="reply even" markdown="1">

### 2022/05/07 10:32 — [人名2]

Hi [人名14] ，

HCI log不是蓝牙连接的时候才需要吗？dongle连接的USB-C，是不是可以不需要？主要是客户那边在抓，能最简单给他们操作就尽量简单；

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 10:34 — [人名14]

Hi @[邮箱已隐藏],

    这题你们报的不是link loss问题吗？link loss需要先看HCI log确定断线前后发生了什么，再进一步可能还需要抓air log，麻烦先按照我说的提供log。

Thanks.

</div>

<div class="reply even" markdown="1">

### 2022/05/07 10:41 — [人名2]

Hi [人名14] ，

清除。

</div>

<div class="reply odd" markdown="1">

### 2022/05/07 10:42 — [人名2]

Hi [人名14] ，

清楚。

</div>

<div class="reply even" markdown="1">

### 2022/05/09 18:06 — [人名2]

Hi [人名14] ，

客户从17:45开始，使用“R”操作上一曲，期间也转到“L”操作，最后在“R”边17:46:20附近 发现再次操作无效了，“R”显示连接断开的状态（我看到是link loss）。HCI log正在想办法导出。

有个疑问，耳机并没有跟手机连接，HCI的log会有对应时间戳的记录吗？还是说HCI log 会有dongle的HID的内容？

感谢。

[附件: earbud_log_L.pcapng]

[附件: earbud_log_R.pcapng]

[附件: dongle_log.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/05/09 18:30 — [人名2]

Hi [人名14] ，

HIC log 见附件；

[附件: bugreport-PD1981-RP1A.200720.012-2022-05-09-18-13-18.zip]

</div>

<div class="reply even" markdown="1">

### 2022/05/10 09:23 — [人名14]

Hi @[邮箱已隐藏],

    我前面不是说要dongle和耳机的HCI log和syslog吗？你传的[附件: bugreport-PD1981-RP1A.200720.012-2022-05-09-18-13-18.zip]是dongle和耳机的HCI log吗？而且不是说要到ATK目录下面的log文件夹，把对应串口的文件提供上来吗？为什么提供的只有syslog？

    dongle和耳机的连线不是走BT吗？走BT的话dongle和耳机怎么会没有HCI log？而且右耳并没有发生link loss，请问你是怎么判断右耳link loss的？你所理解的link loss的含义是什么？

    右耳明显是page timeout，需要录air log

Thanks.

</div>

<div class="reply odd" markdown="1">

### 2022/05/10 10:25 — [人名2]

Hi [人名14] ([人名14])，

1. 提供dongle earbuds syslog和HCI log；
2. 提供完成的log（包括dongle和耳机的syslog以及HCI log）

您提到两次要对应的log的情况，是我一直没有get到你要的是“dongle跟earbuds之间的HCI”，昨天提供的是手机HCI log，里面没有包含您要的内容；

link loss的判断是我测试手机 link loss的时候，发现reason是8。然后出现这个问题时，reason是一致的。您更专业，不必考虑我的判断。

昨天是请客户（在东莞）到贵司华润置地大厦E座，并请教贵司同仁梁鹏才清楚如何抓取的手机HCI log，但是方向错了。问题在客户的手机（IQOO Neo3）上才容易复现，我的Google Pixel 4a 一直没能复现的，今天我请客户使用logging tool抓完后，提供完整的log内容，再麻烦您看看。不行的话，我需要再约梁鹏的时间才能体用air log，我司没有可抓air log的 Ellisys 。

感谢支持；

[图片: Snipaste_2022-05-10_10-10-53.png]

</div>

<div class="reply even" markdown="1">

### 2022/05/10 13:45 — [人名14]

Hi @[邮箱已隐藏],

    你这个写法不是用来判断ACL link loss的呀，你可以去看这个callback  register听的不是ACL event呀？link loss在bt_connection_manager.c里面的bt_cm_remote_acl_disconnected_confirm()里面做的处理，register callback的时候听的是GAP module抛上来的event，请先自行理清代码行为逻辑。

Thanks.

 

!image-2022-05-10-13-39-45-025.png|width=981,height=177[图片: 

]image-2022-05-10-13-43-32-903.png|width=1232,height=416!

</div>

<div class="reply odd" markdown="1">

### 2022/05/10 14:29 — [人名2]

Hi [人名14] ([人名14])，

好的，我在理一下代码。

附件是客户抓到的log，问题发生在com3（R边）的14:09:07左右 ，手法是客户一直操作com5（L边）上一曲，直到问题出现停止操作；在14:09:20 左右，com3又回连了。com7 是dongle log；

如果需要air log，我这边再抽时间安排。感谢支持；

[附件: LOG(1).zip]

</div>

<div class="reply even" markdown="1">

### 2022/05/10 14:47 — [人名2]

Hi [人名14] ([人名14])，

com3（R边 log）
com5（L边 log）
com7 是dongle log

刚刚的回复中，问题描述中有说明的。感谢支持；

</div>

<div class="reply odd" markdown="1">

### 2022/05/10 14:48 — [人名14]

Hi @[邮箱已隐藏]，

    @[附件: LOG(1).zip]这个需要抓airlog，这次R在14:09:11是真的发生了link loss了（前面的log看都不是link loss），需要airlog才能看出具体原因。

Thanks.

!image-2022-05-10-14-45-32-975.png|width=896,height=297!

</div>

<div class="reply even" markdown="1">

### 2022/05/10 15:34 — [人名2]

Hi [人名14] ([人名14])，

好的。我这边没有 Ellisys，不知您是否在深圳，如果在的话，我可以跟客户一起到贵司，麻烦您一起抓这个air log，顺便当面向您请教。

感谢支持。

</div>

<div class="reply odd" markdown="1">

### 2022/05/11 13:41 — [人名14]

Hi @[邮箱已隐藏],

    你看看05/12有没有空可以过来抓air log

Thanks.

</div>

<div class="reply even" markdown="1">

### 2022/05/11 14:15 — [人名2]

Hi [人名14] ([人名14])，

好的，12号明天下午两点，这个时间可以吗？我跟客户到贵司13楼。

</div>

<div class="reply odd" markdown="1">

### 2022/05/11 14:28 — [人名14]

Hi @[邮箱已隐藏],

    行，明天下午2点13楼，我带一台ellisys上去。

</div>

<div class="reply even" markdown="1">

### 2022/05/12 09:35 — [人名2]

Hi [人名14] ([人名14])，

今天贵司停工，可否改到明天下午两点？

</div>

<div class="reply odd" markdown="1">

### 2022/05/12 09:41 — [人名14]

Hi @[邮箱已隐藏],

    抱歉因深圳暴雨今天居家办公，周五下午2点我还有会议需要参加，请问周五上午是否有空？我上午9点半到12点都可以。

</div>

<div class="reply even" markdown="1">

### 2022/05/12 10:05 — [人名2]

Hi [人名14] ([人名14])，

没关系。

周五上午约了贵司硬件同事调试ANC，下周一或周二下午如何？

</div>

<div class="reply odd" markdown="1">

### 2022/05/12 10:09 — [人名14]

Hi @[邮箱已隐藏]，

   周二可以，看了日程周一下午也有会议，周二暂无安排。如果比较急，周一上午也是可以的。

Thanks.

</div>

<div class="reply even" markdown="1">

### 2022/05/12 10:25 — [人名2]

Hi [人名14] ([人名14])，

好的，周二下午两点，麻烦了。

</div>

<div class="reply odd" markdown="1">

### 2022/05/17 09:54 — [人名9]

@[邮箱已隐藏]

这题有过来测试抓log了吗？

</div>

<div class="reply even" markdown="1">

### 2022/05/17 10:00 — [人名2]

HI 杜工，

约好了今天下午两点。

</div>

<div class="reply odd" markdown="1">

### 2022/05/17 14:00 — [人名2]

Hi [人名14] ([人名14])，

我在1301洽谈室；

</div>

<div class="reply even" markdown="1">

### 2022/05/17 14:12 — [人名2]

7317	2022-05-17 14:07:19.093839	 [M:BT_DM_EDR C:info F: L: ]: [BT_DM] link key:17,19,c8,c3,  b0,5e,11,8a,  b4,8a,9a,d7,  d0,92,e5,7c

6792	2022-05-17 14:07:18.904977	 [M:BT_DM_EDR C:info F: L: ]: [BT_DM] Addr type 1, address:0x80:0x23:0xec:0xf4:0x23:0x71

</div>

<div class="reply odd" markdown="1">

### 2022/05/17 14:35 — [人名14]

airlog

14:31:39左右，partner link loss
[附件: [ABT-42](ABT-42.md)_14_31_39.rar]

</div>

<div class="reply even" markdown="1">

### 2022/05/17 14:45 — [人名2]

Hi [人名14] ([人名14])，

问题出现在R边，14:31:39附近。

[附件: Logging220517_140350_COM77_R.7z]

[附件: Config_20220517_140656_COM76_L.7z]

[附件: Logging220517_141733_COM83_dongle.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/05/23 15:13 — [人名2]

Hi [人名14] ([人名14])，

这题是否有结果？

</div>

<div class="reply even" markdown="1">

### 2022/05/23 15:52 — [人名14]

Hi @[邮箱已隐藏],

    这题需要换[附件: libpka_ull_[ABT-42](ABT-42.md).rar]这份lib重新抓airlog，我这周除了周三都有空，看看你们什么时候方便过来抓一下airlog。

Thanks.

</div>

<div class="reply odd" markdown="1">

### 2022/05/23 16:56 — [人名2]

Hi [人名14] ([人名14])，

我这边使用EVK 更新 你的lib试下看能否复现问题，暂定周四下午两点半到贵司。

感谢支持；

</div>

<div class="reply even" markdown="1">

### 2022/05/26 14:43 — [人名2]

[M:apps C:info F: L: ]: [ULL_activity], dongle address is 91:EC:F6:65:B5:83
[M:BT_DM_EDR C:info F: L: ]: [BT_DM] link key:c8,eb,a5,35,  58,76,27,c4,  5d,c5,88,54,  9c,67,66,59

</div>

<div class="reply odd" markdown="1">

### 2022/05/26 14:52 — [人名2]

14996	2022-05-26 14:51:58.105568	 [M:BT_DM_EDR C:info F: L: ]: [BT_DM] link key:9f,54,f2,c9,  28,76,0b,fc,  ec,5c,a7,55,  d7,c4,77,5a

</div>

<div class="reply even" markdown="1">

### 2022/05/26 15:59 — [人名14]

update:

05/26压测一个半小时未复现，换手机测试看情况，如果还能复现，05/27下午2点半再来ARSZ 13F 用复现的手机+EVK抓airlog

</div>

<div class="reply odd" markdown="1">

### 2022/05/26 19:37 — [人名2]

Hi [人名15]，

如沟通，客户又用她的手机复现了，明天下午两点半，仍需抓Airlog ；

</div>

<div class="reply even" markdown="1">

### 2022/05/27 14:46 — [人名2]

26911	2022-05-27 14:45:50.032777	 [M:apps C:info F: L: ]: [ULL_activity], dongle address is D9:4C:67:3E:B7:C2

26149	2022-05-27 14:45:49.816289	 [M:BT_DM_EDR C:info F: L: ]: [BT_DM] link key:af,fc,62,be,  11,c2,da,45,  8d,96,ea,81,  69,ad,b3,73

</div>

<div class="reply odd" markdown="1">

### 2022/05/27 14:56 — [人名14]

airlog:

时间：14:54:47
[附件: 14_54_47.rar]

</div>

<div class="reply even" markdown="1">

### 2022/05/27 15:07 — [人名2]

问题在parnter ；时间 2022-05-27 14:54:47

[附件: agent.7z]

[附件: parnter.7z]

[附件: dongle.7z]

</div>

<div class="reply odd" markdown="1">

### 2022/05/27 15:24 — [人名14]

麻烦帮合入[附件: libpka_ull_merge_false_ack_bugfix.rar]试试

</div>

<div class="reply even" markdown="1">

### 2022/05/27 17:13 — [人名14]

update:

合入[附件: libpka_ull_merge_false_ack_bugfix.rar]后用常复现该问题的手机+EVK压测一小时，未复现。

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-41](ABT-41.md)　[→ 下一个工单：ABT-43](ABT-43.md)

</div>
