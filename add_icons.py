import re

def add_icons(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Dictionary of keyword to font-awesome icon
    icons = {
        r'\bStatic Analysis\b': '<i class="fa-solid fa-magnifying-glass"></i> Static Analysis',
        r'\bDynamic Analysis\b': '<i class="fa-solid fa-bolt"></i> Dynamic Analysis',
        r'\bEvidence Graph\b': '<i class="fa-solid fa-diagram-project"></i> Evidence Graph',
        r'\bGenAI\b': '<i class="fa-solid fa-brain"></i> GenAI',
        r'\bRisk Score\b': '<i class="fa-solid fa-gauge-high"></i> Risk Score',
        r'\bRisk Scoring\b': '<i class="fa-solid fa-gauge-high"></i> Risk Scoring',
        r'\bReport\b': '<i class="fa-solid fa-file-invoice"></i> Report',
        r'\bReports\b': '<i class="fa-solid fa-file-invoice"></i> Reports',
        r'\bAPK\b': '<i class="fa-brands fa-android"></i> APK',
        r'\bAPKs\b': '<i class="fa-brands fa-android"></i> APKs',
        r'\bCustomer\b': '<i class="fa-solid fa-user"></i> Customer',
        r'\bBank\b': '<i class="fa-solid fa-building-columns"></i> Bank',
        r'\bFraud\b': '<i class="fa-solid fa-user-secret"></i> Fraud',
        r'\bMalware\b': '<i class="fa-solid fa-bug"></i> Malware',
        r'\bDashboard\b': '<i class="fa-solid fa-chart-line"></i> Dashboard',
        r'\bExport\b': '<i class="fa-solid fa-download"></i> Export',
        r'\bUpload\b': '<i class="fa-solid fa-upload"></i> Upload',
        r'\bPrivacy\b': '<i class="fa-solid fa-shield-halved"></i> Privacy',
        r'\bSecurity\b': '<i class="fa-solid fa-shield"></i> Security',
        r'\bCompliance\b': '<i class="fa-solid fa-clipboard-check"></i> Compliance',
        r'\bDataset\b': '<i class="fa-solid fa-database"></i> Dataset',
        r'\bValidation\b': '<i class="fa-solid fa-circle-check"></i> Validation',
        r'\bArchitecture\b': '<i class="fa-solid fa-sitemap"></i> Architecture',
        r'\bReverse Engineering\b': '<i class="fa-solid fa-cogs"></i> Reverse Engineering',
        r'\bPhishing\b': '<i class="fa-solid fa-fish-fins"></i> Phishing',
        r'\bCredential\b': '<i class="fa-solid fa-id-card"></i> Credential',
        r'\bCredentials\b': '<i class="fa-solid fa-id-card"></i> Credentials',
        r'\bOTP\b': '<i class="fa-solid fa-key"></i> OTP',
        r'\bSMS\b': '<i class="fa-solid fa-comment-sms"></i> SMS',
        r'\bNetwork\b': '<i class="fa-solid fa-network-wired"></i> Network',
        r'\bEmulator\b': '<i class="fa-solid fa-mobile-screen"></i> Emulator',
        r'\bScore\b': '<i class="fa-solid fa-star-half-stroke"></i> Score',
    }

    # We only want to replace inside text, not inside HTML tags.
    # A simple way is to split by '>' and '<'
    parts = re.split(r'(<[^>]*>)', html)
    
    for i in range(0, len(parts)):
        # Even indices are text outside tags
        if i % 2 == 0:
            text = parts[i]
            # Avoid double replacement if an icon is already there
            # We will use a quick hack to avoid replacing if it's already right after an icon
            # Let's just do a simple replacement for now, since we haven't added these specific ones yet.
            for pattern, replacement in icons.items():
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
            parts[i] = text

    # Join back
    new_html = "".join(parts)

    # Some manual fixes where icons are put inside attributes or styles, though our split handles tag contents
    # Let's write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == "__main__":
    add_icons("ps1.html")
