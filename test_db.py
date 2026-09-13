import sys
import os
sys.path.append('c:\\Users\\alans\\OneDrive\\Desktop\\antigravity\\26-2__sql\\25-2__8-9 PM\\face_recognition_attendance')
from db import Database

try:
    db = Database()
    res = db.get_attendance(date=None)
    print(f"Attendance length: {len(res) if res else 'None'}")
    
    res_all = db.get_attendance(date='all')
    print(f"Attendance all: {len(res_all) if res_all else 'None'}")
except Exception as e:
    print(f"ERROR: {e}")
