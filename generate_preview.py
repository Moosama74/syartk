import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, base_dir)

from app.templates import templates
from app.database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("SELECT key, value FROM settings")
settings = {r['key']: r['value'] for r in cursor.fetchall()}

cursor.execute("SELECT * FROM vehicles WHERE status != 'hidden' AND is_featured = 1 ORDER BY id DESC LIMIT 6")
featured = cursor.fetchall()

cursor.execute("SELECT * FROM vehicles WHERE status != 'hidden' ORDER BY id DESC LIMIT 8")
latest = cursor.fetchall()

cursor.execute("SELECT * FROM vehicles WHERE status != 'hidden' AND is_special_offer = 1 ORDER BY id DESC LIMIT 4")
special = cursor.fetchall()

cursor.execute("SELECT brand, COUNT(*) as count FROM vehicles WHERE status != 'hidden' GROUP BY brand")
brands = cursor.fetchall()

cursor.execute("SELECT * FROM testimonials WHERE is_approved = 1 ORDER BY id DESC")
testimonials = cursor.fetchall()

cursor.execute("SELECT COUNT(*) as total FROM vehicles WHERE status != 'hidden'")
total_inventory = cursor.fetchone()['total']

conn.close()

# Render template
template = templates.get_template('index.html')
rendered = template.render(
    request=None,
    lang='ar',
    settings=settings,
    featured_vehicles=featured,
    latest_vehicles=latest,
    special_offers=special,
    brands=brands,
    testimonials=testimonials,
    total_inventory=total_inventory
)

# Inline the luxury CSS so that double clicking opens beautifully anywhere without a web server
css_file = os.path.join(base_dir, 'static', 'css', 'style.css')
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

rendered = rendered.replace('<link rel="stylesheet" href="/static/css/style.css">', f'<style>\n{css}\n</style>')

target_file = os.path.join(base_dir, 'preview.html')
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(rendered)

print('SUCCESS: preview.html generated successfully!')
