import sys

filepath = "/Users/toru/Projects and codes/project manager/ps1.html"

with open(filepath, "r") as f:
    content = f.read()

s6_start = content.find("<!-- SLIDE 6:")
if s6_start == -1:
    print("Could not find slide 6")
    sys.exit(1)

s7_start = content.find("<!-- SLIDE 7:", s6_start)
if s7_start == -1:
    print("Could not find slide 7")
    sys.exit(1)

new_slide_6 = """<!-- SLIDE 6: Bank Profile -->
<div class="slide" style="display: flex; flex-direction: column; padding: 22px 38px 40px 42px;">
    <!-- TOP SECTION: Titles -->
    <div style="font-weight: bold; color: #7F7F7F; font-size: 14px; text-transform: uppercase; margin-bottom: 4px; margin-left: 1px;">TARGETED ANALYSIS</div>
    <h2 style="font-family: var(--font-main); font-size: 32px; font-weight: 800; color: var(--boi-navy); margin: 0 0 6px 0;">Bank Profile Adapter & Evidence Graph</h2>
    <div style="font-size: 15px; color: var(--text-muted); margin-bottom: 24px;">Dynamic context switching and logic chains mapped to specific banking targets to detect brand impersonation.</div>
    
    <div style="display: flex; gap: 24px; flex: 1; min-height: 0;">
        <!-- Left Column: BOI JSON + Table -->
        <div style="flex: 1; display: flex; flex-direction: column;">
            <div style="font-size: 15px; font-weight: 800; color: #4472C4; margin-bottom: 10px; border-bottom: 3px solid #4472C4; padding-bottom: 4px; text-transform: uppercase;">BOI Profile JSON</div>
            <pre style="background: #F8FAFC; border: 2px solid #5B9BD5; border-radius: 4px; padding: 12px; font-family: monospace; font-size: 12.5px; color: #203864; overflow-x: hidden; margin-bottom: 24px; box-shadow: 3px 3px 0px rgba(91,155,213,0.3); font-weight: bold;">
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
            
            <div style="font-size: 15px; font-weight: 800; color: #C65911; margin-bottom: 8px; text-transform: uppercase;">Official vs Suspicious</div>
            <table style="width: 100%; border-collapse: collapse; font-size: 12.5px; text-align: left; border: 2px solid #595959; box-shadow: 3px 3px 5px rgba(0,0,0,0.1);">
                <tr style="background: #4472C4; color: white;">
                    <th style="padding: 8px 10px; border: 1px solid #595959;">Attribute</th>
                    <th style="padding: 8px 10px; border: 1px solid #595959;">Official BOI App</th>
                    <th style="padding: 8px 10px; border: 1px solid #595959;">Suspicious APK</th>
                </tr>
                <tr style="background: white;">
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; font-weight: bold;">Package</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; font-family: monospace;">com.boi.ua.android</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; font-family: monospace; color: #C00000; font-weight: bold;">com.fake.boi.kyc</td>
                </tr>
                <tr style="background: #F2F2F2;">
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; font-weight: bold;">Certificate</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF;">Known signer</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; color: #C00000; font-weight: bold;">Unknown signer</td>
                </tr>
                <tr style="background: white;">
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; font-weight: bold;">Domain</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF;">BOI domain</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; color: #C00000; font-weight: bold;">Non-bank endpoint</td>
                </tr>
                <tr style="background: #F2F2F2;">
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; font-weight: bold;">UI text</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF;">Official flow</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; color: #C00000; font-weight: bold;">KYC expired</td>
                </tr>
                <tr style="background: white;">
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; font-weight: bold;">Risk</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; color: #548235; font-weight: bold;">Baseline</td>
                    <td style="padding: 8px 10px; border: 1px solid #BFBFBF; color: #C00000; font-weight: 900;">High/Critical</td>
                </tr>
            </table>
        </div>

        <!-- Center Column: Decision Flow -->
        <div style="flex: 1; border-left: 2px dashed #BFBFBF; border-right: 2px dashed #BFBFBF; padding: 0 24px; display: flex; flex-direction: column;">
            <div style="font-size: 15px; font-weight: 800; color: #4472C4; margin-bottom: 24px; border-bottom: 3px solid #4472C4; padding-bottom: 4px; text-transform: uppercase;">Impersonation Detection</div>
            
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: flex-start; flex: 1;">
                <div style="background: #DDEBF7; border: 2px solid #5B9BD5; padding: 14px; text-align: center; font-size: 13.5px; font-weight: bold; width: 100%; border-radius: 4px; box-shadow: 3px 3px 0 rgba(91,155,213,0.3); color: #203864;">Extract UI Strings & Icons</div>
                
                <div style="height: 24px; width: 3px; background: #94A3B8; margin: 4px 0;"></div>
                <div style="width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid #94A3B8; margin-bottom: 6px;"></div>
                
                <div style="background: #FFF2CC; border: 2px solid #BF8F00; padding: 14px; text-align: center; font-size: 13.5px; font-weight: 800; width: 100%; border-radius: 4px; box-shadow: 3px 3px 0 rgba(191,143,0,0.3); color: #7F6000;">Match BOI Profile?</div>
                
                <div style="display: flex; width: 100%; justify-content: space-between; margin-top: 10px; margin-bottom: 10px; padding: 0 4px;">
                    <div style="font-size: 11.5px; font-weight: bold; color: #548235;">NO → Generic rules</div>
                    <div style="font-size: 11.5px; font-weight: bold; color: #C00000;">YES → High Suspicion</div>
                </div>
                
                <div style="height: 24px; width: 3px; background: #94A3B8; margin: 4px 0;"></div>
                <div style="width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid #94A3B8; margin-bottom: 6px;"></div>
                
                <div style="background: #FFF2CC; border: 2px solid #BF8F00; padding: 14px; text-align: center; font-size: 13.5px; font-weight: 800; width: 100%; border-radius: 4px; box-shadow: 3px 3px 0 rgba(191,143,0,0.3); color: #7F6000;">Check Package & Cert</div>
                
                <div style="display: flex; width: 100%; justify-content: space-between; margin-top: 10px; margin-bottom: 10px; padding: 0 4px;">
                    <div style="font-size: 11.5px; font-weight: bold; color: #548235;">MATCH → Official</div>
                    <div style="font-size: 11.5px; font-weight: bold; color: #C00000;">MISMATCH → Impersonator</div>
                </div>
                
                <div style="height: 24px; width: 3px; background: #94A3B8; margin: 4px 0;"></div>
                <div style="width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid #94A3B8; margin-bottom: 6px;"></div>
                
                <div style="background: #FCE4D6; border: 2px solid #C65911; padding: 14px; text-align: center; font-size: 13.5px; font-weight: 900; color: #C00000; width: 100%; border-radius: 4px; box-shadow: 3px 3px 0 rgba(198,89,17,0.3);">Flag as Phishing/Fraud</div>
            </div>
        </div>

        <!-- Right Column: Evidence Chains -->
        <div style="flex: 1; display: flex; flex-direction: column;">
            <div style="font-size: 15px; font-weight: 800; color: #4472C4; margin-bottom: 16px; border-bottom: 3px solid #4472C4; padding-bottom: 4px; text-transform: uppercase;">Evidence Chains</div>
            
            <div style="background: #FCE4D6; border: 2px solid #C65911; border-left: 6px solid #C00000; padding: 14px; margin-bottom: 22px; border-radius: 2px; box-shadow: 3px 3px 5px rgba(0,0,0,0.08);">
                <div style="font-size: 14px; font-weight: 800; color: #C00000; margin-bottom: 8px;">Chain 1: SMS Exfiltration</div>
                <div style="font-family: monospace; font-size: 12.5px; color: #404040; line-height: 1.5; font-weight: bold;">
                    SMS_RECEIVED<br>
                    &nbsp;<span style="color: #C65911;">↳</span> OTP regex matching<br>
                    &nbsp;&nbsp;<span style="color: #C65911;">↳</span> HTTP POST (Non-bank)
                </div>
            </div>
            
            <div style="background: #FCE4D6; border: 2px solid #C65911; border-left: 6px solid #C00000; padding: 14px; margin-bottom: 22px; border-radius: 2px; box-shadow: 3px 3px 5px rgba(0,0,0,0.08);">
                <div style="font-size: 14px; font-weight: 800; color: #C00000; margin-bottom: 8px;">Chain 2: Credential Overlay</div>
                <div style="font-family: monospace; font-size: 12.5px; color: #404040; line-height: 1.5; font-weight: bold;">
                    BOI app launch detected<br>
                    &nbsp;<span style="color: #C65911;">↳</span> SYSTEM_ALERT_WINDOW<br>
                    &nbsp;&nbsp;<span style="color: #C65911;">↳</span> Fake Login WebView<br>
                    &nbsp;&nbsp;&nbsp;<span style="color: #C65911;">↳</span> Credential capture
                </div>
            </div>

            <div style="background: #FCE4D6; border: 2px solid #C65911; border-left: 6px solid #C00000; padding: 14px; border-radius: 2px; box-shadow: 3px 3px 5px rgba(0,0,0,0.08);">
                <div style="font-size: 14px; font-weight: 800; color: #C00000; margin-bottom: 8px;">Chain 3: Accessibility</div>
                <div style="font-family: monospace; font-size: 12.5px; color: #404040; line-height: 1.5; font-weight: bold;">
                    AccessibilityService<br>
                    &nbsp;<span style="color: #C65911;">↳</span> Read Screen Content<br>
                    &nbsp;&nbsp;<span style="color: #C65911;">↳</span> Auto-click "Grant"
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

new_content = content[:s6_start] + new_slide_6 + "\n" + content[s7_start:]

with open(filepath, "w") as f:
    f.write(new_content)

print("Updated Slide 6 successfully")
