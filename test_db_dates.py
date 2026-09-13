import sys
sys.path.append('c:\\Users\\alans\\OneDrive\\Desktop\\antigravity\\26-2__sql\\25-2__8-9 PM\\face_recognition_attendance')
from db import Database

try:
    db = Database()
    res = db.get_attendance(date=None)
    for r in res[:5]:
        print(f"Date: {r['date']} Type: {type(r['date'])}")
except Exception as e:
    print(f"ERROR: {e}")
