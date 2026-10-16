# -*- coding: utf-8 -*-
"""
Mansur Durdimatov (@durd1ma7ov06) — Cyberpunk Theme-Aware Profile Generator.
With Humanoid Robotics, Drone Systems, AI and Full-Stack Engineering.
Generates:
  - dark.svg / light.svg (Hero Banner with Humanoid Robot & Drone)
  - projects-dark.svg / projects-light.svg (Featured Projects Matrix)
"""

import base64
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))

NAME = "MANSUR DURDIMATOV"
TAGLINE = "Full-Stack Dev 💻 | Drone & Humanoid Robotics Engineer 🤖 | AI Systems"
SUBLINE = "Engineering humanoid bipedal robotics, autonomous UAV drones & intelligent AI systems"

PALETTES = {
    "dark": {
        "bg": "#0A101F", "card": "#0E1626", "grid": "#1B2740", "border": "#22304D",
        "text": "#F8FAFC", "muted": "#94A3B8", "dim": "#64748B",
        "cyan": "#22D3EE", "purple": "#A78BFA", "green": "#10B981", "amber": "#FBBF24", "red": "#EF3B2D",
        "chip_bg": "#131F35", "chip_text": "#CBD5E1",
    },
    "light": {
        "bg": "#FFFFFF", "card": "#F8FAFC", "grid": "#E2E8F0", "border": "#CBD5E1",
        "text": "#0F172A", "muted": "#475569", "dim": "#64748B",
        "cyan": "#0891B2", "purple": "#7C3AED", "green": "#059669", "amber": "#D97706", "red": "#D62F22",
        "chip_bg": "#F1F5F9", "chip_text": "#334155",
    },
}

SANS = "'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace"

HERO_CHIPS = ["Humanoid Robotics", "ROS / ROS 2", "Autonomous Drone", "Python", "C++", "Inverse Kinematics", "TypeScript", "Computer Vision", "Docker"]

ICONS = {
    "car": '<path d="M4 11.5 6 6.2A2.5 2.5 0 0 1 8.4 4.5h7.2A2.5 2.5 0 0 1 18 6.2l2 5.3"/>'
           '<rect x="2.5" y="11.5" width="19" height="6.5" rx="2"/>'
           '<circle cx="7" cy="19.6" r="1.4"/><circle cx="17" cy="19.6" r="1.4"/>',
    "drone": '<circle cx="5" cy="5" r="2.8"/><circle cx="19" cy="5" r="2.8"/>'
             '<circle cx="5" cy="19" r="2.8"/><circle cx="19" cy="19" r="2.8"/>'
             '<rect x="9" y="9" width="6" height="6" rx="1.6"/>'
             '<path d="M7 7l2 2M17 7l-2 2M7 17l2-2M17 17l-2-2"/>',
    "medkit": '<rect x="2.5" y="7" width="19" height="13" rx="2.5"/>'
              '<path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M12 11v6M9 14h6"/>',
    "school": '<path d="M2.5 8.8 12 4.2l9.5 4.6L12 13.4z"/>'
              '<path d="M6.3 11.2V16c0 1.7 2.6 3 5.7 3s5.7-1.3 5.7-3v-4.8"/>'
              '<path d="M21.5 8.8v5"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="2.2"/>'
            '<rect x="9.6" y="9.6" width="4.8" height="4.8" rx="1"/>'
            '<path d="M9.2 3v3M14.8 3v3M9.2 18v3M14.8 18v3'
            'M3 9.2h3M3 14.8h3M18 9.2h3M18 14.8h3"/>',
    "sparkles": '<path d="M11 3.2l1.7 4.4 4.4 1.7-4.4 1.7L11 15.4 9.3 11 4.9 9.3 9.3 7.6z"/>'
                '<path d="M18 14.4l.85 2.2 2.2.85-2.2.85-.85 2.2-.85-2.2-2.2-.85 2.2-.85z"/>',
    "server": '<rect x="3" y="3.4" width="18" height="6.2" rx="2"/>'
              '<rect x="3" y="14.4" width="18" height="6.2" rx="2"/>'
              '<path d="M6.9 6.5h.02M6.9 17.5h.02M10.5 6.5h4M10.5 17.5h4"/>',
    "code": '<path d="M8.6 7.4 3.4 12l5.2 4.6M15.4 7.4 20.6 12l-5.2 4.6M13.6 4l-3.2 16"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6"/>'
             '<path d="M12 3c2.6 2.9 2.6 15.1 0 18M12 3c-2.6 2.9-2.6 15.1 0 18"/>',
    "shield": '<path d="M12 3.2l8 3v5.9c0 4.4-3.2 7.9-8 8.7-4.8-.8-8-4.3-8-8.7V6.2z"/>'
              '<path d="M9 12l2.2 2.2L15.2 10"/>',
    "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "bot": '<rect x="4" y="9" width="16" height="12" rx="3"/><circle cx="12" cy="4" r="2"/>'
           '<path d="M12 6v3M8 14h.01M16 14h.01M9 18h6"/>',
    "humanoid": '<circle cx="12" cy="4" r="2.5"/><path d="M12 6.5v7M7 9h10M8.5 13.5l-2.5 7.5M15.5 13.5l2.5 7.5M6 9l-2 5M18 9l2 5"/>',
    "hands": '<path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v7M10 10.5V6a2 2 0 0 0-4 0v8"/>'
             '<path d="M6 14v1a6 6 0 0 0 6 6h1a6 6 0 0 0 6-6V9a2 2 0 0 0-4 0"/>',
}

