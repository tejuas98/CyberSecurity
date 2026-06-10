# SurakshaAPK — Human-Made SIH-Style Revision Guide

This guide is for converting the current SurakshaAPK PPT from a **card-heavy / AI-generated web-dashboard look** into a **human-made SIH-style technical submission deck**.

Current problem: the deck has strong content, but too many slides look like clean generated UI sections with repeated cards, chips, tiny text, emojis, and large empty boxed areas.

Target style:

> Dense but readable. Technical but not messy. More like a real system design submission with diagrams, artifacts, flowcharts, outputs, tables, and prototype mockups.

---

# 1. Why the current deck still feels AI-generated

## Main causes

1. **Too many identical rounded cards**  
   Every slide uses the same card/panel pattern. It starts looking generated.

2. **Inline emojis/icons in text**  
   Examples like `APK`, `Bank`, `Risk`, `GenAI` with emoji icons inside sentences make the deck look web/AI-generated.

3. **Too many tiny chips**  
   Chips are good, but too many small pills make slides look like SaaS dashboards.

4. **Scrollbars inside panels**  
   Any scrollable panel inside a PPT-style slide immediately looks like a webpage, not a presentation.

5. **Text is too small in tables and flowcharts**  
   Judges will not zoom. If it cannot be read in presentation view, it should be enlarged or simplified.

6. **Too much perfect symmetry**  
   AI decks often use perfect equal cards, perfect spacing, and repeated component styles. SIH-winning decks often feel more manually composed.

7. **Not enough concrete artifacts**  
   Winning decks show screenshots, mockups, logs, diagrams, logos, workflows, cost/feasibility tables, etc.

---

# 2. Global rules to make the PPT feel human-made

## Rule 1: Remove inline emojis from all slide text

Remove emojis/icons from sentences like:

```text
SurakshaAPK uses GenAI to explain APK evidence
```

Do not write:

```text
SurakshaAPK uses 🧠 GenAI to explain ☁ APK evidence
```

Use icons only as separate visual elements, not inside normal text.

---

## Rule 2: No internal scrollbars

Any panel with a scrollbar must be redesigned.

If making slides through HTML/CSS, remove:

```css
overflow: auto;
overflow-y: scroll;
```

Use:

```css
overflow: visible;
```

or reduce content/font size until everything fits.

In PowerPoint, no textbox should look scrollable.

---

## Rule 3: Use one big visual per slide

Every slide should have one dominant artifact:

| Slide Type | Main Artifact |
|---|---|
| Problem | fraud flow + fake KYC phone |
| Gaps | challenge-response table + intent gap |
| Solution | feature list + pipeline + prototype mockups |
| Architecture | decision flowchart |
| Bank profile | JSON + official vs suspicious comparison |
| Static/Dynamic | APK tree + runtime workflow/logs |
| Evidence graph | source-to-sink graph |
| GenAI/Risk | risk gauge + report preview |
| Outputs | report mockup + IOC/YARA/SIEM snippets |
| Dataset | dataset table + validation pipeline |
| Final | demo workflow + impact roadmap |

---

## Rule 4: Use fewer colors per slide

Use max 4 active colors per slide:

```text
Navy: #0B1F3A
Blue: #005BAC
Green: #00A676
Orange: #E85D04
Red only for critical/risk
```

Avoid rainbow chips everywhere.

---

## Rule 5: Add prototype/mockup artifacts

To avoid AI-generated feel, add product-like evidence:

- upload dashboard mockup
- terminal log
- evidence graph viewer
- risk report preview
- IOC JSON
- YARA rule
- fake KYC APK phone mockup
- report/export panel

Even if prototype is not ready, label them honestly:

```text
Prototype UI Mockup
Demo Screen Preview
Synthetic fraud APK UI example
```

---

## Rule 6: Use SIH-style footer

Keep the footer on all slides:

```text
SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1
```

Blue footer strip:

```text
#005BAC
```

White text, page number at right.

---

# 3. Recommended slide reduction / merging

Your current 15 slides are detailed but can feel too much. To make it tighter and less repetitive, use one of these options.

---

## Option A — Keep 15 slides, but simplify visuals

Keep current structure, but make each slide less card-heavy and remove emojis/scrollbars.

Best if you already built all slides and do not want major restructuring.

---

## Option B — Recommended 12-slide version

