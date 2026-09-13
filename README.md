# Realtime Face Recognition Attendance System

## Abstract

This project presents an automated student attendance management system that leverages face recognition technology to streamline and enhance the attendance-marking process. The system utilizes advanced computer vision and deep learning techniques to identify and authenticate students in real-time, eliminating manual roll calls and improving accuracy.

The application integrates a graphical user interface built with modern UI frameworks to provide an intuitive experience for administrators and staff. Upon startup, users are authenticated through a secure login mechanism before accessing the main dashboard. The system employs deep face embedding models to extract and compare facial features, enabling reliable student identification even under varying lighting and angle conditions. When a student's face is recognized, their attendance is automatically recorded with a timestamp in the database.

The platform includes comprehensive administrative features such as student enrollment with facial registration, attendance record management, and data analytics capabilities. The system maintains persistent records of all attendance events, allowing administrators to generate reports, track attendance trends over time, and monitor student presence patterns. The attendance statistics dashboard displays real-time metrics including present and absent counts, with graphical visualizations of historical attendance data.

## Detailed Features List

### 1. User Roles
- **Admin**: Full system access, can manage students, teachers, and all attendance records.
- **Teacher**: Department-specific access, can mark attendance and view their respective department students.
- **Student**: Portal access to view their own attendance records and statistics.

### 2. Student Management
- **Comprehensive Enrollment**: Add new students with detailed profiles including Student ID (auto-generated), Full Name, Roll Number, Department, Year, Email, and Phone.
- **Login Credentials**: Ability to assign username and password for student portal access.
- **Data Maintenance**: Update student details or delete records as needed.
- **Facial Registration**: Dedicated module to register and update face recognition models for individual students.

### 3. Teacher Management
- **Teacher Onboarding**: Add teachers with specific usernames, passwords, names, and assigned departments.
- **Record Updating**: Modify teacher details or remove teacher access as required.

### 4. Face Recognition
- **On-the-fly Capture**: Capture a student's face directly during the initial registration process.
- **Subsequent Registration**: Register a face later using the integrated camera interface.
- **Real-time Detection**: Live camera feed with a guide overlay for accurate positioning and immediate face detection.
- **Anti-Fraud Mechanisms**: Duplicate face detection ensures the same face isn't registered to multiple students.

### 5. Attendance Marking
- **Automated Marking**: Seamless, face-based automatic attendance logging.
- **Manual Overrides**: Manual attendance marking capabilities for teachers and admins in case of technical issues.
- **Flexible Logging**: Ability to mark attendance for any specific date, past or present, as Present or Absent.

### 6. Attendance Reports
- **Comprehensive Logs**: View all historical attendance records in a centralized dashboard.
- **Advanced Filtering**: Filter attendance data by specific dates, departments, or attendance status (Present/Absent).
- **Data Export**: Export filtered or complete attendance reports directly to Excel (.xlsx format) for external record-keeping.

### 7. Dashboard & Statistics
- **Overall Metrics**: At-a-glance overall attendance statistics and today's attendance summary.
- **Trend Analysis**: Visual attendance trend charts tracking data over the last 7 days.
- **Granular Stats**: Drill down into department-wise and individual student-wise attendance statistics.

### 8. Student Portal
- **Self-Service Access**: Students can log in to view their own attendance history.
- **Detailed Statistics**: View personal attendance metrics including total days, present days, and attendance percentage.
- **Daily Status**: Quick check to see if they have been marked present for the current day.

### 9. Security & Authentication
- **Data Protection**: Secure password hashing using SHA256.
- **Session Control**: Robust session management to handle user logins and timeouts securely.
- **Access Control**: Role-based access control ensures users can only access authorized routes and data.
- **Multiple Login Methods**: Support for traditional username/password login.

## Technology Stack
- **Backend**: Python Flask
- **Database**: MySQL
- **Face Recognition**: `face_recognition` library (dlib)
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **DataTables**: For interactive tables
- **Excel Export**: `openpyxl`

## Default Accounts
- **Admin**: username=`admin`, password=`admin123`
- **Teacher**: username=`teacher`, password=`teacher123`
- **Student**: username=`student`, password=`student123`

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alan-Saji-33/Realtime-Face-Recognition-Attendance-System.git
   cd Realtime-Face-Recognition-Attendance-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Configuration:**
   Ensure MySQL is running and update `config.py` with your database credentials.

4. **Run the application:**
   ```bash
   python app.py
   ```
   The application will be accessible via `http://localhost:5000`

## License
MIT License