SECTIONS = [
    ("HUMANOID ROBOTICS, DRONES & EMBEDDED", "purple", [
        ("humanoid", "Humanoid Bipedal Core", "Muvozanat & Inverse Kinematics",  "ROS 2 · C++ · Gazebo · IK"),
        ("drone",    "Autonomous Drone UAV",  "LiDAR, to'siqdan qochish & parvoz", "PX4 · ArduPilot · MAVLink"),
        ("bot",      "Bionic Manipulator",    "6-eksa robot qo'l & servo boshqaruv","ESP32 · Inverse Kinematics"),
        ("hands",    "motion 3D Tracking",    "3D qo'l imo-ishoralarini robotga uzatish","MediaPipe · Three.js · JS"),
        ("zap",      "Voltguard IoT",         "Aqlli energiya monitoringi & himoya","IoT · ESP32 · C++"),
        ("server",   "Teahouse Combinator",   "Aqlli telemetriya & avtomatlashtirish","IoT · Node.js · C++"),
    ]),
    ("AI, COMPUTER VISION & PLATFORMS", "cyan", [
        ("medkit",   "pnevmoscan AI",         "Pnevmoniya & rentgen AI tashxisi",   "Python · FastAPI · PyTorch"),
        ("sparkles", "Maqola_agent",          "Avtomatlashtirilgan ilmiy maqolalar", "Python · LLM · AI Agent"),
        ("school",   "MockLife Platform",     "IELTS & CEFR AI imtihon simulyatori", "TypeScript · React · Postgres"),
    ]),
    ("WEB, CLOUD & BOT ECOSYSTEM", "green", [
        ("globe",    "Digital-edu",           "Raqamli texnologiyalar ta'lim portali","React · Tailwind · Node.js"),
        ("server",   "Muhtojman",             "Xayriya va ijtimoiy ko'mak tizimi",    "Full-Stack · JavaScript"),
        ("bot",      "Ittifoq-Boti",          "Telegram avtomatlashtirilgan boti",    "Node.js · Telegram API"),
    ]),
]

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def avatar_b64():
    path = os.path.join(HERE, "avatar.png")
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

def icon(name, x, y, size, color, sw=2.0):
    k = size / 24.0
    ic_data = ICONS.get(name, ICONS["code"])
    return ('<g transform="translate(%.2f,%.2f) scale(%.4f)" fill="none" stroke="%s" '
            'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>'
            % (x, y, k, color, sw / k, ic_data))