This is stronger and more balanced.

| New Slide | Merges From Current | Title |
|---|---|---|
| 1 | 1 | Title & Overview |
| 2 | 2 | Problem Understanding & Fraud Landscape |
| 3 | 3 | Analyst Bottleneck & Current Issues |
| 4 | 4 | Proposed Solution + Prototype Preview |
| 5 | 5 | Decision-Based System Architecture |
| 6 | 6 + 9 | Bank Profile Adapter + Evidence Graph |
| 7 | 7 + 8 | Static & Dynamic Analysis Engines |
| 8 | 10 + 12 | GenAI, Risk Scoring & Report Outputs |
| 9 | 11 | Technical Stack + Deployment Modes |
| 10 | 13 | Dataset & Validation Plan |
| 11 | 14 | Research, Comparison & Feasibility |
| 12 | 15 | Demo Strategy, Use Cases & Impact |

### Why this is better

- Less repetition.
- Fewer slides for judges to skim.
- Stronger technical density.
- Related ideas are together.
- More like SIH-winning decks.

---

## Option C — 13-slide balanced version

If you do not want to merge too much:

| Slide | Title |
|---|---|
| 1 | Title & Overview |
| 2 | Problem Understanding |
| 3 | Current Gaps |
| 4 | Proposed Solution |
| 5 | System Architecture |
| 6 | Bank Profile Adapter |
| 7 | Static + Dynamic Analysis |
| 8 | Evidence Graph |
| 9 | GenAI + Risk + Outputs |
| 10 | Tech Stack |
| 11 | Dataset + Validation |
| 12 | Research + Comparison + Feasibility |
| 13 | Demo + Impact + Closing |

This is also good.

---

# 4. Slide-by-slide revision notes for the current deck

---

# Slide 1 — Title & Overview

## Current status

Mostly good after revision.

## Keep

- Hackathon title
- Problem context
- SurakshaAPK name
- terminal preview
- pipeline
- footer

## Fix

- Ensure official package is exactly:

```text
com.boi.ua.android
```

- Remove all emojis from terminal/text.
- Keep title block slightly asymmetric, not perfect landing page style.
- Use one small output preview card if space allows.

## Recommended final look

```text
Top: Hackathon title
Left: problem/team context
Right: terminal preview + demo output preview
Bottom-left: SurakshaAPK title + pitch
Bottom: pipeline
Footer
```

---

# Slide 2 — Problem Understanding & Fraud Landscape

## Current status

Good. It has enough content now.

## Keep

- Problem Statement Coverage Map
- Typical Fraud APK Kill Chain
- Fake KYC phone mockup
- High-risk behavior row
- Why this matters strip

## Fix

1. Change title of flowchart to:

```text
Typical Fraud APK Kill Chain
```

2. Ensure final flow box says:

```text
[07] Unauthorized Transaction
```

3. Make behavior cards evidence-style:

```text
E1: OTP Theft
E2: Overlay Attack
E3: Accessibility Abuse
E4: C2 Exfiltration
E5: Impersonation
```

4. Add small source note under phone:

```text
Example based on common fake KYC lure patterns
```

5. Remove any emoji inside body text.

## Optional improvement

Add small icon-only visuals beside flow steps: message, APK, lock, server, warning. Use PowerPoint icons, not emojis.

---

# Slide 3 — Analyst Bottleneck & Current Core Issues

## Current status

Strong. Around 9/10.

## Keep

- Manual APK analysis flow
- Current issues vs SurakshaAPK response table
- Permission ≠ malicious intent panel
- Bottom intent statement

## Fix

1. Remove all inline emojis.
2. Ensure no scrollbars.
3. Fix capitalization:

```text
Selective dynamic validation
```

not

```text
Selective dynamic Validation
```

4. Shorten bottom strip:

```text
SurakshaAPK converts raw APK indicators into evidence-backed fraud behavior chains.
Current tools find indicators; SurakshaAPK proves intent.
```

## Do not redesign

This slide is already strong.

---

# Slide 4 — Proposed Solution: SurakshaAPK

## Current issue

Content is good, but visual still feels generated because of emojis, too many bars, and tiny prototype mockups.

## Must fix

1. Remove all inline emojis.
2. Remove scrollbar from left panel.
3. Reduce feature bars from 7 to 6.
4. Make prototype screenshots bigger.
5. Use only 2 large prototype previews instead of 3 tiny ones.

