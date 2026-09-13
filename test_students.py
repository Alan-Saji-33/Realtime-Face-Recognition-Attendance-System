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

response = client.get('/api/students')
print(f"Status CODE: {response.status_code}")
if response.status_code != 200:
    print(response.data)
else:
    data = json.loads(response.data)
    print(f"Data length: {len(data)}")
