BOI\CyberShield

# Project AEGIS
Automated Engine for
                    Generative Intelligence and Security
Harnessing Generative AI for Automated Reverse Engineering, Static and Dynamic Analysis, and Risk Scoring of Fraudulent Mobile Applications (APKs) and Malwares.

## Official Problem Statement

### Problem Statement 1 — Issued by Bank of India & IIT Hyderabad
Fraudsters increasingly distribute malicious mobile applications (APKs) through platforms such as WhatsApp, SMS, email, and phishing links to steal customer credentials, access sensitive information, and perform unauthorized financial transactions. Manual analysis of such APKs is complex, time-consuming, and dependent on skilled cybersecurity experts.
The proposed solution aims to develop a Generative AI-powered malware analysis system capable of automatically analyzing suspicious APK files and identifying malicious behavior. The system should leverage GenAI for reverse engineering, malware pattern recognition, automated code interpretation, and intelligent threat summarization, along with static and dynamic analysis techniques to examine application permissions, APIs, embedded code, runtime activities, and network communications.
Using AI-driven insights, the solution should detect malware patterns, classify threat severity, generate risk scores, and produce detailed investigation reports with actionable recommendations. The objective is to enable faster identification of fraudulent applications and support proactive cybersecurity and fraud prevention measures for banks.

## Problem Understanding - PS1 Specific
People download Android apps as APKs. While some are normal, others are fake apps, banking scams,
                        spyware, or malware designed to steal data, OTPs, contacts, SMS, or money.
Security teams usually analyze these manually to understand what the app contains, its
                        permissions, hidden suspicious code, and runtime behavior. That manual work is slow, highly
                        technical, and hard to scale.
How do we quickly and automatically detect whether an APK is
                        fraudulent or malicious?
- Thousands of suspicious APKs appear every day.
- Manual reverse engineering takes massive time and expert knowledge.
- Attackers constantly mutate malware to evade simple antivirus checks.
- Fake apps can steal money, passwords, and personal data.
- Security teams need faster triage to prioritize threats.
Not just detect malware, but drastically reduce time, effort, and
                        human dependency.
To understand the problem, we must first understand what an APK (Android Package Kit) is and what
                        reverse engineering entails. An APK is a compiled archive. It contains Dalvik bytecode
                        (
), compiled resources (
), a manifest file
                        (
), and native libraries (
files). When a
                        developer writes an app in Java or Kotlin, it is translated into a machine-readable format that
                        cannot be easily read by humans.
is the art of deconstructing this compiled APK back into
                        human-readable source code (Java/Kotlin or Smali bytecode) to understand how it functions.
- Hundreds of thousands of new Android applications are
                            generated daily. Security operations centers (SOCs) and app store reviewers cannot manually
                            reverse-engineer every single app.
- Malicious actors use tools like ProGuard, DexGuard, and
                            custom packers to scramble the code. Variable names become a, b, c. Strings (like URLs to
                            command-and-control servers) are encrypted. Traditional static analyzers (which look for
                            specific code patterns) are easily blinded by this.
- Advanced malware knows when it is being watched. If it
                            detects it is running in a sandbox (a secure virtual machine used by security analysts), it
                            will act benign. It might check battery levels, gyroscope movement, or specific emulator
                            IPs, and only execute its malicious payload if it believes it is on a real victim's phone.
- A traditional scanner might flag an app because it
                            accesses the camera and the internet. But what is the intent? Is it a video calling app
                            (benign intent) or a flashlight app secretly taking photos and uploading them (malicious
                            intent)? Static rules cannot decipher intent.
They want a system that automatically:
- Takes an APK as input and analyzes it statically and dynamically.
- Uses Generative AI to summarize findings and infer intent.
- Assigns a hard risk score.
- Explains why the app is suspicious in human-readable language.
A system that not only detects bad apps, but also explains
                        behavior, supports analysts, and makes the result universally understandable.
FakeBankUpdate.apk
"A tool that works like an AI malware analyst for Android apps: opening, inspecting, running,
                        understanding, and judging how dangerous they are."
FakeBankUpdate.apk

## The Core Problem & Why It Must Be Solved
Millions of new malicious mobile applications are created every year. Human security
                    analysts cannot keep up. Manually decompiling, reading millions of lines of messy code, and watching
                    an app's behavior takes hours or days per app.
Security operations are slow. Financial fraud via malicious APKs moves instantly. Organizations
                        need a system that can ingest a suspicious app file and accurately flag whether it is dangerous
                        in minutes, rather than days, without needing an army of expensive human experts.
