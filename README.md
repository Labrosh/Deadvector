# Dead Vector — Solo Ship‑Maintenance Mini‑RPG

**Status**: early design draft · open to tweaks & pull‑requests

## Table of Contents

- [Concept](#concept)
- [Setting](#setting)
- [Core Loop](#core-loop)
- [Quickstart](#quickstart)
- [Gameplay Mechanics](#gameplay-mechanics)
  - [Subsystems & Rooms](#subsystems--rooms)
  - [Malfunction Events](#malfunction-events)
  - [Difficulty & Severity](#difficulty--severity)
  - [Dice Resolution](#dice-resolution)
  - [Health & Integrity](#health--integrity-win--lose-conditions)
- [Companion App](#companion-app)
  - [Requirements](#requirements)
  - [Installation & Run](#installation--run)
- [Playing With an AI Narrator](#playing-with-an-ai-narrator)
- [Playing With a Human GM](#playing-with-a-human-gm)
- [Extending Content (YAML Files)](#extending-content-yaml-files)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## Concept

Dead Vector is a light, narrative‑first mini‑RPG about keeping an ailing cargo clunker barely space‑worthy while an odd bio‑engine — the Jump Spine — throbs at its heart. Play solo with the built‑in dice roller, co‑op with friends, or pair with ChatGPT (or any GM) as a story narrator.

## Setting

A quarantined star‑system littered with derelicts and unmanned depots. You are the only known human aboard the MV Jalopy, an out‑of‑date freighter. Escape requires nursing the Jump Spine back to full power — and surviving the mundane (and occasionally uncanny) breakdowns along the way.

## Core Loop

1. Draw a malfunction (or let the App / GM trigger one).
2. The AI announces the fault according to difficulty.
3. You diagnose & attempt a fix, rolling dice when required.
4. Success stabilises the ship; failure escalates severity or spawns follow‑up events.
5. Between crises you trade, explore derelicts, or push for a jump.

## Quickstart

```bash
# clone & run prototype
pip install -r requirements.txt
python deadvector.py
```

1. Select difficulty (Easy | Medium | Hard).
2. Click "Trigger Malfunction" to start.
3. Follow the AI's instructions or consult the PDF Event Deck.
4. Roll a d6 / d20 as prompted and click "Apply Result".

## Gameplay Mechanics

### Subsystems & Rooms

| Room | Purpose | Can Fail With |
|------|---------|--------------|
| Bridge | Navigation & comms | Nav Gyro Drift, Antenna Mis‑align |
| Living Quarters | Crew rest | HVAC Clog, Short‑circuit Fire |
| Cargo Hold | Storage & salvage | Door Jam, Pressure Leak |
| Jump Spine Chamber | Bio‑engine core | Cramps, Nutrient Drain |
| Engine Bay | Thrust & RCS | Coolant Pump Stall, Power Bus Fault |
| Reactor Core | Primary power | Fuse Blowout, Heat Spike |
| Life Support | Air & water | CO₂ Scrubber Fail, Filter Clot |

### Malfunction Events

Defined in `/events/*.yaml`. Each file contains:

- id, subsystem, severity, difficulty_text, ai_opening, failure_consequence.

### Difficulty & Severity

- Difficulty controls how much info the AI reveals.
- Severity sets the timer & penalty if unresolved.

### Dice Resolution

Default table (tweak in rules.yaml):

| d20 Roll | Outcome |
|----------|---------|
| 1‑5 | Fail — escalate severity |
| 6‑14 | Partial — fix but spawn a new Minor event |
| 15‑20 | Success — subsystem stable |

### Health & Integrity (Win / Lose Conditions)

- **Player HP** – starts at 6 (1 heart = 2 HP). Certain events can injure you (electrical shock, decompression). HP 0 ⇒ You're incapacitated; the ship's AI or another player has limited turns to stabilise you before total loss.

- **Ship HP** – starts at 10 ("structural integrity" pips). Every unresolved or escalated fault may tick 1–3 damage. HP 0 ⇒ Total hull failure … game over.

Both pools can be healed/repaired between events if spare parts or med‑kits are on board; otherwise the next malfunction might be fatal.

## Companion App

### Requirements

- Python 3.11+
- PySimpleGUI ≤ 5.0 (or tkinter fallback)

### Installation & Run

See [Quickstart](#quickstart) or run `python gui.py --help` for options.

#### Built‑in Narration Tiers

- **Boiler‑plate Text Pack** – every event YAML already contains short success / partial / fail sentences. Always free and offline.
- **Copy‑&‑Paste Prompt Button** – click to copy a neatly formatted prompt; paste it into any LLM or free chat service for richer prose.
- **API Plug‑in (Opt‑in)** – enter your own OpenAI/Anthropic key in Settings; the app will fetch narrated outcomes automatically. Entirely optional; the game never requires a paid key.

## Playing With an AI Narrator

Paste the AI opening line into ChatGPT and ask: "What happens on a Fail / Success?" — let the model narrate the scene, then apply mechanical results back in the app.

## Playing With a Human GM

GM draws events, reads only the matching difficulty hint aloud, adjudicates dice rolls, narrates outcome.

## Extending Content (YAML Files)

1. Copy `events/template.yaml` → `events/NEW.yaml`.

2. Fill in fields & add to `events/index.yaml`.

3. Restart the app — your event is live.

## Contributing

Pull‑requests for new events, rules tweaks, or GUI polish are welcome. See CONTRIBUTING.md.

### Build Loops (Milestones)

The project grows outward in concentric rings. Finish each ring before starting the next.

| Loop ID | Goal ("Definition of Done") | Adds to Player Experience |
|---------|----------------------------|--------------------------|
| 0 · Micro‑Console | One YAML event triggers in the terminal, you type a d20 roll, outcome text prints. | Validates text content & dice table. |
| 1 · Core Console | Random event picker, success/fail thresholds adjustable by difficulty flag. | True fault→fix→resolve flow. |
| 2 · Minimal GUI | PySimpleGUI window with event list, "Roll" button, and outcome box. | Click‑based play; no more terminal. |
| 3 · Blueprint Clicks | Static ship map image; clicking a room filters its faults. | Spatial reasoning; feels like you're inside the ship. |
| 3b · Health & Integrity | Player HP & Ship HP pools, events deal damage, lose conditions trigger. | Real stakes; every repair feels meaningful. |
| 4 · Escalation Timers | Severity raises if a fault isn't fixed within X ticks; display countdown. | Tension & prioritisation. |
| 5 · AI Narration Modes | Toggle: Text‑only · ChatGPT prompt · Human GM notes. | Story flavour options. |
| 6 · Content Pass | ≥ 20 curated faults, three difficulty lines each, balanced roll tables. | Variety; replay value. |
| 7 · Polish | Sounds, save/load, prettier widgets, icons. | Shippable alpha. |

### Stretch Goals & Future Ideas (Maybe one day)

These are ambitious or experimental features not required for a 1.0 release. Park them here until the core milestone track feels rock‑solid.

#### More Content

- **Alternate Ship Layouts**: science cutter, bulk freighter, escort corvette—each with unique room grids.

- **Additional Bio‑Subsystems**: Living Reactor, Parasite‑Navigation Cluster.

- **Bigger Event Library**: 100+ malfunctions, chained story arcs, seasonal variants.

#### Expanded Gameplay

- **Salvage‑Run Mini‑Game**: hex map travel, fuel pips, loot tables.

- **EVA Hazard Deck**: micrometeoroids, tether tangles, suit leaks.

- **Skill Tracks & Perks**: Mechanical, Electrical, Bio‑Spine leveling.

- **Achievement Logbook**: unlockable badges & captain's log entries.

#### Narrative & Modding

- **Chained Event Arcs**: vision cards, multi‑step mysteries.

- **Hardcore Toggles**: AI misdirection, permadeath, no boiler‑plate text.

- **Mod Hook Folder**: auto‑load any YAML in `mods/` for community content.

#### Alternate Formats

- **Web Front‑End**: browser UI via Flask + React; remote co‑op.

- **Print‑and‑Play Kit**: folded rules zine, event cards, blueprint poster.

(When a stretch goal graduates to active development, move it into the milestone table and open a GitHub issue.)

## Roadmap

- Actually start the project.

## License

MIT — see LICENSE file.
