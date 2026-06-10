import re
import os

filepath = "/Users/toru/Projects and codes/project manager/ps1.html"

with open(filepath, "r") as f:
    content = f.read()

# Split by <!-- SLIDE X:
slides_raw = re.split(r'(<!-- SLIDE \d+:.*?-->)', content)
# slides_raw[0] is everything before slide 1
# slides_raw[1] is <!-- SLIDE 1: ... -->
# slides_raw[2] is the content of slide 1
# etc.

# Let's extract preamble, slide 1, 2, 3, 4
preamble = slides_raw[0]

def get_slide_content(num):
    for i in range(1, len(slides_raw), 2):
        if f"<!-- SLIDE {num}:" in slides_raw[i]:
            return slides_raw[i] + slides_raw[i+1]
    return ""

slide1 = get_slide_content(1)
slide2 = get_slide_content(2)
slide3 = get_slide_content(3)
slide4 = get_slide_content(4)

# Remove emojis from Slide 3
emojis_to_remove = ["⏳", "🔄", "⚠️", "❌", "🚫", "📌", "📉"]
for e in emojis_to_remove:
    slide3 = slide3.replace(e, "")
# Replace the emoji in Analyst gap if any like '⚡'
slide3 = re.sub(r'[^\x00-\x7F]+', '', slide3) # removing all non-ascii just in case, wait no, don't remove all non-ascii, could break things. 
# Better: just use string replace for known ones.
slide3 = slide3.replace("⏱️", "").replace("🚨", "").replace("🧠", "").replace("🔍", "").replace("⚙️", "")

# Fix footers for 1-4
for i in range(1, 5):
    slide1 = re.sub(r'1 / \d+', '1 / 10', slide1)
    slide2 = re.sub(r'2 / \d+', '2 / 10', slide2)
    slide3 = re.sub(r'3 / \d+', '3 / 10', slide3)
    slide4 = re.sub(r'4 / \d+', '4 / 10', slide4)

