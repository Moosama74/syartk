import os
import re

BASE_DIR = r"C:\Users\SHOEIB TEK\.gemini\antigravity\scratch\motora"

# Dictionary of file-specific or general replacements
files_to_update = [
    os.path.join(BASE_DIR, "templates", "base.html"),
    os.path.join(BASE_DIR, "templates", "index.html"),
    os.path.join(BASE_DIR, "templates", "inventory.html"),
    os.path.join(BASE_DIR, "templates", "vehicle_detail.html"),
    os.path.join(BASE_DIR, "templates", "tracking.html"),
    os.path.join(BASE_DIR, "templates", "admin", "base_admin.html"),
    os.path.join(BASE_DIR, "templates", "admin", "dashboard.html"),
    os.path.join(BASE_DIR, "templates", "admin", "login.html"),
    os.path.join(BASE_DIR, "templates", "admin", "settings.html"),
    os.path.join(BASE_DIR, "templates", "admin", "vehicles_list.html"),
    os.path.join(BASE_DIR, "templates", "admin", "vehicle_form.html"),
    os.path.join(BASE_DIR, "templates", "admin", "tracking_manager.html"),
    os.path.join(BASE_DIR, "templates", "admin", "tracking_stage_edit.html"),
    os.path.join(BASE_DIR, "app", "routers", "public.py"),
    os.path.join(BASE_DIR, "app", "routers", "admin.py"),
    os.path.join(BASE_DIR, "app", "database.py"),
    os.path.join(BASE_DIR, "run.py"),
]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Specific replacements for bilingual branding
    if "base.html" in file_path:
        content = content.replace("MOTORA</title>", "{% if lang == 'ar' %}سيارتك{% else %}SYARTK{% endif %}</title>")
        # Main logo box
        content = re.sub(
            r'<div class="w-10 h-10 rounded-lg bg-gradient-to-br from-gold-light via-gold to-gold-dark flex items-center justify-center text-black font-black text-xl[^"]*">\s*M\s*</div>',
            '<div class="w-10 h-10 rounded-lg bg-gradient-to-br from-gold-light via-gold to-gold-dark flex items-center justify-center text-black font-black text-xl shadow-lg shadow-gold/20 group-hover:scale-105 transition-transform">{% if lang == \'ar\' %}س{% else %}S{% endif %}</div>',
            content
        )
        content = content.replace('<span class="text-2xl font-black tracking-widest text-white group-hover:text-gold transition font-mono">MOTORA</span>',
                                  '<span class="text-2xl font-black tracking-widest text-white group-hover:text-gold transition font-mono">{% if lang == \'ar\' %}سيارتك{% else %}SYARTK{% endif %}</span>')
        # Footer logo box
        content = re.sub(
            r'<div class="w-8 h-8 rounded bg-gold flex items-center justify-center text-black font-black font-mono">\s*M\s*</div>',
            '<div class="w-8 h-8 rounded bg-gold flex items-center justify-center text-black font-black font-mono">{% if lang == \'ar\' %}س{% else %}S{% endif %}</div>',
            content
        )
        content = content.replace('<span class="text-xl font-black text-white tracking-widest font-mono">MOTORA</span>',
                                  '<span class="text-xl font-black text-white tracking-widest font-mono">{% if lang == \'ar\' %}سيارتك{% else %}SYARTK{% endif %}</span>')
        content = content.replace("صالة موتورا", "صالة سيارتك")
        content = content.replace("MOTORA Showroom", "SYARTK Showroom")
        content = content.replace("MOTORA owner", "SYARTK owner")
        content = content.replace("MTR-2026-XXXX", "SYR-2026-XXXX")
        content = content.replace("© 2026 MOTORA Automotive Marketplace.", "© 2026 {% if lang == 'ar' %}سيارتك (SYARTK){% else %}SYARTK Automotive Platform{% endif %}.")

    elif "base_admin.html" in file_path:
        content = content.replace('<div class="w-9 h-9 rounded-lg bg-gold text-black flex items-center justify-center font-black font-mono shadow-md shadow-gold/20">M</div>',
                                  '<div class="w-9 h-9 rounded-lg bg-gold text-black flex items-center justify-center font-black font-mono shadow-md shadow-gold/20">S</div>')
        content = content.replace('<span class="text-xl font-black text-white tracking-widest font-mono">MOTORA</span>',
                                  '<span class="text-xl font-black text-white tracking-widest font-mono">SYARTK <span class="text-sm font-bold text-gold">(سيارتك)</span></span>')
        content = content.replace("MOTORA Admin", "SYARTK Admin | سيارتك")
        content = content.replace("مالك موتورا", "مالك سيارتك")

    elif "dashboard.html" in file_path:
        content = content.replace("لوحة تحكم معرض موتورا", "لوحة تحكم معرض سيارتك (SYARTK)")
        content = content.replace("معرض موتورا", "معرض سيارتك")
        content = content.replace("MOTORA Control Center", "SYARTK Control Center")
        content = content.replace("MOTORA", "SYARTK")

    elif "login.html" in file_path:
        content = content.replace("MOTORA", "SYARTK (سيارتك)")
        content = content.replace("معرض موتورا", "معرض سيارتك")
        content = content.replace("صالة موتورا", "صالة سيارتك")

    elif "index.html" in file_path:
        content = content.replace("MOTORA | Exclusive Imported Automobiles Showroom Egypt", "SYARTK | Exclusive Imported Automobiles Showroom Egypt")
        content = content.replace("موتورا | صالة استيراد السيارات الفاخرة إلى مصر", "سيارتك | صالة استيراد السيارات الفاخرة إلى مصر")
        content = content.replace("منصة MOTORA توفر لك", "منصة سيارتك توفر لك")
        content = content.replace("MOTORA provides hand-picked", "SYARTK provides hand-picked")
        content = content.replace("لماذا تختار موتورا؟", "لماذا تختار سيارتك؟")
        content = content.replace("Why Choose MOTORA?", "Why Choose SYARTK?")
        content = content.replace("صالة عرض موتورا - القاهرة", "صالة عرض سيارتك - القاهرة")
        content = content.replace("MOTORA Cairo Showroom", "SYARTK Cairo Showroom")
        content = content.replace("صالة موتورا", "صالة سيارتك")
        content = content.replace("MOTORA", "SYARTK")
        content = content.replace("موتورا", "سيارتك")

    # General replacements across other files
    content = content.replace("صالة عرض موتورا", "صالة عرض سيارتك")
    content = content.replace("صالة موتورا", "صالة سيارتك")
    content = content.replace("معرض موتورا", "معرض سيارتك")
    content = content.replace("MOTORA Showroom", "SYARTK Showroom")
    content = content.replace("MOTORA", "SYARTK")
    content = content.replace("موتورا", "سيارتك")
    content = content.replace("MTR-", "SYR-")

    if content != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[UPDATED] {os.path.basename(file_path)}")

print("[COMPLETE] Brand updated to SYARTK / سيارتك across all templates & backend!")
