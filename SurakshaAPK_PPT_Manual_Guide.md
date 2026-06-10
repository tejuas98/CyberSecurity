# SurakshaAPK PPT Manual Guide

**Project name:** SurakshaAPK  
**Subtitle:** Evidence-First GenAI Malware Investigator for Fraudulent Banking APKs  
**Hackathon:** PSB's Cybersecurity, Fraud & AI Hackathon 2026 in collaboration with IIT Hyderabad  
**Problem Statement:** PS1 — Harnessing Generative AI for Automated Reverse Engineering, Static and Dynamic Analysis, and Risk Scoring of Fraudulent Mobile Applications (APKs) and Malwares.

---

## 0. Overall PPT Style Direction

Your friends' PPTs look less AI-generated because they use:

- technical diagrams
- prototype screenshots/mockups
- technology logos/icons
- tables
- workflow diagrams
- flowcharts with arrows
- challenge vs solution tables
- output previews
- footer strip and page numbers

So SurakshaAPK PPT should be:

> **dense + visual + technical + manually designed**

Not minimal, not too much whitespace, not only bullets.

Every slide should have at least one concrete artifact:

| Slide Type | Artifact to Add |
|---|---|
| Problem slide | fraud flow + fake KYC phone mockup |
| Solution slide | prototype dashboard/report mockups |
| Architecture slide | system architecture + module icons |
| Static analysis | APK tree + sample JSON + tool icons |
| Dynamic analysis | emulator mockup + runtime logs |
| Evidence graph | source-to-sink graph + evidence JSON |
| GenAI/risk | GenAI I/O + risk gauge + compliance preview |
| Output slide | report preview + IOC/YARA/SIEM snippets |
| Dataset slide | dataset table + validation pipeline |
| Final slide | demo flow + roadmap + impact chips |

---

## 1. Global Visual Theme

### Background

Use cream/off-white:

```text
#F7F1E5
```

or

```text
#FAF6ED
```

### Main Colors

| Use | Color | Hex |
|---|---|---|
| Main title/navy | Dark Navy | `#0B1F3A` |
| Bank/primary blue | BOI Blue | `#005BAC` |
| Success/evidence | Cyber Green | `#00A676` |
| Warning/risk | Orange | `#E85D04` |
| Critical/malware | Red | `#DC2626` |
| Body gray | Slate Gray | `#475569` |
| Card fill | Soft White | `#FFFDF8` |
| Light border | Warm Gray | `#D8D2C4` |
| Terminal bg | Almost Black | `#101820` |
| Terminal bar | Charcoal | `#1F2937` |

### Fonts

Use only 2 fonts:

```text
Main: Aptos / Aptos Display
Code/terminal: Menlo or Consolas
```

### Font Sizes

| Element | Size |
|---|---:|
| Slide title | 30–34 |
| Subtitle | 12.5–14 |
| Section labels | 8.5–9.5 |
| Panel/card titles | 11–15 |
| Body text | 8–12 |
| Tables | 7–10 |
| Code/terminal | 7–9 |
| Footer | 8–9 |

### Footer Strip

Use on every slide except maybe title slide.

```text
SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1
```

- Fill: `#005BAC`
- Text: white
- Height: 0.25–0.35 inch
- Page number right side

---

## 2. Things NOT to Put in PPT

Avoid these because they reduce credibility:

```text
GPT-4 generates obfuscated malware variants
RBI Clause violated
100% detection / guaranteed detection
45-second full dynamic analysis
No competing team has this
100% open-source stack
RBI violation detected
Full production-ready system
Fake achieved accuracy like 94.3% unless tested
```

Use safer replacements:

| Avoid | Use Instead |
|---|---|
| GPT-4 generates malware variants | Safe synthetic obfuscation test on controlled APKs |
| RBI clause violated | Mapped to RBI/CERT-In incident-response requirements |
| 100% detection | Evidence-based risk scoring with confidence |
| 45-second full analysis | Fast static triage + selective dynamic validation |
| 100% open source | Open-source-first stack |
| LLM detects malware | LLM explains verified evidence |

---

## 3. Prototype Mockup Assets to Create Once and Reuse

Create these mockups manually in PowerPoint using shapes. Label as **Prototype UI Mockup** or **Demo Screen Preview** if not fully built.

### Mockup 1: Upload Dashboard

```text
SurakshaAPK Dashboard

[ Drop APK here ]
BOI_KYC_Update.apk
SHA-256: calculating...
Bank Profile: Bank of India
Mode: Local Offline
[ Analyze APK ]
```

### Mockup 2: Analysis Console

```text
[STATIC] Manifest parsed
[STATIC] RECEIVE_SMS detected
[STATIC] SYSTEM_ALERT_WINDOW detected
[GRAPH] Evidence E1 created
[RISK] Score: 87/100
[AI] Report generated
```

### Mockup 3: Evidence Graph Viewer

```text
SMS_RECEIVED → OTP Regex → AES Encode → HTTP POST → Unknown C2
```

### Mockup 4: Risk Report

```text
Risk Score: 87/100
Confidence: 92%
Verdict: Critical
Classification: Fake KYC Banking Trojan

Evidence:
E1 OTP Theft
E2 Fake Overlay
E3 Non-bank C2
```

