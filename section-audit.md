# Fizzleblast Dashboard - Full Section Audit

**File:** `C:/DND Campaigns/Prompt Library/fizzleblast-fieldtrip/index.html`
**Total Lines:** 17,126
**Total Sections:** 37
**Total Tabs:** 7 (RECAP, STATS, ANALYSIS, MOMENTS, CHARACTERS, LORE, VISUALS)
**Campaign:** Charisma Company: Fizzleblast's Fieldtrip (One-Shot)
**Players:** Moor (Cleric/Kyle), Aramil (Warlock/Kyle), Opal (Barbarian/Shannon), Lavender (Warlock/Kelsey), Bob (Rogue/Josh)

---

## Pre-Tab Content (Always Visible)

### Ticker Tape (no section ID -- fixed position)
- **Content:** Scrolling ticker with session highlights
- **Components:** Session name, date (Feb 18 2026), party names with colors, nat 20 alert (Opal 4 nat 20s), MVP race (Lavender vs Bob 8.4), energy highlights
- **Quality:** Good. Content is specific and accurate to the Fizzleblast session.
- **Notes:** Ticker says "Opal rolls 4 natural 20s" but the Credits section (line 3764) says "Nat 20s: 0 / Nat 1s: 1". This is a DATA CONFLICT. The Analytics section confirms Opal had 4 nat 20s on skill checks, but credits only counted combat nat 20s (0). The ticker is misleading.

### Hero Section (`id="hero"`)
- **Content:** Full-screen hero with campaign title, subtitle, date, and party avatars
- **Components:** Hero title "CHARISMA COMPANY: FIZZLEBLAST'S FIELDTRIP", subtitle "A Charisma Company One-Shot", date "ONE-SHOT // THE CHULTAN EXPEDITION // ~4H", 5 player cards with emoji avatars
- **Quality:** Good. All 5 players correctly listed with proper classes and player names.
- **Notes:** No issues. Correct campaign.

---

## Tab: RECAP (`id="tab-recap"`)

### Section: The Story So Far (`id="recap"`)
- **Content:** Narrative prose recap of the session, starting with an epigraph about the golden serpent
- **Components:** Blockquote epigraph, multi-paragraph prose with decorative diamond separators, collapsible text with "Read Full Recap" button
- **Quality:** Excellent. Rich, literary prose covering the key beats -- temple entrance, gorallons, prism room, giant snake, looting, fireball, the sun going out. Well-written with a strong narrative voice.
- **Notes:** Text uses `font-size:1.05rem` throughout -- compliant. Drop cap uses `font-size:2.8rem` -- fine.

### Section: Timeline (`id="timeline"`)
- **Content:** Horizontal scrollable timeline of session events
- **Components:** 11 timeline events with colored dots indicating type (combat, exploration, climax), legend below
- **Quality:** Good. Events are specific to the session: Briefing, Potion Splash, Combat with Girallons, Mirror/Gold Puzzles, Opal Blinded, Zephyr Reliquary Removed, Skeleton Horde, Serpent/Mirror Alignment, Judgment Scale, T-Rex Stealth, Great Escape.
- **Notes:** No "Social" or "Puzzle" events despite having those legend categories. Minor mismatch between legend and actual events shown.

### Section: Table Energy Peaks (`id="hype"`)
- **Content:** Top 10 moments ranked by energy score (10-point scale)
- **Components:** 10 hype cards with rank, score, moment name, description, and type badge
- **Quality:** Excellent. All moments are specific and vivid: "The Escape by 4:20" (10/10), "Opal Crits the Snake Blind" (9/10), "Squirtons and Gushers" (8.5/10), "Bob Goes Batman" (8.5/10), etc.
- **Notes:** No issues. Strong, entertaining content.

### Section: Campaign Codex (`id="codex"`)
- **Content:** World reference encyclopedia with NPCs, locations, and artifacts
- **Components:** 3 subsections -- NPCs (9 entries), Locations (4 entries), Artifacts (7 entries). Each has icon, name, type, description. Artifacts have owner tags.
- **Quality:** Excellent. Thorough coverage of key NPCs (Fizzleblast, Niles, Tika, Jezebel, Blackwater, T-Rex, Snake, Gorallons, Charisma Company), locations (Temple, Shore, Royal Community College, Port Nyanzaru), and artifacts (Golden Snake Idol, Eye of the Serpent, Zephyr Reliquary, Scales of Justice, Staff of Healing, Belt of Hill Giant Strength, Cloak of the Bat).
- **Notes:** Belt item says "Hill Giant Strength" (STR 21) in codex but character profile for Opal says "Belt of Stone Giant Strength." DATA CONFLICT -- these are different items (Hill Giant = 21, Stone Giant = 23).