# Slide 5: Decision-Based Architecture + Tech Stack
slide5 = """<!-- SLIDE 5: System Architecture -->
<div class="slide">
    <div class="header">
        <div class="title">System Architecture: Decision-Based Flow</div>
        <div class="subtitle">SurakshaAPK processes an APK from upload to report, including fallbacks</div>
    </div>
    
    <div style="display: flex; gap: 20px; flex: 1; margin-bottom: 10px;">
        <!-- Flowchart -->
        <div style="flex: 2; border-right: 2px solid #D9D9D9; padding-right: 20px;">
            <div style="font-size: 14px; font-weight: bold; color: #4472C4; margin-bottom: 10px; border-bottom: 1px solid #4472C4; padding-bottom: 4px;">Decision-Based APK Investigation Flow</div>
            
            <div style="display: flex; flex-direction: column; gap: 4px; font-family: monospace; font-size: 11px; color: #404040;">
                <div style="background: #E2EFDA; border: 1px solid #548235; padding: 4px; text-align: center; font-weight: bold;">APK / Link Intake</div>
                <div style="text-align: center;">↓</div>
                <div style="background: #DDEBF7; border: 1px solid #2F5597; padding: 4px; text-align: center;">Secure Hashing + Quarantine</div>
                <div style="text-align: center;">↓</div>
                <div style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 4px; text-align: center; font-weight: bold;">Duplicate hash found?</div>
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <div style="text-align: center; color: #548235;">YES → Return Existing Report</div>
                    <div style="text-align: center; color: #C00000;">NO → Load BOI Bank Profile</div>
                </div>
                <div style="text-align: center;">↓</div>
                <div style="background: #DDEBF7; border: 1px solid #2F5597; padding: 4px; text-align: center;">Static Analysis</div>
                <div style="text-align: center;">↓</div>
                <div style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 4px; text-align: center; font-weight: bold;">Decompiler success?</div>
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <div style="text-align: center; color: #C00000;">NO → Fallback: Smali / APKiD → Human Queue</div>
                    <div style="text-align: center; color: #548235;">YES → Build Static Evidence Graph</div>
                </div>
                <div style="text-align: center;">↓</div>
                <div style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 4px; text-align: center; font-weight: bold;">Static risk ≥ threshold OR bank impersonation?</div>
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <div style="text-align: center; color: #548235;">NO → Low-Risk Report</div>
                    <div style="text-align: center; color: #C00000;">YES → Generate Dynamic Trigger Plan</div>
                </div>
                <div style="text-align: center;">↓</div>
                <div style="background: #DDEBF7; border: 1px solid #2F5597; padding: 4px; text-align: center;">Selective Dynamic Sandbox</div>
                <div style="text-align: center;">↓</div>
                <div style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 4px; text-align: center; font-weight: bold;">Runtime behavior confirmed?</div>
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <div style="text-align: center; color: #548235;">NO → Suspicious / Analyst Review</div>
                    <div style="text-align: center; color: #C00000;">YES → Update Evidence Graph</div>
                </div>
                <div style="text-align: center;">↓</div>
                <div style="background: #FCE4D6; border: 1px solid #C65911; padding: 4px; text-align: center;">Risk Scoring Engine</div>
                <div style="text-align: center;">↓</div>
                <div style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 4px; text-align: center; font-weight: bold;">Critical risk?</div>
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <div style="text-align: center; color: #C00000;">YES → SOC Alert + CERT-In Draft</div>
                    <div style="text-align: center; color: #548235;">NO → Standard Investigation Report</div>
                </div>
                <div style="text-align: center;">↓</div>
                <div style="background: #E2EFDA; border: 1px solid #548235; padding: 4px; text-align: center;">Local GenAI Report</div>
            </div>
        </div>

        <!-- Right Side Artifacts -->
        <div style="flex: 1;">
            <div style="font-size: 14px; font-weight: bold; color: #C65911; margin-bottom: 10px; border-bottom: 1px solid #C65911; padding-bottom: 4px;">Artifacts Generated</div>
            <div style="background: #F2F2F2; border: 1px solid #BFBFBF; padding: 12px; font-family: monospace; font-size: 12px; color: #404040; line-height: 1.8;">
                <div>📄 sha256.txt</div>
                <div>📄 manifest.json</div>
                <div>📄 static_features.json</div>
                <div>📄 evidence_graph.json</div>
                <div>📄 trigger_plan.json</div>
                <div>📄 runtime_trace.json</div>
                <div>📄 risk_report.json</div>
                <div>📄 report.pdf</div>
                <div>📄 iocs.json</div>
                <div>📄 yara_rule.yar</div>
                <div>📄 siem_event.json</div>
            </div>
            
            <div style="margin-top: 15px; font-size: 14px; font-weight: bold; color: #404040; margin-bottom: 8px;">Export Formats</div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <div style="background: #C00000; color: white; padding: 4px 8px; font-size: 11px; font-weight: bold; border-radius: 2px;">PDF</div>
                <div style="background: #4472C4; color: white; padding: 4px 8px; font-size: 11px; font-weight: bold; border-radius: 2px;">IOC JSON</div>
                <div style="background: #548235; color: white; padding: 4px 8px; font-size: 11px; font-weight: bold; border-radius: 2px;">YARA</div>
                <div style="background: #ED7D31; color: white; padding: 4px 8px; font-size: 11px; font-weight: bold; border-radius: 2px;">SIEM</div>
            </div>
        </div>
    </div>
    
    <!-- Tech Stack Bottom -->
    <div style="margin-top: auto; border-top: 2px solid #4472C4; padding-top: 10px;">
        <div style="font-size: 12px; font-weight: bold; color: #4472C4; margin-bottom: 6px;">Technical Stack Elements</div>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; font-family: monospace; font-size: 12px;">
            <span style="background: #E2EFDA; border: 1px solid #548235; padding: 4px 8px; color: #385723;">Python</span>
            <span style="background: #E2EFDA; border: 1px solid #548235; padding: 4px 8px; color: #385723;">FastAPI</span>
            <span style="background: #DDEBF7; border: 1px solid #2F5597; padding: 4px 8px; color: #1F3864;">JADX</span>
            <span style="background: #DDEBF7; border: 1px solid #2F5597; padding: 4px 8px; color: #1F3864;">AndroGuard</span>
            <span style="background: #DDEBF7; border: 1px solid #2F5597; padding: 4px 8px; color: #1F3864;">APKiD</span>
            <span style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 4px 8px; color: #833C0C;">YARA</span>
            <span style="background: #FCE4D6; border: 1px solid #C65911; padding: 4px 8px; color: #833C0C;">Android</span>
            <span style="background: #FCE4D6; border: 1px solid #C65911; padding: 4px 8px; color: #833C0C;">ADB</span>
            <span style="background: #FCE4D6; border: 1px solid #C65911; padding: 4px 8px; color: #833C0C;">Frida</span>
            <span style="background: #FCE4D6; border: 1px solid #C65911; padding: 4px 8px; color: #833C0C;">MITMProxy</span>
            <span style="background: #E2EFDA; border: 1px solid #548235; padding: 4px 8px; color: #385723;">Ollama</span>
            <span style="background: #E2EFDA; border: 1px solid #548235; padding: 4px 8px; color: #385723;">Docker</span>
            <span style="background: #E2EFDA; border: 1px solid #548235; padding: 4px 8px; color: #385723;">PostgreSQL</span>
        </div>
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>5 / 10</span>
    </div>
</div>
"""