### Mockup 5: Export Panel

```text
Export Options:
[Download PDF Report]
[Export IOCs JSON]
[Generate YARA Rule]
[SIEM JSON]
[CERT-In Draft]
```

---

# Final 15-Slide PPT Guide

---

# Slide 1 — Title & Overview

## Slide Title

```text
PSB's Cybersecurity, Fraud & AI Hackathon 2026
```

## Purpose

Establish hackathon, problem, project name, team, and technical credibility.

## Main Content

```text
in collaboration with IIT Hyderabad | Bank of India

PROBLEM CONTEXT

Problem Statement – Harnessing Generative AI for Automated Reverse Engineering,
Static & Dynamic Analysis, and Risk Scoring of Fraudulent APKs and Malwares

Domain: Cybersecurity • Fraud Prevention • Generative AI
Bank Profile: Bank of India | Official Package: com.boi.ua.android

Tejas | SSGBCE Bhusawal | DBATU
Contact: tejusj98@gmail.com

PROPOSED SOLUTION

SurakshaAPK
Evidence-First GenAI Malware Investigator for Fraudulent Banking APKs

SurakshaAPK analyzes suspicious APKs, builds evidence-based attack chains, uses GenAI to explain verified findings, assigns transparent risk scores, and generates bank-ready investigation reports.
```

## Terminal Mockup

```bash
$ surakshaapk analyze BOI_KYC_Update.apk --profile boi --mode local

[00:00] SHA-256 calculated
[00:02] Static scan: manifest + permissions parsed
[00:04] Bank profile loaded: com.boi.ua.android
[00:06] Evidence E1: SMS OTP access detected
[00:08] Evidence E2: overlay / fake login behavior
[00:10] Evidence E3: suspicious non-bank endpoint
[00:12] Risk Score: 87/100 | Confidence: 92%
[00:13] Verdict: CRITICAL Banking APK Fraud
[00:15] Exported: report.pdf | iocs.json | yara_rule.yar
```

## Bottom Pipeline

```text
Suspicious APK → Evidence Graph → Risk Score → GenAI Report → Bank Action
```

## Layout

```text
┌──────────────────────────────────────────────────────────────┐
│ PSB Hackathon title centered                                 │
│                                                              │
│ PROBLEM CONTEXT                    ┌ Terminal Preview ┐      │
│ Problem statement + domain         │ $ surakshaapk... │      │
│ Bank profile + team                │ Risk 87/100      │      │
│                                    └──────────────────┘      │
│ PROPOSED SOLUTION                                            │
│ SurakshaAPK                                                  │
│ Subtitle + pitch                                             │
│                                                              │
│ [Suspicious APK] → [Evidence Graph] → [Risk Score] → ...     │
└──────────────────────────────────────────────────────────────┘
```

## Visual Instructions

- Main title: Aptos Display Bold, 30–34, `#0B1F3A`
- SurakshaAPK: Aptos Display Bold, 36–42, `#0B1F3A`
- Subtitle: Aptos Semibold, 15–17, `#005BAC`
- Terminal: dark `#101820`, font Menlo/Consolas 7–8
- Pipeline boxes: blue/green/orange/navy/green

---

# Slide 2 — Problem Understanding & Fraud Landscape

## Slide Title

```text
Problem Understanding & Fraud Landscape
```

## Small Label

```text
PROBLEM UNDERSTANDING
```

## Main Message

```text
Fraudsters distribute fake banking APKs through WhatsApp, SMS, email and phishing links to steal credentials, OTPs and sensitive customer data.
```

## Layout

Use 3 panels + bottom strip:

```text
LEFT: Official PS1 decomposition
CENTER: Fraud APK attack chain
RIGHT: high-risk behavior examples + fake KYC phone mockup
BOTTOM: urgency for banks
```

## Left Table: Official PS1 Requirement → SurakshaAPK Coverage

| Official PS1 Requirement | SurakshaAPK Coverage |
|---|---|
| Automated APK analysis | Secure APK intake + SHA-256 hashing |
| Reverse engineering | JADX / AndroGuard / API-chain extraction |
| Static analysis | Manifest, permissions, code, URLs, certificates |
| Dynamic analysis | Selective runtime validation with triggers |
| GenAI code interpretation | Local LLM explains verified evidence |
| Risk scoring | Evidence-based score + confidence |
| Investigation reports | IOCs, YARA, SIEM JSON, CERT-In/RBI-ready draft |

## Center Flowchart

```text
1. Distribution
WhatsApp • SMS • Email • Phishing links
        ↓
2. Fake Banking APK
KYC update • Loan approval • Security patch
        ↓
3. Permission Abuse
SMS • Overlay • Accessibility • Internet
        ↓
4. Data Theft
Credentials • OTP • Screen text • Contacts
        ↓
5. C2 Exfiltration
Non-bank endpoint • Suspicious server
        ↓
6. Fraud Outcome
Unauthorized transfer • Customer loss
```

## Right Cards

```text
OTP Theft
SMS_RECEIVED → OTP regex → network exfiltration

Overlay Attack
Bank app launch → fake login screen → credential capture

Accessibility Abuse
Screen-read + auto-click behavior for unauthorized actions

Fake KYC Phishing
BOI logo/text + urgent KYC warning + non-bank domain
```

