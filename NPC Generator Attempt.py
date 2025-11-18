<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>D&D 5e NPC Generator</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-grad-start: #020617;
      --bg-grad-end: #0f172a;
      --accent: #38bdf8;
      --accent-soft: rgba(56, 189, 248, 0.1);
      --accent-strong: rgba(56, 189, 248, 0.35);
      --accent-alt: #a855f7;
      --border-subtle: rgba(148, 163, 184, 0.3);
      --card-bg: rgba(15, 23, 42, 0.92);
      --text-main: #e5e7eb;
      --text-muted: #94a3b8;
      --danger: #fb7185;
      --shadow-soft: 0 24px 60px rgba(15, 23, 42, 0.9);
      --radius-lg: 24px;
      --radius-md: 18px;
      --radius-sm: 12px;
      --transition-fast: 150ms ease-out;
      --transition-med: 220ms ease-out;
    }

    * {
      box-sizing: border-box;
    }

    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
    }

    body {
      font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: radial-gradient(circle at top left, #1e293b 0, transparent 45%),
                  radial-gradient(circle at bottom right, #0f172a 0, transparent 50%),
                  linear-gradient(135deg, var(--bg-grad-start), var(--bg-grad-end));
      color: var(--text-main);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
    }

    .app-shell {
      width: 100%;
      max-width: 1080px;
      background: radial-gradient(ellipse at top, rgba(56,189,248,0.06), transparent 55%),
                  radial-gradient(ellipse at bottom, rgba(168,85,247,0.07), transparent 55%),
                  var(--card-bg);
      border-radius: 28px;
      box-shadow: var(--shadow-soft);
      border: 1px solid rgba(148, 163, 184, 0.35);
      padding: 22px 22px 20px;
      position: relative;
      overflow: hidden;
    }

    .app-shell::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(120deg, rgba(248,250,252,0.06), transparent 60%),
        linear-gradient(300deg, rgba(15,118,110,0.18), transparent 55%);
      mix-blend-mode: soft-light;
      opacity: 0.6;
      pointer-events: none;
    }

    .app-inner {
      position: relative;
      z-index: 1;
    }

    .app-header {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      padding-bottom: 18px;
      border-bottom: 1px solid rgba(148, 163, 184, 0.35);
    }

    .title-block {
      flex: 1 1 240px;
      min-width: 0;
    }

    .app-title {
      margin: 0 0 4px;
      font-family: "Cinzel", "Times New Roman", serif;
      font-weight: 700;
      letter-spacing: 0.06em;
      font-size: 1.6rem;
      text-transform: uppercase;
      color: #e5e7eb;
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }

    .title-pill {
      font-family: inherit;
      font-size: 0.7rem;
      padding: 3px 10px;
      border-radius: 999px;
      border: 1px solid rgba(248, 250, 252, 0.2);
      background: radial-gradient(circle at top left, rgba(251, 191, 36, 0.35), rgba(30, 64, 175, 0.6));
      color: #fefce8;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      white-space: nowrap;
    }

    .app-subtitle {
      margin: 0;
      font-size: 0.9rem;
      color: var(--text-muted);
      max-width: 460px;
    }

    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: flex-end;
      justify-content: flex-end;
    }

    .field {
      display: flex;
      flex-direction: column;
      gap: 4px;
      min-width: 140px;
    }

    .field label {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: #9ca3af;
      font-weight: 600;
    }

    select {
      -webkit-appearance: none;
      appearance: none;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.6);
      padding: 7px 26px 7px 12px;
      font-size: 0.82rem;
      font-weight: 500;
      background:
        radial-gradient(circle at top left, rgba(148, 163, 184, 0.28), transparent 55%),
        rgba(15, 23, 42, 0.85);
      color: var(--text-main);
      outline: none;
      position: relative;
      cursor: pointer;
      transition: border-color var(--transition-fast), box-shadow var(--transition-fast), background var(--transition-fast), transform var(--transition-fast);
    }

    select:focus-visible {
      outline: 2px solid transparent;
      box-shadow: 0 0 0 1px rgba(15,23,42,0.9), 0 0 0 2px rgba(59, 130, 246, 0.85);
    }

    select:focus,
    select:hover {
      border-color: rgba(148, 163, 184, 0.95);
      box-shadow: 0 0 0 1px rgba(30, 64, 175, 0.75);
      background:
        radial-gradient(circle at top left, rgba(129, 140, 248, 0.6), transparent 55%),
        rgba(15, 23, 42, 0.92);
      transform: translateY(-0.5px);
    }

    .select-wrap {
      position: relative;
    }

    .select-wrap::after {
      content: "▾";
      position: absolute;
      right: 11px;
      top: 50%;
      transform: translateY(-52%);
      font-size: 0.62rem;
      color: #9ca3af;
      pointer-events: none;
    }

    button {
      font: inherit;
    }

    .btn-primary {
      border-radius: 999px;
      border: 1px solid transparent;
      padding: 8px 18px;
      font-size: 0.86rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: #0b1120;
      background: radial-gradient(circle at top left, #bef264, transparent 40%),
                  linear-gradient(135deg, #22c55e, #22d3ee);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 14px 30px rgba(45, 212, 191, 0.55);
      transition: transform var(--transition-fast), box-shadow var(--transition-fast), filter var(--transition-fast);
      white-space: nowrap;
    }

    .btn-primary span.icon {
      font-size: 0.8rem;
      opacity: 0.9;
    }

    .btn-primary:hover {
      transform: translateY(-1px) translateZ(0);
      box-shadow: 0 20px 45px rgba(34, 211, 238, 0.7);
      filter: brightness(1.03);
    }

    .btn-primary:active {
      transform: translateY(0);
      box-shadow: 0 10px 22px rgba(15, 23, 42, 0.9);
      filter: brightness(0.98);
    }

    .btn-secondary {
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.9);
      padding: 7px 14px;
      font-size: 0.78rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--text-main);
      background: radial-gradient(circle at top left, rgba(148, 163, 184, 0.3), transparent 55%),
                  rgba(15, 23, 42, 0.92);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 10px 22px rgba(15, 23, 42, 0.78);
      transition: background var(--transition-fast), box-shadow var(--transition-fast), transform var(--transition-fast), border-color var(--transition-fast), color var(--transition-fast);
      white-space: nowrap;
    }

    .btn-secondary:hover {
      background: radial-gradient(circle at top left, rgba(129, 140, 248, 0.6), transparent 55%),
                  rgba(15, 23, 42, 0.96);
      border-color: rgba(191, 219, 254, 0.9);
      transform: translateY(-1px) translateZ(0);
      box-shadow: 0 18px 36px rgba(15, 23, 42, 0.92);
    }

    .btn-secondary:active {
      transform: translateY(0);
      box-shadow: 0 8px 20px rgba(15, 23, 42, 0.95);
    }

    .btn-secondary .icon {
      font-size: 0.8rem;
      opacity: 0.9;
    }

    .npc-layout {
      display: grid;
      grid-template-columns: minmax(0, 1.5fr) minmax(0, 1.15fr);
      gap: 16px;
    }

    .card {
      position: relative;
      border-radius: var(--radius-md);
      background: radial-gradient(circle at top left, rgba(148, 163, 184, 0.26), transparent 60%),
                  rgba(15, 23, 42, 0.96);
      border: 1px solid rgba(148, 163, 184, 0.45);
      box-shadow: 0 18px 40px rgba(15, 23, 42, 0.95);
      padding: 14px 16px 14px;
      overflow: hidden;
    }

    .card::before {
      content: "";
      position: absolute;
      inset: -1px;
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), transparent 40%, rgba(168, 85, 247, 0.18));
      opacity: 0;
      mix-blend-mode: soft-light;
      transition: opacity var(--transition-med);
      pointer-events: none;
    }

    .card:hover::before {
      opacity: 0.5;
    }

    .card-header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 6px;
      margin-bottom: 8px;
    }

    .card-title {
      margin: 0;
      font-size: 0.94rem;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #cbd5f5;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .card-title span.icon {
      font-size: 0.86rem;
      opacity: 0.9;
    }

    .tag-strip {
      display: inline-flex;
      flex-wrap: wrap;
      gap: 4px;
    }

    .tag {
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.7);
      padding: 1px 8px;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #9ca3af;
      background: rgba(15, 23, 42, 0.9);
      white-space: nowrap;
    }

    .tag.tag-accent {
      border-color: rgba(56, 189, 248, 0.7);
      color: #7dd3fc;
      background: rgba(8, 47, 73, 0.85);
    }

    .npc-main {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .npc-side {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .npc-identity-grid {
      display: grid;
      grid-template-columns: minmax(0, 1.1fr) minmax(0, 1.1fr);
      gap: 12px;
      margin-top: 4px;
    }

    .field-row {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 10px;
      padding: 6px 8px;
      border-radius: var(--radius-sm);
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(30, 64, 175, 0.9);
      box-shadow: inset 0 0 0 1px rgba(15, 23, 42, 0.9);
    }

    .field-row:nth-child(2n) {
      border-color: rgba(56, 189, 248, 0.65);
    }

    .field-label {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      color: #9ca3af;
      flex-shrink: 0;
    }

    .field-value {
      font-size: 0.9rem;
      text-align: right;
      color: #e5e7eb;
      font-weight: 500;
    }

    .field-value.muted {
      color: #9ca3af;
      font-weight: 400;
    }

    .name-main {
      font-size: 1.15rem;
      font-weight: 600;
      color: #f9fafb;
    }

    .name-sub {
      font-size: 0.79rem;
      color: #9ca3af;
    }

    .name-block {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .pill-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
    }

    .pill {
      border-radius: 999px;
      padding: 3px 9px;
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      border: 1px solid rgba(148, 163, 184, 0.7);
      color: #e5e7eb;
      background: radial-gradient(circle at top left, rgba(148, 163, 184, 0.3), transparent 55%),
                  rgba(15, 23, 42, 0.96);
      white-space: nowrap;
    }

    .pill.pill-race {
      border-color: rgba(56, 189, 248, 0.75);
      color: #7dd3fc;
      background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.3), transparent 55%),
                  rgba(8, 47, 73, 0.96);
    }

    .pill.pill-gender {
      border-color: rgba(244, 114, 182, 0.8);
      color: #f9a8d4;
      background: radial-gradient(circle at top left, rgba(236, 72, 153, 0.32), transparent 55%),
                  rgba(88, 28, 135, 0.97);
    }

    .pill.pill-occupation {
      border-color: rgba(52, 211, 153, 0.8);
      color: #bbf7d0;
      background: radial-gradient(circle at top left, rgba(16, 185, 129, 0.28), transparent 55%),
                  rgba(5, 46, 22, 0.97);
    }

    .divider {
      margin: 10px -16px 8px;
      border: none;
      border-top: 1px dashed rgba(148, 163, 184, 0.5);
    }

    .text-block {
      font-size: 0.86rem;
      line-height: 1.46;
      color: var(--text-main);
    }

    .text-label {
      font-size: 0.76rem;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #9ca3af;
      margin-bottom: 2px;
    }

    .text-chunk {
      margin-bottom: 7px;
    }

    .text-chunk:last-child {
      margin-bottom: 0;
    }

    .deity-line {
      display: flex;
      flex-wrap: wrap;
      gap: 4px 6px;
      align-items: baseline;
      font-size: 0.86rem;
    }

    .deity-chip {
      padding: 2px 7px;
      border-radius: 999px;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      border: 1px solid rgba(56, 189, 248, 0.7);
      color: #7dd3fc;
      background: rgba(8, 47, 73, 0.92);
      white-space: nowrap;
    }

    .deity-desc {
      color: #e5e7eb;
    }

    textarea {
      width: 100%;
      min-height: 90px;
      resize: vertical;
      border-radius: 16px;
      border: 1px solid rgba(148, 163, 184, 0.7);
      padding: 8px 10px;
      font-size: 0.82rem;
      font-family: inherit;
      color: var(--text-main);
      background: radial-gradient(circle at top left, rgba(148, 163, 184, 0.3), transparent 55%),
                  rgba(15, 23, 42, 0.96);
      outline: none;
      box-shadow: inset 0 0 0 1px rgba(15, 23, 42, 0.9);
      transition: border-color var(--transition-fast), box-shadow var(--transition-fast), background var(--transition-fast), transform var(--transition-fast);
    }

    textarea::placeholder {
      color: #64748b;
    }

    textarea:focus-visible {
      outline: 2px solid transparent;
      border-color: rgba(59, 130, 246, 0.9);
      box-shadow: 0 0 0 1px rgba(30, 64, 175, 0.85), 0 0 0 2px rgba(56, 189, 248, 0.8);
      background: radial-gradient(circle at top left, rgba(129, 140, 248, 0.55), transparent 55%),
                  rgba(15, 23, 42, 0.98);
      transform: translateY(-0.5px);
    }

    .actions-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: 8px;
    }

    .status {
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    .status-ok {
      color: #4ade80;
    }

    .status-error {
      color: var(--danger);
    }

    .footer {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px dashed rgba(148, 163, 184, 0.4);
      font-size: 0.72rem;
      color: #64748b;
      gap: 8px;
      flex-wrap: wrap;
    }

    .footer span strong {
      color: #e5e7eb;
      font-weight: 500;
    }

    .footer a {
      color: #7dd3fc;
      text-decoration: none;
      border-bottom: 1px dotted rgba(125, 211, 252, 0.65);
    }

    .footer a:hover {
      border-bottom-style: solid;
    }

    .card-animate {
      animation: fadeInUp 0.42s ease-out;
    }

    @keyframes fadeInUp {
      0% {
        opacity: 0;
        transform: translateY(8px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @media (prefers-reduced-motion: reduce) {
      * {
        scroll-behavior: auto !important;
        animation-duration: 0.001ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.001ms !important;
      }
    }

    @media (max-width: 900px) {
      .npc-layout {
        grid-template-columns: minmax(0, 1fr);
      }

      .app-shell {
        padding: 18px 14px 16px;
        border-radius: 20px;
      }

      .card {
        padding: 12px 12px 12px;
      }

      .divider {
        margin-inline: -12px;
      }
    }

    @media (max-width: 720px) {
      .app-header {
        align-items: flex-start;
      }

      .controls {
        width: 100%;
        justify-content: flex-start;
      }

      .field {
        flex: 1 1 120px;
      }

      .app-title {
        font-size: 1.3rem;
      }
    }

    @media (max-width: 520px) {
      body {
        padding: 10px;
      }

      .app-shell {
        padding: 14px 12px 12px;
      }

      .app-header {
        gap: 10px;
        margin-bottom: 14px;
        padding-bottom: 12px;
      }

      .app-subtitle {
        font-size: 0.8rem;
      }

      .controls {
        flex-direction: column;
        align-items: stretch;
      }

      .btn-primary {
        width: 100%;
        justify-content: center;
      }

      .actions-row {
        flex-direction: column-reverse;
        align-items: stretch;
      }

      .btn-secondary {
        width: 100%;
        justify-content: center;
      }
    }
  </style>
</head>
<body>
  <div class="app-shell">
    <div class="app-inner">
      <header class="app-header">
        <div class="title-block">
          <h1 class="app-title">
            NPC Forge
            <span class="title-pill">5E Ready</span>
          </h1>
          <p class="app-subtitle">
            Generate flavorful, ready-to-play NPCs for your homebrew campaign: names, hooks, secrets, and more in a single click.
          </p>
        </div>
        <div class="controls">
          <div class="field">
            <label for="regionSelect">Region flavor</label>
            <div class="select-wrap">
              <select id="regionSelect">
                <option value="any">Any</option>
                <option value="urban">Bustling City</option>
                <option value="rural">Rural Village</option>
                <option value="frontier">Frontier / Wilds</option>
                <option value="underdark">Underdark</option>
                <option value="seafaring">Coastal / Seafaring</option>
                <option value="desert">Desert Lands</option>
                <option value="arctic">Arctic</option>
                <option value="religious">Holy City / Temple</option>
              </select>
            </div>
          </div>
          <div class="field">
            <label for="toneSelect">Tone</label>
            <div class="select-wrap">
              <select id="toneSelect">
                <option value="any">Any</option>
                <option value="light">Light-hearted</option>
                <option value="grim">Gritty</option>
                <option value="mysterious">Mysterious</option>
              </select>
            </div>
          </div>
          <button id="generateBtn" class="btn-primary">
            <span class="icon">✨</span>
            <span>Generate NPC</span>
          </button>
        </div>
      </header>

      <main class="npc-layout">
        <section class="npc-main">
          <article class="card" id="identityCard">
            <div class="card-header">
              <h2 class="card-title">
                <span class="icon">🎭</span>
                <span>Identity</span>
              </h2>
              <div class="tag-strip">
                <span class="tag tag-accent" id="npcRegionTag">Any Region</span>
                <span class="tag" id="npcToneTag">Any Tone</span>
              </div>
            </div>
            <div class="npc-identity-grid">
              <div>
                <div class="name-block">
                  <div class="text-label">Name</div>
                  <div class="name-main" id="npcName">—</div>
                  <div class="name-sub" id="npcNameHint"></div>
                </div>
                <div class="pill-strip" style="margin-top:8px;">
                  <span class="pill pill-race" id="npcRacePill">Race</span>
                  <span class="pill pill-gender" id="npcGenderPill">Gender</span>
                  <span class="pill pill-occupation" id="npcOccupationPill">Occupation</span>
                </div>
              </div>
              <div>
                <div class="field-row">
                  <span class="field-label">Race</span>
                  <span class="field-value" id="npcRace">—</span>
                </div>
                <div class="field-row">
                  <span class="field-label">Gender</span>
                  <span class="field-value" id="npcGender">—</span>
                </div>
                <div class="field-row">
                  <span class="field-label">Occupation</span>
                  <span class="field-value" id="npcOccupation">—</span>
                </div>
                <div class="field-row">
                  <span class="field-label">Deity</span>
                  <span class="field-value" id="npcDeity">—</span>
                </div>
              </div>
            </div>
          </article>

          <article class="card" id="personalityCard">
            <div class="card-header">
              <h2 class="card-title">
                <span class="icon">🧠</span>
                <span>Personality & Hooks</span>
              </h2>
              <div class="tag-strip">
                <span class="tag">Use as Roleplay Cue</span>
              </div>
            </div>
            <div class="text-block">
              <div class="text-chunk">
                <div class="text-label">Personality</div>
                <div id="npcPersonality">—</div>
              </div>
              <div class="text-chunk">
                <div class="text-label">Goal</div>
                <div id="npcGoal">—</div>
              </div>
              <div class="text-chunk">
                <div class="text-label">Secret</div>
                <div id="npcSecret">—</div>
              </div>
            </div>
          </article>
        </section>

        <aside class="npc-side">
          <article class="card" id="appearanceCard">
            <div class="card-header">
              <h2 class="card-title">
                <span class="icon">👁️</span>
                <span>Appearance</span>
              </h2>
              <div class="tag-strip">
                <span class="tag">Describe at the Table</span>
              </div>
            </div>
            <div class="text-block">
              <div id="npcAppearance">—</div>
            </div>
          </article>

          <article class="card">
            <div class="card-header">
              <h2 class="card-title">
                <span class="icon">✍️</span>
                <span>DM Notes</span>
              </h2>
              <div class="tag-strip">
                <span class="tag">Session Prep</span>
              </div>
            </div>
            <div class="text-block">
              <div class="text-chunk">
                <div class="text-label">Your notes</div>
                <textarea id="gmNotes" placeholder="Add links, relationships, or how this NPC connects to your current arc."></textarea>
              </div>
              <div class="text-chunk">
                <div class="text-label">Deity (detailed)</div>
                <div class="deity-line">
                  <span class="deity-chip" id="npcDeityChip">No patron</span>
                  <span class="deity-desc" id="npcDeityDescription"></span>
                </div>
              </div>
              <div class="actions-row">
                <button id="copyBtn" class="btn-secondary">
                  <span class="icon">📋</span>
                  <span>Copy NPC as Text</span>
                </button>
                <div class="status" id="copyStatus">Ready to copy.</div>
              </div>
            </div>
          </article>
        </aside>
      </main>

      <footer class="footer">
        <span>Built for <strong>homebrew 5e</strong> — tweak anything to fit your world.</span>
        <span>Tip: click “Generate NPC” whenever you need a tavern patron, quest giver, or suspicious stranger.</span>
      </footer>
    </div>
  </div>

  <script>
    (function () {
      function randFrom(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
      }

      function pickFromTone(pool, tone) {
        if (!tone || tone === "any" || !pool[tone]) {
          return randFrom(pool.any);
        }
        var merged = pool.any.concat(pool[tone]);
        return randFrom(merged);
      }

      function generateName() {
        var starts = ["Al", "Ba", "Bel", "Cal", "Da", "El", "Fa", "Gal", "Ka", "La", "Ma", "Na", "Or", "Per", "Ra", "Sa", "Sha", "Ta", "Ther", "Va", "Vor", "Za", "Zel", "Kor", "Jun", "Eri", "Lio", "Syl", "Thal", "Vor", "Xan"];
        var mids = ["a", "e", "i", "o", "u", "ae", "ia", "ai", "ea", "ou", "ar", "ir", "or", "ur", "an", "en", "in", "on", "un", "el", "il", "as", "is", "os", "ys"];
        var ends = ["n", "s", "th", "r", "nd", "nn", "l", "mir", "dor", "drim", "zor", "thar", "das", "ric", "mon", "var", "gorn", "dil", "morn", "viel", "non", "dris", "vash", "dane", "riel", "thor", "ian"];
        var surnames = [
          "Amberfall", "Blackwater", "Stormwind", "Duskhollow", "Brightshield", "Ironvein", "Thornbriar",
          "Nightbloom", "Riversong", "Stonebrook", "Highspire", "Ashwillow", "Silverstring",
          "Glimmerforge", "Frostglen", "Shadowfen", "Goldmantle", "Oakensong", "Moonridge",
          "Cinderstep", "Hawkspear", "Deepcurrent", "Starwatch", "Windrider", "Grimstone"
        ];

        var syllables = Math.random() < 0.5 ? 2 : 3;
        var first = randFrom(starts);
        if (syllables === 3) {
          first += randFrom(mids);
        }
        first += randFrom(ends);

        var name = first;
        if (Math.random() < 0.75) {
          name += " " + randFrom(surnames);
        }
        return name;
      }

      function inferNameHint(name, race) {
        var hint = "";
        if (race.indexOf("Elf") !== -1 || race.indexOf("Drow") !== -1) {
          hint = "Flowing, elven cadence.";
        } else if (race.indexOf("Dwarf") !== -1) {
          hint = "Solid, dwarven name.";
        } else if (race.indexOf("Halfling") !== -1 || race.indexOf("Gnome") !== -1) {
          hint = "Bouncy, light-footed name.";
        } else if (race.indexOf("Dragonborn") !== -1 || race.indexOf("Tiefling") !== -1) {
          hint = "Strong, dramatic syllables.";
        } else if (race.indexOf("Orc") !== -1 || race.indexOf("Goliath") !== -1) {
          hint = "Harsh consonants, sturdy sound.";
        } else {
          hint = "Common regional name.";
        }
        return hint;
      }

      function pickRace(region) {
        var base = [
          "Human", "Elf", "Half-Elf", "Dwarf", "Halfling", "Gnome", "Half-Orc", "Tiefling", "Dragonborn",
          "Aasimar", "Goliath", "Firbolg", "Tabaxi", "Genasi (air)", "Genasi (earth)", "Genasi (fire)", "Genasi (water)",
          "Goblin", "Orc", "Triton", "Kenku"
        ];
        var regional = {
          any: base,
          urban: base.concat(["Human", "Human", "Tiefling", "Half-Elf", "Half-Elf", "Gnome", "Goblin"]),
          rural: ["Human", "Human", "Human", "Halfling", "Halfling", "Dwarf", "Half-Elf", "Firbolg", "Gnome"],
          frontier: ["Human", "Human", "Half-Orc", "Goliath", "Firbolg", "Tabaxi", "Dragonborn", "Half-Elf", "Orc"],
          underdark: ["Drow", "Duergar", "Deep Gnome (Svirfneblin)", "Drow", "Drow", "Deep Gnome (Svirfneblin)", "Kobold", "Goblin", "Half-Drow"],
          seafaring: ["Human", "Half-Elf", "Triton", "Triton", "Sea Elf", "Human", "Tabaxi", "Genasi (water)", "Genasi (air)"],
          desert: ["Human", "Human", "Genasi (fire)", "Genasi (air)", "Tiefling", "Dragonborn", "Halfling", "Tabaxi"],
          arctic: ["Human", "Human", "Goliath", "Goliath", "Dwarf", "Firbolg", "Genasi (water)", "Half-Elf"],
          religious: base.concat(["Aasimar", "Aasimar", "Human", "Human", "Dwarf"])
        };
        var pool = regional[region] || base;
        return randFrom(pool);
      }

      function pickGender() {
        var genders = [
          "Woman", "Man", "Nonbinary", "Genderfluid", "Agender"
        ];
        return randFrom(genders);
      }

      function pickOccupation(region) {
        var base = [
          "innkeeper", "wandering bard", "city guard", "street vendor", "scholar", "archivist",
          "blacksmith", "apothecary", "hunter", "cartographer", "courier", "fence for stolen goods",
          "local noble's steward", "sage", "monster scout", "village elder", "mercenary captain", "scribe",
          "artisan", "shipwright", "coach driver", "herbalist", "fortune-teller", "orcish diplomat",
          "gravekeeper", "arena promoter", "monster hunter", "temple acolyte"
        ];
        var pools = {
          any: base,
          urban: base.concat([
            "guild factor", "moneylender", "dock foreman", "thieves' guild contact", "street preacher"
          ]),
          rural: [
            "farmer", "mill worker", "shepherd", "bee keeper", "woodcutter", "village herbalist", "local reeve",
            "brewer", "trapper", "Weaver", "travelling tinker"
          ],
          frontier: [
            "monster hunter", "scout", "ranger guide", "camp quartermaster", "prospector", "border guard",
            "smuggler", "beast wrangler"
          ],
          underdark: [
            "mushroom farmer", "slave trader", "underground guide", "information broker", "poisoner",
            "drow house retainer", "duergar artisan", "spore druid"
          ],
          seafaring: [
            "sailor", "ship's quartermaster", "harbormaster's clerk", "smuggler", "dockside bartender",
            "navigator", "shipwright", "whaler"
          ],
          desert: [
            "caravan master", "nomad scout", "oasis keeper", "sand mage", "spice merchant", "camel handler",
            "ruin delver"
          ],
          arctic: [
            "trapper", "ice fisher", "sled driver", "whaler", "glacier guide", "aurora mystic",
            "frontier priest"
          ],
          religious: [
            "temple acolyte", "high priest's aide", "choir leader", "itinerant preacher", "scribe of holy texts",
            "relic keeper", "pilgrim guide"
          ]
        };
        var pool = pools[region] || pools.any;
        return randFrom(pool);
      }

      var personalities = {
        any: [
          "Warm and quick to laugh, but carefully watches what others reveal before sharing much about themself.",
          "Soft-spoken and courteous, with a habit of apologizing even when they have done nothing wrong.",
          "Blunt and practical, more comfortable with tasks than with small talk.",
          "Inquisitive to a fault, constantly asking how things work and why people made certain choices.",
          "Charming and theatrical, treating even mundane events as if they were on stage.",
          "Stoic and difficult to read, but observant of small details others miss.",
          "Optimistic and energetic, always convinced the next opportunity will be the big one.",
          "Dryly sarcastic, using humor to deflect when conversation veers too close to their past.",
          "Methodical and precise, keeping everything in careful order and growing anxious when plans change.",
          "Secretly sentimental, collecting small trinkets that remind them of places and people."
        ],
        light: [
          "Playfully dramatic, turning every story into an entertaining exaggeration.",
          "Earnest and friendly, always eager to help and quick to trust.",
          "A bit scatterbrained but endlessly enthusiastic, often forgetting small details while chasing new ideas.",
          "Loves gossip and rumors, but rarely repeats anything that would truly hurt someone."
        ],
        grim: [
          "World-weary and guarded, assuming the worst so they can be pleasantly surprised.",
          "Pragmatic to the point of cynicism, willing to make hard choices if it means survival.",
          "Haunted by old mistakes and determined not to repeat them, even if it makes them seem harsh."
        ],
        mysterious: [
          "Speaks in half-answers and parables, as if everything is part of a larger pattern only they can see.",
          "Calm and distant, studying others with the patience of a scribe reading a difficult text.",
          "Occasionally slips and uses terminology that suggests secret affiliations or forbidden knowledge."
        ]
      };

      var goals = {
        any: [
          "Wants to secure enough coin to retire somewhere quiet, away from political and planar turmoil.",
          "Hopes to prove themself worthy of a mentor who once dismissed them as ordinary.",
          "Is quietly gathering information about adventurers, looking for a reliable group to back a risky venture.",
          "Aims to restore a damaged reputation after being blamed for a failure that was not entirely their fault.",
          "Wants to map out a forgotten route that would cut days off a common journey and make them famous.",
          "Is searching for someone who disappeared years ago and follows any rumor that might be related."
        ],
        light: [
          "Dreams of opening a small tavern or shop that becomes the heart of their neighborhood.",
          "Wants to organize a grand festival that will be remembered for generations.",
          "Hopes to collect stories from travelers to compile into a book of legends."
        ],
        grim: [
          "Seeks leverage over a cruel authority figure who has harmed their family or community.",
          "Plans to pay off a dangerous debt before the wrong people decide to make an example of them.",
          "Wants to expose corruption within a respected institution, even if it costs them dearly."
        ],
        mysterious: [
          "Is following cryptic prophecies that suggest their actions today will influence events centuries from now.",
          "Hunts for an artifact they refuse to name, claiming too many ears are listening.",
          "Needs specific information from travelers about distant lands, but never explains why."
        ]
      };

      var secrets = {
        any: [
          "Once stole a minor relic from a temple and quietly returned it years later, but still fears discovery.",
          "Is connected by blood or oath to a powerful figure and hides their true surname.",
          "Has a hidden stash of coin or contraband that even close friends know nothing about.",
          "Is quietly in communication with a rival faction and passes along information in exchange for small favors.",
          "Accidentally caused a tragedy in their youth and has spent years trying to make amends from the shadows.",
          "Knows the location of a forgotten tunnel or portal that bypasses a heavily guarded area.",
          "Is far more skilled than they pretend to be, using a humble role as a convenient disguise.",
          "Carries a small token that marks them as part of a secret society most assume is only rumor."
        ],
        light: [
          "Secretly writes romantic ballads about local adventurers and performs them under a pseudonym.",
          "Has been feeding a stray magical creature that has started following them around town.",
          "Keeps a detailed, mildly embarrassing scrapbook of heroes and villains that pass through the area."
        ],
        grim: [
          "Once accepted payment to look the other way during a crime and has been blackmailed ever since.",
          "Smuggles medicine and supplies to a forbidden group the authorities consider dangerous.",
          "Knows that a respected local leader is involved in something foul—but confronting them alone would be fatal."
        ],
        mysterious: [
          "Has dreams that sometimes show real events from far away, though they do not fully understand why.",
          "Carries a sealed letter they were told to deliver only to someone matching a vague description—which seems to fit one of the characters.",
          "Can see faint, ghostlike figures in mirrors and still water, and tries very hard to pretend they cannot."
        ]
      };

      var diaryAppearances = [
        "Their hair is carefully braided and wrapped with bits of colored thread, adding warmth to an otherwise practical outfit.",
        "Their armor bears the scuffs and dents of real use, but it is polished and maintained with obvious pride.",
        "They smell faintly of incense and parchment, with ink stains along their fingers and cuffs.",
        "A streak of silver runs through their hair despite their relatively young features, hinting at strange magic or stress.",
        "Their clothes are a patchwork of careful repairs, suggesting sentimentality or a lack of coin—or both.",
        "They favor layered, flowing fabrics, with patterns that echo the motifs of their homeland.",
        "A small charm hangs from their neck or belt, worn smooth by anxious fingers.",
        "Their boots are sturdy and travel-worn, but their hands are surprisingly soft and clean.",
        "They carry themselves with straight-backed discipline, even when trying to stay unnoticed.",
        "Their eyes are alert and restless, tracking exits, faces, and valuables almost unconsciously."
      ];

      var featureAppearances = [
        "A visible scar along the jaw or cheek, softened by a friendly expression.",
        "Eyes that catch the light in an unusual hue, suggesting distant bloodlines or subtle magic.",
        "Elaborate tattoos peeking out from beneath sleeves, hinting at cultural or arcane significance.",
        "A missing or prosthetic finger, which they compensate for with clever adjustments.",
        "An ever-present smudge of soot, ink, or dust, no matter how often they try to clean it.",
        "Jewelry that is inexpensive but obviously well cared for, perhaps a family heirloom.",
        "A subtle limp that only appears when they are tired or distracted.",
        "A voice that is unexpectedly melodic, with a lilting cadence.",
        "A laugh that comes suddenly and fully, often startling quieter patrons.",
        "A gaze that lingers a heartbeat too long, as if weighing the truth of every word spoken."
      ];

      var regionFlavorAppearances = {
        any: [
          "Their cloak is cut in a style common across the trade roads, functional and nondescript.",
          "A medley of travel-worn trinkets dangle from their belt, each from a different region."
        ],
        urban: [
          "Their clothes slant toward city fashion: layered, sharp lines with an eye for local trends.",
          "A badge, sash, or discrete token marks them as tied to one of the city's many guilds."
        ],
        rural: [
          "Mud-spattered boots and sun-browned skin speak of long days spent outdoors.",
          "Simple, sturdy fabrics dyed with natural colors clearly mark them as rural folk."
        ],
        frontier: [
          "Their gear is practical and mismatched, clearly assembled from whatever survived the last journey.",
          "A well-used cloak hangs from their shoulders, stained by weather and rough travel."
        ],
        underdark: [
          "Bioluminescent fungus spores cling faintly to their clothes, glowing softly in dim light.",
          "Pieces of chitin and strange bone adorn their gear, trophies from creatures of the deep earth."
        ],
        seafaring: [
          "Salt crust and faded sun-bleached fabric give them the look of someone long familiar with open water.",
          "They move with the easy balance of someone used to the pitch and roll of a ship's deck."
        ],
        desert: [
          "Their garments are layered and light-colored, designed to keep out sand and searing sun alike.",
          "A scarf or veil hangs ready to be drawn up against dust storms."
        ],
        arctic: [
          "Thick furs and a frost-crusted hood leave only their eyes and nose visible in true cold.",
          "Their cheeks are reddened by harsh winds, and their gear is trimmed in white fur."
        ],
        religious: [
          "Subtle holy symbols are worked into the stitching of their clothing.",
          "Their garments are neat and orderly, with colors echoing a nearby temple's iconography."
        ]
      };

      var deities = [
        {
          name: "Lathander",
          title: "god of dawn and renewal",
          flavor: "They greet new ideas like sunrise, quick to encourage fresh starts."
        },
        {
          name: "Mystra",
          title: "goddess of magic",
          flavor: "They treat magic as a sacred pattern and fear its reckless use."
        },
        {
          name: "Tymora",
          title: "goddess of luck",
          flavor: "They flip a coin or roll a die for small decisions, trusting fortune to guide them."
        },
        {
          name: "Tempus",
          title: "god of war and honorable battle",
          flavor: "They view conflict as inevitable and judge others by how they face it."
        },
        {
          name: "Chauntea",
          title: "goddess of agriculture and growth",
          flavor: "They are most at ease around growing things and offer quiet blessings over meals."
        },
        {
          name: "Bahamut",
          title: "god of justice and nobility",
          flavor: "They strive to act with fairness, even when it costs them."
        },
        {
          name: "Tiamat",
          title: "goddess of wealth and ruthless ambition",
          flavor: "They hide a fierce hunger for power behind polite manners."
        },
        {
          name: "The Raven Queen",
          title: "mistress of fate and winter",
          flavor: "They are calm around death, viewing it as a necessary turning of the wheel."
        },
        {
          name: "Moradin",
          title: "dwarven god of craft and creation",
          flavor: "They prize well-made work and quietly judge shoddy craftsmanship."
        },
        {
          name: "Corellon",
          title: "patron of art and arcane grace",
          flavor: "They speak with an artist's flair and move with deliberate elegance."
        },
        {
          name: "Selûne",
          title: "goddess of the moon and travelers",
          flavor: "They feel most at peace under the open sky and are fond of night journeys."
        },
        {
          name: "Ilmater",
          title: "god of endurance and compassion",
          flavor: "They will accept hardship themselves rather than see others suffer."
        }
      ];

      function pickDeity(region) {
        var noneChances = 0.18;
        if (region === "religious") {
          noneChances = 0.08;
        }
        if (Math.random() < noneChances) {
          return null;
        }

        var pool = deities.slice();
        if (region === "seafaring") {
          pool.push({
            name: "Umberlee",
            title: "goddess of the sea's fury",
            flavor: "They leave offerings at docks and pray before any voyage."
          });
        }
        if (region === "desert") {
          pool.push({
            name: "Kelemvor",
            title: "god of the ordered afterlife",
            flavor: "They speak of the dead with quiet certainty and respect."
          });
        }
        if (region === "underdark") {
          pool.push({
            name: "Lolth",
            title: "queen of spiders and schemes",
            flavor: "They weigh every relationship like a web of obligations and leverage."
          });
        }

        return randFrom(pool);
      }

      function buildAppearance(region) {
        var base1 = randFrom(diaryAppearances);
        var base2 = randFrom(featureAppearances);
        var regionalList = regionFlavorAppearances[region] || regionFlavorAppearances.any;
        var regional = randFrom(regionalList);
        return base1 + " " + base2 + " " + regional;
      }

      function buildRegionTag(region) {
        var map = {
          any: "Any Region",
          urban: "Bustling City",
          rural: "Rural Village",
          frontier: "Frontier / Wilds",
          underdark: "Underdark",
          seafaring: "Coastal / Seafaring",
          desert: "Desert Lands",
          arctic: "Arctic",
          religious: "Holy City / Temple"
        };
        return map[region] || "Any Region";
      }

      function buildToneTag(tone) {
        var map = {
          any: "Any Tone",
          light: "Light-hearted Tone",
          grim: "Gritty Tone",
          mysterious: "Mysterious Tone"
        };
        return map[tone] || "Any Tone";
      }

      function animateCards() {
        var cards = [document.getElementById("identityCard"), document.getElementById("personalityCard"), document.getElementById("appearanceCard")];
        cards.forEach(function (card) {
          if (!card) return;
          card.classList.remove("card-animate");
          void card.offsetWidth;
          card.classList.add("card-animate");
        });
      }

      function buildCopyText(npc) {
        var lines = [];
        lines.push("NPC: " + npc.name);
        lines.push("Race: " + npc.race);
        lines.push("Gender: " + npc.gender);
        lines.push("Occupation: " + npc.occupation);
        lines.push("Deity: " + (npc.deityText || "None / no fixed patron"));
        lines.push("");
        lines.push("Appearance:");
        lines.push("  " + npc.appearance);
        lines.push("");
        lines.push("Personality:");
        lines.push("  " + npc.personality);
        lines.push("");
        lines.push("Goal:");
        lines.push("  " + npc.goal);
        lines.push("");
        lines.push("Secret:");
        lines.push("  " + npc.secret);
        return lines.join("\n");
      }

      function generateNPC() {
        var regionSelect = document.getElementById("regionSelect");
        var toneSelect = document.getElementById("toneSelect");
        var region = regionSelect ? regionSelect.value : "any";
        var tone = toneSelect ? toneSelect.value : "any";

        var race = pickRace(region);
        var gender = pickGender();
        var occupation = pickOccupation(region);
        var name = generateName();
        var appearance = buildAppearance(region);
        var personality = pickFromTone(personalities, tone);
        var goal = pickFromTone(goals, tone);
        var secret = pickFromTone(secrets, tone);
        var deityObj = pickDeity(region);

        var deityText = "None / no specific patron";
        var deityChip = "No patron";
        var deityDesc = "They offer the occasional prayer to any deity who might be listening, but have no formal allegiance.";
        if (deityObj) {
          deityText = deityObj.name + ", " + deityObj.title;
          deityChip = deityObj.name;
          deityDesc = deityObj.flavor;
        }

        var hint = inferNameHint(name, race);

        document.getElementById("npcName").textContent = name;
        document.getElementById("npcNameHint").textContent = hint;
        document.getElementById("npcRace").textContent = race;
        document.getElementById("npcGender").textContent = gender;
        document.getElementById("npcOccupation").textContent = occupation.charAt(0).toUpperCase() + occupation.slice(1);

        document.getElementById("npcRacePill").textContent = race;
        document.getElementById("npcGenderPill").textContent = gender;
        document.getElementById("npcOccupationPill").textContent = occupation;

        document.getElementById("npcDeity").textContent = deityText;
        document.getElementById("npcDeityChip").textContent = deityChip;
        document.getElementById("npcDeityDescription").textContent = deityDesc;

        document.getElementById("npcPersonality").textContent = personality;
        document.getElementById("npcGoal").textContent = goal;
        document.getElementById("npcSecret").textContent = secret;
        document.getElementById("npcAppearance").textContent = appearance;

        document.getElementById("npcRegionTag").textContent = buildRegionTag(region);
        document.getElementById("npcToneTag").textContent = buildToneTag(tone);

        animateCards();

        window.__lastNPC = {
          name: name,
          race: race,
          gender: gender,
          occupation: occupation,
          appearance: appearance,
          personality: personality,
          goal: goal,
          secret: secret,
          deityText: deityText
        };

        var status = document.getElementById("copyStatus");
        if (status) {
          status.textContent = "Ready to copy.";
          status.classList.remove("status-ok");
          status.classList.remove("status-error");
        }
      }

      function wireCopyButton() {
        var copyBtn = document.getElementById("copyBtn");
        var status = document.getElementById("copyStatus");
        if (!copyBtn) return;
        copyBtn.addEventListener("click", function () {
          if (!window.__lastNPC) {
            if (status) {
              status.textContent = "Generate an NPC first.";
              status.classList.add("status-error");
            }
            return;
          }
          var text = buildCopyText(window.__lastNPC);
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(function () {
              if (status) {
                status.textContent = "NPC copied to clipboard.";
                status.classList.remove("status-error");
                status.classList.add("status-ok");
              }
            }).catch(function () {
              if (status) {
                status.textContent = "Could not access clipboard; copy manually from the page.";
                status.classList.remove("status-ok");
                status.classList.add("status-error");
              }
            });
          } else {
            try {
              var temp = document.createElement("textarea");
              temp.value = text;
              temp.setAttribute("readonly", "");
              temp.style.position = "absolute";
              temp.style.left = "-9999px";
              document.body.appendChild(temp);
              temp.select();
              document.execCommand("copy");
              document.body.removeChild(temp);
              if (status) {
                status.textContent = "NPC copied to clipboard.";
                status.classList.remove("status-error");
                status.classList.add("status-ok");
              }
            } catch (e) {
              if (status) {
                status.textContent = "Could not access clipboard; copy manually from the page.";
                status.classList.remove("status-ok");
                status.classList.add("status-error");
              }
            }
          }
        });
      }

      document.addEventListener("DOMContentLoaded", function () {
        var generateBtn = document.getElementById("generateBtn");
        if (generateBtn) {
          generateBtn.addEventListener("click", generateNPC);
        }
        wireCopyButton();
        generateNPC();
      });
    })();
  </script>
</body>
</html>