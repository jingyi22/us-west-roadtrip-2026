# 🧳 TripGenie AI Trip Planner UX 研究与原型设计

## 项目概述
针对 Trip.com AI Trip Planner 竞品研究，包含携程问道、Expedia Romie、Priceline Penny 等国内外竞品分析，以及基于研究结果的原型设计。

**所属团队**: IBU CSC UXA (Trip.com 内部研究/UX团队)

## 主要文件
- `AI_Planner_Competitor_Research_20250522.pptx` — 竞品研究原始PPT（75MB）
- `Trip_com_AI_Redesign_Prototype.html` — v1 原型
- `TripGenie_AI_Prototype.html` — 主原型文件
- `TripGenie_v3.html` / `TripGenie_fixed.html` / `TripGenie_test.html` — 迭代版本
- `TripGenie_AI_Prototype.py` / `build_prototype.py` — 构建脚本

## 竞品分析
### 国内竞品
携程问道、同程旅行程心 AI、飞猪 AI 问一问、马蜂窝 AI 小蚂、去哪儿

### 海外竞品
Booking.com AI Trip Planner、Expedia Romie、Priceline Penny、Airbnb、Kayak Ask Kayak

## TripGenie 改进机会
| 维度 | 问题 |
|------|------|
| 语音交互 | 只支持语音转文字，缺少真正的语音对话能力 |
| 多语言适配 | 能识别语言，但不会自动用用户语言回复 |
| 条件理解 | 无法正确理解基本用户需求（预算/人数等） |
| 行程合理性 | 行程建议较机械，缺乏文化理解 |
| 文化敏感度 | 未识别用户文化背景（如 Muslim、Chef 等身份） |
| 对话语气 | 语气模板化，不够自然亲切 |
| 客服接入 | 敏感场景未主动接入人工客服 |

## 核心竞品亮点
- **Expedia Romie**: 答案质量最佳，能自动适配用户语言
- **Priceline Penny**: 交互体验突出，支持多条件筛选
