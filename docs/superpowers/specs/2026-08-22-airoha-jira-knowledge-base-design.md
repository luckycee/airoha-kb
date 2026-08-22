# Airoha JIRA 工单知识库 — 设计文档

> 日期：2026-08-22
> 状态：已确认（待试点验证）

## 1. 背景与目标

收集 Airoha JIRA 服务台门户的客户工单（MIUIX1565-15 ~ MIUIX1565-760，约 746 条），
形成一个公开可访问、可全文搜索、每条工单有独立超链接页面的知识库网站。

**验收标准：**
- 746 条工单全部入库（无法访问的跳过并记录）
- 每条工单：独立页面 + 原始门户链接 + 全文可搜索
- 网站部署于 GitHub Pages，Gitee 镜像仓库备份
- 每周自动增量同步新工单
- 公开前自动脱敏（邮箱/电话/长数字串）

## 2. 架构（内容即代码）

```
Python 爬虫 ──→ Markdown 文件（docs/tickets/*.md）──→ MkDocs 构建 ──→ GitHub Pages
                    ↑ 内容即代码：知识以 Markdown 存储在仓库，
                      网站只是渲染层，可随时切换托管平台
```

- **数据源**：`https://eservice.airoha.com.tw/servicedesk/customer/portal/1038/MIUIX1565-{id}`（Atlassian JIRA 服务台，需登录）
- **网站**：MkDocs + Material 主题，内置全文搜索、标签分类
- **CI**：GitHub Actions 每周定时增量抓取 → 构建 → 发布 Pages

## 3. 采集内容（每条工单）

| 字段 | 来源 | 说明 |
|---|---|---|
| id | URL | MIUIX1565-{编号} |
| title | 页面标题 | 工单主题 |
| date | Details 区块 | 时间 |
| description | Description 区块 | 问题描述 |
| comments | 回复列表 | 每回复含时间+作者+正文 |
| source | — | 原始门户 URL（点击可跳回原文） |

**不抓取**：附件、图片（正文中保留"此工单有 N 个附件"提示）。

## 4. 登录态与抓取策略

- **Cookie 方案**：用户浏览器登录门户后导出 `cookies.txt`（Netscape 格式）
- 初次全量：本机运行，746 条，并发 3 + 随机延迟 + 失败重试 3 次（指数退避）
- 增量：已存在 Markdown 的工单跳过；无法访问的记入 `skip.log`
- 定期同步：GitHub Actions 每周运行；Cookie 过期时通知用户手动更新（约 1 分钟操作）

## 5. 脱敏（简化版）

| 类型 | 规则 |
|---|---|
| 邮箱 | 正则 → `[邮箱已隐藏]` |
| 电话（含 +886/09xx 台湾格式） | 正则 → `[电话已隐藏]` |
| 长数字串（≥10 位，序列号/IMEI） | → `[序列号已隐藏]` |

- 幂等（重复运行不重复替换）
- 每次抓取生成脱敏报告供抽样复核

## 6. 数据格式

```markdown
---
id: MIUIX1565-15
title: ULL 被强制退出
date: 2022/01/11 20:06
tags: [ULL, Pairing]
source: https://eservice.airoha.com.tw/.../MIUIX1565-15
---

## 问题描述
（Description 内容）

## 回复记录
### 2022/01/12 09:30 — 支持工程师
（回复正文）
```

- 标签：内置关键词表自动匹配（蓝牙、ULL、dongle、固件等），形成分类导航
- 附件提示：`> 📎 此工单有 N 个附件（未采集，可点击上方原始链接查看）`

## 7. 站点与发布

- MkDocs + Material：首页（工单列表）、每工单一页、全文搜索、按标签分类
- GitHub Actions 工作流：
  1. 每周定时 + 手动触发
  2. 运行爬虫（Cookie 存 secrets）→ 增量更新 Markdown
  3. 若 cookie 失效 → 通知用户（issue / 邮件），跳过本次发布
  4. `mkdocs build` → 部署 Pages
  5. 同步推送到 Gitee 镜像仓库（Actions 配 SSH key 或 token）
- Gitee：仅代码备份（Gitee Pages 已暂停服务）

## 8. 访问权限（当前 + 演进路径）

- **当前**：公开仓库 + GitHub Pages + 简化脱敏（已确认接受搜索引擎收录风险）
- **未来可切换**（内容零迁移）：
  - GitHub 私有仓库 + Pages（需 GitHub Team 计划，$4/人/月）
  - Cloudflare Pages + Access（免费 ≤50 人，邮箱验证码登录）
  - 切换仅改仓库可见性与托管配置，Markdown 与构建不变

## 9. 试点验证（先行，用户要求）

全量抓取前先抓 10 条（分散采样：15, 100, 200, 300, 400, 500, 600, 700, 750, 760），
验证：页面解析正确性、Markdown 格式、站点渲染与搜索效果。
用户确认满意后再全量。不满意则调整解析/格式后重抓 10 条，避免 Token 浪费。

## 10. 技术栈

- Python 3.10+：requests, beautifulsoup4, lxml
- MkDocs + Material 主题
- GitHub Actions CI
- 无 Node 依赖

## 11. 错误处理与测试

- 网络失败：重试 3 次指数退避；连续失败超过阈值则暂停并告警
- 登录失效：检测到登录页/302 到 login → 立即停止，通知用户更新 Cookie
- 解析失败：保留原始 HTML 到 `raw/` 供排查，记录日志
- 测试：脱敏正则单元测试、Markdown 格式校验（front matter 完整、无脱敏遗漏抽查）
