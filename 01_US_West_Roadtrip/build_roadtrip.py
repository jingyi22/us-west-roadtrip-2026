#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

html = open('/Users/jingyilu/.openclaw/workspace/roadtrip-usa-2026.html', 'a', encoding='utf-8')

# Day 7 continued
html.write('''  <!-- DAY 7 -->
  <div class="day" onclick="toggleDay(this)">
    <div class="dh">
      <div class="dl"><div class="dn">D7</div><div class="di"><div class="dt">Day 7 · 9月30日（周二）</div><div class="ds">蒙特雷 → 东 Sierra · US-395 内陆回程</div></div></div>
      <div class="da">▼</div>
    </div>
    <div class="db"><div class="dc">
      <div class="tl">
        <div class="ti"><div class="tm">08:00</div><div class="tp">🚗 退房出发，驶入内陆</div><div class="td">今日是赶路日，穿越 Salinas Valley，横穿 Central Valley</div></div>
        <div class="ti"><div class="tm">10:00</div><div class="tp">🌾 穿越 Salinas Valley</div><div class="td">农田风光，翻越 Tehachapi Pass，进入 Sierra 山麓</div></div>
        <div class="ti"><div class="tm">14:00</div><div class="tp">🏜️ 进入 Owens Valley（东部 Sierra 山谷）</div><div class="td">地形从绿色农田变为荒漠山谷，Sierra Nevada 山脉在右侧拔地而起</div></div>
        <div class="ti"><div class="tm">17:30</div><div class="tp">🏘️ 抵达 Bishop（东部 Sierra 最大补给小镇）</div><div class="td">采购补给（CVS、超市、餐厅齐全）</div></div>
        <div class="ti"><div class="tm">19:00</div><div class="tp">🍽️ Bishop 晚餐</div><div class="td">推荐：Schuby's（德国菜）或 Criterium（自行车主题咖啡馆）</div></div>
      </div>
      <div class="tp"><span class="ic">💡</span><div class="tx"><div class="tt">赶路日提示</div>今日景点少，主要任务是到达 Eastern Sierra。建议在 Bishop 补充水、零食、水果，为接下来两天的高原探险做准备。</div></div>
      <div style="margin-top:10px"><span class="g g-d">🚗 赶路日</span><span class="g g-c">🏔️ 山景</span></div>
    </div></div>
  </div>

  <!-- DAY 8 -->
  <div class="day" onclick="toggleDay(this)">
    <div class="dh">
      <div class="dl"><div class="dn warn">D8</div><div class="di"><div class="dt">Day 8 · 10月1日（周三）🌅 必早起！</div><div class="ds">Alabama Hills 日出 · Mobius Arch · Mammoth Lakes</div></div></div>
      <div class="da">▼</div>
    </div>
    <div class="db"><div class="dc">
      <div class="wb"><span class="ic">🌅</span><div class="tx"><div class="tt">日出必去！Alabama Hills Mobius Arch</div>Mount Whitney alpenglow（ alpenglow 粉红光）仅持续10-15分钟。日出前30分钟到达停车场，天黑需手电筒。</div></div>
      <div class="tl">
        <div class="ti highlight"><div class="tm">05:30</div><div class="tp">🌅 出发前往 Alabama Hills（从 Bishop 开车约20分钟）</div><div class="td">天黑路暗，开大灯，导航至 "Mobius Arch Trailhead, Lone Pine, CA"</div></div>
        <div class="ti highlight"><div class="tm">06:00</div><div class="tp">📸 Mobius Arch · Alpenglow 日出</div><div class="td">0.6英里环形步道，免费。从停车场步行约3分钟即到。<br>经典角度：Mobius Arch 框架中的 Mount Whitney（14,505尺）🌄<br>Mount Williamson（14,375尺）同步被照亮</div></div>
        <div class="ti highlight"><div class="tm">08:00</div><div class="tp">🚗 继续游览 Alabama Hills · Movie Flat Road</div><div class="td">环线约17英里驾驶，经过多部电影拍摄地。Boot Arch、Shark Fin 等岩石拱门</div></div>
        <div class="ti\"><div class="tm\">10:00</div><div class="tp\">🍳 Lone Pine 小镇早餐</div><div class="td">回到 Lone Pine 补充能量，这里有咖啡馆和快餐店</div></div>
        <div class="ti\"><div class="tm">12:00</div><div class="tp\">🚗 前往 Mammoth Lakes（约50英里，1小时）</div><div class="td">沿 US-395 北上，途径 Owens River Gorge 观景点</div></div>
        <div class="ti highlight"><div class="tm">13:30</div><div class="tp">🏔️ Mammoth Lakes 游览</div><div class="td">Lake Mamie（湖边漫步）、Lake Mary（野餐）、或乘 Mammoth Mountain 缆车（$29/人）登顶俯瞰</div></div>
        <div class="ti\"><div class="tm">18:00</div><div class="tp\">🌇 Mammoth Lakes 小镇晚餐 + 住宿</div><div class="td">推荐：Mammoth Rock Brasserie 或热带雨林咖啡馆</div></div>
      </div>
      <div style="margin-top:10px">
        <span class="g g-p">📸 日出摄影</span>
        <span class="g g-h\">🥾 轻松徒步</span>
        <span class="g g-s">🏔️ 雪山湖泊</span>
      </div>
    </div></div>
  </div>

  <!-- DAY 9 -->
  <div class="day" onclick="toggleDay(this)">
    <div class="dh">
      <div class="dl"><div class="dn warn">D9</div><div class="di"><div class="dt">Day 9 · 10月2日（周四）🌅 必早起！</div><div class="ds\">Mono Lake 日出 · Bodie 鬼城 · Lee Vining</div></div></div>
      <div class="da\">▼</div>
    </div>
    <div class="db"><div class="dc">
      <div class="wb"><span class="ic">🌅</span><div class="tx"><div class="tt">日出必去！Mono Lake South Tufa</div>"加州最上镜日出地之一"——日出时 Sierra 峰粉红，钙华塔林变金色，光影令人窒息。South Tufa $3/人。建议日出前45分钟到达。</div></div>
      <div class="tl">
        <div class="ti highlight"><div class="tm">05:45</div><div class="tp">🌅 出发前往 Mono Lake South Tufa（约1小时车程）</div><div class="td\">天黑，带手电筒。导航：South Tufa Area, Lee Vining, CA</div></div>
        <div class="ti highlight"><div class="tm">07:00</div><div class="tp">📸 Mono Lake South Tufa 日出</div><div class="td">1英里环形步道，全程无遮阳。带水和防晒。早晨气温约35-45°F（1-7°C）🧥<br>经典角度：Tufa 塔林剪影 + Sierra 金色山峰倒影</div></div>
        <div class="ti\"><div class="tm">09:30</div><div class="tp\">☕ Lee Vining 小镇早餐</div><div class="td">Mono Inn 或 Nic's Deli（时间早可能还没开，备选）</div></div>
        <div class="ti highlight"><div class="tm">10:30</div><div class="tp\">🏚️ Bodie Ghost Town（鬼城）</div><div class="td">13英里土路，最后3英里较颠簸（普通轿车可行但开慢点）<br>$8/人 + $3 guidebook（强烈建议买）<br>游览时间：2-3小时，穿舒适步行鞋，带水<br>注意：Bodie 诅咒——拿走任何东西会倒霉 😄</div></div>
        <div class="ti\"><div class="tm">16:00</div><div class="tp\">🚗 返回 Lee Vining</div><div class="td">约1小时车程，路况好</div></div>
        <div class="ti\"><div class="tm\">17:30</div><div class="tp\">🌇 Lee Vining 看日落</div><div class="td">Mono Lake 西岸，日落视角超棒 · Tioga Pass 山口也在这里</div></div>
      </div>
      <div style="margin-top:10px">
        <span class="g g-p">📸 日出摄影</span>
        <span class="g g-s">🏚️ 鬼城探秘</span>
        <span class="g g-h\">🧥 需带外套（高原冷）</span>
      </div>
    </div></div>
  </div>

  <!-- DAY 10 -->
  <div class="day" onclick="toggleDay(this)">
    <div class="dh">
      <div class="dl"><div class="dn warn">D10</div><div class="di"><div class="dt">Day 10 · 10月3日（周五）⚠️ 出发前打电话确认</div><div class="ds\">Lee Vining → Tioga Pass → Yosemite → 洛杉矶</div></div></div>
      <div class="da\">▼</div>
    </div>
    <div class="db"><div class="dc">
      <div class="wb"><span class="ic">⚠️</span><div class="tx"><div class="tt">Tioga Pass 状态确认</div>Tioga Pass 通常10月底-11月初关闭，但10月初可能因天气提前关闭。<strong>出发前必做：</strong>致电 ☎️ (209) 372-0200（按1,1）确认路况，或查看 NPS 官网。如已关闭，改走 CA-49 / CA-140 绕道入 Yosemite。</div></div>
      <div class="tl">
        <div class="ti\"><div class="tm">07:00</div><div class="tp">🚗 出发，经 Tioga Pass 进入 Yosemite</div><div class="td">约1小时穿越 Yosemite 东门（从 Lee Vining 出发）</div></div>
        <div class="ti highlight\"><div class="tm\">08:30</div><div class="tp\">🏔️ Tunnel View（隧道景观）</div><div class="td\">经典 Yosemite 明信片角度：El Capitan + Bridalveil Fall + Half Dome 🌄</div></div>
        <div class="ti\"><div class="tm\">09:30</div><div class="tp\">💧 Bridalveil Fall（新娘面纱瀑布）</div><div class="td">0.5英里步道，瀑布水雾扑面，停车观景点</div></div>
        <div class="ti\"><div class="tm\">11:00</div><div class="tp\">🧗 El Capitan Picnic Area</div><div class="td\">攀岩圣地，野餐观巨岩</div></div>
        <div class="ti\"><div class="tm\">12:30</div><div class="tp\">🍽️ Yosemite Valley 午餐</div><div class="td">The Village Grill 或 Degnan's Deli（快餐式，简餐为主）</div></div>
        <div class="ti\"><div class="tm\">14:00</div><div class="tp\">🌲 Glacier Point（提前确认开放）</div><div class="td">如开放，全景制高点俯瞰 Yosemite Valley（4,000尺高差）。门票含在 $35/车入园费内</div></div>
        <div class="ti\"><div class="tm\">15:30</div><div class="tp\">🚗 出发返回洛杉矶</div><div class="td">沿 CA-41（Fresno方向）→ I-5，约4-5小时</div></div>
        <div class="ti\"><div class="tm\">20:00</div><div class="tp\">🏨 LAX 附近住宿</div><div class="td\">还车准备次日航班</div></div>
      </div>
      <div style="margin-top:10px">
        <span class="g g-s">🏔️ 国家公园</span>
        <span class="g g-h\">🥾 轻松徒步</span>
        <span class="g g-w\">⚠️ 提前打电话确认路况</span>
      </div>
    </div></div>
  </div>

  <!-- DAY 11 -->
  <div class="day" onclick="toggleDay(this)">
    <div class="dh">
      <div class="dl"><div class="dn resty">D11</div><div class="di"><div class="dt\">Day 11 · 10月4日（周六）</div><div class="ds\">洛杉矶自由活动 · 还车准备 · 出发回家</div></div></div>
      <div class=\"da\">▼</div>
    </div>
    <div class="db"><div class="dc">
      <div class="tl">
        <div class="ti\"><div class="tm\">上午</div><div class="tp\">🛍️ The Grove / Beverly Hills 最后购物</div><div class="td\">或 Getty Center 免费艺术博物馆（强烈推荐！俯瞰洛杉矶全景）</div></div>
        <div class="ti\"><div class="tm\">下午</div><div class="tp\">🚗 提前还车</div><div class="td\">建议航班起飞前3小时还车，留出充足时间</div></div>
        <div class="ti\"><div class="tp\">🎉 庆祝行程圆满结束！</div></div>
      </div>
    </div></div>
  </div>
</div>
''')

html.close()
print("Days 7-11 written")
