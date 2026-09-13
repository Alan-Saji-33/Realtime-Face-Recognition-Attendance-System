import sys
sys.path.append('c:\\Users\\alans\\OneDrive\\Desktop\\antigravity\\26-2__sql\\25-2__8-9 PM\\face_recognition_attendance')
from app import app
import json

app.config['TESTING'] = True
client = app.test_client()

with client.session_transaction() as sess:
    sess['user_id'] = 1
    sess['username'] = 'admin'
    sess['role'] = 'admin'

# Test export with period 1
response = client.get('/api/attendance/export?status=all&period=1')
print(f"Status CODE (Period 1): {response.status_code}")
if response.status_code == 200:
    print("Success: File received")
    print(f"Content Type: {response.headers.get('Content-Type')}")
    print(f"Content Disposition: {response.headers.get('Content-Disposition')}")
else:
    print(f"Error: {response.data}")

# Test export with non-existent data for period 99
response = client.get('/api/attendance/export?status=all&period=99')
print(f"Status CODE (Period 99): {response.status_code}")
print(f"Response: {response.data}")
