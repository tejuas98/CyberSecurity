# Project AEGIS v3.0

> **BOI CyberShield Hackathon 2026** - Problem Statement 1 Submission  
> Developed by: Tejas  
> Institution: SSGBCE, Bhusawal (DBATU affiliated)

## Evidence-First GenAI Automated Malware Investigation

AEGIS is an automated Android malware analysis system designed specifically to detect fraudulent banking applications (APKs) that target bank customers via phishing, SMS, WhatsApp, and overlay attacks. 

Unlike traditional platforms that rely solely on static signatures or generic dynamic sandboxes, AEGIS uses a **Bank Profile Adapter** and an **APK Fraud Evidence Graph** to deterministicly map malicious behavior. A local, privacy-first GenAI model (Llama-3-8B) is then used to explain the evidence and generate actionable, regulation-ready compliance reports.

### Key Capabilities

- **Bank Profile Adapter:** Replaces generic analysis with targeted impersonation detection. For Bank of India, the profile is strictly configured around `com.boi.ua.android`.
- **Evidence-First Detection:** Generates a Fraud Evidence Graph by linking API calls, permissions, and network sinks (e.g., SMS read → encrypted → sent to unknown C2).
- **Selective Dynamic Validation:** Uses an asynchronous, triggered sandbox to inject synthetic OTPs and simulate bank applications, capturing high-fidelity runtime evidence without claiming to defeat all anti-emulation.
- **Air-Gapped GenAI Synthesis:** Uses a local Llama-3-8B model by default to ensure zero sensitive bank data leaves the organizational perimeter.
- **Automated Compliance:** Maps observed MITRE ATT&CK techniques directly to RBI IT/Cybersecurity Controls and CERT-In reporting fields.

### Architecture Workflow

1. **Intake & Triage:** APK is ingested, hashed, and metadata is extracted.
2. **Deterministic Orchestrator:** Python pipeline runs JADX/AndroGuard to build the Evidence Graph.
3. **Selective Dynamic Validation:** High-risk samples are routed to a containerized sandbox for runtime confirmation.
4. **Evidence-Based Risk Scoring:** A 0-100 score is computed purely on the deterministic evidence chains.
5. **AI Synthesis:** The local LLM explains the evidence, translates technical findings into actionable business intelligence, and drafts the compliance reports.

### Local Development Setup

*Note: The full source code for the AEGIS orchestrator, frontend dashboard, and containerized sandbox is available to hackathon evaluators upon request during the shortlisting phase to maintain proprietary integrity prior to the final presentation.*

```bash
# 1. Clone the repository
git clone https://github.com/tejuas98/bank-of-india.git
cd bank-of-india

# 2. Launch the Web Interface Prototype
# The frontend dashboard showcasing the user flow and risk scoring visualization.
open index.html
```

### Validation Targets

Our prototype benchmarks evaluate robustness against behavior-preserving obfuscated APKs:
- **Static Triage Precision Target:** >85%
- **Dynamic Trigger Success Target:** >80% (on controlled samples)
- **False Positive Rate Target:** <5% (on legitimate finance applications)

---
*This repository contains the interactive presentation and UX prototype for the BOI CyberShield 2026 submission.*