## Replace left feature list with 6 bars

```text
Secure APK / link intake with SHA-256 hashing
Static reverse engineering of manifest, code, APIs and URLs
Bank Profile Adapter for BOI-specific impersonation checks
APK Fraud Evidence Graph for source-to-sink attack chains
Selective dynamic validation with fake OTP and sinkhole triggers
Local GenAI reports + risk score + CERT-In/RBI-ready outputs
```

## Improve pipeline with outputs

```text
L1 Static Decomposition
Manifest • Permissions • APIs • URLs • Certificates
Output: static_features.json

L2 Selective Dynamic Sandbox
Fake OTP • Overlay • Accessibility • Sinkhole
Output: runtime_trace.json

L3 GenAI Evidence Explanation
Code intent • MITRE mapping • Threat summary
Output: threat_summary.md

L4 Risk + Compliance Reports
0–100 score • Confidence • IOCs • Report
Output: report.pdf + iocs.json
```

## Prototype mockups to show

Use 2 bigger mockups:

### Upload Dashboard

```text
SurakshaAPK Dashboard
[Drop APK here]
BOI_KYC_Update.apk
Mode: Local Offline
Bank Profile: Bank of India
[Analyze APK]
```

### Risk Report

```text
Risk Score: 87/100
Confidence: 92%
Verdict: CRITICAL
Evidence: E1, E2, E3
Exports: PDF | IOC JSON | YARA
```

---

# Slide 5 — System Architecture

## Current status

Current phase-card version looks bad and generated.

## Required redesign

Use a **decision-based flowchart** with yes/no branches.

## New title

```text
System Architecture: Decision-Based APK Investigation Flow
```

## Main flow

```text
[APK / Link Intake]
        ↓
[Secure Hashing + Quarantine]
        ↓
◇ Duplicate hash found?
   ├─ YES → [Return Existing Report]
   └─ NO
        ↓
[Load BOI Bank Profile]
        ↓
[Static Analysis]
        ↓
◇ Decompiler success?
   ├─ NO → [Fallback: Smali / APKiD / Packer Flag] → [Human Analyst Queue]
   └─ YES
        ↓
[Build Static Evidence Graph]
        ↓
◇ Static risk ≥ threshold OR bank impersonation?
   ├─ NO → [Low-Risk Report]
   └─ YES
        ↓
[Generate Dynamic Trigger Plan]
        ↓
[Selective Dynamic Sandbox]
        ↓
◇ Runtime behavior confirmed?
   ├─ NO → [Suspicious / Analyst Review]
   └─ YES
        ↓
[Update Evidence Graph with Runtime Proof]
        ↓
[Risk Scoring Engine]
        ↓
◇ Critical risk?
   ├─ YES → [SOC Alert + CERT-In/RBI Draft]
   └─ NO → [Standard Investigation Report]
        ↓
[Local GenAI Report Generation]
        ↓
[Exports: PDF | IOC JSON | YARA | SIEM]
```

## Right artifact panel

```text
Artifacts Generated
sha256.txt
manifest.json
static_features.json
evidence_graph.json
trigger_plan.json
runtime_trace.json
risk_report.json
report.pdf
iocs.json
yara_rule.yar
siem_event.json
```

## Privacy chips

```text
Local/offline
No raw APK egress
Restricted network
Sinkholed C2
Encrypted quarantine
Audit logs
Metadata-only cloud optional
```

## Visual advice

- Use diamonds for decisions.
- Use green `YES` branches and red/orange `NO` branches.
- Avoid giant phase boxes.
- Avoid dashed huge lab boundary.
- Avoid scrollbars.

---

# Slide 6 — Bank Profile Adapter & BOI Threat Intelligence

## Current status

Good structure, but too generated because of emojis and large clean panels.

## Keep

- BOI profile JSON
- Detection logic flow
- Official vs suspicious table
- Bottom multi-bank scalability line

## Fix

1. Remove emojis from title and text.
2. Reduce JSON height if too empty.
3. Make detection logic more decision-like with yes/no labels.
4. Add small fake KYC phone mini-card if space allows.
5. Highlight `com.boi.ua.android` and `com.fake.boi.kyc` clearly.

## Improve detection flow

