import requests

try:
    s = requests.Session()
    # We need to login first to bypass @login_required
    res_login = s.post('http://localhost:5000/login', data={'username': 'admin', 'password': 'admin123'})
    print(f"Login status: {res_login.status_code}")
    
    res = s.get('http://localhost:5000/api/attendance?date=all')
    print(f"Attendance status: {res.status_code}")
    print(res.json())
except Exception as e:
    print(f"ERROR: {e}")
