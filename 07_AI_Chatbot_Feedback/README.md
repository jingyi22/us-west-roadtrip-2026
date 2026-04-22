# 07: AI Chatbot Feedback Mechanism Demo

## 项目概述

基于 Trip.com《AI Chatbot Feedback Mechanism Comparison Analysis》(July 2025) 报告的全链路交互原型。

**数据来源**: `AI Chatbot Feedback Mechanism Comparison Analysis_20250730v1.pptx` (IBU CSC UXA)

## 报告核心发现

- 11个平台中8个已有AI反馈机制
- 最佳触发时机：对话结束时自动触发
- 最佳UX形式：对话内嵌入评价
- Trip.com 缺陷：缺少主动邀请文案（script）

## Demo 链路（5个页面）

1. **Introduction** — 研究背景 + 11个平台覆盖 + 3个核心发现
2. **AI Chat End** — Trip.com AI对话结束 + 主动反馈邀请卡片
3. **Feedback Choice** — 用户选择：快捷反馈(👍/👎) 或 完整CSAT评价
4. **CSAT Survey** — 3题渐进式评价（满意度→原因→开放式反馈）
5. **Thank You** — 完成反馈 + 问题未解决时的跟进提示

## 文件

- `index.html` — 完整交互原型（单文件，React 18 inline）
- `SPEC.md` — 设计规范文档

## 打开方式

双击 `index.html` 在浏览器中打开即可体验。

---

*Generated from: AI Chatbot Feedback Mechanism Comparison Analysis_20250730v1.pptx*
