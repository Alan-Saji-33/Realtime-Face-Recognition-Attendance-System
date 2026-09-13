# AttendX: Advanced Face Recognition Attendance System
## Comprehensive Project Documentation

Welcome to the official documentation for **AttendX**, a premium, AI-powered attendance management solution. This document provides an exhaustive breakdown of the system architecture, features, and technical specifications.

---

## 1. Project Overview
**AttendX** is a sophisticated web-based application designed to automate student attendance using real-time Face Recognition technology. It eliminates traditional manual roll calls, prevents proxy attendance through advanced liveliness detection, and provides a seamless interaction loop between Admins, Teachers, and Students.

> [!TIP]
> The system is built for high-performance environments, leveraging deep learning embeddings for near-instant identification even in large databases.

---

## 2. Core Technology Stack
| Layer | Technologies Used |
| :--- | :--- |
| **Backend** | Python Flask, Flask-Session |
| **Database** | MySQL (RDBMS) via `pymysql` |
| **AI / Computer Vision** | `face_recognition` (dlib), OpenCV, NumPy |
| **Frontend** | HTML5, CSS3 (Glassmorphism), Bootstrap 5, JavaScript (ES6+) |
| **Data Visualization** | Chart.js (Trends & Monthly Stats) |
| **Reporting** | OpenPyXL (Excel Export), DataTables.js |
| **Security** | SHA-256 Hashing, RBAC Middleware |

---

## 3. Role-Based Access Control (RBAC) Details
The system implements strict permission isolation for three distinct user types:

### 🛡️ Administrator (Super User)
- **Full System Visibility:** Access to all department records and global statistics.
- **Teacher Management:** Create, update, and delete teacher accounts; assign teachers to specific departments.
- **Student Management:** Register new students, update facial data, and manage records.
- **System Maintenance:** View global logs and export any report to Excel.

### 🎓 Teacher
- **Department Isolation:** Can only view and manage students within their assigned department (e.g., Computer Application, Commerce).
- **Attendance Marking:** 
    - **Face Mode:** Real-time AI marking with liveliness verification.
    - **Manual Mode:** Grid-based marking for flexibility.
- **Session Control:** "Finish Session" feature to bulk-mark remaining students as "Absent" for a specific period.
- **Claim Approval:** Review and respond to student attendance claims (Approve/Deny).

### 👤 Student
- **Personal Dashboard:** Real-time view of attendance percentage, present days, and absent days.
- **Detailed Tracking:** View attendance breakdown for all 6 periods of any given date.
- **Claim System:** File justifications for being marked absent to request a correction.
- **Notification Hub:** Receive alerts when attendance is marked or claims are processed.

---

## 4. Advanced AI & Face Recognition Features
AttendX goes beyond simple face matching with several "minute" technical optimizations:

### 👁️ Liveliness Detection (Anti-Spoofing)
To prevent students from showing a photo or a screen to the camera:
- **Motion Analysis:** The system captures multiple frames and looks for natural micro-movements.
- **Blink Detection:** Requires the user to blink or move during the recognition phase to verify a "live" human presence.
- **Retry Logic:** If a spoof is detected or recognition fails, the system provides up to 3 automatic retries with user-friendly guidance.

### 🧬 Deep Face Embeddings
- **High-Dimensional Mapping:** Converts faces into 128-dimensional mathematical vectors.
- **State-of-the-Art Accuracy:** Uses a strict similarity threshold (Distance < 0.20) to ensure zero false positives.
- **Duplicate Prevention:** During registration, the system scans the entire database to ensure a face isn't already assigned to another Student ID or Teacher ID.

---

## 5. Functional Features Breakdown

### 📅 The 6-Period System
Attendance is not just "daily." It is tracked across **6 distinct periods** throughout the day:
1. Attendance can be marked individually for each period.
2. The system prevents "Double Marking" for the same period.
3. Teachers can see which periods have already been recorded today to avoid overlaps.

### 📩 Automated Notifications
- **In-App Notifications:** Real-time bell alerts for status updates.
- **Background Email Alerts:** When a student is marked **Absent**, the system can automatically dispatch an email to the student (implemented via background threading to ensure zero UI delay).

### 📁 Reporting & Analytics
- **Live Statistics:** Total Students, Present Today, Absent Today, and Daily Attendance Trends (7-day chart).
- **Monthly Analytics:** Grouped attendance visualization for students to track progress over the semester.
- **Export Engine:** One-click Excel downloads with filters for Date, Department, and Attendance Status.

### 📝 Claims & Correction Loop
1. Student views an "Absent" mark for Period 3.
2. Student submits a **Claim** with a reason (e.g., "Medical Issue").
3. Teacher receives a **Pending Claim** notification.
4. Teacher **Approves** the claim.
5. **System Logic:** The attendance record is automatically flipped from "Absent" to "Present" in the database, and the student receives a success notification.

---

## 6. Project Architecture (Minute Details)
- **Database Schema:** 
    - `users`: Core authentication table (hashed passwords).
    - `students`: Extensive student profile with facial embeddings stored as JSON blobs.
    - `attendance`: Transactional table with unique constraints on `(student_id, date, period)`.
    - `claims`: Audit trail of attendance corrections.
    - `notifications`: User-specific alert storage.
- **Directory Structure:**
    - `/encodings`: Storage for pre-computed facial patterns.
    - `/static`: Premium CSS, JS libraries, and UI assets.
    - `/templates`: Jinja2 templates (role-aware sidebars).
    - `/attendance_reports`: Auto-generated Excel files.

---

## 7. Security Measures
> [!IMPORTANT]
> - **Password Hashing:** All passwords are encrypted using SHA-256; plain text is never stored.
> - **Session Security:** `HTTPOnly` and `SameSite=Lax` flags enabled to prevent CSRF and XSS-based session hijacking.
> - **Middleware Protection:** Every sensitive route (API or Page) is wrapped in a `login_required` decorator with role-verification.

---

## 8. Future Roadmap
- [ ] **Mobile App Integration:** Native Android/iOS app for student logins.
- [ ] **SMS Integration:** OTP-based login and SMS alerts for parents.
- [ ] **Leave Management:** Formal leave application and approval workflow.
- [ ] **AI-Powered Prediction:** Predicting students at risk of falling below attendance thresholds.

---
*Documentation generated by Antigravity AI Assistant.*