### Section: End Credits (`id="credits"`)
- **Content:** Cinematic scrolling credits sequence
- **Components:** Scrolling viewport with auto-animation, cast entries (5 players), DM credit (Blue Orbit / Brandon), "By the Numbers" stats grid, special thanks list, music arc (empty), final quote, post-credits teaser
- **Quality:** Good. Cinematic presentation is polished. The "pause on hover" UX is nice.
- **Notes:**
  - Credits say "Nat 20s: 0 / Nat 1s: 1 (Opal, mirror push -- went blind)" -- this contradicts the analytics which show Opal had 4 nat 20s (skill checks). The credits appear to only count combat attack nat 20s = 0, which is confusing.
  - DM credit has redundant text: "Blue Orbit (Brandon)" appears twice (once as name, once as note).
  - CSS line 3323 has a syntax error: `font-size', '1rem, 2vw, 1.1rem);` -- should be `font-size: clamp(1rem, 2vw, 1.1rem);`. This is a CSS BUG.

---

## Tab: STATS (`id="tab-stats"`)

### Section: Stat Cards (`id="stat_cards"`)
- **Content:** 5 player performance stat cards (flat layout, no flip)
- **Components:** Each card has avatar, name, class/player, stats (Words Spoken, Kills, Damage Dealt, Hit Rate, Crits, Times Downed, RP Score), MVP badge, table role. Stats use count-up animation.
- **Quality:** Good. All 5 players present: Moor (7.8 MVP, The Protector), Opal (8.10, Comic Relief), Aramil (7.35, The Face), Lavender (8.40, The Strategist), Bob (8.40, The Lone Wolf).
- **Notes:** Card order is Moor, Opal, Aramil, Lavender, Bob -- not ranked by MVP score. Lavender and Bob are tied at 8.40 but appear 4th and 5th. Consider ordering by MVP rank.

