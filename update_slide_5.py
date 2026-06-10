import sys

filepath = "/Users/toru/Projects and codes/project manager/ps1.html"

with open(filepath, "r") as f:
    content = f.read()

s5_start = content.find("<!-- SLIDE 5: Technical Approach Redesign -->")
if s5_start == -1:
    s5_start = content.find("<!-- SLIDE 5:")
if s5_start == -1:
    print("Could not find slide 5 start marker")
    sys.exit(1)

s6_start = content.find("<!-- SLIDE 6", s5_start)
if s6_start == -1:
    s6_start = content.find("</div>\n</body>", s5_start)

if s6_start == -1:
    print("Could not find slide 6 start marker")
    sys.exit(1)

new_slide_5 = """<!-- SLIDE 5: Technical Approach Redesign -->
<div class="slide slide-5" id="slide-5">
  <div class="header" style="margin-bottom: 12px; margin-top: -8px; flex-shrink: 0;">
    <h1 style="font-family: var(--font-main); font-size: 32px; font-weight: 800; color: var(--boi-navy); margin: 0 0 4px 0; text-transform: uppercase;">TECHNICAL APPROACH</h1>
    <div style="font-family: var(--font-main); font-size: 16px; font-weight: 600; color: var(--text-muted);">System Architecture: Decision-Based APK Investigation Flow</div>
  </div>

  <div class="content" style="display: flex; gap: 16px; height: calc(100% - 70px);">
    
    <!-- LEFT COLUMN (28%) -->
    <div style="width: 28%; display: flex; flex-direction: column; gap: 12px; height: 100%;">
      
      <!-- Tech Stack -->
      <div style="border-left: 4px solid #005BAC; background: #FFFDF8; padding: 12px; display: flex; flex-direction: column; gap: 8px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); font-size: 12px; overflow-y: hidden; flex: 1; min-height: 0;">
        <div style="font-weight: 700; color: #1E293B; font-size: 14px; border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; flex-shrink: 0;">Tech Stack & Tools</div>
        
        <ul style="padding-left: 20px; margin: 0; display: flex; flex-direction: column; gap: 4px; flex-shrink: 0;">
          <li><b>Backend/API:</b> Python, FastAPI</li>
          <li><b>Decompilation:</b> JADX, AndroGuard</li>
          <li><b>Static Analysis:</b> APKiD, YARA</li>
          <li><b>Dynamic Sandbox:</b> Android, ADB, Frida, MITMProxy</li>
          <li><b>AI/ML:</b> Ollama local LLM</li>
          <li><b>Database:</b> PostgreSQL</li>
          <li><b>Orchestration:</b> Docker</li>
        </ul>

        <div style="background: #EAF4FF; border-left: 4px solid #005BAC; padding: 6px 8px; margin-top: 0; font-weight: 600; color: #005BAC; font-size: 11px; flex-shrink: 0;">
          Why this matters:<br>
          <span style="font-weight: 400; color: #334155; font-size: 10px;">Static triage runs first for every APK; dynamic validation is triggered only when evidence indicates risk.</span>
        </div>

        <div style="flex-grow: 1; min-height: 2px;"></div>

        <!-- Tool Logos Grouped -->
        <div style="display: flex; flex-direction: column; gap: 6px; flex-shrink: 0;">
          <div>
            <div style="font-weight: 700; font-size: 9px; color: #64748B; margin-bottom: 2px; text-transform: uppercase;">Backend / Storage</div>
            <div style="display: flex; gap: 8px; align-items: center;">
              <i class="devicon-python-plain colored" style="font-size: 20px;"></i>
              <i class="devicon-fastapi-plain colored" style="font-size: 20px;"></i>
              <i class="devicon-postgresql-plain colored" style="font-size: 20px;"></i>
              <i class="devicon-docker-plain colored" style="font-size: 20px;"></i>
            </div>
          </div>
          <div>
            <div style="font-weight: 700; font-size: 9px; color: #64748B; margin-bottom: 2px; text-transform: uppercase;">APK Analysis</div>
            <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;">
              <i class="devicon-android-plain colored" style="font-size: 20px;"></i>
              <span style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-size: 9px; font-weight: bold; color: #475569;">JADX</span>
              <span style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-size: 9px; font-weight: bold; color: #475569;">AndroGuard</span>
              <span style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-size: 9px; font-weight: bold; color: #475569;">APKiD</span>
              <span style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-size: 9px; font-weight: bold; color: #475569;">YARA</span>
            </div>
          </div>
          <div>
            <div style="font-weight: 700; font-size: 9px; color: #64748B; margin-bottom: 2px; text-transform: uppercase;">Dynamic + AI</div>
            <div style="display: flex; gap: 6px; align-items: center;">
              <span style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-size: 9px; font-weight: bold; color: #475569;">Frida</span>
              <span style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-size: 9px; font-weight: bold; color: #475569;">MITMProxy</span>
              <span style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-size: 9px; font-weight: bold; color: #475569;">Ollama</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Artifact Pipeline Vertical -->
      <div style="background: #F8FAFC; border: 1px solid #D8D2C4; border-radius: 4px; padding: 10px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
        <div style="font-weight: 800; font-size: 11px; color: #1E293B; border-bottom: 1px solid #E2E8F0; padding-bottom: 4px;">Artifact Pipeline</div>
        
        <div style="display: flex; flex-direction: column; gap: 6px;">
          <!-- Input Stage -->
          <div>
            <div style="font-size: 8.5px; font-weight: 700; color: #64748B; text-transform: uppercase; margin-bottom: 3px;">1. Input Stage</div>
            <div style="display: flex; gap: 4px; flex-wrap: wrap;">
              <div style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #CBD5E1; color: #475569;">sha256.txt</div>
              <div style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #CBD5E1; color: #475569;">manifest.json</div>
            </div>
          </div>

          <!-- Processing Stage -->
          <div>
            <div style="font-size: 8.5px; font-weight: 700; color: #64748B; text-transform: uppercase; margin-bottom: 3px;">2. Processing Stage</div>
            <div style="display: flex; gap: 4px; flex-wrap: wrap;">
              <div style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #CBD5E1; color: #475569;">static_features.json</div>
              <div style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #CBD5E1; color: #475569;">evidence_graph.json</div>
              <div style="background: #E2E8F0; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #CBD5E1; color: #475569;">runtime_trace.json</div>
            </div>
          </div>

          <!-- Output Stage -->
          <div>
            <div style="font-size: 8.5px; font-weight: 700; color: #64748B; text-transform: uppercase; margin-bottom: 3px;">3. Output Stage</div>
            <div style="display: flex; gap: 4px; flex-wrap: wrap;">
              <div style="background: #EAF4FF; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #3B82F6; color: #1E40AF; font-weight: bold;">report.pdf</div>
              <div style="background: #EAF4FF; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #3B82F6; color: #1E40AF; font-weight: bold;">iocs.json</div>
              <div style="background: #EAF4FF; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #3B82F6; color: #1E40AF; font-weight: bold;">yara_rule.yar</div>
              <div style="background: #EAF4FF; padding: 3px 5px; border-radius: 3px; font-family: monospace; font-size: 8.5px; border: 1px solid #3B82F6; color: #1E40AF; font-weight: bold;">siem_event.json</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- RIGHT COLUMN: Main Flowchart (72%) -->
    <div style="width: 72%; background: #F8FAFC; border: 1px solid #D8D2C4; border-radius: 6px; padding: 12px 15px; position: relative; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
        
        <!-- Flowchart Header & Phases -->
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; position: relative; z-index: 2; flex-shrink: 0;">
          <div style="display: flex; gap: 10px; font-size: 11px; font-weight: 700;">
            <div style="background: #DBEAFE; color: #1E3A8A; padding: 4px 10px; border-radius: 12px;">1. Intake</div>
            <div style="background: #FFEDD5; color: #9A3412; padding: 4px 10px; border-radius: 12px;">2. Evidence Building</div>
            <div style="background: #DCFCE7; color: #166534; padding: 4px 10px; border-radius: 12px;">3. Risk & Response</div>
          </div>
          <div style="background: #FFFFFF; border: 1px solid #CBD5E1; padding: 6px 8px; border-radius: 4px; font-size: 9px; color: #475569; display: flex; flex-direction: column; gap: 3px;">
            <div style="font-weight: 700; margin-bottom: 2px;">Legend:</div>
            <div style="display: flex; align-items: center; gap: 4px;"><div style="width: 6px; height: 6px; border: 1px solid #BF8F00; background: #FFF2CC; transform: rotate(45deg);"></div> Decision</div>
            <div style="display: flex; align-items: center; gap: 4px;"><div style="width: 12px; height: 2px; background: #548235;"></div> YES = continue</div>
            <div style="display: flex; align-items: center; gap: 4px;"><div style="width: 12px; height: 2px; background: #C00000;"></div> NO = fallback/report</div>
          </div>
        </div>

        <!-- The Flow Canvas with scale(1.08) now that it has full vertical height! -->
        <div style="position: relative; flex-grow: 1; width: 100%; transform: scale(1.08); transform-origin: top left; margin-top: 15px; margin-left: 0px;">
          
          <style>
            .flow-box {
              position: absolute;
              background: #DDEBF7;
              border: 1px solid #5B9BD5;
              border-radius: 2px;
              display: flex;
              align-items: center;
              justify-content: center;
              text-align: center;
              font-weight: 700;
              font-size: 10px;
              color: #2F5597;
              width: 110px;
              height: 32px;
              z-index: 10;
              line-height: 1.1;
              padding: 0 4px;
            }
            .flow-box.important { width: 130px; height: 35px; font-size: 10.5px; }
            .flow-diamond {
              position: absolute;
              background: #FFF2CC;
              border: 1px solid #BF8F00;
              width: 40px;
              height: 40px;
              transform: rotate(45deg);
              z-index: 10;
              display: flex;
              align-items: center;
              justify-content: center;
            }
            .diamond-text {
              position: absolute;
              z-index: 11;
              font-size: 8px;
              font-weight: 700;
              color: #404040;
              text-align: center;
              width: 70px;
              line-height: 1;
            }
            .flow-line { position: absolute; background: #94A3B8; z-index: 1; }
            .flow-line.yes { background: #548235; }
            .flow-line.no { background: #C00000; }
            .flow-line.fallback { background: #C65911; }
            
            .arrow-right { position: absolute; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 6px solid #94A3B8; z-index: 2; transform: translateY(-50%); }
            .arrow-down { position: absolute; width: 0; height: 0; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 6px solid #94A3B8; z-index: 2; transform: translateX(-50%); }
            
            .arrow-right.yes { border-left-color: #548235; }
            .arrow-down.yes { border-top-color: #548235; }
            .arrow-right.no { border-left-color: #C00000; }
            .arrow-down.no { border-top-color: #C00000; }
            .arrow-right.fallback { border-left-color: #C65911; }
            .arrow-down.fallback { border-top-color: #C65911; }

            .flow-label {
              position: absolute;
              font-size: 7.5px;
              font-weight: 700;
              z-index: 12;
              background: #F8FAFC;
              padding: 1px 3px;
              border-radius: 2px;
            }
            .flow-label.yes { color: #548235; }
            .flow-label.no { color: #C00000; }
            .flow-label.fallback { color: #C65911; }
          </style>

          <!-- Nodes -->
          <div class="flow-box" style="left: 0px; top: 10px;">APK / Link Intake</div>
          <div class="flow-box" style="left: 135px; top: 10px;">Secure Hashing</div>
          <div class="flow-box" style="left: 270px; top: 10px;">Static Analysis</div>
          
          <div class="flow-diamond" style="left: 415px; top: 5px;"></div>
          <div class="diamond-text" style="left: 400px; top: 20px;">Decompiler<br>Success?</div>

          <div class="flow-box important" style="left: 500px; top: 8px; background: #FCE4D6; border-color: #C65911; color: #C00000;">Build Evidence Graph</div>

          <div class="flow-box" style="left: 270px; top: 60px; background: #FCE4D6; border-color: #C65911; color: #C00000;">Fallback:<br>Smali / APKiD</div>

          <div class="flow-diamond" style="left: 545px; top: 60px;"></div>
          <div class="diamond-text" style="left: 530px; top: 75px;">Risk &ge; Threshold?</div>

          <div class="flow-box" style="left: 400px; top: 63px; background: #E2EFDA; border-color: #548235; color: #385723;">Low-Risk Report</div>

          <div class="flow-box important" style="left: 500px; top: 105px; background: #FCE4D6; border-color: #C65911; color: #C00000;">Selective Dynamic Sandbox</div>

          <div class="flow-box important" style="left: 500px; top: 150px; background: #FCE4D6; border-color: #C65911; color: #C00000;">Update Evidence Graph</div>
          
          <div class="flow-box important" style="left: 500px; top: 195px; background: #FCE4D6; border-color: #C65911; color: #C00000;">Risk Scoring Engine</div>

          <div class="flow-diamond" style="left: 545px; top: 240px;"></div>
          <div class="diamond-text" style="left: 530px; top: 255px;">Critical?</div>

          <div class="flow-box important" style="left: 360px; top: 242px; background: #E2EFDA; border-color: #548235; color: #385723;">Local GenAI Report</div>

          <div class="flow-box important" style="left: 630px; top: 242px; background: #C00000; border-color: #7B0000; color: #FFFFFF;">SOC Alert / CERT-In</div>

          <div class="flow-box important" style="left: 360px; top: 285px; background: #2F5597; border-color: #203864; color: #FFFFFF;">Reports / Exports</div>

          <!-- Lines & Arrows -->

          <div class="flow-line" style="left: 110px; top: 26px; width: 25px; height: 1.5px;"></div>
          <div class="arrow-right" style="left: 135px; top: 26px;"></div>

          <div class="flow-line" style="left: 245px; top: 26px; width: 25px; height: 1.5px;"></div>
          <div class="arrow-right" style="left: 270px; top: 26px;"></div>

          <div class="flow-line" style="left: 380px; top: 26px; width: 35px; height: 1.5px;"></div>
          <div class="arrow-right" style="left: 415px; top: 26px;"></div>

          <div class="flow-line yes" style="left: 455px; top: 26px; width: 45px; height: 1.5px;"></div>
          <div class="arrow-right yes" style="left: 500px; top: 26px;"></div>
          <div class="flow-label yes" style="left: 465px; top: 16px;">YES</div>

          <div class="flow-line no" style="left: 435px; top: 45px; width: 1.5px; height: 30px;"></div>
          <div class="flow-line no" style="left: 380px; top: 75px; width: 55px; height: 1.5px;"></div>
          <div class="arrow-right no" style="left: 380px; top: 75px; transform: rotate(180deg) translateY(50%);"></div>
          
          <div class="flow-line fallback" style="left: 325px; top: 92px; width: 1.5px; height: 10px;"></div>
          <div class="flow-line fallback" style="left: 325px; top: 102px; width: 240px; height: 1.5px;"></div>
          <div class="flow-line fallback" style="left: 565px; top: 43px; width: 1.5px; height: 59px;"></div>
          <div class="arrow-down fallback" style="left: 565px; top: 43px; transform: rotate(180deg) translateX(50%);"></div>

          <div class="flow-line" style="left: 565px; top: 43px; width: 1.5px; height: 17px;"></div>
          <div class="arrow-down" style="left: 565px; top: 60px;"></div>

          <div class="flow-line no" style="left: 510px; top: 80px; width: 35px; height: 1.5px;"></div>
          <div class="arrow-right no" style="left: 510px; top: 80px; transform: rotate(180deg) translateY(50%);"></div>
          <div class="flow-label no" style="left: 520px; top: 70px;">NO</div>

          <div class="flow-line yes" style="left: 565px; top: 100px; width: 1.5px; height: 5px;"></div>
          <div class="arrow-down yes" style="left: 565px; top: 105px;"></div>
          <div class="flow-label yes" style="left: 570px; top: 100px;">YES</div>

          <div class="flow-line" style="left: 565px; top: 140px; width: 1.5px; height: 10px;"></div>
          <div class="arrow-down" style="left: 565px; top: 150px;"></div>

          <div class="flow-line" style="left: 565px; top: 185px; width: 1.5px; height: 10px;"></div>
          <div class="arrow-down" style="left: 565px; top: 195px;"></div>

          <div class="flow-line" style="left: 565px; top: 230px; width: 1.5px; height: 10px;"></div>
          <div class="arrow-down" style="left: 565px; top: 240px;"></div>

          <div class="flow-line yes" style="left: 585px; top: 260px; width: 45px; height: 1.5px;"></div>
          <div class="arrow-right yes" style="left: 630px; top: 260px;"></div>
          <div class="flow-label yes" style="left: 595px; top: 250px;">YES</div>

          <div class="flow-line no" style="left: 490px; top: 260px; width: 55px; height: 1.5px;"></div>
          <div class="arrow-right no" style="left: 490px; top: 260px; transform: rotate(180deg) translateY(50%);"></div>
          <div class="flow-label no" style="left: 505px; top: 250px;">NO</div>

          <div class="flow-line" style="left: 425px; top: 277px; width: 1.5px; height: 8px;"></div>
          <div class="arrow-down" style="left: 425px; top: 285px;"></div>

        </div>
      </div>
    </div>
  </div>
</div>
"""

new_content = content[:s5_start] + new_slide_5 + "\n" + content[s6_start:]

with open(filepath, "w") as f:
    f.write(new_content)

print("Updated successfully")
