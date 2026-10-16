# -*- coding: utf-8 -*-
"""
Mansur Durdimatov (@durd1ma7ov06) — Cyberpunk Theme-Aware Profile Generator.
Specializing in Frontend & Full-Stack Engineering, Humanoid Bipedal Robotics, and Autonomous Drones.
Generates:
  - dark.svg / light.svg (Hero Banner with Detailed Humanoid Robot & Autonomous Drone)
  - projects-dark.svg / projects-light.svg (Featured Projects Matrix)
"""

import base64
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))

NAME = "MANSUR DURDIMATOV"
TAGLINE = "Frontend & Full-Stack 💻 | Humanoid Robotics & Drone Engineer 🤖 | AI Systems"
SUBLINE = "Engineering bipedal humanoid robotics, autonomous UAV drones & modern reactive web architectures"

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

HERO_CHIPS = [
    "Humanoid Robotics", "ROS 2", "PX4 UAV Drones",
    "Frontend / React", "TypeScript", "Inverse Kinematics",
    "Computer Vision", "C++", "Python"
]

ICONS = {
    "humanoid": '<circle cx="12" cy="4" r="2.5"/><path d="M12 6.5v7M7 9h10M8.5 13.5l-2.5 7.5M15.5 13.5l2.5 7.5M6 9l-2 5M18 9l2 5"/>',
    "drone": '<circle cx="5" cy="5" r="2.8"/><circle cx="19" cy="5" r="2.8"/>'
             '<circle cx="5" cy="19" r="2.8"/><circle cx="19" cy="19" r="2.8"/>'
             '<rect x="9" y="9" width="6" height="6" rx="1.6"/>'
             '<path d="M7 7l2 2M17 7l-2 2M7 17l2-2M17 17l-2-2"/>',
    "bot": '<rect x="4" y="9" width="16" height="12" rx="3"/><circle cx="12" cy="4" r="2"/>'
           '<path d="M12 6v3M8 14h.01M16 14h.01M9 18h6"/>',
    "hands": '<path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v7M10 10.5V6a2 2 0 0 0-4 0v8"/>'
             '<path d="M6 14v1a6 6 0 0 0 6 6h1a6 6 0 0 0 6-6V9a2 2 0 0 0-4 0"/>',
    "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "medkit": '<rect x="2.5" y="7" width="19" height="13" rx="2.5"/>'
              '<path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M12 11v6M9 14h6"/>',
    "sparkles": '<path d="M11 3.2l1.7 4.4 4.4 1.7-4.4 1.7L11 15.4 9.3 11 4.9 9.3 9.3 7.6z"/>'
                '<path d="M18 14.4l.85 2.2 2.2.85-2.2.85-.85 2.2-.85-2.2-2.2-.85 2.2-.85z"/>',
    "school": '<path d="M2.5 8.8 12 4.2l9.5 4.6L12 13.4z"/>'
              '<path d="M6.3 11.2V16c0 1.7 2.6 3 5.7 3s5.7-1.3 5.7-3v-4.8"/>'
              '<path d="M21.5 8.8v5"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6"/>'
             '<path d="M12 3c2.6 2.9 2.6 15.1 0 18M12 3c-2.6 2.9-2.6 15.1 0 18"/>',
    "server": '<rect x="3" y="3.4" width="18" height="6.2" rx="2"/>'
              '<rect x="3" y="14.4" width="18" height="6.2" rx="2"/>'
              '<path d="M6.9 6.5h.02M6.9 17.5h.02M10.5 6.5h4M10.5 17.5h4"/>',
    "code": '<path d="M8.6 7.4 3.4 12l5.2 4.6M15.4 7.4 20.6 12l-5.2 4.6M13.6 4l-3.2 16"/>',
}