```text
Suspicious APK uploaded
↓
Claims BOI identity?
  NO → Generic APK scan
  YES → Continue
↓
Package/certificate mismatch?
↓
Uses KYC/loan/account-freeze bait?
↓
Collects OTP / credentials?
↓
Sends data to non-bank endpoint?
↓
High Risk: Bank Impersonation Fraud APK
```

---

# Slide 7 — Static Analysis Deep Dive

## Current status

Good concept but bad because of scrollbars and tiny middle pipeline.

## Must fix

1. Remove scrollbars.
2. Remove emojis.
3. Make center pipeline bigger.
4. Put toolchain logos/chips more visibly.
5. Add sample static JSON output.

## Add sample static output card

```json
{
  "permissions": ["RECEIVE_SMS", "SYSTEM_ALERT_WINDOW"],
  "urls": ["hxxps://unknown-c2.example/api"],
  "obfuscation_score": 0.72,
  "bank_profile_match": "BOI impersonation suspected"
}
```

## Better layout

```text
LEFT: APK tree
CENTER: static pipeline
RIGHT: feature matrix + sample JSON
BOTTOM: toolchain + output artifacts
```

---

# Slide 8 — Dynamic Analysis Deep Dive

## Current status

Good but runtime log card is too large and empty.

## Fix

1. Remove emojis from title/table/logs.
2. Make runtime log card smaller OR fill it with more realistic logs.
3. Add Android emulator/phone mockup.
4. Keep trigger table and runtime workflow.

## Add emulator mini mockup

```text
Controlled Emulator
Fake OTP received: 582194
Overlay permission requested
Network call captured
```

## Better right panel

Instead of one huge empty log panel, use:

```text
Top: Runtime Evidence Log
Bottom: Android Emulator Mockup
```

---

# Slide 9 — Evidence Graph

## Current status

Strong, but still has emojis and JSON panel too large/empty.

## Fix

1. Remove emojis from title and subtitle.
2. Make JSON text bigger.
3. Add a second mini-chain if space allows.
4. Keep bottom statement.

## Add second mini-chain

```text
BOI app launch → fake overlay → credential capture → non-bank endpoint
```

## Keep strong line

```text
SurakshaAPK detects malicious intent by proving behavior chains — not by blindly flagging dangerous permissions.
```

---

# Slide 10 — GenAI + Risk + Compliance

## Current status

Good structure, but too many boxes/chips and emojis.

## Fix

1. Remove emojis.
2. Add risk gauge visual.
3. Add GenAI output/report preview.
4. Reduce compliance text.

## Add risk gauge

```text
Risk Score: 87/100
CRITICAL
Confidence: 92%
```

Make it large and red/green.

## Add GenAI output preview

```text
AI Summary:
This APK exhibits OTP theft and overlay phishing behavior. Evidence E1 shows SMS_RECEIVED data is parsed and sent to a non-bank endpoint. Evidence E2 indicates fake login overlay indicators targeting the BOI profile.
```

## Strong guardrail

```text
GenAI writes the explanation. Deterministic engines decide the score.
```

---

# Slide 11 — Technical Stack

## Current status

Too empty on the right. Needs tech logos/icons.

## Fix

1. Add a full row/grid of technology logos or labeled chips.
2. Keep layered stack.
3. Add deployment modes.
4. Remove emojis.

## Tech chips to add

```text
Python
FastAPI
React
Next.js
Android
ADB
Frida
MITMProxy
JADX
AndroGuard
APKiD
YARA
Ollama
Llama
Docker
PostgreSQL
SQLite
PDF
JSON
```

## Better slide layout

```text
LEFT: layered architecture stack
RIGHT TOP: deployment modes
RIGHT BOTTOM: technology logo grid
BOTTOM: open-source-first + metadata-only cloud note
```

---

# Slide 12 — Output + Explainability + Bank Response

## Current status

Strong concept but small text and emojis make it look generated.

## Fix

1. Remove emojis.
2. Make report preview bigger and more realistic.
3. Reduce stakeholder matrix rows or font size.
4. Make IOC/YARA card readable.
5. Add export buttons visually.

## Add export buttons

```text
[PDF Report]
[IOC JSON]
[YARA Rule]
[SIEM Event]
[CERT-In Draft]
```

## Report preview should look like paper

Use white document card with header:

