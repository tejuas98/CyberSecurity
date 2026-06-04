import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add CSS
new_css = """
        /* Deep Dive Inner Grid */
        .deep-dive-subsection {
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: 2rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }
        .deep-dive-subsection:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        .deep-dive-subtitle {
            font-weight: 700;
            color: var(--text-color);
            font-size: 1.1rem;
            line-height: 1.4;
            padding-right: 1rem;
        }
        .deep-dive-subcontent p:first-child, .deep-dive-subcontent ul:first-child, .deep-dive-subcontent ol:first-child {
            margin-top: 0;
        }
        @media (max-width: 768px) {
            .deep-dive-subsection {
                grid-template-columns: 1fr;
                gap: 0.5rem;
            }
        }
"""
html = html.replace('/* Section Spacing */', new_css + '\n        /* Section Spacing */')


# 2. Extract and transform the aegis-deep-dives section
start_idx = html.find('id="aegis-deep-dives"')
end_idx = html.find('</section>', start_idx)

section_content = html[start_idx:end_idx]

# We want to find each <div class="deep-dive-content"...> ... </div>
# Since there are multiple blocks, it's easier to regex for <h4>...</h4> and group the following text.
# A simpler approach: replace <h4> with a divider and then split.

# Find all deep-dive-blocks
blocks = re.split(r'(<div class="deep-dive-block".*?>)', section_content)
# blocks[0] is everything before the first block
# blocks[1] is the first block opening tag
# blocks[2] is the inner content up to the next block, and so on...

new_section_content = blocks[0]

for i in range(1, len(blocks), 2):
    block_opening = blocks[1] if i == 1 else blocks[i]
    block_inner = blocks[i+1]
    
    # We need to find all <h4> inside block_inner
    # Let's split by <h4>
    parts = re.split(r'<h4>(.*?)</h4>', block_inner)
    
    # parts[0] is the content before the first <h4> (usually just the <h3> title)
    transformed_inner = parts[0]
    
    for j in range(1, len(parts), 2):
        h4_text = parts[j]
        content = parts[j+1]
        
        transformed_inner += f'''<div class="deep-dive-subsection">
                            <div class="deep-dive-subtitle">{h4_text}</div>
                            <div class="deep-dive-subcontent">{content}</div>
                        </div>'''
                        
    new_section_content += block_opening + transformed_inner

html = html[:start_idx] + new_section_content + html[end_idx:]

with open('index.html', 'w') as f:
    f.write(html)

print("Transform Done")