## Fake Phone Mockup

```text
BOI KYC Update
Your KYC is expired.
Update now to avoid account freeze.

[Enter Mobile Number]
[Enter OTP]
[Submit]
```

Label:

```text
Synthetic fake KYC APK lure example
```

## Bottom Strip

```text
Manual Analysis Bottleneck: Reverse engineering suspicious APKs is slow and expert-dependent.
False Positive Problem: Dangerous permissions alone do not prove malicious intent.
SurakshaAPK Focus: Detect complete fraud behavior chains before customer loss.
```

## Visual Instructions

- Left table header: navy `#0B1F3A`, white text
- Center flow boxes: blue → orange → red → red → navy → green
- Right cards: white with colored left strips
- Bottom strip: pale green `#EAF8F0`

---

# Slide 3 — Analyst Bottleneck & Current Core Issues

## Slide Title

```text
Analyst Bottleneck & Current Core Issues
```

## Small Label

```text
CURRENT GAPS
```

## Main Message

```text
Existing APK triage is slow, expert-dependent and often indicator-based. Banks need automated investigation that proves malicious behavior chains instead of only flagging suspicious permissions.
```

## Layout

```text
LEFT: Manual analyst workflow
CENTER: Challenge vs SurakshaAPK response table
RIGHT: Permission-only vs evidence-chain demo
BOTTOM: key conclusion strip
```

## Left Panel: Manual APK Analysis Flow

```text
Suspicious APK received
↓
Hash + unpack APK
↓
Read AndroidManifest.xml
↓
Decompile with JADX / Smali
↓
Trace APIs and strings
↓
Run sandbox / observe behavior
↓
Write report + IOCs manually

Bottleneck: Requires reverse-engineering skill, tool experience and manual report writing.
```

## Center Table

| Current Core Issue | Why It Fails | SurakshaAPK Response |
|---|---|---|
| Manual reverse engineering | Slow and expert-dependent | Automated static triage + structured evidence |
| Obfuscation and packing | Renamed classes, encrypted strings, hidden payloads | Multi-feature extraction + obfuscation indicators |
| Permission-only detection | Benign apps may also use SMS/Internet | Attack-chain detection using source → transform → sink |
| Sandbox behavior gap | Malware waits for OTP/accessibility/bank app trigger | Selective dynamic validation driven by static findings |
| Reporting bottleneck | Analysts manually summarize IOCs and risk | GenAI drafts evidence-grounded reports and recommendations |

## Right Panel

```text
Permission ≠ Malicious Intent

Traditional Alert
READ_SMS + INTERNET = Suspicious
Problem: benign apps may also use sensitive permissions.

SurakshaAPK Evidence Chain
SMS_RECEIVED → OTP regex → AES/Base64 → HTTP POST → Non-bank C2 = OTP Theft
Intent is proven by behavior chain.
```

## Bottom Strip

```text
SurakshaAPK addresses the analyst bottleneck by converting raw APK indicators into explainable, evidence-backed fraud behavior chains.
Current tools find indicators. SurakshaAPK proves intent.
```

## Visual Instructions

- Challenge table: compact, SurakshaAPK response column light green
- Traditional alert box: pale orange/red
- Evidence-chain box: pale green
- Bottom strip: green border

---

# Slide 4 — Proposed Solution: SurakshaAPK

## Slide Title

```text
Proposed Solution: SurakshaAPK
```

## Subtitle

```text
Evidence-First GenAI Malware Investigator for Fraudulent Banking APKs
```

## Small Label

```text
PROPOSED SOLUTION
```

## Main Message

```text
SurakshaAPK automates suspicious APK investigation by combining static reverse engineering, selective dynamic validation, evidence graph construction, deterministic risk scoring and GenAI-powered reporting.
```

## Layout

```text
LEFT: What SurakshaAPK does feature bars
CENTER: 4-layer pipeline
RIGHT: prototype mockup screenshots
BOTTOM: innovation badges + philosophy line
```

## Left Feature Bars

```text
Secure APK / link intake with SHA-256 hashing
Static reverse engineering of manifest, code, APIs and URLs
Bank Profile Adapter for BOI-specific impersonation checks
APK Fraud Evidence Graph for source-to-sink attack chains
Selective dynamic validation with fake OTP and sinkhole triggers
Local GenAI for code explanation and threat summarization
Risk score, confidence score and CERT-In/RBI-ready reports
```

## Center Pipeline

```text
L1 Static Decomposition
Manifest • Permissions • APIs • URLs • Certificates
        ↓
L2 Selective Dynamic Sandbox
Fake OTP • Overlay • Accessibility • Sinkhole
        ↓
L3 GenAI Evidence Explanation
Code intent • MITRE mapping • Threat summary
        ↓
L4 Risk + Compliance Reports
0–100 score • Confidence • IOCs • Report
```

## Right Prototype Mockups

Use 3 small mockups:

1. Upload Dashboard
2. Evidence Graph Viewer
3. Risk Report

## Bottom Badges

```text
Evidence-First | Local/Offline Default | BOI Profile Adapter | False-Positive Control | Actionable Reports
```

## Bottom Philosophy

