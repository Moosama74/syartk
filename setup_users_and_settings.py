import sqlite3
import os

BASE_DIR = r"C:\Users\SHOEIB TEK\.gemini\antigravity\scratch\motora"
DB_PATH = os.path.join(BASE_DIR, "motora.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. Create Users Table for customer accounts
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    city TEXT DEFAULT 'مدينة العبور - القاهرة',
    created_at TEXT NOT NULL
);
""")

# 2. Add user_id column to bookings if not present
try:
    cursor.execute("ALTER TABLE bookings ADD COLUMN user_id INTEGER;")
except Exception:
    pass

# 3. Update settings table
settings_updates = {
    "site_name_ar": "Syartk",
    "site_name_en": "Syartk",
    "phone_primary": "01125626292",
    "whatsapp_number": "201125626292",
    "phone_secondary": "01125626292",
    "cairo_showroom_address_ar": "مدينة العبور - القاهرة (صالة عرض Syartk)",
    "cairo_showroom_address_en": "El Obour City - Cairo (Syartk Showroom)",
    "tagline_ar": "Syartk - المنصة الحصرية لاستيراد وتوريد السيارات الفاخرة | مدينة العبور - القاهرة",
    "tagline_en": "Syartk - Exclusive Luxury Automotive Import Platform | El Obour City - Cairo",
}

for k, v in settings_updates.items():
    cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (k, v))

conn.commit()
conn.close()
print("[PASS] Database schema and settings updated successfully!")
