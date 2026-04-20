# 🚗 美西自驾环线 (US West Roadtrip 2026)

## 项目概述
11天美西自驾环线行程规划 HTML 页面，展示了完整的路线、日程、天气、装备清单等信息。

**路线**: LAX → Tijuana → Santa Barbara → Morro Bay → Big Sur → Monterey → Bishop → Alabama Hills → Mono Lake → Joshua Tree → LAX

**日期**: 2026年9月24日 - 10月5日

## 主要文件
- `roadtrip-usa-2026.html` — 主页面（带 Leaflet 地图）
- `index.html` — GitHub Pages 实际服务的文件
- `roadtrip-new.html` / `roadtrip-clean.html` — 备选版本
- `roadtrip-usa-2026-backup.html` — 备份版本
- `build_roadtrip.py` — 构建脚本
- `verify.py` — 验证脚本

## 功能特性
- 交互式标签页切换（行程概览、路线图、每日详情）
- Leaflet + CartoDB 底图显示真实 GPS 路线
- 可勾选的装备清单（localStorage 持久化）
- Wikipedia 景点链接
- 天气参考（16个城市）
- Yom Kippur / Tioga Pass 风险提示

## 在线地址
- GitHub: https://github.com/jingyi22/us-west-roadtrip-2026
- 发布: https://jingyi22.github.io/us-west-roadtrip-2026/