def chip(x, y, label, p, h=34, fs=13.5, pad=14):
    w = int(len(label) * fs * 0.58) + pad * 2
    s = ('<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s"/>'
         '<text x="%d" y="%d" font-family="%s" font-size="%d" fill="%s">%s</text>'
         % (x, y, w, h, h // 2, p["chip_bg"], p["border"],
            x + pad, y + h // 2 + int(fs * 0.36), MONO, fs, p["chip_text"], esc(label)))
    return s, x + w + 10

def defs(p):
    return (
        '<defs>'
        '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0%%" stop-color="%s"/><stop offset="55%%" stop-color="%s"/>'
        '<stop offset="100%%" stop-color="%s"/></linearGradient>'
        '<linearGradient id="bgfade" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/></linearGradient>'
        '<radialGradient id="glowC"><stop offset="0%%" stop-color="%s" stop-opacity="0.32"/>'
        '<stop offset="100%%" stop-color="%s" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="glowP"><stop offset="0%%" stop-color="%s" stop-opacity="0.28"/>'
        '<stop offset="100%%" stop-color="%s" stop-opacity="0"/></radialGradient>'
        '<pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse">'
        '<path d="M34 0H0V34" fill="none" stroke="%s" stroke-width="1" stroke-opacity="0.55"/>'
        '</pattern>'
        '<clipPath id="avatarClip"><circle cx="146" cy="208" r="92"/></clipPath>'
        '</defs>'
    ) % (p["cyan"], p["purple"], p["green"], p["bg"], p["card"],
         p["cyan"], p["cyan"], p["purple"], p["purple"], p["grid"])

def neon_avatar(cx, cy, r, p, b64):
    d = r * 2
    o = ['<g>']
    o.append('<circle cx="%d" cy="%d" r="%d" fill="url(#glowC)" opacity="0.9"/>' % (cx, cy, r + 55))
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="14 10" opacity="0.55">'
             '<animateTransform attributeName="transform" type="rotate" '
             'from="0 %d %d" to="360 %d %d" dur="22s" repeatCount="indefinite"/>'
             '</circle>' % (cx, cy, r + 16, p["cyan"], cx, cy, cx, cy))
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="2.2" opacity="0.85"/>'
             % (cx, cy, r + 6, p["purple"]))
    if b64:
        o.append('<image href="data:image/png;base64,%s" x="%d" y="%d" width="%d" height="%d" '
                 'clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>'
                 % (b64, cx - r, cy - r, d, d))
    else:
        o.append('<circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (cx, cy, r, p["card"]))
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="3" opacity="0.95"/>'
             % (cx, cy, r, p["cyan"]))
    o.append('</g>')
    return "".join(o)

def humanoid_and_drone_illustration(cx, cy, p):
    """Futuristic Cyberpunk Humanoid Robot + Autonomous Drone Illustration."""
    return (
        '<g transform="translate(%d,%d)">'
        '  <circle cx="0" cy="0" r="105" fill="url(#glowP)" opacity="0.7"/>'
        '  <!-- ================= HUMANOID ROBOT HEAD & CHEST ================= -->'
        '  <!-- Humanoid Torso / Shoulders -->'
        '  <path d="M-60 85 L60 85 L48 42 L-48 42 Z" fill="%s" stroke="%s" stroke-width="2"/>'
        '  <!-- Core Chest Arc Reactor -->'
        '  <circle cx="0" cy="62" r="14" fill="%s" opacity="0.2"/>'
        '  <circle cx="0" cy="62" r="8" fill="%s"/>'
        '  <circle cx="0" cy="62" r="12" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="3 3"/>'
        '  <!-- Robot Neck Servos -->'
        '  <rect x="-14" y="22" width="28" height="20" rx="3" fill="%s" stroke="%s" stroke-width="1.5"/>'
        '  <line x1="-8" y1="26" x2="-8" y2="38" stroke="%s" stroke-width="2"/>'
        '  <line x1="8" y1="26" x2="8" y2="38" stroke="%s" stroke-width="2"/>'
        '  <!-- Robot Head / Helmet -->'
        '  <polygon points="-32,-42 32,-42 42,-8 28,24 -28,24 -42,-8" fill="%s" stroke="%s" stroke-width="2.5"/>'
        '  <!-- Cybernetic Eye Visor (Glowing Cyan) -->'
        '  <polygon points="-26,-14 26,-14 22,-4 -22,-4" fill="%s" filter="drop-shadow(0 0 6px %s)"/>'
        '  <line x1="-24" y1="-9" x2="24" y2="-9" stroke="#FFFFFF" stroke-width="1.2" opacity="0.8"/>'
        '  <!-- Temple Armor & Audio Sensors -->'
        '  <rect x="-47" y="-22" width="6" height="18" rx="2" fill="%s" stroke="%s" stroke-width="1.5"/>'
        '  <rect x="41" y="-22" width="6" height="18" rx="2" fill="%s" stroke="%s" stroke-width="1.5"/>'
        '  <!-- Forehead Sensor Array -->'
        '  <circle cx="0" cy="-30" r="3.5" fill="%s"/>'
        '  <circle cx="-12" cy="-30" r="2" fill="%s"/>'
        '  <circle cx="12" cy="-30" r="2" fill="%s"/>'
        '  <!-- ================= AUTONOMOUS QUADCOPTER DRONE ================= -->'
        '  <g transform="translate(68,-58)">'
        '    <!-- Drone Glow -->'
        '    <circle cx="0" cy="0" r="28" fill="url(#glowC)" opacity="0.8"/>'
        '    <!-- Drone Arms -->'
        '    <line x1="-22" y1="-22" x2="22" y2="22" stroke="%s" stroke-width="2.5"/>'
        '    <line x1="-22" y1="22" x2="22" y2="-22" stroke="%s" stroke-width="2.5"/>'
        '    <!-- Drone Center Fuselage -->'
        '    <rect x="-11" y="-11" width="22" height="22" rx="5" fill="%s" stroke="%s" stroke-width="2"/>'
        '    <circle cx="0" cy="0" r="4.5" fill="%s"/>'
        '    <!-- 4 Rotors -->'
        '    <circle cx="-22" cy="-22" r="9" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="2 2"/>'
        '    <circle cx="22" cy="-22" r="9" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="2 2"/>'
        '    <circle cx="-22" cy="22" r="9" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="2 2"/>'
        '    <circle cx="22" cy="22" r="9" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="2 2"/>'
        '  </g>'
        '</g>'
    ) % (
        cx, cy,
        p["card"], p["border"],
        p["cyan"], p["cyan"], p["purple"],
        p["card"], p["border"], p["cyan"], p["cyan"],
        p["card"], p["purple"],
        p["cyan"], p["cyan"],
        p["border"], p["purple"], p["border"], p["purple"],
        p["purple"], p["cyan"], p["cyan"],
        p["cyan"], p["purple"], p["card"], p["border"], p["green"],
        p["cyan"], p["cyan"], p["purple"], p["purple"]
    )