Traditional malware analysis relies on static rules and time-consuming manual reverse
                        engineering. AEGIS introduces a paradigm shift by utilizing Large Language Models (LLMs) and
                        Generative AI to "read" decompiled code, understand the intent behind the code, and automate the
                        grueling process of dynamic behavioral mapping.

## What Solution They Want
They want an AI system that can automatically inspect Android apps and malware, understand
                what they do, detect whether they are dangerous or fake, and give a risk score.
An automated pipeline/platform. You upload a raw Android .apk file,
                and the platform runs it through automated reverse engineering tools. The resulting raw data is fed to a
                Generative AI model. The AI instantly synthesizes the code, documents the app's behavior, catches hidden
                malicious intent, and outputs a clean report along with a Risk Score.
AEGIS proposes a hybrid engine. It doesn't just rely on regular
                expressions or simple behavioral flags. It uses Generative AI as a "virtual security analyst." By
                feeding decompiled, obfuscated code to a specifically prompted GenAI model, the system can ask, "What is
                this function trying to achieve?" The AI can connect the semantic dots between a disguised network call
                and a suspicious permission, effectively understanding the intent of the application.
Generative AI acts like an analyst
                    assistant. It can read decompiled code, explain suspicious functions in plain language, and combine
                    multiple signals into a meaningful report. For example, instead of outputting "suspicious network
                    calls detected", it says: "The app requests SMS permissions, contacts a suspicious domain, and is
                    attempting credential theft."

## Technical Stack & Workflow Architecture
- The user uploads an APK file.
User uploads APK
Input:
                                    Upload the APK file.
- Automated tools unzip the APK, extract permissions from the
- , and decompile the Dalvik Executable (
- )
                            files into readable code.
System extracts metadata & Static scanner
                                    analyzes APK structure and code
Static Pipeline: Extract
                                    permissions, strings, and decompiled code using APKTool/JADX.
- The APK is silently installed on a headless Android
                            Emulator. The system monitors system calls, network packets, and file changes.
Sandbox runs APK safely & Dynamic scanner
                                    records behavior
Dynamic Pipeline: Run the APK safely in an
                                    emulator to observe network traffic using Frida.
- The text outputs from the static and dynamic steps
                            (decompiled code snippets, API call logs, network traces) are combined into a structured
                            format (JSON) and passed to an LLM via prompt engineering.
AI model reads all results
AI Layer: Use an LLM to summarize behavior and detect patterns.
- The AI evaluates the inputs against frameworks like
                            MITRE ATT&CK, generates a human-readable security assessment, and calculates a risk score.
Risk engine calculates score & Dashboard
                                    shows verdict and explanation
Risk Engine: Combine signals and
                                    assign a 0-100 score & Report: Generate a clear final verdict.

### Suggested Tech Stack
- Python (FastAPI or Flask) — the industry standard for
                        security automation and AI.
Backend: Python, FastAPI/Flask.
- JADX or Apktool (for decompiling the APK) and Androguard
                        (for extracting features natively in Python).
Static: APKTool, JADX, Androguard, YARA.
- Cuckoo Sandbox or Frida (for hooking and monitoring the
                        application at runtime).
Dynamic: Android Emulator, Frida, Wireshark.
- LangChain or LlamaIndex to build an AI Agentic
                        Workflow (splitting the task into a "Static Analyzer Agent" and a "Dynamic Behavior Agent").
LLM Models: Local open-source security models
                                (e.g., Llama-3-8B or Qwen-2.5-7B) to avoid leaking sensitive software data to external
                                APIs, or OpenAI's API if offline privacy is not a constraint.
AI / ML: LLM API, scikit-learn, XGBoost.

### Existing Open-Source Frameworks & Precedents
This problem is
                actively being explored, meaning you do not have to build it from scratch. You can combine existing
                pieces:
- : An
                    open-source academic framework specifically built to process sandbox-generated malware reports
                    through LLMs (supporting Qwen and Llama models) to automate malware comprehension.
- : An advanced AI-powered static analysis tool hosted on GitHub that automatically
                    scans Android manifests for dangerous permissions and extracts hardcoded secrets.
- :
                    A repository implementing Chain-of-Thought (CoT) reasoning with LLMs to automatically understand
                    malware behavior.
- : Emerging Model Context Protocol (MCP) integrations that link Android decompilers
                    directly into LLMs so an AI can read and analyze an application's code seamlessly.
