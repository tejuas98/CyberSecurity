import sys

filepath = "/Users/toru/Projects and codes/project manager/ps1.html"

with open(filepath, "r") as f:
    content = f.read()

s6_idx = content.find("<!-- SLIDE 6:")
if s6_idx == -1:
    print("Could not find SLIDE 6")
    sys.exit(1)

content_before = content[:s6_idx]

slides_html = """
<!-- SLIDE 6: Bank Profile Adapter + Evidence Graph -->
<div class="slide" style="display: flex; flex-direction: column; padding: 32px 40px; background-color: #FFFFFF;">
    <div style="margin-bottom: 4px; color: #64748B; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">CORE ENGINES</div>
    <h2 style="font-family: var(--font-main); font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">Bank Profile Adapter & Evidence Graph</h2>
    <div class="subtitle" style="font-size: 13px; color: #475569; margin-bottom: 24px;">SurakshaAPK detects malicious intent by proving behavior chains against bank-specific profiles — not by blindly flagging dangerous permissions.</div>
    
    <div style="display: flex; flex: 1; gap: 24px; min-height: 0;">
        
        <!-- Left: Bank Profile Flow -->
        <div style="flex: 1; display: flex; flex-direction: column; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 16px; border-bottom: 2px solid #CBD5E1; padding-bottom: 8px;">Impersonation Detection Flow</div>
            
            <div style="display: flex; flex-direction: column; gap: 8px; flex: 1;">
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; text-align: center; font-weight: 800; font-size: 11px; color: #0F172A;">Suspicious APK Uploaded</div>
                <div style="text-align: center; color: #94A3B8;">↓</div>
                
                <div style="display: flex; align-items: center; justify-content: center; gap: 12px;">
                    <div style="background: #FFF7ED; border: 1.5px solid #EA580C; padding: 10px; border-radius: 6px; text-align: center; font-weight: 800; font-size: 11px; color: #0F172A; width: 140px;">Claims BOI identity?</div>
                    <div style="display: flex; flex-direction: column; gap: 4px;">
                        <div style="font-size: 10px; color: #10B981; font-weight: 800;">NO → Generic scan</div>
                        <div style="font-size: 10px; color: #EF4444; font-weight: 800;">YES → Continue</div>
                    </div>
                </div>
                
                <div style="text-align: center; color: #94A3B8;">↓</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; text-align: center; font-weight: 800; font-size: 11px; color: #0F172A;">Package/certificate mismatch?</div>
                <div style="text-align: center; color: #94A3B8;">↓</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; text-align: center; font-weight: 800; font-size: 11px; color: #0F172A;">Uses KYC/loan/account-freeze bait?</div>
                <div style="text-align: center; color: #94A3B8;">↓</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; text-align: center; font-weight: 800; font-size: 11px; color: #0F172A;">Collects OTP / credentials?</div>
                <div style="text-align: center; color: #94A3B8;">↓</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; text-align: center; font-weight: 800; font-size: 11px; color: #0F172A;">Sends data to non-bank endpoint?</div>
                <div style="text-align: center; color: #EF4444; font-weight: 800;">↓</div>
                <div style="background: #FEF2F2; border: 1.5px solid #EF4444; padding: 10px; border-radius: 6px; text-align: center; font-weight: 800; font-size: 12px; color: #B91C1C;">High Risk: Bank Impersonation Fraud APK</div>
            </div>
        </div>
        
        <!-- Right: Evidence Graph -->
        <div style="flex: 1.2; display: flex; flex-direction: column; gap: 16px;">
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; flex: 1;">
                <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 16px; border-bottom: 2px solid #CBD5E1; padding-bottom: 8px;">Evidence Chains</div>
                
                <div style="font-weight: 800; font-size: 11px; color: #0F172A; margin-bottom: 8px;">Chain 1: SMS Exfiltration</div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: #FFFFFF; border: 1px solid #94A3B8; padding: 12px; border-radius: 6px; margin-bottom: 16px;">
                    <div style="font-family: monospace; font-size: 10px; color: #0284C7; font-weight: 600;">SOURCE<br><span style="color:#0F172A;">android.intent.action.SMS_RECEIVED</span></div>
                    <div style="color: #94A3B8; font-weight: 800;">→</div>
                    <div style="font-family: monospace; font-size: 10px; color: #EA580C; font-weight: 600;">TRANSFORM<br><span style="color:#0F172A;">Regex extraction (OTP)</span></div>
                    <div style="color: #94A3B8; font-weight: 800;">→</div>
                    <div style="font-family: monospace; font-size: 10px; color: #E11D48; font-weight: 600;">SINK<br><span style="color:#0F172A;">hxxps://fake-boi-update.com/log</span></div>
                </div>
                
                <div style="font-weight: 800; font-size: 11px; color: #0F172A; margin-bottom: 8px;">Chain 2: Credential Capture Overlay</div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: #FFFFFF; border: 1px solid #94A3B8; padding: 12px; border-radius: 6px;">
                    <div style="font-family: monospace; font-size: 10px; color: #0284C7; font-weight: 600;">TRIGGER<br><span style="color:#0F172A;">com.boi.ua.android launch</span></div>
                    <div style="color: #94A3B8; font-weight: 800;">→</div>
                    <div style="font-family: monospace; font-size: 10px; color: #EA580C; font-weight: 600;">ACTION<br><span style="color:#0F172A;">SYSTEM_ALERT_WINDOW</span></div>
                    <div style="color: #94A3B8; font-weight: 800;">→</div>
                    <div style="font-family: monospace; font-size: 10px; color: #E11D48; font-weight: 600;">IMPACT<br><span style="color:#0F172A;">Credential Hijack</span></div>
                </div>
            </div>
            
            <div style="background: #0B1F3A; color: #FFFFFF; border-radius: 8px; padding: 16px; font-family: monospace; font-size: 11px; line-height: 1.5;">
                <div style="color: #94A3B8; margin-bottom: 8px;">// boi_profile.json snippet</div>
                <span style="color: #38BDF8;">"official_package"</span>: <span style="color: #A3E635;">"com.boi.ua.android"</span>,<br>
                <span style="color: #38BDF8;">"allowed_domains"</span>: [<span style="color: #A3E635;">"bankofindia.co.in"</span>, <span style="color: #A3E635;">"starconnectcbs.bankofindia.com"</span>],<br>
                <span style="color: #38BDF8;">"sms_patterns"</span>: [<span style="color: #A3E635;">"OTP for BOI"</span>, <span style="color: #A3E635;">"Bank of India"</span>]
            </div>
            
        </div>
    </div>
    
    <div class="footer" style="background-color: transparent; color: #94A3B8; position: static; padding: 20px 0 0 0; display: flex; justify-content: space-between; font-weight: 600;">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • PS1</span>
        <span>6 / 12</span>
    </div>
</div>

<!-- SLIDE 7: Static & Dynamic Analysis Engines -->
<div class="slide" style="display: flex; flex-direction: column; padding: 32px 40px; background-color: #FFFFFF;">
    <div style="margin-bottom: 4px; color: #64748B; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">CORE ENGINES</div>
    <h2 style="font-family: var(--font-main); font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">Static & Dynamic Analysis Engines</h2>
    <div class="subtitle" style="font-size: 13px; color: #475569; margin-bottom: 24px;">Automated decompilation followed by triggered dynamic validation to bypass evasion techniques.</div>
    
    <div style="display: flex; flex: 1; gap: 24px; min-height: 0;">
        
        <!-- Left: Static Pipeline -->
        <div style="flex: 1; display: flex; flex-direction: column; gap: 16px;">
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; flex: 1;">
                <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 12px; border-bottom: 2px solid #CBD5E1; padding-bottom: 8px;">Static Pipeline</div>
                
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; font-weight: 600; font-size: 11px; color: #0F172A;">1. APK Unpacking (Apktool)</div>
                    <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; font-weight: 600; font-size: 11px; color: #0F172A;">2. Manifest Parsing (Permissions/Services)</div>
                    <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; font-weight: 600; font-size: 11px; color: #0F172A;">3. Decompilation (JADX to Java/Smali)</div>
                    <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 10px; border-radius: 6px; font-weight: 600; font-size: 11px; color: #0F172A;">4. IoC Extraction (URLs, IPs, Crypto keys)</div>
                </div>
            </div>
            
            <div style="background: #0B1F3A; color: #FFFFFF; border-radius: 8px; padding: 16px; font-family: monospace; font-size: 10px; line-height: 1.5;">
                <div style="color: #94A3B8; margin-bottom: 4px;">// static_features.json</div>
                <span style="color: #38BDF8;">"permissions"</span>: [<span style="color: #A3E635;">"RECEIVE_SMS"</span>, <span style="color: #A3E635;">"SYSTEM_ALERT_WINDOW"</span>],<br>
                <span style="color: #38BDF8;">"urls"</span>: [<span style="color: #A3E635;">"hxxps://unknown-c2.example/api"</span>],<br>
                <span style="color: #38BDF8;">"obfuscation_score"</span>: <span style="color: #F59E0B;">0.72</span>,<br>
                <span style="color: #38BDF8;">"bank_profile_match"</span>: <span style="color: #EF4444;">"BOI impersonation suspected"</span>
            </div>
        </div>
        
        <!-- Right: Dynamic Analysis -->
        <div style="flex: 1.2; display: flex; flex-direction: column; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 16px; border-bottom: 2px solid #CBD5E1; padding-bottom: 8px;">Dynamic Sandbox Validation</div>
            
            <div style="display: flex; gap: 16px; flex: 1;">
                
                <!-- Emulator Mockup -->
                <div style="width: 140px; background: #000000; border-radius: 16px; border: 4px solid #334155; padding: 4px; display: flex; flex-direction: column;">
                    <div style="height: 12px; background: #1E293B; border-radius: 8px 8px 0 0; display: flex; justify-content: center; align-items: center;"><div style="width: 30px; height: 4px; background: #000; border-radius: 2px;"></div></div>
                    <div style="flex: 1; background: #FFFFFF; padding: 8px; display: flex; flex-direction: column; gap: 8px;">
                        <div style="font-weight: 800; font-size: 10px; color: #005BAC; text-align: center; margin-top: 20px;">Bank Of India KYC</div>
                        <div style="background: #F1F5F9; border: 1px solid #CBD5E1; padding: 4px; font-size: 8px; color: #64748B;">Enter Pan Card Number</div>
                        <div style="background: #F1F5F9; border: 1px solid #CBD5E1; padding: 4px; font-size: 8px; color: #64748B;">Enter OTP</div>
                        <div style="background: #005BAC; color: white; padding: 6px; font-size: 9px; text-align: center; font-weight: bold; border-radius: 4px;">Submit</div>
                    </div>
                </div>
                
                <!-- Runtime Logs -->
                <div style="flex: 1; display: flex; flex-direction: column; gap: 8px;">
                    <div style="background: #FEF2F2; border-left: 3px solid #EF4444; padding: 8px; font-family: monospace; font-size: 9px; color: #0F172A;">
                        <strong style="color: #B91C1C;">[TRIGGER] Fake OTP Injected</strong><br>
                        adb shell dumpsys activity broadcast ...<br>
                        OTP: 582194
                    </div>
                    <div style="background: #FFF7ED; border-left: 3px solid #EA580C; padding: 8px; font-family: monospace; font-size: 9px; color: #0F172A;">
                        <strong style="color: #C2410C;">[ACTION] BroadcastReceiver</strong><br>
                        SMS intercepted by com.fake.boi.kyc.Receiver
                    </div>
                    <div style="background: #FEF2F2; border-left: 3px solid #EF4444; padding: 8px; font-family: monospace; font-size: 9px; color: #0F172A;">
                        <strong style="color: #B91C1C;">[NETWORK] C2 Exfiltration</strong><br>
                        POST hxxps://unknown-c2.example/api/otp<br>
                        Payload: {"otp": "582194"}
                    </div>
                    
                    <div style="margin-top: auto; font-weight: 800; font-size: 11px; color: #0F172A; background: #E2E8F0; padding: 8px; border-radius: 4px; text-align: center;">
                        Verdict: Runtime Fraud Confirmed
                    </div>
                </div>
                
            </div>
        </div>
    </div>
    
    <div class="footer" style="background-color: transparent; color: #94A3B8; position: static; padding: 20px 0 0 0; display: flex; justify-content: space-between; font-weight: 600;">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • PS1</span>
        <span>7 / 12</span>
    </div>
</div>

<!-- SLIDE 8: GenAI, Risk Scoring & Report Outputs -->
<div class="slide" style="display: flex; flex-direction: column; padding: 32px 40px; background-color: #FFFFFF;">
    <div style="margin-bottom: 4px; color: #64748B; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">EXPLAINABILITY & COMPLIANCE</div>
    <h2 style="font-family: var(--font-main); font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">GenAI, Risk Scoring & Outputs</h2>
    <div class="subtitle" style="font-size: 13px; color: #475569; margin-bottom: 24px;">GenAI writes the explanation. Deterministic engines decide the score.</div>
    
    <div style="display: flex; flex: 1; gap: 24px; min-height: 0;">
        
        <!-- Left: Risk Gauge & Actions -->
        <div style="flex: 0 0 300px; display: flex; flex-direction: column; gap: 16px;">
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 24px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1;">
                <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 16px;">Risk Assessment</div>
                
                <div style="width: 120px; height: 120px; border-radius: 50%; border: 12px solid #EF4444; border-bottom-color: #E2E8F0; border-left-color: #E2E8F0; transform: rotate(45deg); display: flex; align-items: center; justify-content: center; margin-bottom: 8px;">
                    <div style="transform: rotate(-45deg); text-align: center;">
                        <div style="font-weight: 900; font-size: 32px; color: #B91C1C; line-height: 1;">87</div>
                        <div style="font-size: 10px; font-weight: 800; color: #64748B;">/ 100</div>
                    </div>
                </div>
                
                <div style="background: #FEF2F2; color: #B91C1C; font-weight: 900; font-size: 18px; padding: 6px 16px; border-radius: 4px; margin-bottom: 8px;">CRITICAL</div>
                <div style="font-size: 12px; color: #475569; font-weight: 600;">Confidence: 92%</div>
            </div>
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; gap: 8px;">
                <div style="font-weight: 800; font-size: 12px; color: #0F172A; margin-bottom: 4px;">Export Formats</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 8px; border-radius: 4px; font-weight: 800; font-size: 11px; color: #0F172A; text-align: center;">PDF Report</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 8px; border-radius: 4px; font-weight: 800; font-size: 11px; color: #0F172A; text-align: center;">IOC JSON</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 8px; border-radius: 4px; font-weight: 800; font-size: 11px; color: #0F172A; text-align: center;">YARA Rule</div>
                <div style="background: #FFFFFF; border: 1px solid #94A3B8; padding: 8px; border-radius: 4px; font-weight: 800; font-size: 11px; color: #0F172A; text-align: center;">SIEM Event</div>
                <div style="background: #0284C7; border: 1px solid #0369A1; padding: 8px; border-radius: 4px; font-weight: 800; font-size: 11px; color: #FFFFFF; text-align: center;">CERT-In Draft</div>
            </div>
        </div>
        
        <!-- Right: GenAI Report Mockup -->
        <div style="flex: 1; background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 16px solid #005BAC; border-radius: 4px; padding: 24px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column;">
            <div style="font-family: serif; font-size: 20px; font-weight: bold; color: #0F172A; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px; margin-bottom: 16px; text-align: center;">SurakshaAPK Investigation Report</div>
            
            <div style="display: flex; justify-content: space-between; margin-bottom: 20px; font-family: monospace; font-size: 11px; color: #475569; border-bottom: 1px dotted #CBD5E1; padding-bottom: 12px;">
                <div><strong>Target:</strong> BOI_KYC_Update.apk<br><strong>SHA-256:</strong> a8f9c3e2...1b4x</div>
                <div style="text-align: right;"><strong>Date:</strong> 2026-06-10<br><strong>Bank Profile:</strong> Bank of India</div>
            </div>
            
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 8px;">AI Threat Summary</div>
            <div style="font-size: 12px; color: #334155; line-height: 1.6; margin-bottom: 24px; background: #F8FAFC; padding: 12px; border-radius: 4px; border-left: 4px solid #005BAC;">
                This APK exhibits OTP theft and overlay phishing behavior. Evidence E1 shows SMS_RECEIVED data is parsed and sent to a non-bank endpoint. Evidence E2 indicates fake login overlay indicators targeting the BOI profile. Static decomposition revealed high obfuscation and misuse of SYSTEM_ALERT_WINDOW.
            </div>
            
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 8px;">Key Evidence Chains</div>
            <ul style="font-size: 12px; color: #334155; margin-bottom: 24px; padding-left: 20px; line-height: 1.6;">
                <li><strong>E1:</strong> Dynamic sandbox captured HTTP POST containing injected fake OTP.</li>
                <li><strong>E2:</strong> Manifest requests SYSTEM_ALERT_WINDOW with activities matching official BOI intent names.</li>
            </ul>
            
            <div style="margin-top: auto; background: #FEF2F2; border: 1px solid #FCA5A5; padding: 12px; border-radius: 4px;">
                <div style="font-weight: 800; font-size: 12px; color: #B91C1C; margin-bottom: 4px;">Recommended Action</div>
                <div style="font-size: 11px; color: #991B1B;">Block domains [hxxps://unknown-c2.example]. Escalate to SOC for takedown. Submit generated CERT-In draft.</div>
            </div>
            
        </div>
    </div>
    
    <div class="footer" style="background-color: transparent; color: #94A3B8; position: static; padding: 20px 0 0 0; display: flex; justify-content: space-between; font-weight: 600;">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • PS1</span>
        <span>8 / 12</span>
    </div>
</div>

<!-- SLIDE 9: Technical Stack & Deployment Modes -->
<div class="slide" style="display: flex; flex-direction: column; padding: 32px 40px; background-color: #FFFFFF;">
    <div style="margin-bottom: 4px; color: #64748B; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">ARCHITECTURE</div>
    <h2 style="font-family: var(--font-main); font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">Technical Stack & Deployment Modes</h2>
    <div class="subtitle" style="font-size: 13px; color: #475569; margin-bottom: 24px;">Built on open-source, deterministic security tooling with flexible, privacy-first deployment models.</div>
    
    <div style="display: flex; flex: 1; gap: 24px; min-height: 0;">
        
        <!-- Left: Stack Layers -->
        <div style="flex: 1.2; display: flex; flex-direction: column; gap: 12px;">
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
                <div style="font-weight: 800; font-size: 14px; color: #0284C7; margin-bottom: 8px;">1. Presentation & API</div>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">React</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">Next.js</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">FastAPI</span>
                </div>
            </div>
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
                <div style="font-weight: 800; font-size: 14px; color: #EA580C; margin-bottom: 8px;">2. Static & Dynamic Analysis Core</div>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">Python</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">JADX</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">AndroGuard</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">APKiD</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">Android AVD</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">ADB</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">Frida</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">MITMProxy</span>
                </div>
            </div>
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
                <div style="font-weight: 800; font-size: 14px; color: #10B981; margin-bottom: 8px;">3. AI & Data Layer</div>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">Ollama (Local LLM)</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">Llama 3</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">PostgreSQL</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">SQLite</span>
                    <span style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 4px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; color: #0F172A;">Docker</span>
                </div>
            </div>
        </div>
        
        <!-- Right: Deployment Modes -->
        <div style="flex: 1; display: flex; flex-direction: column; gap: 16px;">
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; border-bottom: 2px solid #CBD5E1; padding-bottom: 8px;">Deployment Architectures</div>
            
            <div style="background: #FFFFFF; border: 2px solid #005BAC; border-radius: 8px; padding: 16px; position: relative;">
                <div style="position: absolute; top: -10px; right: 16px; background: #005BAC; color: #FFF; font-size: 9px; font-weight: 800; padding: 4px 8px; border-radius: 12px; text-transform: uppercase;">Recommended</div>
                <div style="font-weight: 800; font-size: 13px; color: #0F172A; margin-bottom: 4px;">Fully Local Air-Gapped</div>
                <div style="font-size: 11px; color: #475569; line-height: 1.4;">All static parsing, emulation, and Ollama LLM execution happens locally. Zero data leaves the secure SOC network.</div>
            </div>
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 16px;">
                <div style="font-weight: 800; font-size: 13px; color: #0F172A; margin-bottom: 4px;">Metadata-Only Cloud</div>
                <div style="font-size: 11px; color: #475569; line-height: 1.4;">Heavy processing runs locally. Only anonymized evidence hashes and extracted feature metadata are sent to a cloud endpoint for GenAI compilation. No raw APK egress.</div>
            </div>
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 16px;">
                <div style="font-weight: 800; font-size: 13px; color: #0F172A; margin-bottom: 4px;">Centralized Bank API</div>
                <div style="font-size: 11px; color: #475569; line-height: 1.4;">Headless deployment as an internal API service. Other banking microservices submit APKs and receive automated JSON verdicts.</div>
            </div>
        </div>
    </div>
    
    <div class="footer" style="background-color: transparent; color: #94A3B8; position: static; padding: 20px 0 0 0; display: flex; justify-content: space-between; font-weight: 600;">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • PS1</span>
        <span>9 / 12</span>
    </div>
</div>

<!-- SLIDE 10: Dataset & Validation Plan -->
<div class="slide" style="display: flex; flex-direction: column; padding: 32px 40px; background-color: #FFFFFF;">
    <div style="margin-bottom: 4px; color: #64748B; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">EVALUATION</div>
    <h2 style="font-family: var(--font-main); font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">Dataset & Validation Plan</h2>
    <div class="subtitle" style="font-size: 13px; color: #475569; margin-bottom: 24px;">Rigorous testing against real-world obfuscation and impersonation techniques. No deployable malware is generated; only controlled synthetic samples are used.</div>
    
    <div style="display: flex; flex-direction: column; flex: 1; gap: 20px; min-height: 0;">
        
        <!-- Validation Pipeline -->
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 16px;">
            <div style="font-weight: 800; font-size: 12px; color: #0F172A; margin-bottom: 12px;">Validation Pipeline</div>
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="background: #FFFFFF; border: 1.5px solid #005BAC; padding: 8px 16px; border-radius: 6px; font-weight: 800; font-size: 11px; color: #005BAC; text-align: center;">Dataset<br><span style="font-weight:400; font-size:9px;">Curated APKs</span></div>
                <div style="color: #94A3B8; font-weight: 800;">→</div>
                <div style="background: #FFFFFF; border: 1.5px solid #0F172A; padding: 8px 16px; border-radius: 6px; font-weight: 800; font-size: 11px; color: #0F172A; text-align: center;">Feature Extraction<br><span style="font-weight:400; font-size:9px;">Static + Dynamic</span></div>
                <div style="color: #94A3B8; font-weight: 800;">→</div>
                <div style="background: #FFFFFF; border: 1.5px solid #0F172A; padding: 8px 16px; border-radius: 6px; font-weight: 800; font-size: 11px; color: #0F172A; text-align: center;">Evidence Chain<br><span style="font-weight:400; font-size:9px;">Logic Detection</span></div>
                <div style="color: #94A3B8; font-weight: 800;">→</div>
                <div style="background: #FFFFFF; border: 1.5px solid #0F172A; padding: 8px 16px; border-radius: 6px; font-weight: 800; font-size: 11px; color: #0F172A; text-align: center;">Analyst Review<br><span style="font-weight:400; font-size:9px;">Ground Truth</span></div>
                <div style="color: #94A3B8; font-weight: 800;">→</div>
                <div style="background: #ECFDF5; border: 1.5px solid #10B981; padding: 8px 16px; border-radius: 6px; font-weight: 800; font-size: 11px; color: #047857; text-align: center;">Metrics<br><span style="font-weight:400; font-size:9px;">Accuracy / FP Rate</span></div>
            </div>
        </div>
        
        <!-- Table -->
        <div style="flex: 1; overflow: hidden; border: 1px solid #E2E8F0; border-radius: 8px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 11px; text-align: left;">
                <thead>
                    <tr style="background: #0F172A; color: #FFFFFF;">
                        <th style="padding: 12px; font-weight: 800;">Dataset Category</th>
                        <th style="padding: 12px; font-weight: 800;">Characteristics</th>
                        <th style="padding: 12px; font-weight: 800;">SurakshaAPK Objective</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #E2E8F0;">
                        <td style="padding: 12px; font-weight: 800; color: #0F172A;">Clean / Official Banking</td>
                        <td style="padding: 12px; color: #475569;">Official BOI / PSB applications. Packed, highly permissioned.</td>
                        <td style="padding: 12px; color: #10B981;">Ensure 0% False Positive rate. Prove legitimate context.</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                        <td style="padding: 12px; font-weight: 800; color: #0F172A;">Generic Clean Utility</td>
                        <td style="padding: 12px; color: #475569;">Calculator, Notes. Low permissions.</td>
                        <td style="padding: 12px; color: #10B981;">Baseline testing. Fast-path triage bypass.</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #E2E8F0;">
                        <td style="padding: 12px; font-weight: 800; color: #0F172A;">Synthetic Fraud (Obfuscated)</td>
                        <td style="padding: 12px; color: #475569;">ProGuard / DexGuard applied. Hidden C2 endpoints.</td>
                        <td style="padding: 12px; color: #EA580C;">Test dynamic sandbox trigger hooks and decryption capture.</td>
                    </tr>
                    <tr style="background: #FEF2F2;">
                        <td style="padding: 12px; font-weight: 800; color: #B91C1C;">Targeted BOI Impersonators</td>
                        <td style="padding: 12px; color: #B91C1C;">Fake KYC wrappers, fake logos, SMS stealers, overlay loaders.</td>
                        <td style="padding: 12px; color: #B91C1C;">Test Bank Profile Adapter matching and Critical SOC Alerting.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
    </div>
    
    <div class="footer" style="background-color: transparent; color: #94A3B8; position: static; padding: 20px 0 0 0; display: flex; justify-content: space-between; font-weight: 600;">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • PS1</span>
        <span>10 / 12</span>
    </div>
</div>

<!-- SLIDE 11: Research, Comparison & Feasibility -->
<div class="slide" style="display: flex; flex-direction: column; padding: 32px 40px; background-color: #FFFFFF;">
    <div style="margin-bottom: 4px; color: #64748B; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">FEASIBILITY</div>
    <h2 style="font-family: var(--font-main); font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">Research, Comparison & Feasibility</h2>
    <div class="subtitle" style="font-size: 13px; color: #475569; margin-bottom: 24px;">SurakshaAPK integrates reverse-engineering evidence into a bank-specific workflow, bypassing generic tool limitations.</div>
    
    <div style="display: flex; flex: 1; gap: 24px; min-height: 0;">
        
        <!-- Left: Comparison Table -->
        <div style="flex: 1.2; display: flex; flex-direction: column;">
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 12px;">Market Comparison</div>
            <div style="border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden;">
                <table style="width: 100%; border-collapse: collapse; font-size: 11px; text-align: left;">
                    <thead>
                        <tr style="background: #F8FAFC; border-bottom: 2px solid #E2E8F0;">
                            <th style="padding: 12px; font-weight: 800; color: #475569;">Capability</th>
                            <th style="padding: 12px; font-weight: 800; color: #EF4444; text-align: center;">Generic Scanners<br>(VirusTotal)</th>
                            <th style="padding: 12px; font-weight: 800; color: #10B981; text-align: center;">SurakshaAPK</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 12px; font-weight: 800; color: #0F172A;">Static APK analysis</td>
                            <td style="padding: 12px; text-align: center; color: #10B981;">✔</td>
                            <td style="padding: 12px; text-align: center; color: #10B981;">✔</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 12px; font-weight: 800; color: #0F172A;">Local/private deployment</td>
                            <td style="padding: 12px; text-align: center; color: #EF4444;">✘</td>
                            <td style="padding: 12px; text-align: center; color: #10B981;">✔</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 12px; font-weight: 800; color: #0F172A;">Triggered dynamic validation</td>
                            <td style="padding: 12px; text-align: center; color: #EF4444;">Partial</td>
                            <td style="padding: 12px; text-align: center; color: #10B981;">✔</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 12px; font-weight: 800; color: #0F172A;">Bank Profile Adapter</td>
                            <td style="padding: 12px; text-align: center; color: #EF4444;">✘</td>
                            <td style="padding: 12px; text-align: center; color: #10B981;">✔</td>
                        </tr>
                        <tr>
                            <td style="padding: 12px; font-weight: 800; color: #0F172A;">Evidence-grounded GenAI reports</td>
                            <td style="padding: 12px; text-align: center; color: #EF4444;">✘</td>
                            <td style="padding: 12px; text-align: center; color: #10B981;">✔</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- Right: Feasibility -->
        <div style="flex: 1; display: flex; flex-direction: column;">
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; margin-bottom: 12px;">Implementation Feasibility</div>
            
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="background: #F8FAFC; border-left: 4px solid #EA580C; padding: 12px; border-radius: 0 8px 8px 0;">
                    <div style="font-weight: 800; font-size: 11px; color: #0F172A; margin-bottom: 4px;">Challenge: LLM Hallucination</div>
                    <div style="font-size: 10px; color: #475569;"><strong>Mitigation:</strong> GenAI only formats extracted JSON evidence. It does not dictate the risk score.</div>
                </div>
                
                <div style="background: #F8FAFC; border-left: 4px solid #0284C7; padding: 12px; border-radius: 0 8px 8px 0;">
                    <div style="font-weight: 800; font-size: 11px; color: #0F172A; margin-bottom: 4px;">Challenge: Heavy Infrastructure</div>
                    <div style="font-size: 10px; color: #475569;"><strong>Mitigation:</strong> Emulators run headless. Static triage filters 80% of benign APKs before emulation.</div>
                </div>
                
                <div style="background: #F8FAFC; border-left: 4px solid #10B981; padding: 12px; border-radius: 0 8px 8px 0;">
                    <div style="font-weight: 800; font-size: 11px; color: #0F172A; margin-bottom: 4px;">Challenge: Data Privacy</div>
                    <div style="font-size: 10px; color: #475569;"><strong>Mitigation:</strong> 100% local processing mode guarantees no APK or PII leaves the bank's internal network.</div>
                </div>
            </div>
        </div>
        
    </div>
    
    <div class="footer" style="background-color: transparent; color: #94A3B8; position: static; padding: 20px 0 0 0; display: flex; justify-content: space-between; font-weight: 600;">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • PS1</span>
        <span>11 / 12</span>
    </div>
</div>

<!-- SLIDE 12: Demo Strategy, Use Cases & Impact -->
<div class="slide" style="display: flex; flex-direction: column; padding: 32px 40px; background-color: #FFFFFF;">
    <div style="margin-bottom: 4px; color: #64748B; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">CONCLUSION</div>
    <h2 style="font-family: var(--font-main); font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">Demo Strategy, Use Cases & Impact</h2>
    <div class="subtitle" style="font-size: 13px; color: #475569; margin-bottom: 24px;">SurakshaAPK helps banks move from reactive manual APK analysis to proactive, automated, evidence-based fraud defense.</div>
    
    <div style="display: flex; flex: 1; gap: 24px; min-height: 0;">
        
        <!-- Left: Prototype Dashboard Mockup -->
        <div style="flex: 1; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column;">
            <div style="background: #0F172A; padding: 8px 16px; color: #FFFFFF; font-weight: 800; font-size: 12px; display: flex; justify-content: space-between; align-items: center;">
                <span>SurakshaAPK Console</span>
                <span style="background: #10B981; color: #FFFFFF; font-size: 9px; padding: 2px 6px; border-radius: 4px;">Local Mode</span>
            </div>
            <div style="padding: 24px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1;">
                <div style="border: 2px dashed #94A3B8; border-radius: 8px; width: 100%; padding: 32px; text-align: center; margin-bottom: 16px; background: #FFFFFF;">
                    <div style="font-size: 24px; color: #64748B; margin-bottom: 8px;">📁</div>
                    <div style="font-weight: 800; font-size: 13px; color: #0F172A;">Drop Suspicious APK Here</div>
                    <div style="font-size: 11px; color: #64748B; margin-top: 4px;">BOI_KYC_Update.apk</div>
                </div>
                
                <div style="width: 100%; display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div style="font-size: 11px; color: #475569;"><strong>Profile:</strong> Bank of India</div>
                    <div style="font-size: 11px; color: #475569;"><strong>Tier:</strong> T1 + T2</div>
                </div>
                
                <div style="background: #005BAC; color: #FFFFFF; font-weight: 800; font-size: 13px; padding: 10px; width: 100%; text-align: center; border-radius: 6px;">Initiate Analysis</div>
            </div>
        </div>
        
        <!-- Right: Use Cases and Roadmap -->
        <div style="flex: 1.2; display: flex; flex-direction: column; gap: 16px;">
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; border-bottom: 2px solid #CBD5E1; padding-bottom: 8px;">Key Beneficiaries</div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div style="border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px;">
                    <div style="font-weight: 800; font-size: 12px; color: #0F172A; margin-bottom: 4px;">Tier 1 SOC Analysts</div>
                    <div style="font-size: 10px; color: #475569;">Instant triage. No manual reverse engineering needed. AI summaries explain the threat in plain English.</div>
                </div>
                <div style="border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px;">
                    <div style="font-weight: 800; font-size: 12px; color: #0F172A; margin-bottom: 4px;">Compliance Teams</div>
                    <div style="font-size: 10px; color: #475569;">1-click generation of CERT-In incident reporting drafts and RBI-compliant technical audits.</div>
                </div>
                <div style="border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px;">
                    <div style="font-weight: 800; font-size: 12px; color: #0F172A; margin-bottom: 4px;">Threat Intel (CTI)</div>
                    <div style="font-size: 10px; color: #475569;">Extracts infrastructure IOCs (C2 domains, attacker phone numbers) for immediate firewall blocking.</div>
                </div>
                <div style="border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px;">
                    <div style="font-weight: 800; font-size: 12px; color: #0F172A; margin-bottom: 4px;">Bank Customers</div>
                    <div style="font-size: 10px; color: #475569;">Faster takedowns of fake apps reduce the window of vulnerability, preventing financial loss.</div>
                </div>
            </div>
            
            <div style="font-weight: 800; font-size: 14px; color: #0F172A; border-bottom: 2px solid #CBD5E1; padding-bottom: 8px; margin-top: 8px;">Execution Roadmap</div>
            <div style="display: flex; gap: 8px; align-items: center;">
                <div style="flex: 1; background: #005BAC; color: #FFFFFF; padding: 8px; border-radius: 4px; font-size: 10px; text-align: center; font-weight: 800;">Phase 1<br><span style="font-weight:400; font-size:9px;">Static Core + AI</span></div>
                <div style="color: #94A3B8; font-weight: 800;">→</div>
                <div style="flex: 1; background: #0284C7; color: #FFFFFF; padding: 8px; border-radius: 4px; font-size: 10px; text-align: center; font-weight: 800;">Phase 2<br><span style="font-weight:400; font-size:9px;">Dynamic Hooking</span></div>
                <div style="color: #94A3B8; font-weight: 800;">→</div>
                <div style="flex: 1; background: #0369A1; color: #FFFFFF; padding: 8px; border-radius: 4px; font-size: 10px; text-align: center; font-weight: 800;">Phase 3<br><span style="font-weight:400; font-size:9px;">Bank API Integration</span></div>
            </div>
        </div>
    </div>
    
    <div class="footer" style="background-color: transparent; color: #94A3B8; position: static; padding: 20px 0 0 0; display: flex; justify-content: space-between; font-weight: 600;">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • PS1</span>
        <span>12 / 12</span>
    </div>
</div>
"""

content = content_before + slides_html + "</body>\n</html>"

with open(filepath, "w") as f:
    f.write(content)
print("Updated successfully")