```text
SurakshaAPK does not ask an LLM to guess malware — it asks GenAI to explain verified evidence.
```

## Visual Instructions

- Left feature bars with small icons/accent strips
- Center layer cards: blue/orange/green/navy
- Right mockups should look like mini app screens
- Badges in blue/green/orange/navy

---

# Slide 5 — System Architecture & Privacy-First Data Flow

## Slide Title

```text
System Architecture & Privacy-First Data Flow
```

## Small Label

```text
TECHNICAL ARCHITECTURE
```

## Main Message

```text
SurakshaAPK is designed as a local-first APK investigation pipeline where raw APKs, extracted code and evidence stay inside the bank environment by default.
```

## Main Architecture Flow

```text
Customer / SOC Upload
Suspicious APKs, phishing links, threat feed samples
        ↓
Secure Upload Gateway
SHA-256 hashing • duplicate check • quarantine
        ↓
Static Analysis Worker
Manifest • JADX • AndroGuard • YARA • APKiD
        ↓
Evidence Graph Store
Evidence IDs • source-to-sink chains • IOCs
        ↓
Risk Router
Low-risk → report
High-risk → dynamic validation
        ↓
Dynamic Validation Worker
Emulator • ADB triggers • Frida • Sinkhole
        ↓
Risk Scoring Engine
0–100 score • confidence • verdict
        ↓
Local GenAI Report Engine
Threat summary • MITRE mapping • recommendations
        ↓
Dashboard / PDF / IOC Export
Report • YARA • SIEM JSON • CERT-In/RBI draft
```

## Privacy Panel

```text
Privacy & Safety Controls

✓ Local/offline deployment by default
✓ Raw APK and extracted code stay inside bank environment
✓ Restricted network egress during analysis
✓ C2 traffic routed to sinkhole
✓ High-risk APKs stored in encrypted quarantine
✓ Audit logs: hash, tool versions, timestamps, analyst actions
✓ Optional enhanced mode: sanitized metadata only after approval
```

## Tiered Analysis Panel

```text
Tier 1: Fast Static Triage
All APKs — Manifest + code + IOC extraction

Tier 2: Selective Dynamic Validation
High-risk / unclear APKs — Fake OTP + overlay + sinkhole triggers

Tier 3: Human Analyst Escalation
Critical / low-confidence cases — Forensics bundle + evidence report
```

## Visual Instructions

- Main architecture left 65–70%, privacy/tier panels right
- Add icons: upload, lock, code, graph, Android, gauge, AI, report
- Evidence Graph Store should be highlighted orange/green as central artifact

---

# Slide 6 — Bank Profile Adapter & BOI Threat Intelligence

## Slide Title

```text
Bank Profile Adapter & BOI Threat Intelligence
```

## Small Label

```text
BANK-SPECIFIC FRAUD INTELLIGENCE
```

## Main Message

```text
SurakshaAPK uses configurable bank profiles to compare suspicious APKs against official bank identity, domains, certificates, app behavior and known fraud patterns.
```

## Left JSON

```json
{
  "bank_name": "Bank of India",
  "official_package": "com.boi.ua.android",
  "official_domains": ["bankofindia.co.in"],
  "fraud_keywords": [
    "KYC Update",
    "Account Freeze",
    "Loan Approved",
    "Security Patch"
  ],
  "high_risk_behaviors": [
    "OTP theft",
    "overlay attack",
    "accessibility abuse",
    "credential exfiltration"
  ]
}
```

## Detection Logic Flow