📱
Stage 1: APK Ingestion
Hash check, VirusTotal lookup, metadata extraction
→
🔍
Stage 2: Static Engine
JADX decompilation, manifest parsing, CFG generation, YARA rules
→
🛡️
Stage 3: Dynamic Sandbox
Hardened emulator, Frida instrumentation, MITM network capture
→
🧠
Stage 4: GenAI Synthesis
LLM code interpretation, intent analysis, MITRE ATT&CK mapping
→
📄
Stage 5: Risk Report
0–100 risk score, PDF report, IOC extraction, recommendations

## Breaking Down the Terminology

### Generative AI
Large Language Models (LLMs) like GPT-4 or Claude, used here not to write essays, but to read complex
                    code, find patterns, and explain what the code does in plain English.

### Reverse Engineering
Taking a finished app (where the original human-written code is hidden) and cracking it open to see
                    how it was built.
Taking an APK apart to see how it works (like opening a
                    machine).

### Static Analysis
Inspecting the application's raw files, configurations, and un-executed code for red flags (like a
                    hidden script designed to steal SMS messages).
Inspecting the APK without running it (checking permissions,
                    suspicious strings, hardcoded URLs).

### Dynamic Analysis
Running the app inside a safe, isolated virtual smartphone (sandbox) to see what it actually does
                    when active (e.g., does it secretly try to contact a known hacker server?).
Running the APK safely and watching its behavior (Does it send
                    SMS? Connect to bad servers?).

### Risk Scoring
Calculating a mathematical score (e.g., 0 to 100) determining how dangerous the app is.
Giving the app a priority label (Low, Medium, High, Critical)
                    so teams know what to tackle first.

### Fraudulent APKs & Malware
Fake Android apps (.apk files) designed to mimic legitimate ones (like a fake banking app) to steal
                    money, passwords, or data.

## Innovation & Uniqueness — What Makes AEGIS Different
GenAI De-obfuscation
LLM reads obfuscated code and renames variables based on semantic meaning. No existing tool does this.
AI Smart Monkey
Computer vision + GenAI clicks through the app UI to trigger hidden malware payloads traditional sandboxes miss.
Intent Gap Solver
Doesn't just flag dangerous APIs — understands WHY the app is using them by reading contextual code patterns.
Human-Readable Output
Instead of 50-page XML logs, produces a 1-page plain English threat narrative any bank manager can understand.

## AEGIS System Deep Dives

### System Architecture
What is System Architecture?
In software engineering, System Architecture is the conceptual model that defines the structure,
                        behavior, and more views of a system. It is the master blueprint that details how different
                        microservices, databases, APIs, and processing engines communicate with one another. A good
                        architecture must solve for
(handling 1 app or 10,000 apps
                        simultaneously),
(if one component crashes, the system survives),
                        and
(adding new features easily).
The Problems with Traditional Malware Architecture
Legacy malware analysis systems are monolithic. You upload a file, it runs through a sequential
                        pipeline (unpack -> static scan -> dynamic scan -> report), and if the dynamic scan hangs, the
                        whole system crashes. They are not built for parallel processing or heavy AI inferencing.
The AEGIS System Architecture Solution
AEGIS is designed as an asynchronous, event-driven microservices architecture, heavily utilizing
                        message queues and containerization.
- A RESTful API built on FastAPI. Users (or automated
                            scraping bots) submit APK files here.
- The APK metadata is placed on a queue.
                            This decouples the upload process from the heavy lifting, preventing system timeouts.
- A central microservice that picks up the task from the
                            queue and coordinates the pipeline. It stores the raw APK in cloud object storage (AWS S3 or
                            MinIO).
- The Orchestrator sends a command to a
                            Docker container running JADX and Apktool. This node rips the APK apart, extracting the
                            AndroidManifest.xml, decompiling .dex into Smali and Java, and pulling out resources.
- The pipeline now splits into two
                            simultaneous tracks:
- Scans the extracted code.
- Installs the APK in a secure Android
                                    emulator (e.g., Anbox, Android Studio Emulator with Frida attached) and monitors it.
- This is the heart of AEGIS. The outputs from both
                            the Static and Dynamic engines (JSON logs, Smali snippets, network PCAPs) are aggregated and
                            passed to the LLM (via API like Gemini Pro or locally hosted Llama-3).
- Takes the AI's semantic analysis and translates it
                            into a hard, mathematical risk score (0-100).
- The final data is pushed to a NoSQL database (MongoDB) and
                            visualized on a React.js dashboard.
User
FastAPI Gateway
Kafka/RabbitMQ Broker
Orchestrator
Static Analysis Engine
Dynamic Sandbox Engine
GenAI Synthesis Core (LLM)
Risk Scoring Engine → MongoDB → React Dashboard