SECTIONS = [
    ("HUMANOID ROBOTICS, DRONES & EMBEDDED", "purple", [
        ("humanoid", "Humanoid Bipedal Core", "Muvozanat, yurish & Inverse Kinematics",  "ROS 2 · C++ · Gazebo · IK"),
        ("drone",    "Autonomous Drone UAV",  "LiDAR, to'siqdan qochish & parvoz",       "PX4 · ArduPilot · MAVLink"),
        ("bot",      "Bionic Manipulator",    "6-eksa robot qo'l & servo kinematika",     "ESP32 · C++ · IK Solver"),
        ("hands",    "motion 3D Tracking",    "3D qo'l imo-ishoralarini robotga uzatish", "MediaPipe · Three.js · JS"),
        ("zap",      "Voltguard IoT",         "Aqlli energiya monitoringi & himoya",      "IoT · ESP32 · C++"),
        ("server",   "Teahouse Combinator",   "Aqlli telemetriya & tele-boshqaruv",      "IoT · Node.js · C++"),
    ]),
    ("AI, COMPUTER VISION & PLATFORMS", "cyan", [
        ("school",   "MockLife Platform",     "IELTS & CEFR AI imtihon simulyatori",     "TypeScript · React · Postgres · AWS"),
        ("medkit",   "pnevmoscan AI",         "Pnevmoniya & rentgen AI tashxisi",        "Python · FastAPI · PyTorch"),
        ("sparkles", "Maqola_agent",          "Avtomatlashtirilgan ilmiy maqolalar",     "Python · LLM · AI Agent"),
    ]),
    ("FRONTEND, WEB & CLOUD ECOSYSTEM", "green", [
        ("code",     "MockLife Frontend SPA", "14-bosqichli reaktiv interfeys & Paywall", "React 19 · Vite · Tailwind · TS"),
        ("globe",    "Digital-edu Portal",    "Raqamli texnologiyalar ta'lim platformasi","React · Tailwind · Node.js"),
        ("server",   "Muhtojman Web Tizimi",  "Xayriya va ijtimoiy ko'mak web-platformasi","Full-Stack · JavaScript · DB"),
    ]),
]

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def avatar_b64():
    path = os.path.join(HERE, "avatar.png")
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

def defs(p):
    return (
        '<defs>'
        '  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">'
        '    <stop offset="0%%" stop-color="%s"/>'
        '    <stop offset="50%%" stop-color="%s"/>'
        '    <stop offset="100%%" stop-color="%s"/>'
        '  </linearGradient>'
        '  <linearGradient id="bgfade" x1="0" y1="0" x2="0" y2="1">'
        '    <stop offset="0%%" stop-color="%s"/>'
        '    <stop offset="100%%" stop-color="%s"/>'
        '  </linearGradient>'
        '  <linearGradient id="laserBeam" x1="0" y1="0" x2="0" y2="1">'
        '    <stop offset="0%%" stop-color="%s" stop-opacity="0.8"/>'
        '    <stop offset="100%%" stop-color="%s" stop-opacity="0.0"/>'
        '  </linearGradient>'
        '  <radialGradient id="glowC" cx="50%%" cy="50%%" r="50%%">'
        '    <stop offset="0%%" stop-color="%s" stop-opacity="0.32"/>'
        '    <stop offset="100%%" stop-color="%s" stop-opacity="0"/>'
        '  </radialGradient>'
        '  <radialGradient id="glowP" cx="50%%" cy="50%%" r="50%%">'
        '    <stop offset="0%%" stop-color="%s" stop-opacity="0.32"/>'
        '    <stop offset="100%%" stop-color="%s" stop-opacity="0"/>'
        '  </radialGradient>'
        '  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">'
        '    <path d="M 28 0 L 0 0 0 28" fill="none" stroke="%s" stroke-width="0.8"/>'
        '  </pattern>'
        '</defs>'
    ) % (
        p["cyan"], p["purple"], p["green"],
        p["bg"], p["card"],
        p["cyan"], p["cyan"],
        p["cyan"], p["cyan"],
        p["purple"], p["purple"],
        p["grid"]
    )

