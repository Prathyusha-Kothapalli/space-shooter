"""
Local Web Server for Starlight Vanguard Space Shooter.
Serves a complete HTML5 Canvas 2D Space Shooter Web Application,
interactive dashboard, sector map viewer, and telemetry API at http://localhost:8000.
"""

import http.server
import socketserver
import json
import os
import sys
from typing import Dict, Any

PORT = 8000

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Starlight Vanguard - 2D Space Shooter</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: #0a0c14;
            color: #f5f5fa;
            font-family: 'Outfit', sans-serif;
            overflow: hidden;
            display: flex;
            height: 100vh;
            width: 100vw;
        }
        #sidebar {
            width: 320px;
            background: rgba(15, 20, 30, 0.85);
            backdrop-filter: blur(12px);
            border-right: 1px solid rgba(0, 230, 255, 0.2);
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            z-index: 10;
        }
        h1 {
            font-size: 22px;
            font-weight: 800;
            background: linear-gradient(135deg, #00e6ff, #1e90ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 1px;
        }
        .subtitle { font-size: 12px; color: #646e7d; font-family: 'JetBrains Mono', monospace; }
        .card {
            background: rgba(30, 35, 45, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 16px;
        }
        .card h3 { font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #00e6ff; margin-bottom: 12px; }
        .stat-row { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px; }
        .stat-val { font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ffd700; }
        .weapon-pill {
            display: flex; align-items: center; justify-content: space-between;
            padding: 8px 12px; border-radius: 8px; background: rgba(0, 0, 0, 0.3);
            margin-bottom: 6px; font-size: 12px; cursor: pointer; transition: all 0.2s;
            border: 1px solid transparent;
        }
        .weapon-pill.active { border-color: #00e6ff; background: rgba(0, 230, 255, 0.15); }
        #canvas-container {
            flex: 1;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle at center, #101424 0%, #05060a 100%);
        }
        canvas {
            border-radius: 8px;
            box-shadow: 0 0 40px rgba(0, 230, 255, 0.15);
            background: #0a0c14;
        }
        #controls-overlay {
            position: absolute;
            bottom: 20px;
            right: 20px;
            background: rgba(15, 20, 30, 0.7);
            backdrop-filter: blur(8px);
            padding: 12px 18px;
            border-radius: 8px;
            font-size: 12px;
            color: #b4c8dc;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        kbd {
            background: rgba(255, 255, 255, 0.15);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
            color: #00e6ff;
        }
    </style>
</head>
<body>
    <div id="sidebar">
        <div>
            <h1>STARLIGHT VANGUARD</h1>
            <div class="subtitle">2D SPACE SHOOTER ENGINE</div>
        </div>

        <div class="card">
            <h3>Mission Status</h3>
            <div class="stat-row"><span>SCORE</span><span class="stat-val" id="hud-score">0</span></div>
            <div class="stat-row"><span>HIGH SCORE</span><span class="stat-val" id="hud-highscore">100,000</span></div>
            <div class="stat-row"><span>WAVE</span><span class="stat-val" id="hud-wave">1</span></div>
            <div class="stat-row"><span>COMBO</span><span class="stat-val" id="hud-combo">1.0x</span></div>
            <div class="stat-row"><span>LIVES</span><span class="stat-val" id="hud-lives">3</span></div>
        </div>

        <div class="card">
            <h3>Weapon Arsenal</h3>
            <div class="weapon-pill active" id="wpn-0"><span>1. Pulse Cannon</span><span>[Lvl 1]</span></div>
            <div class="weapon-pill" id="wpn-1"><span>2. Spread Shot</span><span>[Lvl 1]</span></div>
            <div class="weapon-pill" id="wpn-2"><span>3. Heavy Plasma</span><span>[Lvl 1]</span></div>
            <div class="weapon-pill" id="wpn-3"><span>4. Homing Missiles</span><span>[Lvl 1]</span></div>
            <div class="weapon-pill" id="wpn-4"><span>5. Quantum Railgun</span><span>[Lvl 1]</span></div>
            <div class="weapon-pill" id="wpn-5"><span>6. Beam Cannon</span><span>[Lvl 1]</span></div>
        </div>

        <div class="card">
            <h3>Telemetry</h3>
            <div class="stat-row"><span>FPS</span><span class="stat-val" id="hud-fps">60</span></div>
            <div class="stat-row"><span>ACTIVE ENTITIES</span><span class="stat-val" id="hud-entities">0</span></div>
            <div class="stat-row"><span>SYSTEM</span><span class="stat-val" style="color:#50cd50;">ONLINE</span></div>
        </div>
    </div>

    <div id="canvas-container">
        <canvas id="gameCanvas" width="960" height="640"></canvas>
        <div id="controls-overlay">
            Controls: <kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> Move | <kbd>SPACE</kbd> Fire | <kbd>1</kbd>-<kbd>6</kbd> Switch Weapon
        </div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        // Game State Engine
        let score = 0;
        let highScore = 100000;
        let wave = 1;
        let combo = 1.0;
        let comboStreak = 0;
        let activeWeaponIndex = 0;
        let fps = 60;
        let frameCount = 0;
        let lastTime = performance.now();

        const player = {
            x: canvas.width / 2,
            y: canvas.height - 80,
            speed: 6,
            radius: 18,
            health: 100,
            maxHealth: 100,
            shield: 100,
            maxShield: 100,
            lives: 3
        };

        const keys = {};
        window.addEventListener('keydown', e => {
            keys[e.code] = true;
            if (e.code.startsWith('Digit')) {
                const num = parseInt(e.code.replace('Digit', '')) - 1;
                if (num >= 0 && num < 6) selectWeapon(num);
            }
        });
        window.addEventListener('keyup', e => keys[e.code] = false);

        function selectWeapon(index) {
            activeWeaponIndex = index;
            document.querySelectorAll('.weapon-pill').forEach((el, i) => {
                if (i === index) el.classList.add('active');
                else el.classList.remove('active');
            });
        }

        // Entities Arrays
        const projectiles = [];
        const enemies = [];
        const particles = [];
        const stars = [];

        // Init Starfield
        for (let i = 0; i < 100; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                speed: 1 + Math.random() * 3,
                size: Math.random() * 2,
                color: ['#00e6ff', '#1e90ff', '#ffffff'][Math.floor(Math.random() * 3)]
            });
        }

        let fireCooldown = 0;
        let enemySpawnTimer = 0;

        function spawnEnemy() {
            const types = ['SCOUT', 'INTERCEPTOR', 'CRUISER', 'BOMBER', 'STEALTH'];
            const type = types[Math.floor(Math.random() * types.length)];
            enemies.push({
                x: 40 + Math.random() * (canvas.width - 80),
                y: -30,
                type: type,
                speed: 1.5 + Math.random() * 2,
                radius: type === 'CRUISER' ? 26 : (type === 'BOMBER' ? 22 : 16),
                health: type === 'CRUISER' ? 80 : 30,
                maxHealth: type === 'CRUISER' ? 80 : 30,
                color: type === 'SCOUT' ? '#ff3232' : (type === 'INTERCEPTOR' ? '#ff8c00' : (type === 'CRUISER' ? '#9b59b6' : '#32cd32'))
            });
        }

        function createExplosion(x, y, color) {
            for (let i = 0; i < 20; i++) {
                const angle = Math.random() * Math.PI * 2;
                const speed = 1 + Math.random() * 5;
                particles.push({
                    x: x, y: y,
                    vx: Math.cos(angle) * speed,
                    vy: Math.sin(angle) * speed,
                    life: 1.0,
                    color: color,
                    size: 2 + Math.random() * 4
                });
            }
        }

        function fireWeapon() {
            if (activeWeaponIndex === 0) {
                // Pulse Cannon
                projectiles.push({ x: player.x, y: player.y - 20, vy: -12, radius: 5, color: '#00e6ff', damage: 20 });
            } else if (activeWeaponIndex === 1) {
                // Spread Shot
                projectiles.push({ x: player.x, y: player.y - 20, vx: -3, vy: -10, radius: 4, color: '#ffd700', damage: 14 });
                projectiles.push({ x: player.x, y: player.y - 20, vx: 0, vy: -10, radius: 4, color: '#ffd700', damage: 14 });
                projectiles.push({ x: player.x, y: player.y - 20, vx: 3, vy: -10, radius: 4, color: '#ffd700', damage: 14 });
            } else if (activeWeaponIndex === 2) {
                // Heavy Plasma
                projectiles.push({ x: player.x, y: player.y - 20, vy: -7, radius: 12, color: '#ff0080', damage: 60 });
            } else if (activeWeaponIndex === 3) {
                // Homing Missiles
                projectiles.push({ x: player.x - 10, y: player.y, vx: -2, vy: -8, radius: 6, color: '#ff8c00', damage: 30 });
                projectiles.push({ x: player.x + 10, y: player.y, vx: 2, vy: -8, radius: 6, color: '#ff8c00', damage: 30 });
            } else if (activeWeaponIndex === 4) {
                // Quantum Railgun
                projectiles.push({ x: player.x, y: player.y - 20, vy: -24, radius: 3, color: '#b464ff', damage: 90 });
            } else if (activeWeaponIndex === 5) {
                // Beam Cannon
                projectiles.push({ x: player.x, y: player.y - 20, vy: -18, radius: 8, color: '#32cd32', damage: 15 });
            }
        }

        function update() {
            // Player Movement
            if (keys['KeyW'] || keys['ArrowUp']) player.y = Math.max(30, player.y - player.speed);
            if (keys['KeyS'] || keys['ArrowDown']) player.y = Math.min(canvas.height - 30, player.y + player.speed);
            if (keys['KeyA'] || keys['ArrowLeft']) player.x = Math.max(30, player.x - player.speed);
            if (keys['KeyD'] || keys['ArrowRight']) player.x = Math.min(canvas.width - 30, player.x + player.speed);

            // Firing
            if (fireCooldown > 0) fireCooldown--;
            if (keys['Space'] && fireCooldown <= 0) {
                fireWeapon();
                fireCooldown = activeWeaponIndex === 0 ? 8 : (activeWeaponIndex === 2 ? 22 : 14);
            }

            // Starfield
            stars.forEach(star => {
                star.y += star.speed;
                if (star.y > canvas.height) { star.y = 0; star.x = Math.random() * canvas.width; }
            });

            // Projectiles
            for (let i = projectiles.length - 1; i >= 0; i--) {
                const p = projectiles[i];
                p.x += (p.vx || 0);
                p.y += p.vy;
                if (p.y < -20 || p.x < 0 || p.x > canvas.width) projectiles.splice(i, 1);
            }

            // Enemies Spawn
            enemySpawnTimer++;
            if (enemySpawnTimer > 45) {
                spawnEnemy();
                enemySpawnTimer = 0;
            }

            // Enemies update & collisions
            for (let i = enemies.length - 1; i >= 0; i--) {
                const e = enemies[i];
                e.y += e.speed;

                // Collision with player projectiles
                for (let j = projectiles.length - 1; j >= 0; j--) {
                    const p = projectiles[j];
                    const dist = Math.hypot(e.x - p.x, e.y - p.y);
                    if (dist < e.radius + p.radius) {
                        e.health -= p.damage;
                        projectiles.splice(j, 1);
                        createExplosion(p.x, p.y, p.color);

                        if (e.health <= 0) {
                            createExplosion(e.x, e.y, e.color);
                            score += e.maxHealth * 10;
                            comboStreak++;
                            combo = Math.min(5.0, 1.0 + Math.floor(comboStreak / 5) * 0.5);
                            if (score > highScore) highScore = score;
                            enemies.splice(i, 1);
                            break;
                        }
                    }
                }

                if (e.y > canvas.height + 40) enemies.splice(i, 1);
            }

            // Particles
            for (let i = particles.length - 1; i >= 0; i--) {
                const pt = particles[i];
                pt.x += pt.vx;
                pt.y += pt.vy;
                pt.life -= 0.03;
                if (pt.life <= 0) particles.splice(i, 1);
            }

            // Update UI Stats
            document.getElementById('hud-score').innerText = score.toLocaleString();
            document.getElementById('hud-highscore').innerText = highScore.toLocaleString();
            document.getElementById('hud-wave').innerText = wave;
            document.getElementById('hud-combo').innerText = combo.toFixed(1) + 'x';
            document.getElementById('hud-lives').innerText = player.lives;
            document.getElementById('hud-entities').innerText = projectiles.length + enemies.length + particles.length;

            // FPS Counter
            frameCount++;
            const now = performance.now();
            if (now - lastTime >= 1000) {
                fps = frameCount;
                frameCount = 0;
                lastTime = now;
                document.getElementById('hud-fps').innerText = fps;
            }
        }

        function render() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw Stars
            stars.forEach(s => {
                ctx.fillStyle = s.color;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
                ctx.fill();
            });

            // Draw Player Ship
            ctx.fillStyle = '#00e6ff';
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(player.x, player.y - 20);
            ctx.lineTo(player.x - 18, player.y + 15);
            ctx.lineTo(player.x + 18, player.y + 15);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();

            // Player Shield Ring
            ctx.strokeStyle = 'rgba(0, 230, 255, 0.4)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(player.x, player.y, 26, 0, Math.PI * 2);
            ctx.stroke();

            // Draw Projectiles
            projectiles.forEach(p => {
                ctx.fillStyle = p.color;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fill();
            });

            // Draw Enemies
            enemies.forEach(e => {
                ctx.fillStyle = e.color;
                ctx.beginPath();
                ctx.arc(e.x, e.y, e.radius, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#ffffff';
                ctx.stroke();
            });

            // Draw Particles
            particles.forEach(pt => {
                ctx.fillStyle = pt.color;
                ctx.globalAlpha = pt.life;
                ctx.beginPath();
                ctx.arc(pt.x, pt.y, pt.size * pt.life, 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 1.0;
            });
        }

        function gameLoop() {
            update();
            render();
            requestAnimationFrame(gameLoop);
        }

        gameLoop();
    </script>
</body>
</html>
"""

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "ONLINE", "game": "Starlight Vanguard", "port": PORT}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            super().do_GET()

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"[Server] Starlight Vanguard Web Server running at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()