slide6 = """<!-- SLIDE 6: Bank Profile -->
<div class="slide">
    <div class="header">
        <div class="title">Bank Profile Adapter & Evidence Graph</div>
        <div class="subtitle">Dynamic context switching and logic chains mapped to specific banking targets</div>
    </div>
    
    <div style="display: flex; gap: 15px; height: 100%;">
        <!-- Left Column: BOI JSON + Table -->
        <div style="flex: 1; display: flex; flex-direction: column;">
            <div style="font-size: 14px; font-weight: bold; color: #4472C4; margin-bottom: 6px; border-bottom: 1px solid #4472C4; padding-bottom: 4px;">BOI Profile JSON</div>
            <pre style="background: #F2F2F2; border: 1px solid #BFBFBF; padding: 8px; font-family: monospace; font-size: 10px; color: #404040; overflow-x: hidden; margin-bottom: 15px;">
{
  "bank_name": "Bank of India",
  "official_package": "com.boi.ua.android",
  "official_domains": ["bankofindia.co.in"],
  "fraud_keywords": [
    "KYC Update", 
    "Account Freeze", 
    "Loan Approved"
  ],
  "high_risk_behaviors": [
    "OTP theft", 
    "overlay attack", 
    "accessibility abuse"
  ]
}
            </pre>
            
            <div style="font-size: 13px; font-weight: bold; color: #C65911; margin-bottom: 6px;">Official vs Suspicious</div>
            <table style="width: 100%; border-collapse: collapse; font-size: 10px; text-align: left;">
                <tr style="background: #4472C4; color: white;">
                    <th style="padding: 4px; border: 1px solid #BFBFBF;">Attribute</th>
                    <th style="padding: 4px; border: 1px solid #BFBFBF;">Official BOI App</th>
                    <th style="padding: 4px; border: 1px solid #BFBFBF;">Suspicious APK</th>
                </tr>
                <tr>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; font-weight: bold;">Package</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; font-family: monospace;">com.boi.ua.android</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; font-family: monospace; color: #C00000;">com.fake.boi.kyc</td>
                </tr>
                <tr>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; font-weight: bold;">Certificate</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF;">Known signer</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; color: #C00000;">Unknown signer</td>
                </tr>
                <tr>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; font-weight: bold;">Domain</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF;">BOI domain</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; color: #C00000;">Non-bank endpoint</td>
                </tr>
                <tr>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; font-weight: bold;">UI text</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF;">Official flow</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; color: #C00000;">KYC expired</td>
                </tr>
                <tr>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; font-weight: bold;">Risk</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; color: #548235;">Baseline</td>
                    <td style="padding: 4px; border: 1px solid #BFBFBF; color: #C00000; font-weight: bold;">High/Critical</td>
                </tr>
            </table>
        </div>

        <!-- Center Column: Decision Flow -->
        <div style="flex: 1; border-left: 1px dashed #BFBFBF; border-right: 1px dashed #BFBFBF; padding: 0 15px; display: flex; flex-direction: column;">
            <div style="font-size: 14px; font-weight: bold; color: #4472C4; margin-bottom: 6px; border-bottom: 1px solid #4472C4; padding-bottom: 4px;">Impersonation Detection</div>
            
            <div style="background: #DDEBF7; border: 1px solid #2F5597; padding: 6px; text-align: center; font-size: 11px; margin-bottom: 8px;">Extract UI Strings & Icons</div>
            <div style="text-align: center; margin-bottom: 8px;">↓</div>
            <div style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 6px; text-align: center; font-size: 11px; margin-bottom: 8px; font-weight: bold;">Match BOI Profile?</div>
            <div style="display: flex; gap: 10px; margin-bottom: 8px; font-size: 10px;">
                <div style="flex: 1; text-align: center; color: #548235;">NO → Generic rules</div>
                <div style="flex: 1; text-align: center; color: #C00000;">YES → High Suspicion</div>
            </div>
            <div style="text-align: center; margin-bottom: 8px;">↓</div>
            <div style="background: #FFF2CC; border: 1px solid #BF8F00; padding: 6px; text-align: center; font-size: 11px; margin-bottom: 8px; font-weight: bold;">Check Package & Cert</div>
            <div style="display: flex; gap: 10px; margin-bottom: 8px; font-size: 10px;">
                <div style="flex: 1; text-align: center; color: #548235;">MATCH → Official BOI</div>
                <div style="flex: 1; text-align: center; color: #C00000;">MISMATCH → Impersonator</div>
            </div>
            <div style="text-align: center; margin-bottom: 8px;">↓</div>
            <div style="background: #FCE4D6; border: 1px solid #C65911; padding: 6px; text-align: center; font-size: 11px; font-weight: bold;">Flag as Phishing/Fraud</div>
        </div>

        <!-- Right Column: Evidence Chains -->
        <div style="flex: 1; display: flex; flex-direction: column;">
            <div style="font-size: 14px; font-weight: bold; color: #4472C4; margin-bottom: 6px; border-bottom: 1px solid #4472C4; padding-bottom: 4px;">Evidence Chains</div>
            
            <div style="background: #F8CBAD; border: 1px solid #C65911; padding: 8px; margin-bottom: 12px;">
                <div style="font-size: 12px; font-weight: bold; color: #C00000; margin-bottom: 4px;">Chain 1: SMS Exfiltration</div>
                <div style="font-family: monospace; font-size: 10px; color: #404040;">
                    SMS_RECEIVED<br>
                    &nbsp;↳ OTP regex matching<br>
                    &nbsp;&nbsp;↳ HTTP POST (Non-bank)
                </div>
            </div>
            
            <div style="background: #F8CBAD; border: 1px solid #C65911; padding: 8px; margin-bottom: 12px;">
                <div style="font-size: 12px; font-weight: bold; color: #C00000; margin-bottom: 4px;">Chain 2: Credential Overlay</div>
                <div style="font-family: monospace; font-size: 10px; color: #404040;">
                    BOI app launch detected<br>
                    &nbsp;↳ SYSTEM_ALERT_WINDOW<br>
                    &nbsp;&nbsp;↳ Fake Login WebView<br>
                    &nbsp;&nbsp;&nbsp;↳ Credential capture
                </div>
            </div>

            <div style="background: #F8CBAD; border: 1px solid #C65911; padding: 8px;">
                <div style="font-size: 12px; font-weight: bold; color: #C00000; margin-bottom: 4px;">Chain 3: Accessibility</div>
                <div style="font-family: monospace; font-size: 10px; color: #404040;">
                    AccessibilityService<br>
                    &nbsp;↳ Read Screen Content<br>
                    &nbsp;&nbsp;↳ Auto-click "Grant"
                </div>
            </div>
        </div>
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>6 / 10</span>
    </div>
</div>
"""