### Section: MVP Leaderboard (`id="mvp"`)
- **Content:** Full MVP ranking with expandable detail panels, category awards, and meta-stats
- **Components:** 5-row leaderboard (Lavender #1, Bob #2, Opal #3, Moor #4, Aramil #5), each with expandable detail showing 6 mini-stats + 5 category bar charts + highlight quote. MVPExplainer sidebar. Category Awards grid (6 awards). Meta-stats row (Tightest Race, Biggest Gap, Most Balanced, Most Specialized).
- **Quality:** Good. Comprehensive system. Category breakdowns are well-structured.
- **Notes:**
  - FONT-SIZE VIOLATION: `font-size:0.75em` used 6 times in the category awards for player name parentheticals like "(Josh)", "(Kyle 1)", "(Kelsey)". This is approximately 12px at typical parent sizes. **Should be at least 1rem.**
  - MVP explainer descriptions have awkward phrasing: "Bob's Bob was the MVP of the actual heist" -- the possessive + name repetition reads poorly.

### Section: Combat Dashboard (`id="combat"`)
- **Content:** Combat analytics with lethality index and glass cannon ratings
- **Components:** Lethality Index (4 encounters with danger meters), Glass Cannon ratings (per-player damage dealt vs taken ratios)
- **Quality:** Good. Encounters are specific: Beach Ambush (50/100), Gas Chamber (30/100), Giant Constrictor Snake (90/100), T-Rex Escape (50/100).
- **Notes:** No issues found.

### Section: The Healer's Burden (`id="healer"`)
- **Content:** Healing economy analysis
- **Components:** Summary stats (171 HP taken, 148 HP healed, 0.87 ratio, 1 downed, B- sustainability), damage-vs-healing bars per player, healer player cards
- **Quality:** Good. Moor-centric as expected (he did all 148 HP of healing).
- **Notes:** No issues.

### Section: Dice Luck Tracker (`id="dice"`)
- **Content:** Dice analytics with distributions, luck ratings, and charts
- **Components:** Hero stats row, player luck cards, embedded Chart.js charts (histogram, pie, line)
- **Quality:** Good content. Comprehensive dice analysis with 60 d20 rolls tracked.
- **Notes:**
  - **CRITICAL BUG -- WRONG CAMPAIGN DATA:** The dice histogram chart (line ~17085) uses dataset labels "Lane (n=10)", "Nywen (n=4)", "Valerie (n=3)", "Landolf (n=1)" -- these are WHISPERS BEYOND THE VALE characters, NOT Fizzleblast characters. The chart data is from the wrong campaign entirely. This chart shows 4 Whispers characters instead of the 5 Fizzleblast characters (Moor, Aramil, Opal, Lavender, Bob).
  - **FONT-SIZE VIOLATION:** Chart.js legend labels use `size: 12` (12px) on lines 17022 and 17093. Should be minimum 14.
  - The pie chart (line 17022) also uses `size: 12` for legend labels.

---

## Tab: ANALYSIS (`id="tab-analysis"`)

### Section: Combat Replay Timeline (`id="combat_replay"`)
- **Content:** Turn-by-turn combat replay across all encounters
- **Components:** Summary stats (4 encounters, 8 rounds, 28 turns), legend, expandable encounter panels with per-turn breakdowns
- **Quality:** Good. Detailed turn-by-turn actions for each encounter.
- **Notes:** No issues.

### Section: Session Pacing Stats (`id="pacing"`)
- **Content:** Session pacing analysis
- **Components:** Summary cards (runtime ~4h, 9 scenes, 10/10 peak energy), scene-by-scene breakdown
- **Quality:** Good. Covers the full session arc with energy scores per scene.
- **Notes:** No issues.

### Section: Growth Report Cards (`id="growth"`)
- **Content:** Character development analysis with letter grades
- **Components:** Growth cards for each character with radar chart SVGs showing 7 dimensions, letter grades per dimension, and overall growth assessment
- **Quality:** Good. Each character has a personalized growth assessment with specific session references.
- **Notes:** No issues.

### Section: Party Chemistry (`id="chemistry"`)
- **Content:** Pair-by-pair chemistry analysis
- **Components:** Summary stats (~114 exchanges, 6.9/10 avg chemistry, 8.5/10 consensus health), pair analysis cards with SVG score rings, chemistry types, justifications, best moments, and quotes
- **Quality:** Good. All major pair combinations analyzed with specific session evidence.
- **Notes:** No issues.

### Section: Personality Profiles (`id="personality"`)
- **Content:** Psychological analysis (MBTI, Enneagram, Big Five) based on session behavior
- **Components:** Expandable cards for each character with MBTI type, Enneagram, nickname, fictional character comparison, and detailed trait breakdown
- **Quality:** Good. Moor (ISTJ 1w9, "Geralt of Rivia"), Aramil (ENTP 3w4, "Belloq"), Opal (ESFP 7w8, "Kronk"), Lavender (ENFJ 2w3, "Hermione Granger"), Bob (ISTP 5w6, "Bilbo Baggins").
- **Notes:** No issues.

### Section: Dark Triad Analysis (`id="dark-triad-amplified"`)
- **Content:** Narcissism, Machiavellianism, and Psychopathy trait scoring
- **Components:** Cards for each character with standard/amplified bar charts for each trait, scores, evidence quotes
- **Quality:** Good. Each character scored with session-specific evidence.
- **Notes:** No issues.

### Section: Gameplay Analytics (`id="analytics"`)
- **Content:** Comprehensive gameplay metrics dashboard
- **Components:** Multiple analytics cards organized by category: Action Economy Breakdown (table), Skill Check Leaderboard (table + nat 20/1 callouts), Resource Burn Rate (table), Lethality Index (meter + table), Actually Useful Index (table + MVP grid), Party Chemistry Stats (table), Glass Cannon Rating (table), Dice Luck Tracker (table)
- **Quality:** Good. 21 metrics analyzed. Tables are well-structured with per-character breakdowns.
- **Notes:** Aramil's damage is listed as "0" in Glass Cannon table but "6" in his stat card. Minor data inconsistency -- the 6 damage was likely Eldritch Blast damage that missed (stat card counts "dealt" broadly, analytics counts hits only).

### Section: Emotional Arc Sentiment (`id="sentiment"`)
- **Content:** Session emotional arc across 7 acts
- **Components:** D3-rendered sentiment waveform chart, act detail panel (click/hover), range summary
- **Quality:** Good. 7 acts tracked with specific emotional descriptors and key moments.
- **Notes:** No issues.

### Section: Leeroy Jenkins Index (`id="leeroy"`)
- **Content:** Analysis of impulsive/reckless decisions
- **Components:** Ranked leaderboard with expandable detail panels showing each "Leeroy moment" -- situation, action, consequence, outcome rating (Brilliant/Acceptable/Problematic)
- **Quality:** Good. Specific moments with full context: Moor's Mirror Angle, Moor's Scale Yoink, etc.
- **Notes:** No issues.

### Section: Session Conspiracy Board (`id="conspiracy"`)
- **Content:** Conspiracy-style analysis of session mysteries
- **Components:** Central mystery card ("WHO ACTUALLY BENEFITS FROM THE GOLDEN SNAKE IDOL BEING REMOVED"), 9 evidence nodes with 6 active connections
- **Quality:** Good. Focuses on the core mystery: did Fizzleblast know what would happen? Aramil's secret theft. The sun going out.
- **Notes:** No issues. This was previously reworked to reduce node count.

---

## Tab: MOMENTS (`id="tab-moments"`)

### Section: Quote Book (`id="quotes"`)
- **Content:** 18 collected quotes from the session
- **Components:** Filter buttons (All, Funniest, Most In Character, Most Dramatic, Most Unhinged, Most Creative), quote cards with text, speaker, fire rating, context, and category tag
- **Quality:** Excellent. Quotes are genuinely funny and well-selected: "Get fucked, Advil!", "If the men find out we can shapeshift...", "I hate mirrors! Hold this mirror!", "And how many squirtons in a gusher?", "I'm, uh... Married."
- **Notes:** No issues.

### Section: Session Awards (`id="awards"`)
- **Content:** 10 session awards/superlatives
- **Components:** Award cards with icon, title, winner, description, and runner-up
- **Quality:** Good. Awards include MVP (Bob), Best One-Liner (Moor), Best Tactical Call (Lavender), etc.
- **Notes:** Awards MVP goes to Bob but the MVP Leaderboard section has Lavender at #1 (tied with Bob at 8.40). This could be intentional (different criteria) but may confuse readers.

### Section: The Biggest Moment (`id="moments"`)
- **Content:** Single featured moment with impact score
- **Components:** Featured moment card with title, description, impact score (45/50), involved character chip
- **Quality:** Good. "Aramil secretly pried the golden eye from the Snake Idol" -- 45/50 impact.
- **Notes:** No issues.

### Section: Post-Session Interviews (`id="interviews"`)
- **Content:** AI-generated in-character interviews for each PC
- **Components:** AI disclaimer badge, character summary chips (showing question count per character), expandable interview Q&A sections per character
- **Quality:** Good. Each character has 6-7 interview questions. Interviews are conducted by "Elswyth Pattle, field chronicler for Mercenaries, Murders, and Mothers-in-Law Monthly."
- **Notes:** No issues.

### Section: Session Soundtrack (`id="music"`)
- **Content:** Character theme songs with embedded Suno players
- **Components:** Suno embed cards for each character's theme song with genre labels
- **Quality:** Good. All 5 characters have theme songs: Moor (Sacred Hymnal Orchestral), Aramil (Vaudeville Villain Waltz), Opal (80s Girl Power), Lavender (genre TBD), Bob (genre TBD).
- **Notes:** Embedded iframes depend on external Suno service availability.

### Section: Session Drinking Game (`id="drinking"`)
- **Content:** "How drunk would you have been?" drinking game analysis
- **Components:** Player scoreboard cards, rules grid, per-rule tallies
- **Quality:** Good. Entertaining content with specific session-triggered rules.
- **Notes:** No issues.

### Section: Previously On... (`id="previously_on"`)
- **Content:** DM read-aloud recap script for the next session
- **Components:** Performance notes (DM-only), collapsible script text with musical stage directions, formatted as a dramatic reading
- **Quality:** Excellent. Full dramatic script with stage directions, music cues, pacing notes. Very polished.
- **Notes:** No issues.

### Section: Follow-Up Scenarios (`id="followup"`)
- **Content:** Post-mortem analysis + alternate universe hooks
- **Components:** Post-mortem grid (what went right/wrong), 3 alternate universe scenario cards
- **Quality:** Good. Explores "what if" scenarios for campaign continuation.
- **Notes:** No issues.

### Section: DM Report Card (`id="dm_thanks"`)
- **Content:** DM quality assessment
- **Components:** Overall score (8.7/10, A+), session stats (duration, laughter instances), graded categories (Encounter Design, Narrative, Pacing, NPC Performance, etc.), strengths/areas for improvement
- **Quality:** Good. Balanced assessment with specific evidence.
- **Notes:** No issues.

---

## Tab: CHARACTERS (`id="tab-characters"`)

### Section: Character Profiles (`id="characters"`)
- **Content:** Full character dossiers for all 5 PCs
- **Components:** Character selector tabs (Moor, Aramil, Opal, Lavender, Bob), detailed profile panels for each with: hero header (initial, name, class, player, badges), signature moment, stat boxes (4 key stats), character description, personality traits, notable gear (3 items each), relationships (4 per character), epigraph quote
- **Quality:** Excellent. Deeply detailed profiles with campaign-specific information. Each character has a unique personality, memorable gear, and specific relationship descriptions.
- **Notes:**
  - Moor's profile says "Dragonborn Cleric -- Life Domain -- Level 3" -- consistent.
  - Aramil listed as "Kyle 2" (playing two characters for one player Kyle).
  - Bob's profile has the shortest character note: "Bob is very short. He wears a backpack festooned with gear and a hood so deep that you can only see the shine in his eyes." -- feels slightly thin compared to other profiles.

---

## Tab: LORE (`id="tab-lore"`)

### Section: The Verdant Codex (`id="lore_world"`)
- **Content:** World wiki / lore encyclopedia
- **Components:** Tome-styled layout with sidebar table of contents, 31 lore entries covering Threats, Locations, Factions, Items & Quests
- **Quality:** Good. Styled as an in-world book/tome.
- **Notes:** No issues.

### Section: Character Backstories (`id="lore_backstory"`)
- **Content:** Extended character backstories
- **Components:** Tab bar for selecting character, 5 characters with 35 total story sections
- **Quality:** Good. Extensive backstory content for each character.
- **Notes:** No issues.

### Section: In-World Documents (`id="lore_documents"`)
- **Content:** 6 in-world documents (letters, scrolls, inscriptions)
- **Components:** Expandable document cards with themed headers, document titles, and full text content. Includes Fizzleblast's Expedition Contract and other artifacts.
- **Quality:** Good. Documents are styled with appropriate iconography and themed as physical in-world objects.
- **Notes:** No issues.

### Section: Campaign Novelization (`id="lore_novelization"`)
- **Content:** 5-chapter prose retelling of the session
- **Components:** Epigraph quote, chapter list with expandable full text, styled with Cinzel/Crimson Text serif fonts
- **Quality:** Good. Chapter titles include "The Cashmere and the Clay" and others. Full literary prose retelling.
- **Notes:** CSS margin uses `0.85em` (line 11607) which is not a font-size, so this is compliant.

### Section: The Port Nyanzaru Chronicle (`id="lore_newspaper"`)
- **Content:** In-world newspaper reporting on the session events
- **Components:** Multi-page newspaper with page-turning navigation, themed as "Volume XLIV, Issue 312", headline about the sun being extinguished
- **Quality:** Good. Creative presentation as an in-world newspaper.
- **Notes:** No issues.

---

## Tab: VISUALS (`id="tab-visuals"`)

### Section: Who Talked to Whom (`id="viz_chord"`)
- **Content:** D3 chord diagram showing dialogue flow between speakers
- **Components:** Intro text, stats row, D3-rendered interactive chord diagram, speaker breakdown
- **Quality:** Good. 1,247 total utterances across 6 speakers (5 PCs + DM).
- **Notes:** No issues.

### Section: Session Pacing (`id="viz_waveform"`)
- **Content:** Session pacing waveform visualization
- **Components:** Legend, D3-rendered waveform chart with hover tooltips, stats summary, detail panel
- **Quality:** Good. 50 segments, 34,280 words, 4h runtime.
- **Notes:** No issues.

### Section: Player Synergy (`id="viz_synergy"`)
- **Content:** Pair synergy visualization across 4 dimensions
- **Components:** D3-rendered synergy chart with tab filters, sidebar detail panel, tooltip
- **Quality:** Good. Group overall 6.1/10.
- **Notes:** Synergy tooltip CSS has `font-size: 14px` -- this is compliant (minimum met).

### Section: DM Fairness (`id="viz_radar"`)
- **Content:** Radar chart showing DM attention distribution across 5 fairness axes
- **Components:** SVG radar chart, context banner, session type badge, player cards with per-axis scores
- **Quality:** Good. 5 players scored across Speaking Time, Plot Relevance, Combat Spotlight, RP Engagement, Mechanical Engagement.
- **Notes:** No issues.

### Section: Session Timeline (`id="viz_radial"`)
- **Content:** Concentric radial timeline visualization
- **Components:** 4-ring concentric D3 chart, clickable segments, legend with filter toggles, sidebar detail
- **Quality:** Good. 36 segments across 4 rings.
- **Notes:** No issues.

### Section: NPC Connections (`id="viz_entity"`)
- **Content:** Entity relationship map (NPC network graph)
- **Components:** D3 force-directed graph, zoom controls, entity legend, tooltip, sidebar stats
- **Quality:** Good. 28 entities, 89 relationships. Interactive zoom/drag.
- **Notes:** No issues.

### Section: Story Branches (`id="viz_tree"`)
- **Content:** Decision tree showing story branching points
- **Components:** D3 vertical tree layout, 8 decision points, 11 alternate branches, clickable nodes with glow animations
- **Quality:** Good. Divergence score 7.5/10.
- **Notes:** No issues.

---

## ISSUES SUMMARY

### CRITICAL BUGS

1. **WRONG CAMPAIGN DATA IN DICE CHART (line ~17085):** The dice histogram Chart.js chart uses Whispers Beyond the Vale character names (Lane, Nywen, Valerie, Landolf) instead of Fizzleblast characters (Moor, Aramil, Opal, Lavender, Bob). This is data from an entirely different campaign rendered in this dashboard.

2. **CSS SYNTAX ERROR (line 3323):** The `.credits-sub-title` rule has broken CSS: `font-size', '1rem, 2vw, 1.1rem);` -- this is not valid CSS. Should be `font-size: clamp(1rem, 2vw, 1.1rem);`.

### FONT-SIZE VIOLATIONS

3. **Chart.js legend labels at 12px (lines 17022, 17093):** Two Chart.js chart configurations use `size: 12` for legend label fonts. Should be minimum 14.

4. **0.75em font-size in MVP Category Awards (line 3969, 6 occurrences):** The player name parentheticals "(Josh)", "(Kyle 1)", "(Kelsey)" use `font-size:0.75em`. At typical parent sizes, this renders below 14px. Should be `font-size:1rem` or removed.

### DATA INCONSISTENCIES

5. **Nat 20 count conflict:** Ticker says "Opal rolls 4 natural 20s", Analytics confirms 4 nat 20s on skill checks. Credits section says "Nat 20s: 0". The credits section appears to only count combat attack roll nat 20s, but this creates confusion without clarification.

6. **Belt item name inconsistency:** Codex says "Belt of Hill Giant Strength" (STR 21), but Opal's character profile says "Belt of Stone Giant Strength" (STR 23). These are different D&D items.

7. **Awards MVP vs Leaderboard MVP:** The Awards section gives MVP to Bob, while the MVP Leaderboard has Lavender at #1 (tied 8.40 with Bob). While potentially intentional (different evaluation criteria), this is confusing.

8. **Aramil damage conflict:** Stat card shows 6 damage dealt, Glass Cannon table in Analytics shows 0 damage. The 6 is likely Eldritch Blast damage from attack rolls, while the 0 may only count hits.

### MINOR ISSUES

9. **DM credit duplication (line 3750-3751):** "Blue Orbit (Brandon)" appears as both `credits-dm-name` and `credits-dm-note` -- the note should be different descriptive text.

10. **CSS comment references Whispers (line 688):** Comment says "Flip-card layout (default Whispers)" -- this is a cosmetic issue in a CSS comment, not a functional bug.

11. **Timeline legend mismatch:** Timeline has legend entries for "Social" and "Puzzle" event types, but no timeline events use those categories.

12. **MVP explainer awkward phrasing:** Descriptions like "Bob's Bob was the MVP of the actual heist" have name duplication.

13. **Bob's character profile is thinner than others:** His description is only two sentences compared to full paragraphs for other characters.

---

## SECTION COUNT BY TAB

| Tab | Sections | Section IDs |
|-----|----------|-------------|
| RECAP | 5 | recap, timeline, hype, codex, credits |
| STATS | 5 | stat_cards, mvp, combat, healer, dice |
| ANALYSIS | 10 | combat_replay, pacing, growth, chemistry, personality, dark-triad-amplified, analytics, sentiment, leeroy, conspiracy |
| MOMENTS | 9 | quotes, awards, moments, interviews, music, drinking, previously_on, followup, dm_thanks |
| CHARACTERS | 1 | characters |
| LORE | 5 | lore_world, lore_backstory, lore_documents, lore_novelization, lore_newspaper |
| VISUALS | 7 | viz_chord, viz_waveform, viz_synergy, viz_radar, viz_radial, viz_entity, viz_tree |
| **TOTAL** | **42** (37 `<section>` tags + hero + ticker + tab-bar + nav + theme-switcher) | |
