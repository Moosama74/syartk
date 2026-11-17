import urllib.request
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

with urllib.request.urlopen('http://127.0.0.1:8000') as response:
    html = response.read().decode('utf-8')

css_path = os.path.join(base_dir, 'static', 'css', 'style.css')
js_path = os.path.join(base_dir, 'static', 'js', 'main.js')

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace css link with inline style
html = html.replace('<link rel="stylesheet" href="/static/css/style.css">', f'<style>\n{css_content}\n</style>')
# Replace js script with inline script
html = html.replace('<script src="/static/js/main.js"></script>', f'<script>\n{js_content}\n</script>')

target_file = os.path.join(base_dir, 'preview.html')
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html)

print('Standalone preview.html created successfully!')