slide7 = """<!-- SLIDE 7: Engines -->
<div class="slide">
    <div class="header">
        <div class="title">Static + Dynamic Analysis Engines</div>
        <div class="subtitle">Extracting source-sink mappings and validating them in a triggered sandbox</div>
    </div>
    
    <div style="display: flex; gap: 20px; flex: 1; margin-bottom: 10px;">
        <!-- Left: Static -->
        <div style="flex: 1; border: 2px solid #5B9BD5; padding: 15px; background: #F2F8FD;">
            <div style="font-size: 16px; font-weight: bold; color: #2F5597; margin-bottom: 10px;">L1 Static Engine</div>
            
            <div style="display: flex; flex-direction: column; gap: 6px; font-family: monospace; font-size: 12px; color: #404040; margin-bottom: 15px;">
                <div style="border-left: 3px solid #2F5597; padding-left: 8px;">APK Unpacking</div>
                <div style="border-left: 3px solid #2F5597; padding-left: 8px;">Manifest Parsing</div>
                <div style="border-left: 3px solid #2F5597; padding-left: 8px;">Decompilation</div>
                <div style="border-left: 3px solid #2F5597; padding-left: 8px;">IoC Extraction</div>
                <div style="border-left: 3px solid #2F5597; padding-left: 8px; font-weight: bold;">Source-Sink Mapping</div>
                <div style="border-left: 3px solid #2F5597; padding-left: 8px;">Obfuscation Detection</div>
            </div>
            
            <div style="font-size: 12px; font-weight: bold; color: #404040; margin-bottom: 4px;">static_features.json</div>
            <pre style="background: #FFFFFF; border: 1px solid #BFBFBF; padding: 10px; font-family: monospace; font-size: 11px; color: #2F5597;">
{
  "permissions": [
    "RECEIVE_SMS", 
    "SYSTEM_ALERT_WINDOW"
  ],
  "urls": ["hxxps://unknown-c2.example/api"],
  "obfuscation_score": 0.72,
  "bank_profile_match": "BOI impersonation"
}
            </pre>
        </div>

        <!-- Right: Dynamic -->
        <div style="flex: 1; border: 2px solid #C65911; padding: 15px; background: #FDF3EB; display: flex; gap: 15px;">
            <div style="flex: 1; display: flex; flex-direction: column;">
                <div style="font-size: 16px; font-weight: bold; color: #C65911; margin-bottom: 10px;">L2 Dynamic Sandbox</div>
                <div style="font-size: 12px; color: #404040; margin-bottom: 15px;">Validates static evidence via targeted triggers.</div>
                
                <div style="font-size: 12px; font-weight: bold; color: #404040; margin-bottom: 4px;">Runtime Logs</div>
                <pre style="background: #111827; color: #00FF00; border: 1px solid #404040; padding: 10px; font-family: monospace; font-size: 10px; flex: 1;">
> [TRIGGER] Fake OTP injected
> [ACTION] SmsReceiver invoked
> [NETWORK] C2 exfiltration
  -> dest: unknown-c2.example
> Verdict: Runtime Fraud Confirmed
                </pre>
            </div>
            
            <!-- Phone Mockup -->
            <div style="width: 120px; border: 4px solid #111827; border-radius: 12px; padding: 0; background: white; box-shadow: 2px 2px 6px rgba(0,0,0,0.2); position: relative; display: flex; flex-direction: column; overflow: hidden;">
                <div style="width: 30px; height: 5px; background: #111827; border-radius: 0 0 4px 4px; margin: 0 auto; position: absolute; top: 0; left: 50%; transform: translateX(-50%); z-index: 10;"></div>
                <div style="background: #F2F2F2; color: #404040; padding: 12px 4px 4px 4px; text-align: center; font-size: 8px; border-bottom: 1px solid #D9D9D9;">AVD / Sandbox</div>
                <div style="padding: 8px; flex: 1; background: #FFF2CC;">
                    <div style="font-size: 9px; font-weight: bold; color: #C00000; text-align: center; margin-bottom: 6px;">BOI Update</div>
                    <div style="border: 1px solid #BFBFBF; padding: 4px; font-size: 8px; color: #7F7F7F; margin-bottom: 4px; background: white;">OTP: 492011</div>
                    <div style="border: 1px solid #BFBFBF; padding: 4px; font-size: 8px; color: #7F7F7F; margin-bottom: 4px; background: white;">PIN: ****</div>
                    <div style="background: #4472C4; color: white; text-align: center; padding: 4px; font-size: 8px; font-weight: bold; border-radius: 2px; margin-top: 10px;">Submit</div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Tech Stack Bottom -->
    <div style="margin-top: 10px; display: flex; justify-content: center; gap: 12px; font-family: monospace; font-size: 13px; font-weight: bold;">
        <span style="border-bottom: 2px solid #2F5597; padding-bottom: 2px;">JADX</span>
        <span style="border-bottom: 2px solid #2F5597; padding-bottom: 2px;">AndroGuard</span>
        <span style="border-bottom: 2px solid #2F5597; padding-bottom: 2px;">APKiD</span>
        <span style="border-bottom: 2px solid #2F5597; padding-bottom: 2px;">YARA</span>
        <span style="border-bottom: 2px solid #C65911; padding-bottom: 2px;">Android AVD</span>
        <span style="border-bottom: 2px solid #C65911; padding-bottom: 2px;">ADB</span>
        <span style="border-bottom: 2px solid #C65911; padding-bottom: 2px;">Frida</span>
        <span style="border-bottom: 2px solid #C65911; padding-bottom: 2px;">MITMProxy</span>
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>7 / 10</span>
    </div>
</div>
"""