### Static Analysis Deep Dive
What is Static Analysis?
(ZIP archive)
├──
├──
├──
├──
├──
└──
permissions, API calls, strings, certificates, obfuscation score
Static analysis is the process of examining the code of an application without actually executing
                        or running it. Think of it like a building inspector looking at the blueprints of a house to
                        find structural flaws, rather than testing the house by experiencing an earthquake.
Problems with Current Static Analysis
Traditional static analysis relies on YARA rules or hash matching. It looks for known bad
                        signatures (e.g.,
).
- Malware authors change the code structure
                            slightly every time they compile, changing the file hash.
- The code is encrypted. The static analyzer
                            only sees a small "stub" of code that unpacks the real malware in memory later.
- Many legitimate apps use dangerous permissions
                            (e.g., WhatsApp needs SMS permissions for OTP).
How AEGIS Solves This: The Deep Dive
The AEGIS Static Analysis Engine performs a multi-layered deconstruction:
- It parses the AndroidManifest.xml to map
                            out all requested permissions, registered broadcast receivers, services, and entry points.
                            It looks for toxic combinations (e.g.,
- — a classic banking trojan combo).
- Using specialized engines (JADX), it converts Dalvik
                            bytecode into Java source code.
- AEGIS maps out how functions call each
                            other. If Function A gets the user's location, and Function B encrypts data, and Function C
                            sends data to the internet, the CFG links A -> B -> C.
- This is the breakthrough. When AEGIS encounters
                            heavily obfuscated code where variable names are garbage (e.g.,
- ), it isolates the function block and sends it to the
                            GenAI engine.
- "Analyze this obfuscated Java function. What is
                                    its core functionality? Rename the variables to reflect their probable purpose based
                                    on the API calls within."
- The LLM acts as an automated reverse engineer, interpreting that
- is
                                    likely
- based on the cryptography libraries it imports.

### Dynamic Analysis Deep Dive
What is Dynamic Analysis?
Dynamic analysis is the process of executing the malware in a controlled, isolated environment (a
                        sandbox) and watching what it actually does when it is running. If static analysis is looking at
                        blueprints, dynamic analysis is living in the house and watching the pipes leak.
Problems with Current Dynamic Analysis
- Malware checks if it is running on an
                            emulator. It checks for specific drivers (e.g., VirtualBox drivers), checks if the device
                            has a realistic number of contacts or photos, or checks if the gyroscope is moving. If it
                            detects a fake environment, it simply closes or acts like a normal calculator app.
- Malware often requires a user to click a specific
                            button (like "Grant Accessibility Permissions") to activate. Automated sandboxes usually
                            just open the app and wait. If no one clicks, the malware doesn't run.
How AEGIS Solves This: The Deep Dive
AEGIS employs an active, AI-driven dynamic sandbox.
- AEGIS uses highly customized Android
                            images where all emulator traces (Build.MODEL, Build.FINGERPRINT) are rewritten to mimic
                            real devices (e.g., mimicking a Samsung Galaxy S22). Fake data (contacts, SMS history,
                            sensor telemetry) is injected to fool the malware.
- AEGIS injects Frida (a dynamic code
                            instrumentation toolkit) directly into the app's memory process as it runs. This allows
                            AEGIS to hook into system APIs. When the malware tries to call
- to encrypt files, Frida intercepts the call, logs the encryption key being used, and then
                            lets the call proceed.
- All traffic leaving the emulator is routed
                            through a Man-In-The-Middle proxy. Even if the malware uses HTTPS, AEGIS intercepts the
                            traffic, decrypts it, logs the Command and Control (C2) IP addresses, and analyzes the
                            payload.
- Instead of random clicking,
                            AEGIS uses computer vision and GenAI to understand the screen. If a pop-up appears asking
                            for "Accessibility Service," the AI reads the screen, understands the context, and instructs
                            the testing script to click "Allow" to coax the malware into revealing its true payload.

### GenAI Engine + Risk Scoring
What is the GenAI Engine and Risk Scoring?
The GenAI Engine is the analytical brain that interprets the raw data gathered by the Static and
                        Dynamic stages. Risk Scoring is the mathematical framework that quantifies how dangerous the
                        application is, allowing human analysts to triage threats.
The Problem it Solves
Traditional engines output 50-page XML logs showing every single API call an app made. A human
                        analyst has to read this and determine if it's bad. This is cognitively exhausting and
                        unscalable.
How AEGIS Solves This
- AEGIS aggregates the Static CFG, the Dynamic API
                            hooks, and the Network PCAP logs into a structured JSON format. This structured data is fed
                            into a Large Language Model (e.g., Gemini 1.5 Pro, due to its massive context window).
