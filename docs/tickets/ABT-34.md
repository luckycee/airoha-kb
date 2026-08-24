---
id: ABT-34
title: ULL dongle通话问题
date: 2022/04/11 11:05
status: Closed
source: https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-34
---

# ABT-34 ULL dongle通话问题

> 📅 2022/04/11 11:05　🔗 [原始工单链接](https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-34)

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-33](ABT-33.md)　[→ 下一个工单：ABT-35](ABT-35.md)

</div>

## 问题描述

Hi [人名5]，

发现在通话状态有几个问题：

1. 通过log看到，音乐播放状态，来电，state 由APP_ULTRA_LOW_LATENCY_PLAYING 改为 APP_CONNECTED，不是在APP_[人名9]P_INCOMING ；

2. 接听的短按，看到发送的KeyEvent 是0x53，但是实际又能跟接听电话，但是长按无法拒绝电话；

3. 接听电话之后，state 又变为了 APP_ULTRA_LOW_LATENCY_PLAYING ，这个有点困惑啊；

---

## 回复记录

<div class="reply odd" markdown="1">

### 2022/04/11 11:06 — [人名2]

[附件: LOG.pcapng]

</div>

<div class="reply even" markdown="1">

### 2022/04/11 11:58 — [人名2]

Hi [人名5]，

来电没有同步铃声，是不是也因为state 不对？

</div>

<div class="reply odd" markdown="1">

### 2022/04/12 15:14 — [人名5]

!https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v1/assets/emoticons/cwl/default/100_f.png|width=50!

</div>

<div class="reply even" markdown="1">

### 2022/04/14 09:32 — [人名5]

Hi 黄工，

我们ULL dongle 连接电脑之后，在跟耳机连接就没有[人名9]P 跟 A2DP 协议了，所以不支持这些状态。

</div>

<div class="reply odd" markdown="1">

### 2022/04/14 10:07 — [人名2]

Hi [人名5]，

啊，这样子的话，我该如何处理客户的问题：

1. 手机连接了dongle，但是无铃声；
2. 无法拒绝电话；
3. 已经为什么能够接听电话。

</div>

<div class="reply even" markdown="1">

### 2022/04/14 14:26 — [人名5]

Hi @[邮箱已隐藏]，

没得做，手机通过USB传给dongle就没得[人名9]P协议，你看你客户有什么其他产品是有得做的，可以提需求给PLM评估。

</div>

<div class="reply odd" markdown="1">

### 2022/04/15 14:44 — [人名2]

Hi [人名5]，

有结果吗？我需要回复客户。

</div>

<div class="reply even" markdown="1">

### 2022/04/15 17:11 — [人名2]

[附件: dongle_log_播放音乐.pcapng]

[附件: dongle_log_来电接听.pcapng]

</div>

<div class="reply odd" markdown="1">

### 2022/04/17 16:12 — [人名5]

Hi @[邮箱已隐藏]，

如电话沟通，我们USB HID协议发送paly/pause指令的时候，会对指令引脚输出不同信号电平，默认情况下，play/pause 这个bit 拉高1ms，手机收到这个信号之后，假如这情况下有来电，就可能会识别为接通，但是这也看手机，有些手机就不识别为接听。

假如把play/pause 这个bit 拉高1ms改成拉高2ms左右，识别为接听的手机就会识别成拒绝。

具体修改如下：

static bt_status_t bt_ull_handle_usb_hid_control(bt_ull_usb_hid_control_t action)
\{
 bt_status_t status = BT_STATUS_SUCCESS;
 bt_ull_context_t* ctx = bt_ull_get_context();
 ull_report("[ULL] usb_hid_control: 0x%x, role:0x%x", 2, action, ctx->ull_role);

#ifdef MTK_USB_DEMO_ENABLED
 if (Get_USB_Host_Type() == USB_HOST_TYPE_XBOX) \{
 ull_report("[ULL] usb_hid_control, current is XBOX mode, ignore the HID control event", 0);
 return BT_STATUS_FAIL;
 }
#endif /* MTK_USB_DEMO_ENABLED */

if (ctx->is_ull_connected) \{
 if (BT_ULL_ROLE_CLIENT == ctx->ull_role) \{
#ifdef MTK_AWS_MCE_ENABLE
 bt_aws_mce_role_t cur_role = bt_device_manager_aws_local_info_get_role();
 if (BT_AWS_MCE_ROLE_PARTNER == cur_role
 || BT_AWS_MCE_ROLE_CLINET == cur_role) \{
 /* partner role cannot switch latency */
 return BT_STATUS_FAIL;
 }
#endif
 bt_ull_req_t request;
 memset(&request, 0x00, sizeof(request));
 request.event = BT_ULL_EVENT_USB_HID_CONTROL_ACTION;
 request.hid_control = action;
 bt_ull_send_data(ctx->spp_handle, (uint8_t*)&request, sizeof(request));
 } else if (BT_ULL_ROLE_SERVER == ctx->ull_role) \{
#if defined(MTK_USB_DEMO_ENABLED) && (defined(MTK_USB_AUDIO_V1_ENABLE) || defined(MTK_USB_AUDIO_V2_ENABLE)) && defined(MTK_USB_AUDIO_HID_ENABLE)
 if (BT_ULL_USB_HID_PLAY_PAUSE_TOGGLE == action
 || BT_ULL_USB_HID_PAUSE == action
 || BT_ULL_USB_HID_PLAY == action) \{
 {color:#d04437}//USB_Audio_HID_PlayPause();{color}
{color:#d04437} USB_Audio_HID_PlayPause_RejectCall();{color}
 } else if (BT_ULL_USB_HID_PREVIOUS_TRACK == action) \{
 USB_Audio_HID_ScanPreviousTrack();
 } else if (BT_ULL_USB_HID_NEXT_TRACK == action) \{
 USB_Audio_HID_ScanNextTrack();
 }
#endif
 }
 }
 return status;
}

[图片: image-2022-04-17-16-09-10-552.png]

</div>

<div class="reply even" markdown="1">

### 2022/04/18 17:38 — [人名2]

Hi [人名5]，

dongle端怎么发消息给耳机端？

</div>

<div class="reply odd" markdown="1">

### 2022/04/20 14:27 — [人名5]

Hi @[邮箱已隐藏]，

这个API是dongle和耳机都可以用的，可以在代码里面搜一下看看怎么用

 

[图片: image-2022-04-20-14-26-56-199.png]

</div>

<div class="reply even" markdown="1">

### 2022/04/27 10:03 — [人名8]

@[邮箱已隐藏]

这题还有其他疑问吗？

</div>

<div class="reply odd" markdown="1">

### 2022/04/27 11:05 — [人名2]

Hi [人名8],

没有了，问题关闭；

</div>

<div class="ticket-nav" markdown="1">

[← 上一个工单：ABT-33](ABT-33.md)　[→ 下一个工单：ABT-35](ABT-35.md)

</div>