slide8 = """<!-- SLIDE 8: GenAI -->
<div class="slide">
    <div class="header">
        <div class="title">GenAI, Risk Scoring & Outputs</div>
        <div class="subtitle">Deterministic engines decide the score; GenAI explains the evidence.</div>
    </div>
    
    <div style="display: flex; gap: 15px; flex: 1; margin-bottom: 15px;">
        <!-- Left: Risk Gauge & Buttons -->
        <div style="flex: 0 0 25%; display: flex; flex-direction: column; gap: 15px;">
            <div style="background: white; border: 2px solid #C00000; border-radius: 8px; padding: 15px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <div style="font-size: 14px; font-weight: bold; color: #404040; margin-bottom: 10px;">Risk Assessment</div>
                <div style="font-size: 36px; font-weight: bold; color: #C00000; margin-bottom: 5px; line-height: 1;">87<span style="font-size: 18px;">/100</span></div>
                <div style="background: #C00000; color: white; display: inline-block; padding: 4px 12px; font-weight: bold; font-size: 14px; border-radius: 4px; margin-bottom: 8px;">CRITICAL</div>
                <div style="font-size: 12px; color: #595959; font-weight: bold;">Confidence: 92%</div>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div style="background: #4472C4; color: white; padding: 8px; text-align: center; font-weight: bold; font-size: 12px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📄 PDF Report</div>
                <div style="background: #548235; color: white; padding: 8px; text-align: center; font-weight: bold; font-size: 12px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">{" "} IOC JSON</div>
                <div style="background: #C65911; color: white; padding: 8px; text-align: center; font-weight: bold; font-size: 12px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">🛡️ YARA Rule</div>
                <div style="background: #203864; color: white; padding: 8px; text-align: center; font-weight: bold; font-size: 12px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📊 SIEM Event</div>
                <div style="background: #404040; color: white; padding: 8px; text-align: center; font-weight: bold; font-size: 12px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📝 CERT-In Draft</div>
            </div>
        </div>

        <!-- Center: Investigation Report Preview -->
        <div style="flex: 1; background: #FDFDFD; border: 1px solid #D9D9D9; border-top: 4px solid #4472C4; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); display: flex; flex-direction: column;">
            <div style="padding: 12px; border-bottom: 1px solid #D9D9D9; font-size: 16px; font-weight: bold; color: #203864; text-align: center;">SurakshaAPK Investigation Report</div>
            <div style="padding: 15px; font-size: 12px; color: #404040; line-height: 1.5; flex: 1;">
                <div style="font-weight: bold; color: #C00000; margin-bottom: 4px;">AI Threat Summary:</div>
                <div style="margin-bottom: 12px;">This APK exhibits OTP theft and overlay phishing behavior targeting Bank of India credentials.</div>
                
                <div style="font-weight: bold; color: #C65911; margin-bottom: 4px;">Key Evidence Chains:</div>
                <div style="font-family: monospace; background: #F2F2F2; padding: 8px; margin-bottom: 12px;">
                    <b>E1:</b> Dynamic sandbox captured HTTP POST containing injected fake OTP.<br>
                    <b>E2:</b> Manifest requests SYSTEM_ALERT_WINDOW with BOI-matching activity names.
                </div>
                
                <div style="font-weight: bold; color: #548235; margin-bottom: 4px;">Recommended Action:</div>
                <div>Block domains, escalate to SOC, submit generated CERT-In draft.</div>
            </div>
        </div>

        <!-- Right: Code Snippets -->
        <div style="flex: 0 0 30%; display: flex; flex-direction: column; gap: 10px;">
            <div style="flex: 1; border: 1px solid #BFBFBF; background: #F2F2F2; display: flex; flex-direction: column;">
                <div style="background: #404040; color: white; padding: 4px 8px; font-size: 10px; font-weight: bold; font-family: monospace;">iocs.json</div>
                <pre style="padding: 8px; font-family: monospace; font-size: 10px; color: #C00000; margin: 0;">
{
  "sha256": "9f3a...c21b",
  "domains": [
    "unknown-c2.example"
  ],
  "risk": 87,
  "confidence": 92
}
                </pre>
            </div>
            
            <div style="flex: 1; border: 1px solid #BFBFBF; background: #F2F2F2; display: flex; flex-direction: column;">
                <div style="background: #404040; color: white; padding: 4px 8px; font-size: 10px; font-weight: bold; font-family: monospace;">rule.yar</div>
                <pre style="padding: 8px; font-family: monospace; font-size: 10px; color: #C65911; margin: 0;">
rule BOI_Overlay_OTP {
  strings:
    $kyc = "KYC Update"
    $sms = "SMS_RECEIVED"
  condition:
    $kyc and $sms
}
                </pre>
            </div>
        </div>
    </div>
    
    <!-- GenAI Guardrail Line -->
    <div style="background: #EAF8F0; border: 1px solid #00A676; padding: 10px; text-align: center; font-size: 14px; font-weight: bold; color: #00A676;">
        GenAI writes the explanation. Deterministic engines decide the score and evidence mapping.
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>8 / 10</span>
    </div>
</div>
"""

