import requests

try:
    s = requests.Session()
    s.post('http://localhost:5000/login', data={'username': 'admin', 'password': 'admin123'})
    
    res = s.get('http://localhost:5000/api/attendance')
    print(f"Empty date length: {len(res.json())}")
    
    res = s.get('http://localhost:5000/api/attendance?date=Today')
    print(f"Today date length: {len(res.json())}")
except Exception as e:
    print(f"ERROR: {e}")