```text
SurakshaAPK Investigation Report
Risk: 87/100 CRITICAL
Confidence: 92%
Evidence: E1, E2, E3
Recommended Action: Block IOCs + SOC escalation
```

---

# Slide 13 — Dataset + Validation

## Current status

Actually one of the better slides. It is dense and useful.

## Fix

1. Remove emojis.
2. Make dataset table readable.
3. Keep validation metrics.
4. Keep safe obfuscation test.
5. Maybe add validation pipeline visual.

## Add validation pipeline

```text
Dataset → Feature Extraction → Evidence Chain Detection → Analyst Review → Metrics
```

## Keep warning

```text
No deployable malware is generated; only controlled synthetic samples are used for robustness testing.
```

---

# Slide 14 — Research + Comparison + Feasibility

## Current status

Good but comparison table may be too small.

## Fix

1. Remove emojis.
2. Make comparison table simpler.
3. Increase font size if possible.
4. Keep challenge/mitigation table.

## Optional simplification

Reduce comparison rows to 5:

```text
Static APK analysis
Triggered dynamic validation
Local/private deployment
Bank Profile Adapter
Evidence-grounded GenAI reports
```

This improves readability.

## Keep mature line

```text
SurakshaAPK does not replace existing tools; it integrates reverse-engineering evidence into a bank-specific investigation and reporting workflow.
```

---

# Slide 15 — Demo + Impact

## Current status

Good, but use-case cards are too empty and impact area is too clean.

## Fix

1. Remove emojis.
2. Add 2–3 prototype screenshots/mockups.
3. Make demo workflow more visually dominant.
4. Use a small roadmap.
5. Keep closing line.

## Recommended layout

```text
LEFT: demo workflow
CENTER: prototype screenshots
RIGHT: use cases + impact + roadmap
BOTTOM: why shortlist + closing line
```

## Prototype screenshots to include

- Upload dashboard
- Evidence graph viewer
- Risk report output

## Closing line

```text
SurakshaAPK helps banks move from reactive manual APK analysis to proactive, automated, evidence-based fraud defense.
```

---

# 5. Specific cleanup list for the whole deck

Do these globally:

## Remove all emojis in text

Search and remove symbols like:

```text
☁ 🏦 🧠 🛡 ⚙ ✅ ⭐ 🐞 🤖 🔑 📄
```

Use proper icons outside text if needed.

---

## Remove all scrollbars

No slide should show scrollbars inside any panel.

---

## Reduce chips by 30–40%

Only use chips for:

- capabilities
- privacy controls
- tech stack
- impact metrics

Do not chip every small phrase.

---

## Increase table readability

If table text is below 7 pt, simplify table.

---

## Use more artifacts

Add these across slides:

- terminal logs
- JSON snippets
- YARA snippet
- report preview
- phone mockup
- evidence graph
- tech logos/chips
- challenge/solution table

---

## Make prototype mockups bigger

Tiny mockups look decorative and fake. Use fewer, bigger mockups.

---

# 6. Final recommended action plan

## Step 1: Global cleanup

- Remove emojis.
- Remove scrollbars.
- Fix package `com.boi.ua.android` everywhere.
- Ensure project name is SurakshaAPK everywhere.

## Step 2: Fix worst slides first

Priority order:

1. Slide 5 architecture — redesign as decision flowchart.
2. Slide 4 proposed solution — remove scrollbar, make mockups bigger.
3. Slide 11 tech stack — add technology logos/chips.
4. Slide 15 final — add prototype screenshots and reduce empty cards.
5. Slide 8 dynamic — add emulator mockup / reduce empty log panel.

## Step 3: Decide slide count

If you want tighter deck, reduce to 12 slides using the merge plan.

If deadline is near, keep 15 slides and polish.

---

# 7. Final judge-style guidance

Your content is strong. The remaining problem is presentation style.

The deck should look like:

```text
technical submission + prototype evidence + manually drawn workflows
```

Not like:

```text
clean generated SaaS dashboard
```

The fastest way to fix that:

1. Use decision flowcharts.
2. Remove emojis and scrollbars.
3. Add prototype mockups/screens.
4. Add tech logos/chips.
5. Use fewer but larger diagrams.
6. Merge repetitive slides if possible.

If these changes are done, the deck will feel much closer to a human-made SIH finalist submission.