slide9 = """<!-- SLIDE 9: Dataset & Validation -->
<div class="slide">
    <div class="header">
        <div class="title">Dataset, Feasibility & Competitive Comparison</div>
        <div class="subtitle">Rigorous testing, clear advantages, and practical implementations</div>
    </div>
    
    <div style="display: flex; flex-direction: column; height: 100%; gap: 10px;">
        
        <!-- Validation Pipeline -->
        <div style="background: #DDEBF7; border: 1px solid #2F5597; padding: 8px; text-align: center; font-weight: bold; font-size: 12px; color: #2F5597;">
            Dataset → Feature Extraction → Evidence Chain Detection → Analyst Review → Metrics
        </div>

        <div style="display: flex; gap: 15px; flex: 1;">
            <!-- Left: Dataset Table -->
            <div style="flex: 1; display: flex; flex-direction: column;">
                <div style="font-size: 13px; font-weight: bold; color: #4472C4; margin-bottom: 6px;">Evaluation Dataset</div>
                <table style="width: 100%; border-collapse: collapse; font-size: 10px; text-align: left;">
                    <tr style="background: #4472C4; color: white;">
                        <th style="padding: 4px; border: 1px solid #BFBFBF;">Dataset Category</th>
                        <th style="padding: 4px; border: 1px solid #BFBFBF;">Purpose</th>
                    </tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Official BOI / PSB apps</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Known-good baseline</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Benign finance apps</td><td style="padding: 4px; border: 1px solid #BFBFBF;">False-positive testing</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Synthetic fraud APKs</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Safe OTP/overlay validation</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Public malware datasets</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Static feature validation</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Threat intel reports</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Scam patterns and IOCs</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Bank pilot samples</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Real-world validation</td></tr>
                </table>
            </div>

            <!-- Center: Comparison Table -->
            <div style="flex: 1; display: flex; flex-direction: column;">
                <div style="font-size: 13px; font-weight: bold; color: #4472C4; margin-bottom: 6px;">Competitive Edge</div>
                <table style="width: 100%; border-collapse: collapse; font-size: 10px; text-align: left;">
                    <tr style="background: #4472C4; color: white;">
                        <th style="padding: 4px; border: 1px solid #BFBFBF;">Capability</th>
                        <th style="padding: 4px; border: 1px solid #BFBFBF;">Generic Scanners</th>
                        <th style="padding: 4px; border: 1px solid #BFBFBF;">SurakshaAPK</th>
                    </tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Static APK analysis</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Yes</td><td style="padding: 4px; border: 1px solid #BFBFBF; font-weight:bold; color:#548235;">Yes</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Local/private deployment</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Limited/No</td><td style="padding: 4px; border: 1px solid #BFBFBF; font-weight:bold; color:#548235;">Yes</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Triggered dynamic validation</td><td style="padding: 4px; border: 1px solid #BFBFBF;">Partial</td><td style="padding: 4px; border: 1px solid #BFBFBF; font-weight:bold; color:#548235;">Yes</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Bank Profile Adapter</td><td style="padding: 4px; border: 1px solid #BFBFBF;">No</td><td style="padding: 4px; border: 1px solid #BFBFBF; font-weight:bold; color:#548235;">Yes</td></tr>
                    <tr><td style="padding: 4px; border: 1px solid #BFBFBF;">Evidence-grounded GenAI reports</td><td style="padding: 4px; border: 1px solid #BFBFBF;">No</td><td style="padding: 4px; border: 1px solid #BFBFBF; font-weight:bold; color:#548235;">Yes</td></tr>
                </table>
            </div>

            <!-- Right: Feasibility -->
            <div style="flex: 1; display: flex; flex-direction: column;">
                <div style="font-size: 13px; font-weight: bold; color: #4472C4; margin-bottom: 6px;">Feasibility / Mitigations</div>
                <div style="font-size: 10px; background: #FDFDFD; border: 1px solid #BFBFBF; padding: 8px; flex: 1; display: flex; flex-direction: column; gap: 6px;">
                    <div><b>LLM hallucination</b> → GenAI explains only verified evidence</div>
                    <div><b>False positives</b> → Attack-chain scoring + BOI baseline</div>
                    <div><b>Dynamic evasion</b> → Static-driven triggers + anti-analysis signals</div>
                    <div><b>Data privacy</b> → Local/offline default</div>
                    <div><b>Build scope</b> → Static MVP first, dynamic validation next</div>
                </div>
            </div>
        </div>

        <!-- Safe Obfuscation Test -->
        <div style="background: #EAF8F0; border: 1px solid #00A676; padding: 8px; text-align: center; font-size: 11px; font-family: monospace; color: #00A676; font-weight: bold;">
            Safe Obfuscation Test: Controlled APK → rename classes + encode strings + add junk code → same behavior chain → detected by SurakshaAPK
        </div>

    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>9 / 10</span>
    </div>
</div>
"""

