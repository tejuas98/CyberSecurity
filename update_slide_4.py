import sys

filepath = "/Users/toru/Projects and codes/project manager/ps1.html"

with open(filepath, "r") as f:
    content = f.read()

s4_start = content.find("<!-- SLIDE 4:")
if s4_start == -1:
    print("Could not find slide 4 start marker")
    sys.exit(1)

s5_start = content.find("<!-- SLIDE 5", s4_start)
if s5_start == -1:
    s5_start = content.find("</div>\n</body>", s4_start)

if s5_start == -1:
    print("Could not find slide 5 start marker")
    sys.exit(1)

slide_4_content = content[s4_start:s5_start]

# Left Panel Replacements
slide_4_content = slide_4_content.replace(
    'gap: 8px; justify-content: space-around;',
    'gap: 4px; justify-content: space-around;'
)
slide_4_content = slide_4_content.replace(
    'padding: 8px; font-size: 12px; font-weight: bold; color: #404040;',
    'padding: 6px 8px; font-size: 11px; font-weight: bold; color: #404040;'
)

# Center Panel Replacements
slide_4_content = slide_4_content.replace(
    'padding:6px 10px;',
    'padding:4px 8px;'
)
slide_4_content = slide_4_content.replace(
    'font-size:12px; font-weight:bold; color:#404040; margin-bottom:2px;',
    'font-size:11px; font-weight:bold; color:#404040; margin-bottom:2px;'
)

# Right Panel Replacements
slide_4_content = slide_4_content.replace(
    'gap: 10px; justify-content: flex-start;',
    'gap: 6px; justify-content: flex-start;'
)

# Screen Headers
slide_4_content = slide_4_content.replace(
    'padding: 6px 8px; color: white; font-size: 12px;',
    'padding: 4px 6px; color: white; font-size: 11px;'
)
# Screen Bodies
slide_4_content = slide_4_content.replace(
    'padding: 8px; font-size: 11px; color: #404040; background: #F2F2F2;',
    'padding: 6px; font-size: 10px; color: #404040; background: #F2F2F2;'
)
slide_4_content = slide_4_content.replace(
    'padding: 8px; font-size: 11px; color: #404040; background: #FFFFFF;',
    'padding: 6px; font-size: 10px; color: #404040; background: #FFFFFF;'
)

# Screen 1 inner
slide_4_content = slide_4_content.replace(
    'padding: 10px; text-align: center; margin-bottom: 6px;',
    'padding: 6px; text-align: center; margin-bottom: 4px;'
)
slide_4_content = slide_4_content.replace(
    'padding: 6px; font-weight: bold; border-radius: 2px; cursor: pointer; border: 1px solid #203864; font-size: 11px;',
    'padding: 4px; font-weight: bold; border-radius: 2px; cursor: pointer; border: 1px solid #203864; font-size: 10px;'
)

# Screen 2 inner
slide_4_content = slide_4_content.replace(
    'padding-bottom: 6px; margin-bottom: 6px;',
    'padding-bottom: 4px; margin-bottom: 4px;'
)
slide_4_content = slide_4_content.replace(
    'margin-bottom: 8px;">\n                            <b>E1</b>',
    'margin-bottom: 4px;">\n                            <b>E1</b>'
)
slide_4_content = slide_4_content.replace(
    'padding: 4px; font-weight: bold; text-align: center; flex: 1;',
    'padding: 2px; font-weight: bold; text-align: center; flex: 1; font-size: 9px;'
)

# Bottom badges margin
slide_4_content = slide_4_content.replace(
    'margin-top: 8px; display: flex; flex-direction: column; gap: 8px;',
    'margin-top: 4px; display: flex; flex-direction: column; gap: 6px;'
)

new_content = content[:s4_start] + slide_4_content + content[s5_start:]

with open(filepath, "w") as f:
    f.write(new_content)

print("Slide 4 successfully updated.")
