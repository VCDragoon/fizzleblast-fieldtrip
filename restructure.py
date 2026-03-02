"""Restructure index_reimagined.html: rearrange tabs, merge sections, add mobile fixes."""
from __future__ import annotations
import re
import sys

INPUT = "index_reimagined.html"
OUTPUT = "index_reimagined.html"

# ---------------------------------------------------------------------------
# Read entire file
# ---------------------------------------------------------------------------
with open(INPUT, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")
total = len(lines)
print(f"Read {total} lines from {INPUT}")

# ---------------------------------------------------------------------------
# Phase 1: Parse file into regions
# ---------------------------------------------------------------------------
# Structure: HEADER ... <div class="tab-content" id="tab-X"> SECTIONS </div> ... FOOTER
# We need: header (everything before first tab-content), each tab block, footer (after last)

# Find all tab-content boundaries
tab_starts = []  # (line_idx, tab_id)
for i, line in enumerate(lines):
    m = re.match(r'\s*<div class="tab-content[^"]*"\s+id="(tab-\w+)"', line)
    if m:
        tab_starts.append((i, m.group(1)))

print(f"Found {len(tab_starts)} tabs: {[t[1] for t in tab_starts]}")

# Find the closing </div> for each tab-content
# Each tab ends at a standalone </div> line followed by the next tab-content or end of tabs
tab_blocks = {}  # tab_id -> (start_line, end_line) inclusive
for idx, (start, tab_id) in enumerate(tab_starts):
    if idx + 1 < len(tab_starts):
        # Find the </div> before the next tab-content
        next_start = tab_starts[idx + 1][0]
        # Walk backwards from next_start to find the closing </div>
        end = next_start - 1
        while end > start and lines[end].strip() == "":
            end -= 1
        if lines[end].strip() == "</div>":
            tab_blocks[tab_id] = (start, end)
        else:
            tab_blocks[tab_id] = (start, end)
    else:
        # Last tab - find its closing </div>
        # Search forward from start for standalone </div> after last </section>
        last_section_end = start
        for j in range(start, total):
            if "</section>" in lines[j]:
                last_section_end = j
        # The closing </div> should be shortly after
        end = last_section_end + 1
        while end < total and lines[end].strip() != "</div>":
            end += 1
        tab_blocks[tab_id] = (start, end)

for tab_id, (s, e) in tab_blocks.items():
    print(f"  {tab_id}: lines {s+1}-{e+1}")

# ---------------------------------------------------------------------------
# Phase 2: Extract sections from each tab
# ---------------------------------------------------------------------------
def extract_sections(tab_start, tab_end):
    """Extract sections within a tab block. Returns list of (section_id, content_lines)."""
    sections = []
    i = tab_start + 1  # Skip the <div class="tab-content"> line
    current_id = None
    current_lines = []
    divider_buffer = []

    while i <= tab_end:
        line = lines[i]

        # Check for section start
        m = re.match(r'\s*<section id="([^"]+)"', line)
        if m:
            # Save previous section if any
            if current_id:
                sections.append((current_id, current_lines))
            current_id = m.group(1)
            current_lines = list(divider_buffer) + [line]
            divider_buffer = []
            i += 1
            continue

        # Check for section divider (between sections)
        if 'section-divider' in line and current_id is None:
            divider_buffer.append(line)
            i += 1
            continue

        if current_id:
            current_lines.append(line)
            if line.strip() == "</section>":
                sections.append((current_id, current_lines))
                current_id = None
                current_lines = []
                divider_buffer = []
        else:
            # Between sections (dividers, whitespace)
            divider_buffer.append(line)

        i += 1

    # Save last section
    if current_id:
        sections.append((current_id, current_lines))

    return sections

all_sections = {}  # section_id -> list of lines
for tab_id, (s, e) in tab_blocks.items():
    sections = extract_sections(s, e)
    for sid, slines in sections:
        all_sections[sid] = slines
        print(f"    Extracted: {sid} ({len(slines)} lines)")

print(f"\nTotal sections extracted: {len(all_sections)}")

# ---------------------------------------------------------------------------
# Phase 3: Header and footer
# ---------------------------------------------------------------------------
first_tab_start = min(s for s, _ in tab_starts)
header_lines = lines[:first_tab_start]

last_tab_end = max(e for _, e in tab_blocks.values())
footer_lines = lines[last_tab_end + 1:]

print(f"Header: {len(header_lines)} lines")
print(f"Footer: {len(footer_lines)} lines")

# ---------------------------------------------------------------------------
# Phase 4: Merge sections
# ---------------------------------------------------------------------------
def get_section_inner(sid):
    """Get inner content of a section (between <section> and </section>)."""
    slines = all_sections.get(sid, [])
    # Find the <section> opening and </section> closing
    inner = []
    started = False
    for line in slines:
        if re.match(r'\s*<section id="', line):
            started = True
            continue
        if line.strip() == "</section>":
            break
        if started:
            inner.append(line)
    return inner

def merge_into(primary_sid, *visual_sids):
    """Merge visual section content into primary section before its </section>."""
    if primary_sid not in all_sections:
        print(f"  WARNING: {primary_sid} not found, skipping merge")
        return

    primary = all_sections[primary_sid]

    # Find the </section> line
    close_idx = None
    for i in range(len(primary) - 1, -1, -1):
        if primary[i].strip() == "</section>":
            close_idx = i
            break

    if close_idx is None:
        print(f"  WARNING: No </section> found in {primary_sid}")
        return

    # Collect visual content to insert
    insert_lines = []
    for vsid in visual_sids:
        if vsid not in all_sections:
            print(f"  WARNING: {vsid} not found, skipping")
            continue
        inner = get_section_inner(vsid)
        if inner:
            insert_lines.append(f'<div class="section-divider"></div>')
            insert_lines.append(f'<!-- Merged from {vsid} -->')
            insert_lines.extend(inner)
            print(f"  Merged {vsid} ({len(inner)} lines) into {primary_sid}")

    if insert_lines:
        # Insert before </section>
        new_primary = primary[:close_idx] + insert_lines + primary[close_idx:]
        all_sections[primary_sid] = new_primary

# Perform merges
print("\n=== MERGING SECTIONS ===")

# combat + combat_replay
merge_into("combat", "combat_replay")

# pacing + viz_waveform
merge_into("pacing", "viz_waveform")

# chemistry + viz_chord + viz_synergy
merge_into("chemistry", "viz_chord", "viz_synergy")

# dm_thanks + viz_radar
merge_into("dm_thanks", "viz_radar")

# codex + viz_entity
merge_into("codex", "viz_entity")

# Mark merged sections for removal (they're now embedded)
merged_away = {"combat_replay", "viz_chord", "viz_waveform", "viz_synergy", "viz_radar", "viz_entity"}

# Also viz_radial should already be gone, but mark it just in case
merged_away.add("viz_radial")

# ---------------------------------------------------------------------------
# Phase 5: Define new tab structure
# ---------------------------------------------------------------------------
new_tabs = [
    ("tab-recap", "RECAP", ["recap", "timeline", "hype", "previously_on", "credits"]),
    ("tab-stats", "STATS", ["stat_cards", "mvp", "dice"]),
    ("tab-analysis", "ANALYSIS", [
        "combat", "pacing", "growth", "chemistry",
        "personality", "dark-triad-amplified",
        "sentiment", "leeroy", "analytics", "dm_thanks"
    ]),
    ("tab-moments", "MOMENTS", ["quotes", "awards", "moments", "interviews", "music", "drinking"]),
    ("tab-characters", "CHARACTERS", ["characters"]),
    ("tab-lore", "LORE", [
        "codex", "lore_world", "lore_backstory", "lore_documents",
        "lore_novelization", "lore_newspaper", "conspiracy", "followup", "viz_tree"
    ]),
]

# ---------------------------------------------------------------------------
# Phase 6: Update header (tab buttons + nav links)
# ---------------------------------------------------------------------------
# Find and replace tab buttons
header_str = "\n".join(header_lines)

# Replace tab button row
old_buttons_pattern = r'(<div class="tab-bar"[^>]*>)(.*?)(</div>\s*<div class="tab-scroll")'
def make_tab_buttons(tabs):
    btns = []
    for i, (tid, label, _) in enumerate(tabs):
        tab_key = tid.replace("tab-", "")
        selected = "true" if i == 0 else "false"
        active = " active" if i == 0 else ""
        btns.append(f'  <button class="tab-btn{active}" data-tab="{tab_key}" role="tab" aria-selected="{selected}" onclick="switchTab(\'{tab_key}\')">{label}</button>')
    return "\n".join(btns)

# Find the tab buttons section
btn_start = None
btn_end = None
for i, line in enumerate(header_lines):
    if 'class="tab-bar"' in line:
        btn_start = i
    if btn_start is not None and '</div>' in line and 'tab-bar' not in line:
        btn_end = i
        break

if btn_start is not None:
    # Find all button lines between tab-bar start and its closing
    new_btn_lines = [header_lines[btn_start]]  # Keep the opening div
    for tid, label, _ in new_tabs:
        tab_key = tid.replace("tab-", "")
        active = " active" if tab_key == "recap" else ""
        selected = "true" if tab_key == "recap" else "false"
        new_btn_lines.append(f'  <button class="tab-btn{active}" data-tab="{tab_key}" role="tab" aria-selected="{selected}" onclick="switchTab(\'{tab_key}\')">{label}</button>')
    new_btn_lines.append("</div>")

    # Find the end of the button container
    j = btn_start + 1
    while j < len(header_lines) and not (header_lines[j].strip() == "</div>" and 'tab-bar' not in header_lines[j]):
        j += 1

    header_lines = header_lines[:btn_start] + new_btn_lines + header_lines[j+1:]
    print(f"\nUpdated tab buttons ({len(new_tabs)} tabs)")

# Now update nav links (the <a href="#section" data-tab="..."> links)
# Find the nav link block
nav_start = None
nav_end = None
for i, line in enumerate(header_lines):
    if '<a href="#' in line and 'data-tab=' in line:
        if nav_start is None:
            nav_start = i
        nav_end = i

if nav_start is not None:
    # Build new nav links
    nav_links = []
    section_labels = {
        "recap": "Recap", "timeline": "Timeline", "hype": "Hype",
        "previously_on": "Previously On", "credits": "Credits",
        "stat_cards": "Stat Cards", "mvp": "MVP", "dice": "Dice",
        "combat": "Combat", "pacing": "Pacing", "growth": "Growth",
        "chemistry": "Chemistry", "personality": "Personality",
        "dark-triad-amplified": "Dark Triad", "sentiment": "Sentiment",
        "leeroy": "Leeroy", "analytics": "Analytics", "dm_thanks": "DM Report",
        "quotes": "Quotes", "awards": "Awards", "moments": "Moments",
        "interviews": "Interviews", "music": "Music", "drinking": "Drinking",
        "characters": "Characters",
        "codex": "Codex", "lore_world": "World", "lore_backstory": "Backstory",
        "lore_documents": "Documents", "lore_novelization": "Novelization",
        "lore_newspaper": "Newspaper", "conspiracy": "Conspiracy",
        "followup": "Follow-Up", "viz_tree": "Story Branches"
    }

    for tid, label, sections in new_tabs:
        tab_key = tid.replace("tab-", "")
        for sid in sections:
            slabel = section_labels.get(sid, sid.replace("_", " ").title())
            nav_links.append(f'  <a href="#{sid}" data-tab="{tab_key}" style="display:none">{slabel}</a>')

    header_lines = header_lines[:nav_start] + nav_links + header_lines[nav_end+1:]
    print(f"Updated nav links ({len(nav_links)} links)")

# ---------------------------------------------------------------------------
# Phase 7: Assemble the new file
# ---------------------------------------------------------------------------
output_lines = list(header_lines)

for tab_idx, (tid, label, section_ids) in enumerate(new_tabs):
    tab_key = tid.replace("tab-", "")
    active = " active" if tab_key == "recap" else ""
    output_lines.append(f'<div class="tab-content{active}" id="{tid}">')

    for sec_idx, sid in enumerate(section_ids):
        if sid in merged_away:
            continue  # Already merged into another section
        if sid not in all_sections:
            print(f"  WARNING: Section '{sid}' not found in extracted sections!")
            continue

        # Add section divider between sections (not before first)
        if sec_idx > 0:
            output_lines.append('<div class="section-divider"></div>')

        # Add section content (skip leading dividers from extraction)
        slines = all_sections[sid]
        for line in slines:
            if 'section-divider' in line:
                continue  # Skip embedded dividers at start
            output_lines.append(line)
            break  # Found first non-divider line, now add the rest

        # Add remaining lines
        found_first = False
        for line in slines:
            if not found_first:
                if 'section-divider' not in line:
                    found_first = True
                    # Already added this line above
                continue
            output_lines.append(line)

    # Close tab-content
    output_lines.append("")
    output_lines.append("</div>")

# Add footer
output_lines.extend(footer_lines)

# ---------------------------------------------------------------------------
# Phase 8: Write output
# ---------------------------------------------------------------------------
output_content = "\n".join(output_lines)
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(output_content)

print(f"\nWrote {len(output_lines)} lines to {OUTPUT}")
print(f"Size: {len(output_content)} bytes ({len(output_content)/1024:.1f} KB)")