def hero(theme, b64):
    p = PALETTES[theme]
    W, H = 1200, 420
    TX = 276
    o = io.StringIO()
    o.write('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'fill="none" role="img" aria-label="Mansur Durdimatov Banner">' % (W, H, W, H))
    o.write(defs(p))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#bgfade)"/>' % (W, H))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#grid)" opacity="0.5"/>' % (W, H))
    o.write('<circle cx="1010" cy="60" r="240" fill="url(#glowC)"/>')
    o.write('<circle cx="70" cy="410" r="230" fill="url(#glowP)"/>')
    o.write('<rect x="0.5" y="0.5" width="%d" height="%d" rx="18" fill="none" stroke="%s"/>'
            % (W - 1, H - 1, p["border"]))
    o.write('<rect x="18" y="0" width="%d" height="3" rx="1.5" fill="url(#accent)" opacity="0.9"/>'
            % (W - 36))

    o.write(neon_avatar(146, 208, 92, p, b64))
    o.write(humanoid_and_drone_illustration(1055, 208, p))

    o.write('<text x="%d" y="98" font-family="%s" font-size="17" fill="%s" letter-spacing="1.5">'
            '<tspan fill="%s">$</tspan> whoami<tspan fill="%s">_</tspan></text>'
            % (TX, MONO, p["muted"], p["green"], p["cyan"]))
    o.write('<text x="%d" y="176" font-family="%s" font-size="52" font-weight="800" '
            'fill="url(#accent)" letter-spacing="2">%s</text>' % (TX - 2, SANS, esc(NAME)))
    o.write('<rect x="%d" y="194" width="160" height="5" rx="2.5" fill="url(#accent)"/>' % TX)
    o.write('<text x="%d" y="246" font-family="%s" font-size="21" font-weight="600" fill="%s">%s</text>'
            % (TX, SANS, p["text"], esc(TAGLINE)))
    o.write('<text x="%d" y="282" font-family="%s" font-size="14.5" fill="%s">%s</text>'
            % (TX, SANS, p["muted"], esc(SUBLINE)))

    x = TX
    for label in HERO_CHIPS:
        s, x = chip(x, 326, label, p)
        o.write(s)

    o.write('</svg>')
    return o.getvalue()

def projects(theme):
    p = PALETTES[theme]
    W = 1200
    PAD, COLS = 22, 3
    TW, TH, GX, GY = 374, 94, 16, 14
    HEAD_H, SEC_GAP = 40, 16

    y = 108
    for _, _, items in SECTIONS:
        rows = (len(items) + COLS - 1) // COLS
        y += HEAD_H + rows * (TH + GY) + SEC_GAP
    H = y + 12

    o = io.StringIO()
    o.write('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'fill="none" role="img" aria-label="Mansur Durdimatov Projects">' % (W, H, W, H))
    o.write(defs(p))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#bgfade)"/>' % (W, H))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#grid)" opacity="0.4"/>' % (W, H))
    o.write('<rect x="0.5" y="0.5" width="%d" height="%d" rx="18" fill="none" stroke="%s"/>'
            % (W - 1, H - 1, p["border"]))

    total = sum(len(i) for _, _, i in SECTIONS)
    o.write('<text x="%d" y="54" font-family="%s" font-size="28" font-weight="800" '
            'fill="url(#accent)" letter-spacing="1.5">FEATURED PROJECTS &amp; INNOVATIONS</text>' % (PAD + 12, SANS))
    o.write('<text x="%d" y="80" font-family="%s" font-size="13.5" fill="%s">'
            '%d loyiha &#183; Humanoid Robotics, UAV Drones, AI &amp; Full-Stack</text>'
            % (PAD + 12, MONO, p["dim"], total))
    o.write('<rect x="%d" y="92" width="%d" height="1" fill="%s"/>'
            % (PAD + 12, W - 2 * (PAD + 12), p["border"]))

    y = 108
    for title, acc_key, items in SECTIONS:
        acc = p[acc_key]
        o.write('<rect x="%d" y="%d" width="4" height="16" rx="2" fill="%s"/>'
                % (PAD + 12, y + 8, acc))
        o.write('<text x="%d" y="%d" font-family="%s" font-size="14" font-weight="700" '
                'fill="%s" letter-spacing="1.6">%s</text>'
                % (PAD + 26, y + 21, MONO, acc, esc(title)))
        o.write('<text x="%d" y="%d" font-family="%s" font-size="12" fill="%s">%d</text>'
                % (W - PAD - 24, y + 21, MONO, p["dim"], len(items)))
        y += HEAD_H

        for i, (ic, name, desc, stack) in enumerate(items):
            cx = PAD + (i % COLS) * (TW + GX)
            cy = y + (i // COLS) * (TH + GY)
            o.write('<g>')
            o.write('<rect x="%d" y="%d" width="%d" height="%d" rx="13" fill="%s" stroke="%s"/>'
                    % (cx, cy, TW, TH, p["card"], p["border"]))
            o.write('<rect x="%d" y="%d" width="3.5" height="%d" rx="1.75" fill="%s" opacity="0.85"/>'
                    % (cx, cy + 20, TH - 40, acc))
            o.write('<rect x="%d" y="%d" width="40" height="40" rx="11" fill="%s" opacity="0.13"/>'
                    % (cx + 16, cy + 26, acc))
            o.write(icon(ic, cx + 24, cy + 34, 24, acc, sw=1.9))
            o.write('<text x="%d" y="%d" font-family="%s" font-size="15" font-weight="700" '
                    'fill="%s">%s</text>' % (cx + 68, cy + 36, SANS, p["text"], esc(name)))
            o.write('<text x="%d" y="%d" font-family="%s" font-size="11.5" fill="%s">%s</text>'
                    % (cx + 68, cy + 54, SANS, p["muted"], esc(desc)))
            o.write('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s" '
                    'letter-spacing="0.3">%s</text>'
                    % (cx + 68, cy + 72, MONO, acc, esc(stack)))
            o.write('</g>')

        rows = (len(items) + COLS - 1) // COLS
        y += rows * (TH + GY) + SEC_GAP

    o.write('</svg>')
    return o.getvalue()

def main():
    b64 = avatar_b64()
    files = {
        "dark.svg": hero("dark", b64),
        "light.svg": hero("light", b64),
        "projects-dark.svg": projects("dark"),
        "projects-light.svg": projects("light"),
    }
    for name, content in files.items():
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(content)
        print("  %-20s %6.1f KB" % (name, len(content) / 1024.0))
    print("\nTayyor!")

if __name__ == "__main__":
    main()
