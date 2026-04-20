html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TripGenie AI - Premium Redesign Prototype</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #FF6B35; --primary-light: #FF8F66; --primary-dark: #E55A28;
            --secondary: #1A1A2E; --accent: #16213E; --success: #00C897;
            --warning: #FFB800; --bg-light: #F8F9FA;
            --text-primary: #1A1A2E; --text-secondary: #6B7280; --text-muted: #9CA3AF;
            --border: #E5E7EB;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.06); --shadow-md: 0 8px 30px rgba(0,0,0,0.08);
            --shadow-lg: 0 20px 60px rgba(0,0,0,0.15);
            --radius-sm: 12px; --radius-md: 20px;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0F0F1A 0%, #1A1A2E 50%, #16213E 100%);
            color: var(--text-primary); min-height: 100vh;
        }
        .bg-orbs { position: fixed; top: 0; left: 0; right: 0; bottom: 0; overflow: hidden; z-index: 0; pointer-events: none; }
        .bg-orb { position: absolute; border-radius: 50%; filter: blur(100px); opacity: 0.35; animation: float 25s ease-in-out infinite; }
        .bg-orb:nth-child(1) { width: 700px; height: 700px; background: radial-gradient(circle, #FF6B35 0%, transparent 70%); top: -250px; right: -150px; }
        .bg-orb:nth-child(2) { width: 500px; height: 500px; background: radial-gradient(circle, #00C897 0%, transparent 70%); bottom: -150px; left: -150px; animation-delay: -8s; }
        .bg-orb:nth-child(3) { width: 400px; height: 400px; background: radial-gradient(circle, #667eea 0%, transparent 70%); top: 40%; left: 25%; animation-delay: -15s; }
        @keyframes float { 0%, 100% { transform: translate(0, 0) scale(1); } 33% { transform: translate(40px, -40px) scale(1.08); } 66% { transform: translate(-30px, 30px) scale(0.95); } }
        .header { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; padding: 14px 40px; display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(20px); background: rgba(26, 26, 46, 0.85); border-bottom: 1px solid rgba(255,255,255,0.08); }
        .logo { display: flex; align-items: center; gap: 10px; color: white; font-weight: 700; font-size: 17px; }
        .logo-icon { width: 34px; height: 34px; background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: 9px; display: flex; align-items: center; justify-content: center; }
        .nav-tabs { display: flex; gap: 6px; background: rgba(255,255,255,0.08); padding: 4px; border-radius: 10px; }
        .nav-tab { padding: 7px 18px; border-radius: 7px; color: rgba(255,255,255,0.65); font-size: 13px; font-weight: 500; cursor: pointer; transition: all 0.25s; border: none; background: transparent; }
        .nav-tab.active { background: rgba(255,255,255,0.95); color: var(--text-primary); }
        .header-tag { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); padding: 5px 12px; border-radius: 18px; font-size: 11px; font-weight: 600; color: white; }
        .main-container { position: relative; z-index: 1; max-width: 1500px; margin: 0 auto; padding: 110px 40px 60px; }
        .hero { text-align: center; margin-bottom: 50px; animation: fadeInUp 0.8s ease; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
        .hero-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,107,53,0.18); border: 1px solid rgba(255,107,53,0.35); padding: 7px 14px; border-radius: 25px; color: var(--primary-light); font-size: 12px; font-weight: 500; margin-bottom: 20px; }
        .hero-badge::before { content: ''; width: 7px; height: 7px; background: var(--primary); border-radius: 50%; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; transform: scale(1.3); } }
        .hero-title { font-size: 52px; font-weight: 700; color: white; line-height: 1.2; margin-bottom: 18px; letter-spacing: -1.5px; }
        .hero-title span { background: linear-gradient(135deg, var(--primary), var(--primary-light)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
        .hero-subtitle { font-size: 18px; color: rgba(255,255,255,0.65); max-width: 580px; margin: 0 auto; line-height: 1.65; }
        .flow-navigator { display: flex; justify-content: center; gap: 14px; margin-bottom: 45px; flex-wrap: wrap; }
        .flow-step { display: flex; align-items: center; gap: 10px; padding: 10px 20px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; cursor: pointer; transition: all 0.3s; color: rgba(255,255,255,0.55); }
        .flow-step:hover, .flow-step.active { background: rgba(255,255,255,0.09); border-color: var(--primary); color: white; }
        .flow-step.active { background: linear-gradient(135deg, rgba(255,107,53,0.22), rgba(255,143,102,0.12)); border-color: rgba(255,107,53,0.6); }
        .flow-step-num { width: 26px; height: 26px; background: rgba(255,255,255,0.08); border-radius: 7px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; }
        .flow-step.active .flow-step-num { background: var(--primary); color: white; }
        .flow-step-text { font-size: 13px; font-weight: 500; }
        .flow-arrow { color: rgba(255,255,255,0.25); font-size: 16px; }
        .phone-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 50px; justify-items: center; }
        .phone-frame { width: 390px; background: linear-gradient(145deg, #2a2a2c, #1d1d1f); border-radius: 52px; padding: 14px; box-shadow: var(--shadow-lg), inset 0 1px 0 rgba(255,255,255,0.1); position: relative; }
        .phone-frame::before { content: ''; position: absolute; top: 20px; left: 50%; transform: translateX(-50%); width: 110px; height: 30px; background: #1d1d1f; border-radius: 22px; z-index: 10; }
        .phone-screen { background: var(--bg-light); border-radius: 42px; overflow: hidden; height: 820px; display: flex; flex-direction: column; }
        .notch { height: 46px; background: #1d1d1f; }
        .screen-status-bar { height: 46px; background: white; display: flex; justify-content: space-between; align-items: center; padding: 0 28px; font-size: 15px; font-weight: 600; }
        .screen-header { background: white; padding: 14px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border); }
        .header-left { display: flex; align-items: center; gap: 14px; }
        .back-btn { width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; color: var(--primary); font-size: 22px; cursor: pointer; }
        .header-title { font-size: 18px; font-weight: 600; color: var(--text-primary); }
        .header-actions { display: flex; gap: 18px; }
        .header-icon { width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; color: var(--text-secondary); cursor: pointer; transition: color 0.2s; }
        .header-icon:hover { color: var(--primary); }
        .chat-area { flex: 1; display: flex; flex-direction: column; overflow: hidden; background: linear-gradient(180deg, var(--bg-light) 0%, #f0f1f3 100%); }
        .chat-messages { flex: 1; overflow-y: auto; padding: 18px; display: flex; flex-direction: column; gap: 14px; }
        .chat-messages::-webkit-scrollbar { width: 0; }
        .message { display: flex; gap: 11px; animation: messageIn 0.45s cubic-bezier(0.16, 1, 0.3, 1); }
        @keyframes messageIn { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: translateY(0); } }
        .message.user { flex-direction: row-reverse; }
        .message-avatar { width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; flex-shrink: 0; }
        .message.ai .message-avatar { background: linear-gradient(135deg, var(--primary), var(--primary-light)); color: white; }
        .message.user .message-avatar { background: var(--secondary); color: white; }
        .message-content { max-width: 80%; }
        .message-bubble { padding: 13px 17px; border-radius: 20px; font-size: 15px; line-height: 1.55; }
        .message.ai .message-bubble { background: white; color: var(--text-primary); border-bottom-left-radius: 7px; box-shadow: var(--shadow-sm); }
        .message.user .message-bubble { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; border-bottom-right-radius: 7px; }
        .thinking-indicator { display: flex; align-items: center; gap: 11px; padding: 15px 19px; background: white; border-radius: 20px; border-bottom-left-radius: 7px; box-shadow: var(--shadow-sm); width: fit-content; }
        .thinking-dots { display: flex; gap: 5px; }
        .thinking-dots span { width: 8px; height: 8px; background: var(--primary); border-radius: 50%; animation: thinkingBounce 1.4s infinite ease-in-out; }
        .thinking-dots span:nth-child(1) { animation-delay: 0s; } .thinking-dots span:nth-child(2) { animation-delay: 0.2s; } .thinking-dots span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes thinkingBounce { 0%, 80%, 100% { transform: scale(0.65); opacity: 0.35; } 40% { transform: scale(1); opacity: 1; } }
        .thinking-text { font-size: 13px; color: var(--text-secondary); font-weight: 500; }
        .thinking-steps { display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap; }
        .thinking-step { display: flex; align-items: center; gap: 5px; font-size: 11px; color: var(--text-muted); background: #f5f5f7; padding: 5px 10px; border-radius: 12px; transition: all 0.3s; }
        .thinking-step.active { background: rgba(255,107,53,0.12); color: var(--primary); }
        .trip-card { background: white; border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); margin-top: 10px; }
        .trip-card-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 22px; color: white; }
        .trip-card-days { font-size: 11px; opacity: 0.8; margin-bottom: 5px; letter-spacing: 0.5px; }
        .trip-card-title { font-size: 19px; font-weight: 600; }
        .trip-card-route { display: flex; align-items: center; gap: 8px; margin-top: 10px; font-size: 13px; opacity: 0.9; }
        .trip-card-body { padding: 16px; }
        .trip-day-item { display: flex; gap: 13px; padding: 14px 0; border-bottom: 1px solid var(--border); cursor: pointer; transition: all 0.2s; }
        .trip-day-item:last-child { border-bottom: none; }
        .trip-day-item:hover { background: rgba(255,107,53,0.06); margin: 0 -16px; padding: 14px 16px; border-radius: 8px; }
        .trip-day-num { width: 38px; height: 38px; background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: 11px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 14px; flex-shrink: 0; }
        .trip-day-info { flex: 1; }
        .trip-day-title { font-size: 14px; font-weight: 600; color: var(--text-primary); margin-bottom: 3px; }
        .trip-day-desc { font-size: 12px; color: var(--text-secondary); }
        .trip-day-meta { display: flex; gap: 6px; margin-top: 6px; flex-wrap: wrap; }
        .trip-day-tag { font-size: 10px; background: #f0f0f5; color: var(--text-secondary); padding: 3px 9px; border-radius: 6px; }
        .trip-day-tag.highlight { background: rgba(0,200,151,0.12); color: #00a87d; }
        .trip-day-arrow { color: var(--text-muted); display: flex; align-items: center; font-size: 16px; }
        .guidance-section { padding: 0 16px 18px; }
        .guidance-label { font-size: 10px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
        .guidance-cards { display: flex; flex-direction: column; gap: 10px; }
        .guidance-card { background: white; border-radius: var(--radius-sm); padding: 15px 17px; display: flex; align-items: center; gap: 14px; cursor: pointer; transition: all 0.25s ease; border: 1px solid var(--border); }
        .guidance-card:hover { border