```text
Suspicious APK uploaded
↓
Claims BOI identity?
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

## Official vs Suspicious Table

| Attribute | Official BOI App | Suspicious APK |
|---|---|---|
| Package | `com.boi.ua.android` | `com.fake.boi.kyc` |
| Certificate | Known BOI signer | Unknown signer |
| Domains | `bankofindia.co.in` | Non-bank endpoint |
| UI text | Official banking flow | “KYC expired”, “Loan approved” |
| Sensitive input | Bank-controlled flow | OTP/PIN/card capture |
| Risk | Baseline | High/Critical |

## Bottom Strip

```text
To onboard another bank, update package names, certificates, domains, brand keywords and fraud templates — no core engine rewrite needed.
```

## Visual Instructions

- Left JSON dark card
- Center decision flow with final red box
- Right comparison table with Official column green and Suspicious column orange/red
- Optional fake KYC phone mockup small in right/bottom

---

# Slide 7 — Static Analysis Deep Dive + APK Feature Engineering

## Slide Title

```text
Static Analysis Deep Dive + APK Feature Engineering
```

## Small Label

```text
LAYER 1 — STATIC DECOMPOSITION
```

## Main Message

```text
SurakshaAPK decomposes APK structure into structured evidence features before execution, enabling fast triage, false-positive control and dynamic trigger planning.
```

## APK Tree

```text
BOI_KYC_Update.apk
├── AndroidManifest.xml
│   └── permissions, receivers, services
├── classes.dex
│   └── Java/Smali code, API calls
├── resources.arsc
│   └── strings, layouts, fake UI text
├── lib/*.so
│   └── native libraries / payloads
├── assets/
│   └── configs, hidden payloads
└── META-INF/
    └── certificate, signature
```

## Static Pipeline

```text
APK Unzip
↓
Manifest Parse
↓
Permission + Component Map
↓
JADX / AndroGuard Decompile
↓
String + URL Extraction
↓
API Source-Sink Mapping
↓
Obfuscation / Packer Detection
↓
Static Evidence JSON
```

## Feature Matrix

| Feature Group | Example Features |
|---|---|
| Permission | SMS, overlay, accessibility, contacts |
| Code/API | crypto, reflection, HTTP, WebView |
| Network | URLs, IPs, HTTP endpoints, C2-like paths |
| Identity | package mismatch, certificate mismatch |
| UI/Content | KYC text, fake login fields, BOI keywords |
| Obfuscation | encrypted strings, packer, junk code |

## Toolchain Chips

```text
JADX | AndroGuard | APKiD | YARA | capa/Ghidra-style native analysis
```

## Output Artifacts

```text
manifest.json | static_features.json | suspicious_apis.json | iocs.json | trigger_plan.json
```

## Bottom Strip

```text
Static output becomes the first layer of the APK Fraud Evidence Graph.
```

## Visual Instructions

- Left APK tree dark code card
- Center pipeline vertical flow
- Right feature table
- Bottom tool chips + artifact chips

---

# Slide 8 — Dynamic Analysis Deep Dive

## Slide Title

```text
Dynamic Analysis Deep Dive: Triggered Runtime Validation
```

## Small Label

```text
LAYER 2 — SELECTIVE DYNAMIC SANDBOX
```

## Main Message

```text
SurakshaAPK executes only high-risk or unclear APKs in a controlled Android environment where static findings drive targeted triggers such as fake OTP injection, overlay flows and sinkholed network capture.
```

## Trigger Plan Table

| Static Finding | Runtime Trigger |
|---|---|
| SMS receiver found | Inject fake OTP SMS |
| Overlay permission found | Trigger overlay permission path |
| Accessibility service found | Open accessibility settings flow |
| BOI targeting found | Launch simulated BOI banking app |
| Network endpoint found | Route traffic to sinkhole/MITM |
| Packer/anti-analysis found | Increase suspicion + analyst escalation |

## Runtime Workflow

```text
Install APK in Isolated Emulator
↓
Load Static Trigger Plan
↓
Inject Fake OTP / Open Permission Paths
↓
Launch Simulated BOI App Environment
↓
Capture API Calls + Network + UI Behavior
↓
Update Evidence Graph with Runtime Confirmation
```

## Runtime Evidence Log

```text
[ADB] Installed BOI_KYC_Update.apk in isolated emulator
[TRIGGER] Fake OTP injected: 582194
[FRIDA] SmsReceiver.onReceive() invoked
[UI] SYSTEM_ALERT_WINDOW overlay requested
[NET] POST /api/otp → non-bank endpoint
[RISK] E1 runtime-confirmed: OTP exfiltration attempt
[GRAPH] Evidence Graph updated with dynamic trace
```

## Safety Controls

```text
Isolated Emulator / VM • No real customer credentials • Restricted network egress • C2 routed to sinkhole • Frida/MITM attempted where feasible • Anti-analysis behavior recorded as risk signal
```

## Important Note

```text
If malware blocks hooks or detects sandboxing, that behavior becomes part of the risk evidence.
```

## Visual Instructions

- Left trigger table
- Center emulator/runtime workflow
- Right dark terminal evidence log
- Bottom safety chips
- Optional Android phone/emulator mockup

---

# Slide 9 — APK Fraud Evidence Graph

## Slide Title

```text
APK Fraud Evidence Graph: Proving Malicious Intent
```

## Small Label

```text
CORE INNOVATION
```

## Main Message

```text
SurakshaAPK links permissions, components, API calls, data sources, transformations, sinks and runtime traces into auditable fraud behavior chains.
```

## Source-to-Sink Graph

```text
E1: OTP Theft Source-to-Sink Chain

SOURCE: SMS_RECEIVED
↓
COMPONENT: SmsReceiver.onReceive()
↓
TRANSFORM: extractOtp()
↓
TRANSFORM: AES/Base64 encode
↓
SINK: NetworkClient.post()
↓
DESTINATION: unknown-c2.example/api/otp
```

## Attack Chain Cards

```text
E1: OTP Theft
SMS → OTP regex → encryption → C2

E2: Overlay Phishing
Bank app launch → fake login UI → credential capture

E3: Accessibility Abuse
Screen-read → auto-click → unauthorized action

E4: Impersonation Risk
BOI branding → cert mismatch → non-bank domain
```

## Evidence JSON

```json
{
  "evidence_id": "E1",
  "behavior": "OTP Theft",
  "source": "SMS_RECEIVED",
  "component": "SmsReceiver.onReceive",
  "transform": "OTP extraction + encryption",
  "sink": "HTTP POST",
  "destination": "unknown C2",
  "risk_contribution": 30,
  "dynamic_status": "confirmed"
}
```

## Benefit Chips

```text
Explainable • Auditable • Reduces Hallucination • Reduces False Positives • Supports Risk Score • Analyst-Verifiable
```

## Bottom Strip

```text
SurakshaAPK detects malicious intent by proving behavior chains — not by blindly flagging dangerous permissions.
```

## Visual Instructions

- Left source-to-sink graph with colored nodes
- Center chain examples cards
- Right dark JSON card
- Bottom chips + strong statement

---

# Slide 10 — GenAI Engine + Risk Scoring + Compliance Mapping

## Slide Title

```text
GenAI Engine + Risk Scoring + Compliance Mapping
```

## Small Label

```text
LAYER 3 & 4 — AI SYNTHESIS + RISK ENGINE
```

## Main Message

```text
SurakshaAPK uses GenAI only to explain verified evidence and draft investigation narratives; final scoring and compliance mapping remain deterministic and auditable.
```

## GenAI Flow

```text
Evidence Graph JSON
+ Decompiled code snippets
+ Dynamic trace summary
+ IOCs / URLs / APIs
↓
Local LLM
↓
Threat summary
Function intent explanation
MITRE mapping
Actionable recommendations

LLM is an explanation assistant — not the final malware judge.
```

## Risk Scoring Table

| Component | Weight |
|---|---:|
| Confirmed malicious behavior chain | 30 |
| Runtime confirmation | 20 |
| Banking impersonation / targeting | 15 |
| Sensitive data access / credential capture | 15 |
| C2 / network exfiltration risk | 10 |
| Obfuscation / anti-analysis / packing | 5 |
| Authenticity mismatch | 5 |
| **Total** | **100** |

## Risk Example

```text
Risk: 87/100
Confidence: 92%
Verdict: Critical
Evidence: E1 + E2 + E3
```

## Compliance Output

```text
Mapped to relevant RBI/CERT-In incident response and security-control requirements.

CERT-In Draft:
incident type • timestamp • affected system • IOC list • technical summary • impact • recommended action

RBI / Bank Security Mapping:
security-control relevance • customer protection action • evidence preservation • analyst escalation

MITRE Mapping:
mobile techniques • behavior category • family similarity if supported
```

## Guardrails

```text
GenAI does not run tools | GenAI does not assign final score | Raw APK is not sent to cloud mode | No malware generation
```

## Bottom Strip

```text
GenAI writes the explanation. Deterministic engines decide the score and evidence mapping.
```

## Visual Instructions

- Left GenAI input/output flow
- Center risk table + risk gauge
- Right compliance/report preview
- Bottom guardrail chips

---

# Slide 11 — Open-Source-First Technical Stack

## Slide Title

```text
Open-Source-First Technical Stack
```

## Small Label

```text
IMPLEMENTATION STACK
```

## Main Message

```text
SurakshaAPK uses proven reverse-engineering, Android automation, local GenAI, backend and reporting components to create a modular bank-deployable APK investigation platform.
```

## Layered Stack

```text
User Interface
React / Next.js Dashboard

API + Orchestration
Python FastAPI + Worker Queue

Static Analysis Engine
JADX + AndroGuard + APKiD + YARA

Dynamic Validation Engine
Android Emulator + ADB + Frida + MITM/Sinkhole

Evidence + Risk Layer
Evidence Graph JSON + Deterministic Scoring

GenAI + Reporting
Ollama/llama.cpp + PDF/JSON/SIEM/YARA Exports

Security Layer
Docker/VM Isolation + Restricted Egress + Encrypted Quarantine
```

## Tool Matrix

| Layer | Tools | Purpose |
|---|---|---|
| Frontend | React / Next.js | Upload, dashboard, report viewer |
| Backend | Python FastAPI | APIs, orchestration, worker execution |
| Static analysis | JADX, AndroGuard, APKiD, YARA | Decompile, parse, detect packers/rules |
| Dynamic validation | Android Emulator, ADB, Frida, MITMProxy/sinkhole | Trigger runtime paths and capture behavior |
| GenAI | Ollama / llama.cpp local LLM | Evidence explanation and report drafting |
| Storage | SQLite/PostgreSQL + JSON | Metadata and Evidence Graph storage |
| Reports | PDF, JSON, SIEM, YARA | Bank-ready outputs |
| Security | Docker/VM isolation | Safe malware containment |

## Deployment Modes

```text
Mode 1: Air-Gapped Bank Lab
Local static/dynamic analysis • Local LLM • No external data egress

Mode 2: Hybrid Enhanced Mode
Local analysis first • Only sanitized metadata to cloud • Approval-based

Mode 3: Research / Demo Mode
Controlled synthetic samples • Safe sinkhole environment • Fast prototype validation
```

## Bottom Strip

```text
Core pipeline is open-source-first. Cloud AI is optional, approval-based and metadata-only.
Prototype focus: static triage + Evidence Graph first, then selective dynamic validation.
```

## Visual Instructions

- Add tech logos/chips: Python, FastAPI, React, Android, Frida, YARA, Ollama/Llama, Docker, PostgreSQL/SQLite
- Use layered stack left, tool matrix center, deployment cards right

---

# Slide 12 — Output + Explainability + Bank Response

## Slide Title

```text
Output + Explainability + Bank Response
```

## Small Label

```text
ACTIONABLE OUTPUTS
```

## Main Message

```text
Every SurakshaAPK verdict is backed by evidence IDs and converted into actionable outputs for SOC, fraud operations, compliance teams and analysts.
```

## Report Preview

```text
SurakshaAPK Investigation Report

APK: BOI_KYC_Update.apk
SHA-256: 9f3a...c21b
Verdict: CRITICAL
Risk Score: 87/100
Confidence: 92%

Classification:
Banking Trojan / Fake KYC APK

Evidence:
E1: OTP theft chain
E2: Fake overlay targeting BOI profile
E3: Non-bank C2 endpoint

Recommendation:
Block IOCs + escalate to SOC + prepare CERT-In draft
```

## Stakeholder Output Matrix

| Team | Output |
|---|---|
| SOC / Cybersecurity | risk score, evidence IDs, APK hash, domains/IPs |
| Fraud Operations | attack summary, fake KYC campaign signals, customer advisory |
| Compliance | CERT-In draft, RBI security-control mapping, chain-of-custody |
| Analyst | code locations, API traces, runtime evidence, manual review note |
| Response Teams | YARA rule, SIEM JSON, blocklist recommendation |

## IOC JSON

```json
{
  "sha256": "9f3a...c21b",
  "domains": ["unknown-c2.example"],
  "permissions": ["RECEIVE_SMS", "SYSTEM_ALERT_WINDOW"],
  "risk": 87,
  "confidence": 92
}
```

## YARA Snippet

```yara
rule Banking_APK_Overlay_OTP {
  strings:
    $kyc = "KYC Update"
    $sms = "SMS_RECEIVED"
  condition:
    $kyc and $sms
}
```

## Example Verdict

```text
Risk Score: 87/100 | Confidence: 92%

E1: SMS OTP theft chain confirmed
E2: Fake overlay targets BOI profile
E3: Credentials sent to non-bank endpoint

Action: Critical SOC escalation + IOC blocking + CERT-In/RBI-ready incident draft
```

## Visual Instructions

- Left mini report preview
- Center stakeholder matrix
- Right dark IOC/YARA/SIEM snippets
- Bottom verdict card

---

# Slide 13 — Dataset Analysis, Validation Plan & Safe Obfuscation Test

## Slide Title

```text
Dataset Analysis, Validation Plan & Safe Obfuscation Test
```

## Small Label

```text
DATASET + VALIDATION
```

## Main Message

```text
SurakshaAPK will be validated using official bank baselines, benign applications, controlled synthetic fraud APKs, public malware datasets and pilot samples under safe handling rules.
```

## Dataset Table

| Dataset / Source | Purpose | Handling |
|---|---|---|
| Official BOI app metadata | Known-good baseline: package, domains, certificate, app identity | Public/bank profile |
| Benign finance apps | False-positive testing against legitimate apps | Hashes + extracted features |
| Synthetic controlled fraud APKs | Safe validation for OTP theft, overlay, fake KYC, sinkholed C2 | Controlled lab only |
| Public Android malware datasets | Static feature validation and behavior-pattern comparison | Legal access only |
| Public threat intelligence reports | Scam templates, malware behavior, IOCs, phishing patterns | Public sources |
| Bank-provided pilot samples | Real-world validation during pilot | Encrypted quarantine + chain-of-custody |

## Features Analyzed Per APK

```text
Package metadata • Signing certificate • Permissions • Receivers/services • API calls • Strings/URLs • UI text/KYC keywords • Obfuscation level • Network indicators • Dynamic traces • Ground-truth label if available
```

## Validation Metrics

```text
Static Triage Precision | Recall | False Positive Rate | Dynamic Trigger Success | Average Triage Time | Report Correctness | Analyst Review Agreement
```

## Safe Obfuscation Test

```text
Controlled Synthetic APK
→ Rename classes + encode strings + add junk code
→ Same behavior chain preserved
→ SurakshaAPK detects source-to-sink chain

No deployable malware is generated; only controlled synthetic samples are used for robustness testing.
```

## Visual Instructions

- Top dataset table
- Middle feature chips + metric chips
- Bottom obfuscation flow
- Orange warning note: No deployable malware generated

---

# Slide 14 — Research Foundation, Comparison & Feasibility

## Slide Title

```text
Research Foundation, Comparison & Feasibility
```

## Small Label

```text
VALIDATION + DIFFERENTIATION
```

## Main Message

```text
SurakshaAPK builds on established Android malware analysis concepts, adds bank-specific fraud intelligence, and follows a realistic MVP-to-pilot development path.
```

## Research Cards

```text
MITRE ATT&CK Mobile
Maps Android malware behaviors such as SMS access, overlay abuse, accessibility misuse and C2 communication.

Hybrid Static + Dynamic Analysis
Static triage extracts evidence; selective dynamic validation confirms high-risk behavior.

Source-to-Sink / Dataflow Analysis
Connects sensitive data sources to transformations and network sinks.

LLM-Assisted Code Explanation
Uses GenAI to summarize verified evidence and analyst reports, not to blindly decide malware.

Banking Trojan Behavior Patterns
Behavior-first similarity: Anatsa-like, Cerberus-like, SpyNote-like, EventBot-like only when supported by evidence.
```

## Comparison Table

| Capability | SurakshaAPK | MobSF | VirusTotal | Joe Sandbox |
|---|---|---|---|---|
| Static APK analysis | Yes | Yes | Partial/indirect | Yes |
| Dynamic behavior | Selective triggered validation | Limited | No local sandbox | Advanced |
| Local/private deployment | Yes | Yes | No | Usually commercial/cloud |
| Bank Profile Adapter | Yes | No | No | No |
| Evidence Graph | Yes | Limited | No | Behavior logs |
| GenAI explanation | Yes | No | No | Limited |
| RBI/CERT-In-ready outputs | Yes | No | No | No |

## Mature Line

```text
SurakshaAPK does not replace existing tools; it integrates reverse-engineering evidence into a bank-specific, GenAI-assisted investigation and reporting workflow.
```

## Feasibility Table

| Challenge | Mitigation |
|---|---|
| LLM hallucination | LLM explains only verified evidence; scoring is deterministic |
| False positives | Attack-chain scoring + BOI known-good baseline |
| Dynamic evasion | Static-driven triggers + anti-analysis behavior treated as risk signal |
| Privacy/legal concerns | Local/offline default + encrypted quarantine + metadata-only cloud option |
| Build scope | Static MVP first, selective dynamic validation next |

## Prototype Path

```text
MVP → Static triage + Evidence Graph + report
Next → Fake OTP + simulated BOI app + sinkhole validation
Pilot → Bank samples + analyst feedback + campaign clustering
```

## Bottom Strip

```text
Prototype path: fast static triage first, selective dynamic validation next, bank pilot after validation.
```

## Visual Instructions

- Left research cards
- Center comparison table
- Right challenge/mitigation feasibility table
- Bottom prototype path strip

---

# Slide 15 — Demo Strategy, Use Cases & Expected Impact

## Slide Title

```text
Demo Strategy, Use Cases & Expected Impact
```

## Small Label

```text
FINAL OUTCOME
```

## Main Message

```text
SurakshaAPK turns suspicious APKs into explainable evidence, risk scores, investigation reports and defensive actions for bank SOC, fraud and compliance teams.
```

## Demo Workflow

```text
Upload BOI_KYC_Update.apk
↓
Static triage extracts manifest, APIs, URLs and certificate signals
↓
Evidence Graph shows OTP / overlay / impersonation chain
↓
Risk engine generates score + confidence
↓
Local GenAI creates analyst report
↓
Export IOCs, YARA, SIEM JSON and CERT-In/RBI-ready draft
↓
Optional controlled dynamic validation with fake OTP + sinkhole
```

## Honest Demo Note

```text
Primary live demo: fast static triage.
Dynamic validation: selective, controlled and safety-bounded.
```

## Use Cases

```text
Bank SOC Triage
Analyze suspicious APKs reported by customers or threat feeds.

Fraud Operations
Identify fake KYC/loan campaigns and customer-risk patterns.

Defensive Blocking
Export hashes, domains, IPs, YARA rules and SIEM JSON.

Compliance & Investigation
Generate CERT-In/RBI-ready drafts with evidence IDs.

Customer Advisory
Create warnings for ongoing fake APK campaigns.

MDM / BYOD Screening
Screen employee-device apps for spyware/fake banking APKs.
```

## Impact Chips

```text
Faster APK Triage
Reduced Analyst Workload
Lower False Positives
Better Fraud Prevention
Privacy-First Deployment
Bank-Ready Reports
```

## Roadmap

```text
Idea → Static MVP → GenAI + Scoring → Selective Dynamic Validation → Bank Pilot
```

## Future

```text
Future: analyst feedback loop, campaign clustering and PSB profile expansion.
```

## Why Shortlist

```text
Direct PS1 alignment • Evidence-first GenAI • BOI-specific profile • Feasible MVP • Actionable bank outputs
```

## Closing

```text
SurakshaAPK helps banks move from reactive manual APK analysis to proactive, automated, evidence-based fraud defense.
```

## Visual Instructions

- Left demo workflow
- Center use-case cards
- Right impact chips + roadmap
- Bottom closing strip
- Add 2–3 small prototype mockups if space: upload screen, graph screen, report screen

---

## 4. Final PPT Quality Checklist

Before exporting PDF, check:

- [ ] Project name changed to **SurakshaAPK** everywhere.
- [ ] No “AEGIS v3.0” remains unless intentionally mentioned as old/internal name.
- [ ] `com.boi.ua.android` is used for Bank of India.
- [ ] No “RBI violated” wording.
- [ ] No “GPT-4 generates malware variants” wording.
- [ ] No unsupported exact accuracy claims.
- [ ] Every slide has a visual artifact: table, flowchart, mockup, code, graph, or architecture.
- [ ] Prototype mockups are labeled honestly if not real.
- [ ] Footer and page numbers are consistent.
- [ ] Exported PDF has no red spellcheck underlines.
- [ ] File size meets portal requirement if applicable.

---

## 5. Final Design Advice

To make it look like a human-built winning PPT:

1. Use more **tables + flowcharts** than bullet lists.
2. Add **prototype screens** even if mockups.
3. Add **tech logos/chips** on Slide 11.
4. Add **terminal/code/JSON cards** on technical slides.
5. Add **official vs suspicious APK comparison** to show BOI-specific thinking.
6. Add **challenge vs mitigation** table.
7. Keep language honest and feasible.
8. Do not over-polish into empty minimalist AI style.

The goal is:

> **technical, dense, credible, manually designed, bank-ready.**