def neon_avatar(cx, cy, r, p, b64):
    d = r * 2
    o = [
        '<defs>',
        '  <clipPath id="avatarClip"><circle cx="%d" cy="%d" r="%d"/></clipPath>' % (cx, cy, r),
        '</defs>',
        '<g>',
        '  <circle cx="%d" cy="%d" r="%d" fill="url(#glowC)"/>' % (cx, cy, r + 45),
        '  <circle cx="%d" cy="%d" r="%d" fill="url(#glowP)"/>' % (cx, cy, r + 25),
        '  <circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 6" opacity="0.6"/>'
        % (cx, cy, r + 14, p["cyan"]),
        '  <circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="2.2" opacity="0.85"/>'
        % (cx, cy, r + 6, p["purple"])
    ]
    if b64:
        o.append('  <image href="data:image/png;base64,%s" x="%d" y="%d" width="%d" height="%d" '
                 'clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>'
                 % (b64, cx - r, cy - r, d, d))
    else:
        o.append('  <circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (cx, cy, r, p["card"]))
    o.append('  <circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="3" opacity="0.95"/>'
             % (cx, cy, r, p["cyan"]))
    o.append('</g>')
    return "".join(o)

def full_humanoid_and_drone_illustration(cx, cy, p):
    """
    State-of-the-art vector illustration featuring:
    1. Full-body bipedal Cybernetic Humanoid Robot with glowing visor, armor plates, chest arc reactor, and hydraulic limbs.
    2. Autonomous Quadcopter UAV Drone hovering above with spinning rotors and downward LiDAR scan beam.
    3. Futuristic HUD telemetry readouts.
    """
    return (
        '<g transform="translate(%d,%d)">'
        '  <!-- Background Power Radiance -->'
        '  <circle cx="0" cy="10" r="140" fill="url(#glowP)" opacity="0.85"/>'
        '  <circle cx="0" cy="-60" r="110" fill="url(#glowC)" opacity="0.75"/>'
        ''
        '  <!-- ================= AUTONOMOUS QUADCOPTER DRONE ================= -->'
        '  <g transform="translate(62,-120)">'
        '    <!-- Laser Scanner Conical Beam -->'
        '    <polygon points="0,0 -45,150 45,150" fill="url(#laserBeam)" opacity="0.35"/>'
        '    <!-- Drone Arms -->'
        '    <line x1="-28" y1="-14" x2="28" y2="14" stroke="%s" stroke-width="3"/>'
        '    <line x1="-28" y1="14" x2="28" y2="-14" stroke="%s" stroke-width="3"/>'
        '    <!-- Rotor Blades (Spinning Effect) -->'
        '    <ellipse cx="-28" cy="-14" rx="14" ry="5" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>'
        '    <ellipse cx="28" cy="14" rx="14" ry="5" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>'
        '    <ellipse cx="-28" cy="14" rx="14" ry="5" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>'
        '    <ellipse cx="28" cy="-14" rx="14" ry="5" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>'
        '    <!-- Drone Body Fuselage -->'
        '    <rect x="-14" y="-12" width="28" height="24" rx="6" fill="%s" stroke="%s" stroke-width="2.2"/>'
        '    <!-- Camera Gimbal & Navigation LEDs -->'
        '    <circle cx="0" cy="0" r="5" fill="%s"/>'
        '    <circle cx="-28" cy="-14" r="2.5" fill="%s"/>'
        '    <circle cx="28" cy="14" r="2.5" fill="%s"/>'
        '    <!-- Drone Label -->'
        '    <text x="0" y="-24" font-family="%s" font-size="9" fill="%s" text-anchor="middle" letter-spacing="1">UAV DRONE · PX4</text>'
        '  </g>'
        ''
        '  <!-- ================= FULL HUMANOID BIPEDAL ROBOT ================= -->'
        '  <g transform="translate(-15,-10)">'
        '    <!-- Humanoid Bipedal Legs -->'
        '    <!-- Left Leg: Thigh, Knee joint, Shin, Foot -->'
        '    <path d="M-22 55 L-30 100 L-26 142 L-40 148 L-16 148 L-18 100 L-14 55 Z" fill="%s" stroke="%s" stroke-width="2"/>'
        '    <circle cx="-28" cy="100" r="5" fill="%s" stroke="%s" stroke-width="1.5"/>'
        '    <!-- Right Leg: Thigh, Knee joint, Shin, Foot -->'
        '    <path d="M14 55 L22 100 L18 142 L6 148 L30 148 L26 100 L22 55 Z" fill="%s" stroke="%s" stroke-width="2"/>'
        '    <circle cx="24" cy="100" r="5" fill="%s" stroke="%s" stroke-width="1.5"/>'
        ''
        '    <!-- Pelvis & Hip Actuators -->'
        '    <polygon points="-28,45 28,45 20,62 -20,62" fill="%s" stroke="%s" stroke-width="2"/>'
        '    <circle cx="-16" cy="52" r="3.5" fill="%s"/>'
        '    <circle cx="16" cy="52" r="3.5" fill="%s"/>'
        ''
        '    <!-- Torso Chassis & Cyber Armor -->'
        '    <path d="M-42 -10 L42 -10 L28 45 L-28 45 Z" fill="%s" stroke="%s" stroke-width="2.5"/>'
        ''
        '    <!-- Chest Arc Reactor Core (Glowing Cyan Pulsar) -->'
        '    <circle cx="0" cy="12" r="16" fill="%s" opacity="0.25"/>'
        '    <circle cx="0" cy="12" r="9" fill="%s"/>'
        '    <circle cx="0" cy="12" r="13" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="4 2"/>'
        '    <line x1="-30" y1="2" x2="-8" y2="2" stroke="%s" stroke-width="1.5"/>'
        '    <line x1="8" y1="2" x2="30" y2="2" stroke="%s" stroke-width="1.5"/>'
        ''
        '    <!-- Bionic Arms & Shoulder Pauldrons -->'
        '    <!-- Left Shoulder & Arm -->'
        '    <circle cx="-48" cy="-6" r="10" fill="%s" stroke="%s" stroke-width="2"/>'
        '    <path d="M-52 4 L-58 45 L-52 78 L-58 88" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
        '    <circle cx="-58" cy="45" r="4.5" fill="%s"/>'
        '    <path d="M-58 88 L-63 94 M-58 88 L-58 96 M-58 88 L-53 94" stroke="%s" stroke-width="1.8"/>'
        ''
        '    <!-- Right Shoulder & Arm -->'
        '    <circle cx="48" cy="-6" r="10" fill="%s" stroke="%s" stroke-width="2"/>'
        '    <path d="M52 4 L58 45 L52 78 L58 88" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
        '    <circle cx="58" cy="45" r="4.5" fill="%s"/>'
        '    <path d="M58 88 L63 94 M58 88 L58 96 M58 88 L53 94" stroke="%s" stroke-width="1.8"/>'
        ''
        '    <!-- Neck & Hydraulic Actuators -->'
        '    <rect x="-12" y="-24" width="24" height="15" rx="3" fill="%s" stroke="%s" stroke-width="1.8"/>'
        '    <line x1="-6" y1="-22" x2="-6" y2="-11" stroke="%s" stroke-width="2"/>'
        '    <line x1="6" y1="-22" x2="6" y2="-11" stroke="%s" stroke-width="2"/>'
        ''
        '    <!-- Cybernetic Humanoid Helmet Head -->'
        '    <polygon points="-26,-72 26,-72 35,-42 22,-22 -22,-22 -35,-42" fill="%s" stroke="%s" stroke-width="2.5"/>'
        '    <!-- Glowing Cyan Optical Visor HUD -->'
        '    <polygon points="-22,-52 22,-52 18,-42 -18,-42" fill="%s"/>'
        '    <line x1="-20" y1="-47" x2="20" y2="-47" stroke="#FFFFFF" stroke-width="1.4" opacity="0.85"/>'
        '    <!-- Forehead AI Sensor Array -->'
        '    <circle cx="0" cy="-62" r="3" fill="%s"/>'
        '    <circle cx="-10" cy="-62" r="1.8" fill="%s"/>'
        '    <circle cx="10" cy="-62" r="1.8" fill="%s"/>'
        '    <!-- Antenna / Communication Fin -->'
        '    <line x1="-28" y1="-58" x2="-36" y2="-76" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>'
        '    <circle cx="-36" cy="-76" r="2.5" fill="%s"/>'
        '  </g>'
        ''
        '  <!-- ================= HUD TELEMETRY LABELS ================= -->'
        '  <g transform="translate(-15,164)">'
        '    <rect x="-85" y="-12" width="170" height="20" rx="5" fill="%s" stroke="%s" stroke-width="1.2"/>'
        '    <text x="0" y="2" font-family="%s" font-size="9.5" font-weight="700" fill="%s" text-anchor="middle" letter-spacing="1.2">HUMANOID BIPEDAL · ROS 2</text>'
        '  </g>'
        '</g>'
    ) % (
        cx, cy,
        p["cyan"], p["purple"],
        p["cyan"], p["cyan"], p["purple"], p["purple"],
        p["card"], p["border"],
        p["green"], p["red"], p["green"],
        MONO, p["cyan"],
        # Humanoid legs
        p["card"], p["border"], p["cyan"], p["purple"],
        p["card"], p["border"], p["cyan"], p["purple"],
        # Pelvis
        p["card"], p["border"], p["cyan"], p["cyan"],
        # Torso
        p["card"], p["purple"],
        # Arc reactor
        p["cyan"], p["cyan"], p["purple"], p["border"], p["border"],
        # Arms
        p["card"], p["cyan"], p["border"], p["cyan"], p["cyan"],
        p["card"], p["purple"], p["border"], p["purple"], p["cyan"],
        # Neck
        p["card"], p["border"], p["cyan"], p["cyan"],
        # Head
        p["card"], p["purple"],
        p["cyan"],
        p["cyan"], p["purple"], p["purple"],
        p["cyan"], p["cyan"],
        # HUD bottom
        p["chip_bg"], p["cyan"], MONO, p["cyan"]
    )

def chip(x, y, text, p):
    w = int(len(text) * 7.5 + 24)
    s = (
        '<g transform="translate(%d,%d)">'
        '  <rect width="%d" height="28" rx="7" fill="%s" stroke="%s" stroke-width="1"/>'
        '  <text x="%d" y="18" font-family="%s" font-size="12" font-weight="600" fill="%s" text-anchor="middle">%s</text>'
        '</g>'
    ) % (x, y, w, p["chip_bg"], p["border"], w // 2, SANS, p["chip_text"], esc(text))
    return s, x + w + 10

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
    o.write('<circle cx="1020" cy="80" r="260" fill="url(#glowC)"/>')
    o.write('<circle cx="70" cy="410" r="230" fill="url(#glowP)"/>')
    o.write('<rect x="0.5" y="0.5" width="%d" height="%d" rx="18" fill="none" stroke="%s"/>'
            % (W - 1, H - 1, p["border"]))
    o.write('<rect x="18" y="0" width="%d" height="3" rx="1.5" fill="url(#accent)" opacity="0.9"/>'
            % (W - 36))

    o.write(neon_avatar(146, 208, 92, p, b64))
    o.write(full_humanoid_and_drone_illustration(1060, 205, p))

    o.write('<text x="%d" y="94" font-family="%s" font-size="16" fill="%s" letter-spacing="1.5">'
            '<tspan fill="%s">$</tspan> whoami<tspan fill="%s">_</tspan></text>'
            % (TX, MONO, p["muted"], p["green"], p["cyan"]))
    o.write('<text x="%d" y="168" font-family="%s" font-size="50" font-weight="800" '
            'fill="url(#accent)" letter-spacing="2">%s</text>' % (TX - 2, SANS, esc(NAME)))
    o.write('<rect x="%d" y="186" width="180" height="5" rx="2.5" fill="url(#accent)"/>' % TX)
    o.write('<text x="%d" y="238" font-family="%s" font-size="20.5" font-weight="600" fill="%s">%s</text>'
            % (TX, SANS, p["text"], esc(TAGLINE)))
    o.write('<text x="%d" y="274" font-family="%s" font-size="14.5" fill="%s">%s</text>'
            % (TX, SANS, p["muted"], esc(SUBLINE)))

    x = TX
    for label in HERO_CHIPS:
        s, x = chip(x, 320, label, p)
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
    o.write('<rect x="18" y="0" width="%d" height="3" rx="1.5" fill="url(#accent)" opacity="0.9"/>'
            % (W - 36))

    o.write('<text x="%d" y="52" font-family="%s" font-size="13" font-weight="700" fill="%s" letter-spacing="2">'
            'PROJECT PORTFOLIO // HARDWARE, ROBOTICS &amp; MODERN WEB</text>' % (PAD, MONO, p["cyan"]))
    o.write('<text x="%d" y="86" font-family="%s" font-size="28" font-weight="800" fill="%s">'
            'Featured Systems &amp; Deployments</text>' % (PAD, SANS, p["text"]))

    cur_y = 124
    for title, colorkey, items in SECTIONS:
        c = p[colorkey]
        o.write('<g transform="translate(%d,%d)">' % (PAD, cur_y))
        o.write('  <circle cx="6" cy="7" r="5" fill="%s"/>' % c)
        o.write('  <text x="20" y="12" font-family="%s" font-size="13" font-weight="700" fill="%s" letter-spacing="1.5">%s</text>'
                % (MONO, c, esc(title)))
        o.write('</g>')
        cur_y += HEAD_H

        for idx, (icon_name, name, desc, tech) in enumerate(items):
            r = idx // COLS
            c_idx = idx % COLS
            bx = PAD + c_idx * (TW + GX)
            by = cur_y + r * (TH + GY)

            o.write('<g transform="translate(%d,%d)">' % (bx, by))
            o.write('  <rect width="%d" height="%d" rx="12" fill="%s" stroke="%s" stroke-width="1.2"/>'
                    % (TW, TH, p["card"], p["border"]))
            o.write('  <rect x="0" y="0" width="4" height="%d" rx="2" fill="%s"/>' % (TH, c))
            o.write('  <g transform="translate(18,18)">')
            o.write('    <rect width="36" height="36" rx="8" fill="%s"/>' % p["chip_bg"])
            o.write('    <g transform="translate(6,6)" stroke="%s" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">'
                    % c)
            o.write(ICONS.get(icon_name, ICONS["sparkles"]))
            o.write('    </g>')
            o.write('  </g>')
            o.write('  <text x="66" y="32" font-family="%s" font-size="15" font-weight="700" fill="%s">%s</text>'
                    % (SANS, p["text"], esc(name)))
            o.write('  <text x="66" y="52" font-family="%s" font-size="12" fill="%s">%s</text>'
                    % (SANS, p["muted"], esc(desc)))
            o.write('  <text x="66" y="74" font-family="%s" font-size="11" font-weight="600" fill="%s">%s</text>'
                    % (MONO, c, esc(tech)))
            o.write('</g>')

        rows = (len(items) + COLS - 1) // COLS
        cur_y += rows * (TH + GY) + SEC_GAP

    o.write('</svg>')
    return o.getvalue()

def main():
    b64 = avatar_b64()
    for theme in ("dark", "light"):
        content = hero(theme, b64)
        out = os.path.join(HERE, "%s.svg" % theme)
        with open(out, "w", encoding="utf-8") as f:
            f.write(content)
        print("Wrote %s (%d bytes)" % (out, len(content)))

        p_content = projects(theme)
        p_out = os.path.join(HERE, "projects-%s.svg" % theme)
        with open(p_out, "w", encoding="utf-8") as f:
            f.write(p_content)
        print("Wrote %s (%d bytes)" % (p_out, len(p_content)))

if __name__ == "__main__":
    main()
