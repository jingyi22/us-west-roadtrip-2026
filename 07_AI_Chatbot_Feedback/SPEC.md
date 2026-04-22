# SPEC: AI Chatbot Feedback Mechanism — Interactive Demo

## 1. Concept & Vision

一个完整的 Trip.com AI Chatbot Feedback 全链路交互原型。用户体验从"与AI对话结束"→"收到反馈邀请"→"选择评价"→"完成CSAT调查"→"结束感谢"的完整流程。设计语言参考 Trip.com 品牌风格（橙色为主色调），风格专业克制，体现 UX research 的严谨感。

## 2. Design Language

**Aesthetic direction**: Trip.com 品牌风格 — 温暖橙色系，干净卡片布局，专业但不冰冷
**Color palette**:
- Primary: #FF6600 (Trip.com orange)
- Primary light: #FF8533
- Background: #F7F8FA
- Card: #FFFFFF
- Text primary: #1A1A2E
- Text secondary: #666666
- Success: #00C853
- Border: #E8E8E8
**Typography**:
- Display: "Poppins", sans-serif (600 weight)
- Body: "Inter", sans-serif
- Chinese fallback: "PingFang SC", "Microsoft YaHei"
**Motion**:
- Page transitions: fade + slight slide up (300ms ease-out)
- Cards: fade in staggered 80ms
- Buttons: scale 0.97 on press, shadow lift on hover
- Chat bubbles: slide in from left/right with 200ms spring

## 3. Layout & Structure

**Pages (5 screens)**:
1. **Introduction Page** — 研究背景 + 问题概述 + 竞品矩阵快照 + 开始按钮
2. **AI Chat End State** — 对话结束界面，AI主动发出反馈邀请
3. **Feedback Choice** — 用户选择：👎/👍 快捷反馈 or 📝 完整survey
4. **CSAT Survey** — 对话内嵌入的评价表单（3题）
5. **Thank You Page** — 感谢页 + 问题解决追踪

**Responsive**: 移动端优先（390×844 iPhone原型尺寸），居中展示

## 4. Features & Interactions

### Flow
```
[Intro] → [AI Chat Ends] → [Feedback Invitation Script] → [Choice: Quick/Detailed]
                ↓ Quick path                   ↓ Detailed path
           [Thumbs 👍/👎]                  [CSAT Survey 3 questions]
                ↓                                   ↓
           [Quick Thank You]                 [Thank You + follow-up]
```

### Introduction Page
- 研究背景文字（来自slide 2）
- 竞品覆盖徽章（11个平台）
- 3个核心发现高亮卡片
- "开始体验" CTA按钮

### AI Chat End State
- 对话气泡：AI发出结束语
- 系统提示：AI给出反馈邀请文案（触发时机：自动在对话结束时）
- 橙色高亮邀请卡片出现（带脚本： "To better assist our customers..."）

### Feedback Choice
- 两个选项卡并列：
  - Option A: 快捷反馈（👍/👎 + 可选简短原因）
  - Option B: 完整评价（3题CSAT量表）

### CSAT Survey（对话内嵌入）
- 问题1：评价星级（1-5星或表情emoji）
- 问题2：选择评价原因（多选tag）
- 问题3：开放式反馈（可选）
- 底部skip选项

### Thank You Page
- 完成动画（打勾图标放大）
- "感谢您的反馈" 文案
- 追踪状态提示（如选了"未解决"则显示"已为您转接人工服务"）

## 5. Component Inventory

| Component | States |
|-----------|--------|
| PageContainer | intro / chat-end / choice / survey / thank-you |
| ChatBubble | ai / user; animated entrance |
| InvitationCard | default / hover; orange left-border accent |
| RatingEmoji | unselected / selected; scale on select |
| SurveyOption | unselected / selected; border highlight |
| ProgressBar | step 1/3, 2/3, 3/3 |
| CTAButton | default / hover / active / loading |
| SkipLink | default / hover |

## 6. Technical Approach

- **Single HTML file** with inline React (Babel)
- **State machine**: `screen` state drives which component renders
- **No external dependencies** beyond React + Babel CDN
- **CSS variables** for theming
- **Smooth transitions** between screens using CSS transitions + opacity