- The LLM is given a system instruction: "You are an expert
                            mobile malware analyst. Review the following static and dynamic behavioral logs of an APK.
                            Identify if the app is a Banking Trojan, Spyware, Ransomware, Adware, or Benign. Provide a
                            step-by-step reasoning."
- The LLM outputs a human-readable narrative. E.g., "This app
                            claims to be a PDF reader, but statically it requests SMS permissions. Dynamically, upon
                            opening, it creates a hidden overlay on top of the banking app com.chase.sig and routes
                            stolen credentials to IP 192.168.x.x. Classification: Banking Trojan."
- The system translates the LLM's findings into a
                            quantitative score (0-100) based on the MITRE ATT&CK for Mobile framework.
- Privilege Escalation attempted? +20 points.
- Network traffic to known malicious IP? +30 points.
- Code obfuscation detected? +10 points.
- Score > 80: Critical Alert. Immediate quarantine.
92
CRITICAL RISK
FakeBankUpdate.apk

## Feasibility, Impact & Use Cases
₹14,000 Cr+
Cyber fraud losses in India (RBI 2024)
1.4 Lakh+
Cybersecurity incidents reported (CERT-In 2023)
40 hrs → 5 min
Analysis time: Manual vs AEGIS
95%+
Target malware detection accuracy
All components rely on proven technologies. Static/dynamic analysis tools are mature and open-source. LLM APIs and models are readily available (e.g. GPT-4, Google Gemini 1.5 Pro). The main challenges are engineering – integrating these pieces into a reliable pipeline, and managing the LLM context size for large binaries. However, as VirusTotal's Gemini example shows, modern LLMs can handle large codebases. Running sandboxes at scale requires infrastructure but is standard in threat intel firms. Thus, implementing AEGIS is well within current capabilities.
Challenge 1: LLM Hallucinations & False Positives
We do not rely solely on the LLM.
                                The Risk Score is a hybrid of deterministic rules (hard facts from Frida) and
                                probabilistic LLM analysis. Human-in-the-loop (HITL) review is required for edge cases.
human-in-the-loop review, ensemble models, threshold tuning, and training on benign/malware corpora.
Challenge 2: Processing Cost, Data Volume & Speed
AEGIS uses a filtering mechanism.
                                Only highly suspicious functions (determined by a lightweight pre-scan) or dynamic
                                behavior anomalies are sent to the LLM, rather than the entire codebase.
parallelize analysis, summarize code in chunks. The Gemini test shows entire samples in ~40s, indicating viability.
Challenge 3: Evasion & Obfuscation
use multiple sandbox configurations, keep images fresh, simulate real devices (virtual phones) to trick evasion checks.
Challenge 4: Privacy / Legal
analyze only in abstract, minimize exposure of sensitive code, possibly analyze on-premise for compliance.
By automating reverse engineering, AEGIS drastically cuts response time to new threats. What used to take days or weeks (manually unpacking and deobfuscating malware) can now take hours or minutes with AI assistance. This accelerates generation of IOCs and patches. Security teams gain a “virtual analyst” that digests code and explains it, as demonstrated by Google’s “Code Insight” tool that uses generative AI to generate analyst-like reports. The risk scoring provides a consistent measure to prioritize threats.
- Saves millions of dollars for telecommunications companies and
                            banks by preventing banking trojans from ever reaching end-user devices.
- Reduces the time to reverse-engineer a complex malware
                            strain from 40 hours (human) to 5 minutes (AEGIS).
- Pre-screening apps before they are
                            published.
Automatically vet new apps for malicious behavior before publishing or installation.
- Scanning apps installed by
                            corporate employees on BYOD devices.
- Integrate AEGIS analysis in their scanning engines to detect hidden Trojans in apps.
- Analyzing state-sponsored spyware (like Pegasus
                            variants) rapidly.
Rapidly analyze seized malware samples or malware-apps found in phishing campaigns, feeding IOCs into defensive measures.
- Analyze third-party libraries or update packages for hidden malicious code or vulnerabilities, as AEGIS can reverse-engineer them quickly.
AEGIS makes comprehensive mobile malware analysis tractable at scale. By combining static/dynamic techniques with cutting-edge generative AI, it addresses the core problem of “speed and depth” in malware intelligence, enabling organizations to stay ahead of fraudsters.

## Research & Comparison Table (AEGIS)
How does AEGIS stand against current industry giants?
By merging traditional, rigorous cybersecurity tools (Frida, JADX)
            with the cognitive reasoning capabilities of Generative AI, AEGIS solves the "intent gap" and the
            "obfuscation problem" that plague legacy systems.
