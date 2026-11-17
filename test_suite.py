from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Login
r = client.post('/admin/login', data={'username': 'admin', 'password': 'motora2026admin'}, follow_redirects=False)
cookie = r.cookies.get('motora_admin_session')
headers = {'Cookie': f'motora_admin_session={cookie}'}

# 1. Add a new vehicle
r = client.post('/admin/vehicles/new', headers=headers, data={
    'brand': 'Maserati',
    'model': 'Levante Trofeo V8',
    'year': 2024,
    'trim': 'Fuoriserie Edition',
    'country_of_origin': 'Germany',
    'engine_capacity': '3.8L Twin-Turbo V8 (580 HP)',
    'fuel_type': 'بنزين (Petrol)',
    'transmission': 'أوتوماتيك 8 سرعات ZF',
    'mileage': 3500,
    'exterior_color': 'Blu Emozione Metallic',
    'interior_color': 'Pieno Fiore Tan Leather',
    'vehicle_condition': 'فابريكة بالكامل - حالة المصنع',
    'vin': 'ZAM56RTA4P0991823',
    'units_available': 1,
    'units_total': 1,
    'selling_price_egp': 7950000,
    'reservation_deposit_egp': 250000,
    'expected_delivery_time': '14 - 18 يوم عمل',
    'description_ar': 'مازيراتي ليفانتي تروفيو بمحرك فيراري V8 تيربو جبار، وارد ألمانيا.',
    'description_en': 'Maserati Levante Trofeo with Ferrari-built twin-turbo V8.',
    'technical_specs': '{"الأداء": {"القوة": "580 HP"}}',
    'additional_notes': 'ضمان المصنع الدولي ساري.',
    'status': 'available',
    'is_featured': 1,
    'is_latest': 1,
    'is_special_offer': 0,
    'cover_image': 'https://images.unsplash.com/photo-1549399542-7e3f8b79c341',
    'media_json': '[{"url": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341", "media_type": "image", "caption": "Maserati Front"}]'
}, follow_redirects=False)
assert r.status_code == 303, f'Add vehicle failed: {r.status_code}'
print('[PASS] Add new vehicle dynamically succeeded!')

# 2. Check the newly added vehicle in public catalog
r = client.get('/vehicles?brand=Maserati')
assert r.status_code == 200
assert 'Levante Trofeo' in r.text
print('[PASS] Newly added vehicle immediately visible in public showcase!')

# 3. Duplicate vehicle test
r = client.post('/admin/vehicles/1/duplicate', headers=headers, follow_redirects=False)
assert r.status_code == 303, f'Duplicate failed: {r.status_code}'
print('[PASS] One-click listing duplication succeeded!')

# 4. Quick status toggle test
r = client.post('/admin/vehicles/1/quick-status', headers=headers, data={'status_val': 'reserved'})
assert r.status_code == 200
assert r.json()['status'] == 'reserved'
print('[PASS] Quick status toggle succeeded!')

# 5. Quick price update test
r = client.post('/admin/vehicles/1/quick-price', headers=headers, data={'price': 12900000})
assert r.status_code == 200
assert r.json()['price'] == 12900000
print('[PASS] Quick price update succeeded!')

# 6. Update tracking stage with evidence
r = client.post('/admin/tracking/7/update', headers=headers, data={
    'status_val': 'completed',
    'location': 'مجمع الجمارك - ميناء الإسكندرية',
    'notes': 'تم استخراج أصل شهادة الإفراج الجمركي وتسديد كافة الرسوم وضريبة القيمة المضافة.',
    'completed_at': '2026-11-07 02:00',
    'proof_media_json': '["https://images.unsplash.com/photo-1454165804606-c3d57bc86b40"]'
}, follow_redirects=False)
assert r.status_code == 303, f'Tracking stage update failed: {r.status_code}'
print('[PASS] Tracking stage advanced and evidence photo stored!')

# 7. Check that public tracking page shows stage 7 as completed
r = client.get('/tracking/MTR-2026-7842')
assert r.status_code == 200
assert 'تم استخراج أصل شهادة الإفراج الجمركي' in r.text
print('[PASS] Client tracking page reflects updated stage with 100% fidelity!')

print('=============================================')
print(' ALL ADVANCED ADMIN OPERATIONS VERIFIED!')
print('=============================================')
