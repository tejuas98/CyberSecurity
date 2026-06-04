from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.output = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag in ['h1', 'h2', 'h3', 'p', 'li']:
            pass

    def handle_endtag(self, tag):
        if self.tags:
            self.tags.pop()

    def handle_data(self, data):
        if not self.tags: return
        tag = self.tags[-1]
        text = data.strip()
        if not text: return
        
        if tag == 'h1': self.output.append(f"\n# {text}\n")
        elif tag == 'h2': self.output.append(f"\n## {text}\n")
        elif tag == 'h3': self.output.append(f"\n### {text}\n")
        elif tag == 'p': self.output.append(f"{text}\n")
        elif tag == 'li': self.output.append(f"- {text}\n")
        elif tag == 'div': self.output.append(f"{text}\n")

parser = MyHTMLParser()
with open('index.html', 'r') as f:
    parser.feed(f.read())

with open('scratch_content.md', 'w') as out:
    out.write(''.join(parser.output))