slide10 = """<!-- SLIDE 10: Final -->
<div class="slide">
    <div class="header">
        <div class="title">Demo Strategy, Use Cases & Impact</div>
        <div class="subtitle">Turning analysis into actionable bank security</div>
    </div>
    
    <div style="display: flex; gap: 15px; flex: 1; margin-bottom: 10px;">
        <!-- Left: Demo Workflow -->
        <div style="flex: 1; border: 1px solid #5B9BD5; background: #DDEBF7; padding: 12px; display: flex; flex-direction: column;">
            <div style="font-size: 14px; font-weight: bold; color: #2F5597; margin-bottom: 10px; text-align: center; border-bottom: 1px solid #2F5597; padding-bottom: 4px;">Demo Workflow</div>
            <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-around; font-size: 12px; font-weight: bold; color: #404040; text-align: center;">
                <div>Upload BOI_KYC_Update.apk</div>
                <div>↓</div>
                <div>Static triage</div>
                <div>↓</div>
                <div>Evidence Graph</div>
                <div>↓</div>
                <div>Risk score + confidence</div>
                <div>↓</div>
                <div>GenAI report</div>
                <div>↓</div>
                <div>Export PDF / IOC / YARA / SIEM</div>
                <div>↓</div>
                <div>Optional dynamic validation</div>
            </div>
        </div>

        <!-- Center: Mockups -->
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
            <div style="background: #404040; color: white; padding: 6px; font-size: 10px; font-weight: bold; text-align: center; border-radius: 4px;">1. Upload Console</div>
            <div style="background: #404040; color: white; padding: 6px; font-size: 10px; font-weight: bold; text-align: center; border-radius: 4px;">2. Evidence Graph Viewer</div>
            <div style="background: #404040; color: white; padding: 6px; font-size: 10px; font-weight: bold; text-align: center; border-radius: 4px;">3. Risk Report Output</div>
        </div>

        <!-- Right: Use Cases & Impact -->
        <div style="flex: 1.5; display: flex; flex-direction: column; gap: 10px;">
            <div style="border: 1px solid #C65911; background: #FCE4D6; padding: 10px;">
                <div style="font-size: 13px; font-weight: bold; color: #C65911; margin-bottom: 6px;">Bank Use Cases</div>
                <div style="display: flex; flex-wrap: wrap; gap: 6px; font-size: 11px; color: #404040;">
                    <span style="background: white; border: 1px solid #BFBFBF; padding: 2px 6px;">Bank SOC Triage</span>
                    <span style="background: white; border: 1px solid #BFBFBF; padding: 2px 6px;">Fraud Operations</span>
                    <span style="background: white; border: 1px solid #BFBFBF; padding: 2px 6px;">Defensive Blocking</span>
                    <span style="background: white; border: 1px solid #BFBFBF; padding: 2px 6px;">Compliance & Inv.</span>
                    <span style="background: white; border: 1px solid #BFBFBF; padding: 2px 6px;">Customer Advisory</span>
                    <span style="background: white; border: 1px solid #BFBFBF; padding: 2px 6px;">MDM / BYOD Screening</span>
                </div>
            </div>
            
            <div style="border: 1px solid #548235; background: #E2EFDA; padding: 10px;">
                <div style="font-size: 13px; font-weight: bold; color: #548235; margin-bottom: 6px;">Impact</div>
                <div style="display: flex; flex-wrap: wrap; gap: 6px; font-size: 11px; color: #404040; font-weight: bold;">
                    <span style="background: white; border: 1px solid #548235; padding: 2px 6px;">Faster APK Triage</span>
                    <span style="background: white; border: 1px solid #548235; padding: 2px 6px;">Reduced Analyst Workload</span>
                    <span style="background: white; border: 1px solid #548235; padding: 2px 6px;">Lower False Positives</span>
                    <span style="background: white; border: 1px solid #548235; padding: 2px 6px;">Better Fraud Prevention</span>
                    <span style="background: white; border: 1px solid #548235; padding: 2px 6px;">Privacy-First Deployment</span>
                    <span style="background: white; border: 1px solid #548235; padding: 2px 6px;">Bank-Ready Reports</span>
                </div>
            </div>
            
            <div style="background: #F2F2F2; border: 1px solid #BFBFBF; padding: 8px; font-size: 11px; text-align: center; color: #404040;">
                <span style="font-weight: bold;">Roadmap:</span> Idea → Static MVP → GenAI + Scoring → Dynamic Validation → Bank Pilot
            </div>
        </div>
    </div>
    
    <div style="background: #203864; color: white; padding: 12px; text-align: center; font-size: 15px; font-weight: bold; border-radius: 4px; box-shadow: 0 4px 6px rgba(0,0,0,0.15);">
        SurakshaAPK helps banks move from reactive manual APK analysis to proactive, automated, evidence-based fraud defense.
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>10 / 10</span>
    </div>
</div>
"""

new_content = preamble + slide1 + slide2 + slide3 + slide4 + slide5 + slide6 + slide7 + slide8 + slide9 + slide10 + "\n</body>\n</html>\n"

with open(filepath, "w") as f:
    f.write(new_content)

print("Updated successfully")
