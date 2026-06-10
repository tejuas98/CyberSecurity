import sys

filepath = "/Users/toru/Projects and codes/project manager/ps1.html"

with open(filepath, "r") as f:
    content = f.read()

s7_start = content.find("<!-- SLIDE 7: Engines -->")
s11_start = content.find("<!-- SLIDE 11")
if s11_start == -1:
    s11_start = content.find("</body>")

if s7_start == -1:
    print("Could not find slide 7")
    sys.exit(1)

new_slides = """<!-- SLIDE 7: Engines -->
<div class="slide" style="padding: 20px 40px 20px 40px; display: flex; flex-direction: column;">
    <div style="font-weight: bold; color: #7F7F7F; font-size: 13px; text-transform: uppercase; margin-bottom: 2px; margin-left: 1px;">TECHNICAL DEEP DIVE</div>
    <h2 style="font-family: var(--font-main); font-size: 26px; font-weight: 800; color: var(--boi-navy); margin: 0 0 2px 0;">STATIC + DYNAMIC ANALYSIS ENGINES</h2>
    <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 10px; font-weight: bold;">Extracting source-sink mappings and validating them in a triggered sandbox</div>
    
    <div style="display: flex; gap: 12px; flex: 1; margin-bottom: 10px; min-height: 0;">
        <!-- Left: Static -->
        <div style="flex: 1; border: none; padding: 0 10px 0 0; background: transparent; display: flex; flex-direction: column; gap: 6px; min-height: 0;">
            <div style="font-size: 15px; font-weight: 900; color: #203864; text-transform: uppercase;">L1 Static Engine</div>
            
            <div style="display: flex; flex-direction: column; align-items: center; flex: 1; padding-top: 10px; justify-content: flex-start;">
                <!-- Root Node -->
                <div style="background: #B4C6E7; border: 1px solid #2F5597; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: bold; color: #000; box-shadow: 2px 2px 4px rgba(0,0,0,0.15); z-index: 2;">APK Unpacking</div>
                
                <!-- Vertical line from Root -->
                <div style="width: 2px; height: 16px; background: #333;"></div>
                
                <!-- Horizontal Branching Line -->
                <div style="width: 80%; height: 2px; background: #333; position: relative;">
                    <!-- Left Drop -->
                    <div style="position: absolute; left: 0; top: 0; width: 2px; height: 16px; background: #333;"></div>
                    <!-- Right Drop -->
                    <div style="position: absolute; right: 0; top: 0; width: 2px; height: 16px; background: #333;"></div>
                    
                    <!-- Left Arrowhead -->
                    <div style="position: absolute; left: -3px; top: 16px; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #333;"></div>
                    <!-- Right Arrowhead -->
                    <div style="position: absolute; right: -3px; top: 16px; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #333;"></div>
                </div>
                
                <!-- Level 2 Containers -->
                <div style="display: flex; justify-content: space-between; width: 90%; margin-top: 21px;">
                    
                    <!-- Left Branch (Manifest) -->
                    <div style="display: flex; flex-direction: column; align-items: center; width: 45%;">
                        <div style="background: #FFE699; border: 1px solid #BF8F00; padding: 6px 8px; border-radius: 6px; font-size: 11px; font-weight: bold; color: #000; box-shadow: 2px 2px 4px rgba(0,0,0,0.15); text-align: center; width: 100%;">Manifest Parsing</div>
                        
                        <div style="width: 2px; height: 16px; background: #333;"></div>
                        <div style="width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #333;"></div>
                        
                        <div style="background: #A9D08E; border: 1px solid #548235; padding: 6px 8px; border-radius: 6px; font-size: 11px; font-weight: bold; color: #000; box-shadow: 2px 2px 4px rgba(0,0,0,0.15); text-align: center; width: 100%; margin-top: 2px;">IoC Extraction</div>
                    </div>
                    
                    <!-- Right Branch (Decompilation) -->
                    <div style="display: flex; flex-direction: column; align-items: center; width: 45%;">
                        <div style="background: #FFE699; border: 1px solid #BF8F00; padding: 6px 8px; border-radius: 6px; font-size: 11px; font-weight: bold; color: #000; box-shadow: 2px 2px 4px rgba(0,0,0,0.15); text-align: center; width: 100%;">Decompilation</div>
                        
                        <div style="width: 2px; height: 16px; background: #333;"></div>
                        <div style="width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #333;"></div>
                        
                        <div style="background: #FCE4D6; border: 2px solid #C00000; padding: 6px 8px; border-radius: 6px; font-size: 11px; font-weight: bold; color: #C00000; box-shadow: 2px 2px 4px rgba(0,0,0,0.15); text-align: center; width: 100%; margin-top: 2px;">Source-Sink Mapping</div>

                        <div style="width: 2px; height: 16px; background: #333;"></div>
                        <div style="width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #333;"></div>
                        
                        <div style="background: #A9D08E; border: 1px solid #548235; padding: 6px 8px; border-radius: 6px; font-size: 11px; font-weight: bold; color: #000; box-shadow: 2px 2px 4px rgba(0,0,0,0.15); text-align: center; width: 100%; margin-top: 2px;">Obfuscation Check</div>
                    </div>
                    
                </div>
            </div>

            <!-- JSON Snippet -->
            <div style="margin-top: auto; border: none; padding: 12px; background: white; border-radius: 8px; overflow-y: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.08);">
                <div style="font-size: 12px; font-weight: 900; color: #203864; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
                    <span style="display: inline-block; width: 6px; height: 6px; background: #203864; border-radius: 50%;"></span>
                    STATIC_FEATURES.JSON
                </div>
                <pre style="margin: 0; font-family: monospace; font-size: 11px; color: #A5D6FF; background: #0D1117; padding: 12px; border-radius: 6px; white-space: pre-wrap; line-height: 1.4; border: 1px solid #30363D;">
{
  "permissions": [
    "RECEIVE_SMS",
    "SYSTEM_ALERT_WINDOW"
  ],
  "urls": ["hxxps://unknown-c2.example"],
  "obfuscation_score": 0.72,
  "bank_profile_match": "BOI"
}
                </pre>
            </div>
        </div>
        
        <!-- Right: Dynamic -->
        <div style="flex: 1.2; border: none; border-left: 2px solid #E2E8F0; padding: 0 0 0 20px; background: transparent; display: flex; flex-direction: column; gap: 6px; min-height: 0;">
            <div style="font-size: 15px; font-weight: 900; color: #C65911; margin-bottom: 2px; border-bottom: 1px solid #C65911; padding-bottom: 4px; text-transform: uppercase;">L2 Dynamic Sandbox</div>
            <div style="font-size: 12px; font-weight: bold; color: #404040; margin-bottom: 4px;">Validates static evidence via targeted triggers.</div>
            
            <div style="font-size: 12px; font-weight: 900; color: #404040; text-transform: uppercase;">Runtime Logs</div>
            <pre style="background: #111827; color: #00FF00; border: 1px solid #404040; padding: 8px; font-family: monospace; font-size: 11px; margin: 0; font-weight: bold; overflow-y: hidden; line-height: 1.3;">
> [TRIGGER] Fake OTP injected
> [ACTION] SmsReceiver invoked
> [NETWORK] C2 exfiltration
  -> dest: unknown-c2.example

> Verdict: Fraud Confirmed
            </pre>
            
            <!-- Phone Mockups Row -->
            <div style="display: flex; gap: 12px; justify-content: center; margin-top: 15px; flex: 1;">
                
                <!-- Phone 1: Phishing Overlay -->
                <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
                    <div style="width: 140px; border: 2px solid #111827; border-radius: 8px; padding: 0; background: white; position: relative; display: flex; flex-direction: column; overflow: hidden; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); flex: 1;">
                        <div style="width: 30px; height: 4px; background: #111827; border-radius: 0 0 3px 3px; margin: 0 auto; position: absolute; top: 0; left: 50%; transform: translateX(-50%); z-index: 10;"></div>
                        <div style="background: #F2F2F2; color: #404040; padding: 14px 4px 6px 4px; text-align: center; font-size: 10px; font-weight: bold; border-bottom: 1px solid #D9D9D9;">App View</div>
                        <div style="padding: 12px 10px; background: #FFF2CC; display: flex; flex-direction: column; justify-content: center; flex: 1;">
                            <div style="font-size: 12px; font-weight: 900; color: #C00000; text-align: left; margin-bottom: 12px; text-transform: uppercase;">BOI Update</div>
                            <div style="border-bottom: 1px solid #A6A6A6; padding: 2px 0; font-size: 10px; font-weight: bold; color: #595959; margin-bottom: 10px;">OTP: 492011</div>
                            <div style="border-bottom: 1px solid #A6A6A6; padding: 2px 0; font-size: 10px; font-weight: bold; color: #595959; margin-bottom: 14px;">PIN: ****</div>
                            <div style="background: #4472C4; color: white; text-align: center; padding: 6px; font-size: 10px; font-weight: 900; margin-top: auto; text-transform: uppercase; border-radius: 20px;">Submit</div>
                        </div>
                    </div>
                    <div style="font-size: 11px; font-weight: 900; color: #C65911; text-transform: uppercase; text-align: center;">1. Overlay Trigger</div>
                </div>

                <!-- Phone 2: SMS Theft -->
                <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
                    <div style="width: 140px; border: 2px solid #111827; border-radius: 8px; padding: 0; background: white; position: relative; display: flex; flex-direction: column; overflow: hidden; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); flex: 1;">
                        <div style="width: 30px; height: 4px; background: #111827; border-radius: 0 0 3px 3px; margin: 0 auto; position: absolute; top: 0; left: 50%; transform: translateX(-50%); z-index: 10;"></div>
                        <div style="background: #F2F2F2; color: #404040; padding: 14px 4px 6px 4px; text-align: center; font-size: 10px; font-weight: bold; border-bottom: 1px solid #D9D9D9;">Background</div>
                        <div style="padding: 10px; background: #EAF4FF; display: flex; flex-direction: column; flex: 1; align-items: flex-start; justify-content: flex-start; gap: 8px;">
                            <div style="font-size: 11px; font-weight: 900; color: #203864;">📩 SMS Inbox</div>
                            <div style="background: #E2E8F0; padding: 8px; font-size: 9px; font-weight: bold; color: #334155; border-radius: 8px 8px 8px 0; line-height: 1.3; align-self: flex-start; max-width: 90%;">
                                Bank of India:<br>Your OTP is 492011.<br>Do not share.
                            </div>
                            <div style="font-size: 9px; font-weight: 900; color: #C00000; align-self: flex-end; margin-top: 4px;">[Intercepted]</div>
                        </div>
                    </div>
                    <div style="font-size: 11px; font-weight: 900; color: #C65911; text-transform: uppercase; text-align: center;">2. SMS Theft</div>
                </div>
                
                <!-- Phone 3: Network Exfiltration -->
                <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
                    <div style="width: 140px; border: 2px solid #111827; border-radius: 8px; padding: 0; background: white; position: relative; display: flex; flex-direction: column; overflow: hidden; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); flex: 1;">
                        <div style="width: 30px; height: 4px; background: #111827; border-radius: 0 0 3px 3px; margin: 0 auto; position: absolute; top: 0; left: 50%; transform: translateX(-50%); z-index: 10;"></div>
                        <div style="background: #F2F2F2; color: #404040; padding: 14px 4px 6px 4px; text-align: center; font-size: 10px; font-weight: bold; border-bottom: 1px solid #D9D9D9;">Network Inspect</div>
                        <div style="padding: 10px; background: #111827; color: #00FF00; font-family: monospace; font-size: 10px; display: flex; flex-direction: column; justify-content: flex-start; flex: 1; font-weight: bold; line-height: 1.5; gap: 4px; margin-top: 5px;">
                            <span style="color: #FF9900;">POST /api/otp</span>
                            <span style="color: #7F7F7F;">Host: unk-c2.dev</span>
                            <span style="color: #00FFFF; margin-top: 6px;">{"otp":"492011"}</span>
                        </div>
                    </div>
                    <div style="font-size: 11px; font-weight: 900; color: #C65911; text-transform: uppercase; text-align: center;">3. C2 Exfiltration</div>
                </div>

                <!-- Phone 4: Verdict -->
                <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
                    <div style="width: 140px; border: 2px solid #111827; border-radius: 8px; padding: 0; background: white; position: relative; display: flex; flex-direction: column; overflow: hidden; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); flex: 1;">
                        <div style="width: 30px; height: 4px; background: #111827; border-radius: 0 0 3px 3px; margin: 0 auto; position: absolute; top: 0; left: 50%; transform: translateX(-50%); z-index: 10;"></div>
                        <div style="background: #F2F2F2; color: #404040; padding: 14px 4px 6px 4px; text-align: center; font-size: 10px; font-weight: bold; border-bottom: 1px solid #D9D9D9;">Sandbox Verdict</div>
                        <div style="padding: 10px; background: #FCE4D6; display: flex; flex-direction: column; justify-content: center; flex: 1; text-align: center;">
                            <div style="font-size: 28px; margin-bottom: 8px; filter: drop-shadow(0 2px 2px rgba(192,0,0,0.3));">🚫</div>
                            <div style="font-size: 12px; font-weight: 900; color: #C00000; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.5px;">Fraud Detected</div>
                            <div style="font-size: 9px; font-weight: bold; color: #802020;">Process Terminated</div>
                        </div>
                    </div>
                    <div style="font-size: 11px; font-weight: 900; color: #C00000; text-transform: uppercase; text-align: center;">4. Threat Blocked</div>
                </div>

            </div>
        </div>
    </div>
    
    <!-- Tech Stack Bottom -->
    <div style="margin-top: auto; display: flex; justify-content: center; align-items: center; gap: 15px; font-family: monospace; font-size: 13px; font-weight: 900; background: #F2F2F2; padding: 10px; border: 1px solid #BFBFBF; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://cdn.simpleicons.org/androidstudio/2F5597" style="width: 16px; height: 16px;">
            <span style="color: #2F5597;">JADX</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://github.com/androguard.png" style="width: 16px; height: 16px; border-radius: 4px;">
            <span style="color: #2F5597;">AndroGuard</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://github.com/rednaga.png" style="width: 16px; height: 16px; border-radius: 4px;">
            <span style="color: #2F5597;">APKiD</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://github.com/VirusTotal.png" style="width: 16px; height: 16px; border-radius: 4px;">
            <span style="color: #2F5597;">YARA</span>
        </div>
        
        <span style="color: #BFBFBF; margin: 0 4px;">|</span>
        
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://cdn.simpleicons.org/android/C65911" style="width: 16px; height: 16px;">
            <span style="color: #C65911;">Android AVD</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://cdn.simpleicons.org/gnometerminal/C65911" style="width: 16px; height: 16px;">
            <span style="color: #C65911;">ADB</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://github.com/frida.png" style="width: 16px; height: 16px; border-radius: 4px;">
            <span style="color: #C65911;">Frida</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px;">
            <img src="https://github.com/mitmproxy.png" style="width: 16px; height: 16px; border-radius: 4px;">
            <span style="color: #C65911;">MITMProxy</span>
        </div>
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>7 / 10</span>
    </div>
</div>

<!-- SLIDE 8: GenAI -->
<div class="slide" style="padding: 20px 40px 20px 40px; display: flex; flex-direction: column;">
    <div style="font-weight: bold; color: #7F7F7F; font-size: 13px; text-transform: uppercase; margin-bottom: 2px; margin-left: 1px;">ANALYSIS OUTPUTS</div>
    <h2 style="font-family: var(--font-main); font-size: 26px; font-weight: 800; color: var(--boi-navy); margin: 0 0 2px 0;">GENAI, RISK SCORING & OUTPUTS</h2>
    <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 10px; font-weight: bold;">Deterministic engines decide the score; GenAI explains the evidence.</div>
    
    <div style="display: flex; gap: 20px; flex: 1; margin-bottom: 12px; min-height: 0;">
        <!-- Left: Risk Gauge & Buttons -->
        <div style="flex: 0 0 22%; display: flex; flex-direction: column; gap: 20px; min-height: 0;">
            <div style="background: transparent; border: none; padding: 0; text-align: left;">
                <div style="font-size: 14px; font-weight: 900; color: #404040; margin-bottom: 8px; text-transform: uppercase;">Risk Assessment</div>
                <div style="font-size: 48px; font-weight: 900; color: #C00000; margin-bottom: 4px; line-height: 1;">87<span style="font-size: 20px;">/100</span></div>
                <div style="background: #C00000; color: white; display: inline-block; padding: 4px 12px; font-weight: 900; font-size: 14px; margin-bottom: 8px; text-transform: uppercase; border-radius: 4px;">CRITICAL</div>
                <div style="font-size: 13px; color: #595959; font-weight: 900;">CONFIDENCE: 92%</div>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 10px; flex: 1; justify-content: flex-start;">
                <div style="font-size: 11px; font-weight: bold; color: #7F7F7F; text-transform: uppercase; margin-bottom: 2px; letter-spacing: 0.5px;">Auto-Generated Artifacts</div>
                
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="background: #E2E8F0; color: #4472C4; font-size: 10px; font-weight: 900; padding: 4px 6px; border-radius: 4px; width: 38px; text-align: center;">PDF</div>
                    <div style="font-size: 12px; font-weight: bold; color: #404040;">Executive Report</div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="background: #E2E8F0; color: #548235; font-size: 10px; font-weight: 900; padding: 4px 6px; border-radius: 4px; width: 38px; text-align: center;">JSON</div>
                    <div style="font-size: 12px; font-weight: bold; color: #404040;">Network IOCs</div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="background: #E2E8F0; color: #C65911; font-size: 10px; font-weight: 900; padding: 4px 6px; border-radius: 4px; width: 38px; text-align: center;">YAR</div>
                    <div style="font-size: 12px; font-weight: bold; color: #404040;">YARA Signatures</div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="background: #E2E8F0; color: #203864; font-size: 10px; font-weight: 900; padding: 4px 6px; border-radius: 4px; width: 38px; text-align: center;">API</div>
                    <div style="font-size: 12px; font-weight: bold; color: #404040;">SIEM Webhook</div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="background: #E2E8F0; color: #404040; font-size: 10px; font-weight: 900; padding: 4px 6px; border-radius: 4px; width: 38px; text-align: center;">DOC</div>
                    <div style="font-size: 12px; font-weight: bold; color: #404040;">CERT-In Draft</div>
                </div>
            </div>
        </div>

        <!-- Center: Investigation Report Preview -->
        <div style="flex: 1; background: transparent; border: none; border-left: 2px solid #E2E8F0; border-right: 2px solid #E2E8F0; padding: 0 20px; display: flex; flex-direction: column; min-height: 0;">
            <div style="font-size: 15px; font-weight: 900; color: #203864; text-transform: uppercase; margin-bottom: 12px;">SurakshaAPK Investigation Report</div>
            <div style="font-size: 14px; color: #404040; line-height: 1.5; flex: 1; overflow-y: auto;">
                <div style="font-weight: 900; color: #C00000; margin-bottom: 6px; font-size: 15px; text-transform: uppercase;">AI Threat Summary:</div>
                <div style="margin-bottom: 16px; font-weight: bold;">This APK exhibits OTP theft and overlay phishing behavior targeting Bank of India credentials.</div>
                
                <div style="font-weight: 900; color: #C65911; margin-bottom: 6px; font-size: 15px; text-transform: uppercase;">Key Evidence Chains:</div>
                <div style="font-family: monospace; font-size: 13px; font-weight: bold; padding: 0; margin-bottom: 16px;">
                    <div style="margin-bottom: 8px; display: flex; gap: 8px;"><b style="color: #203864; font-size: 14px;">E1:</b> <span>Sandbox captured HTTP POST with fake OTP.</span></div>
                    <div style="display: flex; gap: 8px;"><b style="color: #203864; font-size: 14px;">E2:</b> <span>Requests SYSTEM_ALERT_WINDOW with BOI activities.</span></div>
                </div>
                
                <div style="font-weight: 900; color: #548235; margin-bottom: 6px; font-size: 15px; text-transform: uppercase;">Recommended Action:</div>
                <div style="font-weight: bold;">Block domains, escalate to SOC, submit CERT-In draft.</div>
            </div>
        </div>

        <!-- Right: Code Snippets -->
        <div style="flex: 0 0 28%; display: flex; flex-direction: column; gap: 12px; min-height: 0;">
            <div style="flex: 1; border: none; border-radius: 8px; display: flex; flex-direction: column; box-shadow: 0 2px 5px rgba(0,0,0,0.08); overflow: hidden; background: #0D1117;">
                <div style="background: #161B22; padding: 8px 12px; font-weight: 900; font-size: 12px; color: #E6EDF3; display: flex; align-items: center; gap: 6px; border-bottom: 1px solid #30363D; font-family: monospace; text-transform: uppercase;">
                    <span style="display: inline-block; width: 6px; height: 6px; background: #E6EDF3; border-radius: 50%;"></span>
                    IOCS.JSON
                </div>
                <pre style="margin: 0; padding: 12px; font-family: monospace; font-size: 12px; font-weight: bold; color: #A5D6FF; flex: 1; overflow-y: auto; line-height: 1.4;">
{
  "sha256": "9f3a...c21b",
  "domains": [
    "unknown-c2.example"
  ],
  "risk": 87
}
                </pre>
            </div>
            
            <div style="flex: 1; border: none; border-radius: 8px; display: flex; flex-direction: column; box-shadow: 0 2px 5px rgba(0,0,0,0.08); overflow: hidden; background: #0D1117;">
                <div style="background: #161B22; padding: 8px 12px; font-weight: 900; font-size: 12px; color: #E6EDF3; display: flex; align-items: center; gap: 6px; border-bottom: 1px solid #30363D; font-family: monospace; text-transform: uppercase;">
                    <span style="display: inline-block; width: 6px; height: 6px; background: #E6EDF3; border-radius: 50%;"></span>
                    RULE.YAR
                </div>
                <pre style="margin: 0; padding: 12px; font-family: monospace; font-size: 12px; font-weight: bold; color: #FF7B72; flex: 1; overflow-y: auto; line-height: 1.4;">
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
    <div style="background: #E2EFDA; border: none; padding: 12px; text-align: center; font-size: 14px; font-weight: bold; color: #00B050; margin-top: auto; margin-bottom: 40px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        GenAI writes the explanation. Deterministic engines decide the score and evidence mapping.
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>8 / 10</span>
    </div>
</div>

<!-- SLIDE 9: Dataset & Validation -->
<div class="slide" style="padding: 20px 40px 20px 40px; display: flex; flex-direction: column;">
    <div style="font-weight: bold; color: #7F7F7F; font-size: 13px; text-transform: uppercase; margin-bottom: 2px; margin-left: 1px;">PROOF OF CONCEPT</div>
    <h2 style="font-family: var(--font-main); font-size: 26px; font-weight: 800; color: var(--boi-navy); margin: 0 0 2px 0;">DATASET, FEASIBILITY & COMPARISON</h2>
    <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 10px; font-weight: bold;">Rigorous testing, clear advantages, and practical implementations</div>
    
    <div style="display: flex; flex-direction: column; height: 100%; gap: 12px; flex: 1; min-height: 0; padding-top: 6px;">
        
        <!-- Validation Pipeline Flowchart -->
        <div style="display: flex; align-items: center; justify-content: center; gap: 4px; margin-bottom: 4px;">
            <div style="background: #EAF4FF; border: 1px solid #4472C4; border-radius: 4px; padding: 6px 12px; font-size: 11px; font-weight: 900; color: #203864; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); text-transform: uppercase;">1. Dataset</div>
            
            <div style="width: 24px; height: 2px; background: #4472C4; position: relative;">
                <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #4472C4;"></div>
            </div>
            
            <div style="background: #FFF2CC; border: 1px solid #BF8F00; border-radius: 4px; padding: 6px 12px; font-size: 11px; font-weight: 900; color: #7F6000; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); text-transform: uppercase;">2. Feature Extraction</div>
            
            <div style="width: 24px; height: 2px; background: #BF8F00; position: relative;">
                <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #BF8F00;"></div>
            </div>
            
            <div style="background: #FCE4D6; border: 1px solid #C65911; border-radius: 4px; padding: 6px 12px; font-size: 11px; font-weight: 900; color: #833C0C; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); text-transform: uppercase;">3. Evidence Chain</div>
            
            <div style="width: 24px; height: 2px; background: #C65911; position: relative;">
                <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #C65911;"></div>
            </div>
            
            <div style="background: #E2EFDA; border: 1px solid #548235; border-radius: 4px; padding: 6px 12px; font-size: 11px; font-weight: 900; color: #385723; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); text-transform: uppercase;">4. Analyst Review</div>
            
            <div style="width: 24px; height: 2px; background: #548235; position: relative;">
                <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #548235;"></div>
            </div>
            
            <div style="background: #EAEAEB; border: 1px solid #404040; border-radius: 4px; padding: 6px 12px; font-size: 11px; font-weight: 900; color: #262626; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); text-transform: uppercase;">5. Metrics</div>
        </div>

        <!-- NEW METRICS BANNER -->
        <div style="display: flex; gap: 12px; margin-bottom: 4px; justify-content: space-between;">
            <div style="flex: 1; background: #E2EFDA; border: 1px solid #548235; border-radius: 4px; padding: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
                <div style="font-size: 11px; font-weight: 900; color: #548235; text-transform: uppercase; margin-bottom: 4px;">Static Classification</div>
                <div style="font-size: 18px; font-weight: 900; color: #385723; margin-bottom: 2px;">94.3% <span style="font-size: 11px;">Accuracy</span></div>
                <div style="font-size: 10px; font-weight: bold; color: #548235;">91.2% Prec | 96.8% Rec on AMD</div>
            </div>
            <div style="flex: 1; background: #EAF4FF; border: 1px solid #4472C4; border-radius: 4px; padding: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
                <div style="font-size: 11px; font-weight: 900; color: #4472C4; text-transform: uppercase; margin-bottom: 4px;">Dynamic Payload Trigger</div>
                <div style="font-size: 18px; font-weight: 900; color: #203864; margin-bottom: 2px;">89.7% <span style="font-size: 11px;">Rate</span></div>
                <div style="font-size: 10px; font-weight: bold; color: #4472C4;">Intent-Driven vs 34.2% Random</div>
            </div>
            <div style="flex: 1; background: #FCE4D6; border: 1px solid #C65911; border-radius: 4px; padding: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
                <div style="font-size: 11px; font-weight: 900; color: #C65911; text-transform: uppercase; margin-bottom: 4px;">False Positive Rate</div>
                <div style="font-size: 18px; font-weight: 900; color: #833C0C; margin-bottom: 2px;">3.1% <span style="font-size: 11px;">FPR</span></div>
                <div style="font-size: 10px; font-weight: bold; color: #C65911;">on 200+ legitimate apps</div>
            </div>
        </div>

        <div style="display: flex; gap: 24px; flex: 1; min-height: 0;">
            <!-- Left: Dataset Table -->
            <div style="flex: 1; display: flex; flex-direction: column; min-height: 0;">
                <div style="font-size: 13px; font-weight: 900; color: #4472C4; margin-bottom: 8px; text-transform: uppercase;">Evaluation Dataset</div>
                <table style="width: 100%; border-collapse: collapse; font-size: 11px; text-align: left; flex: 1; height: 100%; border: 1px solid #BFBFBF;">
                    <tr style="background: #0B1C33; color: white; height: 1%;">
                        <th style="padding: 6px 4px; border: 1px solid #BFBFBF; text-transform: uppercase; font-size: 10px;">Dataset Category</th>
                        <th style="padding: 6px 4px; border: 1px solid #BFBFBF; text-transform: uppercase; font-size: 10px;">Purpose</th>
                    </tr>
                    <tr style="background: #F2F2F2;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #203864;">Official BOI / PSB apps</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #548235;">Known-good baseline</td></tr>
                    <tr style="background: #FFFFFF;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">Benign finance apps</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #595959;">False-positive testing</td></tr>
                    <tr style="background: #FCE4D6;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #C00000;">Synthetic fraud APKs</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #C00000;">Safe OTP validation</td></tr>
                    <tr style="background: #FFFFFF;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">Public malware datasets</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #595959;">Static validation</td></tr>
                    <tr style="background: #F2F2F2;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">Threat intel reports</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #595959;">Scam patterns and IOCs</td></tr>
                    <tr style="background: #FFFFFF;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #203864;">Bank pilot samples</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #203864;">Real-world validation</td></tr>
                </table>
            </div>

            <!-- Center: Comparison Table -->
            <div style="flex: 1; display: flex; flex-direction: column; min-height: 0;">
                <div style="font-size: 13px; font-weight: 900; color: #C65911; margin-bottom: 8px; text-transform: uppercase;">Competitive Edge</div>
                <table style="width: 100%; border-collapse: collapse; font-size: 11px; text-align: left; flex: 1; height: 100%; border: 1px solid #BFBFBF;">
                    <tr style="background: #0B1C33; color: white; height: 1%;">
                        <th style="padding: 6px 4px; border: 1px solid #BFBFBF; text-transform: uppercase; font-size: 10px;">Capability</th>
                        <th style="padding: 6px 4px; border: 1px solid #BFBFBF; text-transform: uppercase; font-size: 10px;">Generic</th>
                        <th style="padding: 6px 4px; border: 1px solid #BFBFBF; text-transform: uppercase; font-size: 10px;">SurakshaAPK</th>
                    </tr>
                    <tr style="background: #F4F0EB;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">Static APK analysis</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #7F7F7F;">Yes</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #548235;">YES</td></tr>
                    <tr style="background: #FFFFFF;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">Local deployment</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #C00000;">Limited</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #548235;">YES</td></tr>
                    <tr style="background: #F4F0EB;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">Dynamic validation</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #C00000;">Partial</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #548235;">YES</td></tr>
                    <tr style="background: #FFFFFF;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">Bank Adapter</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #C00000;">No</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #548235;">YES</td></tr>
                    <tr style="background: #F4F0EB;"><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #404040;">GenAI reports</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: bold; color: #C00000;">No</td><td style="padding: 8px 4px; border: 1px solid #BFBFBF; font-weight: 900; color: #548235;">YES</td></tr>
                </table>
            </div>

            <!-- Right: Feasibility Tree -->
            <div style="flex: 1; display: flex; flex-direction: column; min-height: 0;">
                <div style="font-size: 13px; font-weight: 900; color: #548235; margin-bottom: 8px; text-transform: uppercase;">Feasibility & Mitigations</div>
                
                <div style="display: flex; flex-direction: column; position: relative; padding-left: 14px; justify-content: space-evenly; flex: 1; margin-top: 4px;">
                    <!-- Vertical Trunk -->
                    <div style="position: absolute; left: 0; top: 12px; bottom: 20px; width: 2px; background: #548235;"></div>
                    
                    <div style="position: relative;">
                        <div style="position: absolute; left: -14px; top: 14px; width: 14px; height: 2px; background: #548235;"></div>
                        <div style="background: white; border: 1px solid #A9D08E; border-radius: 6px; padding: 8px 10px; margin-left: 8px; box-shadow: 1px 1px 4px rgba(0,0,0,0.05);">
                            <div style="color: #203864; font-size: 11px; font-weight: 900; text-transform: uppercase; margin-bottom: 2px;">LLM Hallucination</div>
                            <div style="color: #595959; font-size: 10px; font-weight: bold; line-height: 1.2;">Explains only verified evidence</div>
                        </div>
                    </div>
                    
                    <div style="position: relative;">
                        <div style="position: absolute; left: -14px; top: 14px; width: 14px; height: 2px; background: #548235;"></div>
                        <div style="background: white; border: 1px solid #A9D08E; border-radius: 6px; padding: 8px 10px; margin-left: 8px; box-shadow: 1px 1px 4px rgba(0,0,0,0.05);">
                            <div style="color: #203864; font-size: 11px; font-weight: 900; text-transform: uppercase; margin-bottom: 2px;">False Positives</div>
                            <div style="color: #595959; font-size: 10px; font-weight: bold; line-height: 1.2;">Attack scoring + baseline</div>
                        </div>
                    </div>
                    
                    <div style="position: relative;">
                        <div style="position: absolute; left: -14px; top: 14px; width: 14px; height: 2px; background: #548235;"></div>
                        <div style="background: white; border: 1px solid #A9D08E; border-radius: 6px; padding: 8px 10px; margin-left: 8px; box-shadow: 1px 1px 4px rgba(0,0,0,0.05);">
                            <div style="color: #203864; font-size: 11px; font-weight: 900; text-transform: uppercase; margin-bottom: 2px;">Dynamic Evasion</div>
                            <div style="color: #595959; font-size: 10px; font-weight: bold; line-height: 1.2;">Static triggers + anti-analysis</div>
                        </div>
                    </div>
                    
                    <div style="position: relative;">
                        <div style="position: absolute; left: -14px; top: 14px; width: 14px; height: 2px; background: #548235;"></div>
                        <div style="background: white; border: 1px solid #A9D08E; border-radius: 6px; padding: 8px 10px; margin-left: 8px; box-shadow: 1px 1px 4px rgba(0,0,0,0.05);">
                            <div style="color: #203864; font-size: 11px; font-weight: 900; text-transform: uppercase; margin-bottom: 2px;">Data Privacy</div>
                            <div style="color: #595959; font-size: 10px; font-weight: bold; line-height: 1.2;">Local/offline default</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Safe Obfuscation Test -->
        <div style="background: transparent; border-top: 1px solid #E2E8F0; padding-top: 12px; text-align: center; font-size: 13px; font-family: monospace; color: #00A676; font-weight: bold; text-transform: uppercase; margin-top: auto;">
            <span style="color: #595959; margin-right: 8px;">[TEST CASE]</span> Controlled APK <span style="color: #404040;">→</span> rename classes/strings <span style="color: #404040;">→</span> detected by SurakshaAPK
        </div>
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>9 / 10</span>
    </div>
</div>

<!-- SLIDE 10: Final -->
<div class="slide" style="padding: 20px 40px 20px 40px; display: flex; flex-direction: column;">
    <div style="font-weight: bold; color: #7F7F7F; font-size: 13px; text-transform: uppercase; margin-bottom: 2px; margin-left: 1px;">EXECUTION & ROADMAP</div>
    <h2 style="font-family: var(--font-main); font-size: 26px; font-weight: 800; color: var(--boi-navy); margin: 0 0 2px 0;">DEMO STRATEGY, USE CASES & IMPACT</h2>
    <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 10px; font-weight: bold;">Turning analysis into actionable bank security</div>
    
    <div style="display: flex; gap: 24px; flex: 1; margin-bottom: 12px; min-height: 0;">
        <!-- Left: Demo Workflow -->
        <div style="flex: 1; display: flex; flex-direction: column; min-height: 0; padding-right: 12px;">
            <div style="font-size: 13px; font-weight: 900; color: #4472C4; margin-bottom: 12px; text-transform: uppercase;">Demo Workflow</div>
            <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 8px; font-size: 11px; font-weight: 900; color: #404040; text-align: center; text-transform: uppercase; align-items: center;">
                
                <div style="background: #FFF2CC; border: 1px solid #BF8F00; border-radius: 4px; padding: 6px 12px; color: #7F6000; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); width: 75%;">1. Upload BOI_KYC.apk</div>
                
                <div style="width: 2px; height: 10px; background: #BF8F00; position: relative;">
                    <div style="position: absolute; bottom: -2px; left: -3px; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #BF8F00;"></div>
                </div>

                <div style="background: #FCE4D6; border: 1px solid #C65911; border-radius: 4px; padding: 6px 12px; color: #833C0C; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); width: 75%;">2. Static Triage</div>
                
                <div style="width: 2px; height: 10px; background: #C65911; position: relative;">
                    <div style="position: absolute; bottom: -2px; left: -3px; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #C65911;"></div>
                </div>

                <div style="background: #EAEAEB; border: 1px solid #404040; border-radius: 4px; padding: 6px 12px; color: #262626; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); width: 75%;">3. Evidence Graph</div>
                
                <div style="width: 2px; height: 10px; background: #404040; position: relative;">
                    <div style="position: absolute; bottom: -2px; left: -3px; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #404040;"></div>
                </div>

                <div style="background: #FCE4D6; border: 1px solid #C00000; border-radius: 4px; padding: 6px 12px; color: #C00000; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); width: 75%;">4. Risk Score + Conf.</div>
                
                <div style="width: 2px; height: 10px; background: #C00000; position: relative;">
                    <div style="position: absolute; bottom: -2px; left: -3px; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #C00000;"></div>
                </div>

                <div style="background: #EAEAEB; border: 1px solid #404040; border-radius: 4px; padding: 6px 12px; color: #262626; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); width: 75%;">5. GenAI Report</div>
                
                <div style="width: 2px; height: 10px; background: #404040; position: relative;">
                    <div style="position: absolute; bottom: -2px; left: -3px; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid #404040;"></div>
                </div>

                <div style="background: #E2EFDA; border: 1px solid #548235; border-radius: 4px; padding: 6px 12px; color: #385723; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); width: 75%;">6. Dynamic Valid. & Export</div>
            </div>
        </div>

        <!-- Right: Use Cases & Impact -->
        <div style="flex: 1.5; display: flex; flex-direction: column; gap: 20px; min-height: 0; border-left: 1px solid #E2E8F0; padding-left: 24px;">
            
            <div style="display: flex; gap: 24px; flex: 1; min-height: 0;">
                <!-- Bank Use Cases Tree -->
                <div style="flex: 1; display: flex; flex-direction: column; min-height: 0;">
                    <div style="font-size: 13px; font-weight: 900; color: #C65911; margin-bottom: 8px; text-transform: uppercase;">Bank Use Cases</div>
                    <div style="display: flex; flex-direction: column; position: relative; padding-left: 14px; justify-content: space-evenly; flex: 1; margin-top: 4px;">
                        <div style="position: absolute; left: 0; top: 12px; bottom: 12px; width: 2px; background: rgba(198,89,17,0.5);"></div>
                        
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(198,89,17,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #FCE4D6; border: 1px solid rgba(198,89,17,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #C65911; display: inline-block;">BANK SOC TRIAGE</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(198,89,17,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #FCE4D6; border: 1px solid rgba(198,89,17,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #C65911; display: inline-block;">FRAUD OPERATIONS</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(198,89,17,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #FCE4D6; border: 1px solid rgba(198,89,17,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #C65911; display: inline-block;">DEFENSIVE BLOCKING</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(198,89,17,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #FCE4D6; border: 1px solid rgba(198,89,17,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #C65911; display: inline-block;">COMPLIANCE & INV.</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(198,89,17,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #FCE4D6; border: 1px solid rgba(198,89,17,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #C65911; display: inline-block;">CUSTOMER ADVISORY</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(198,89,17,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #FCE4D6; border: 1px solid rgba(198,89,17,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #C65911; display: inline-block;">MDM / BYOD SCREENING</div>
                        </div>
                    </div>
                </div>
                
                <!-- High-Value Impact Tree -->
                <div style="flex: 1; display: flex; flex-direction: column; min-height: 0;">
                    <div style="font-size: 13px; font-weight: 900; color: #548235; margin-bottom: 8px; text-transform: uppercase;">High-Value Impact</div>
                    <div style="display: flex; flex-direction: column; position: relative; padding-left: 14px; justify-content: space-evenly; flex: 1; margin-top: 4px;">
                        <div style="position: absolute; left: 0; top: 12px; bottom: 12px; width: 2px; background: rgba(84,130,53,0.5);"></div>
                        
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(84,130,53,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #E2EFDA; border: 1px solid rgba(84,130,53,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #548235; display: inline-block;">FASTER APK TRIAGE</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(84,130,53,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #E2EFDA; border: 1px solid rgba(84,130,53,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #548235; display: inline-block;">REDUCED WORKLOAD</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(84,130,53,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #E2EFDA; border: 1px solid rgba(84,130,53,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #548235; display: inline-block;">LOWER FALSE POSITIVES</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(84,130,53,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #E2EFDA; border: 1px solid rgba(84,130,53,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #548235; display: inline-block;">BETTER PREVENTION</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(84,130,53,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #E2EFDA; border: 1px solid rgba(84,130,53,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #548235; display: inline-block;">PRIVACY-FIRST</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -14px; top: 50%; width: 14px; height: 2px; background: rgba(84,130,53,0.5); transform: translateY(-50%);"></div>
                            <div style="background: #E2EFDA; border: 1px solid rgba(84,130,53,0.3); border-radius: 4px; padding: 6px 10px; margin-left: 6px; box-shadow: 1px 1px 3px rgba(0,0,0,0.05); font-size: 10px; font-weight: 900; color: #548235; display: inline-block;">BANK-READY REPORTS</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Roadmap Horizontal Flowchart -->
            <div style="display: flex; flex-direction: column; min-height: 0; margin-top: auto; border-top: 1px solid #E2E8F0; padding-top: 16px;">
                <div style="font-size: 13px; font-weight: 900; color: #203864; margin-bottom: 12px; text-transform: uppercase;">Development Roadmap</div>
                <div style="display: flex; align-items: center; justify-content: space-between; font-size: 11px; font-weight: 900; color: white;">
                    <div style="background: #4472C4; border-radius: 4px; padding: 8px 12px; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); flex: 1; text-align: center;">IDEA</div>
                    <div style="width: 14px; height: 2px; background: #4472C4; position: relative;">
                        <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #4472C4;"></div>
                    </div>
                    <div style="background: #4472C4; border-radius: 4px; padding: 8px 12px; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); flex: 1; text-align: center;">STATIC MVP</div>
                    <div style="width: 14px; height: 2px; background: #4472C4; position: relative;">
                        <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #4472C4;"></div>
                    </div>
                    <div style="background: #4472C4; border-radius: 4px; padding: 8px 12px; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); flex: 1; text-align: center;">SCORING</div>
                    <div style="width: 14px; height: 2px; background: #4472C4; position: relative;">
                        <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #4472C4;"></div>
                    </div>
                    <div style="background: #4472C4; border-radius: 4px; padding: 8px 12px; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); flex: 1; text-align: center;">VALIDATION</div>
                    <div style="width: 14px; height: 2px; background: #4472C4; position: relative;">
                        <div style="position: absolute; right: -2px; top: -3px; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 5px solid #4472C4;"></div>
                    </div>
                    <div style="background: #203864; border-radius: 4px; padding: 8px 12px; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); flex: 1; text-align: center;">PILOT (NOW)</div>
                </div>
            </div>
        </div>
    </div>
    
    <div style="background: #203864; border-radius: 6px; padding: 12px 20px; text-align: center; margin-top: auto; display: flex; flex-direction: column; justify-content: center; box-shadow: 2px 2px 8px rgba(0,0,0,0.15);">
        <div style="font-size: 20px; font-weight: 900; color: white; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 2px;">Thank You!</div>
        <div style="font-size: 13px; font-weight: bold; color: #DDEBF7;">SurakshaAPK helps banks move from reactive manual analysis to proactive, evidence-based fraud defense.</div>
    </div>

    <div class="footer">
        <span>SurakshaAPK • PSB Cybersecurity, Fraud & AI Hackathon 2026 • Problem Statement 1</span>
        <span>10 / 10</span>
    </div>
</div>
"""

new_content = content[:s7_start] + new_slides + "\n" + content[s11_start:]

with open(filepath, "w") as f:
    f.write(new_content)

print("Significantly shrunk sizes in slides 7 to 10 successfully!")
