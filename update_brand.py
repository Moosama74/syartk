import sqlite3
import os
import re

BASE_DIR = r"C:\Users\SHOEIB TEK\.gemini\antigravity\scratch\motora"
DB_PATH = os.path.join(BASE_DIR, "motora.db")

# 1. Update Database settings
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

updates = {
    "site_name_en": "SYARTK",
    "site_name_ar": "سيارتك",
    "tagline_en": "SYARTK - Exclusive Luxury Automotive Import Platform Egypt",
    "tagline_ar": "سيارتك - المنصة الحصرية لاستيراد وتوريد السيارات الفاخرة إلى مصر",
    "cairo_showroom_address_ar": "صالة عرض سيارتك - الشيخ زايد، الجيزة - القاهرة",
    "cairo_showroom_address_en": "SYARTK Showroom - Sheikh Zayed, Cairo, Egypt",
}

for k, v in updates.items():
    cursor.execute("UPDATE settings SET value = ? WHERE key = ?", (v, k))

# Update tracking stages notes if any mention MOTORA
cursor.execute("UPDATE tracking_stages SET stage_title_ar = REPLACE(stage_title_ar, 'موتورا', 'سيارتك')")
cursor.execute("UPDATE tracking_stages SET stage_title_en = REPLACE(stage_title_en, 'MOTORA', 'SYARTK')")
cursor.execute("UPDATE tracking_stages SET location = REPLACE(location, 'موتورا', 'سيارتك')")
cursor.execute("UPDATE tracking_stages SET location = REPLACE(location, 'MOTORA', 'SYARTK')")
cursor.execute("UPDATE tracking_stages SET notes = REPLACE(notes, 'موتورا', 'سيارتك')")
cursor.execute("UPDATE tracking_stages SET notes = REPLACE(notes, 'MOTORA', 'SYARTK')")

# Update vehicles description if any mention MOTORA
cursor.execute("UPDATE vehicles SET description_ar = REPLACE(description_ar, 'موتورا', 'سيارتك')")
cursor.execute("UPDATE vehicles SET description_en = REPLACE(description_en, 'MOTORA', 'SYARTK')")

conn.commit()
conn.close()
print("[PASS] Database updated with SYARTK / Syartk")
