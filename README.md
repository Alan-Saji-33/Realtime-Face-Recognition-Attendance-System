# Realtime Face Recognition Attendance System

## Abstract

This project presents an automated student attendance management system that leverages face recognition technology to streamline and enhance the attendance-marking process. The system utilizes advanced computer vision and deep learning techniques to identify and authenticate students in real-time, eliminating manual roll calls and improving accuracy.

The application integrates a graphical user interface built with modern UI frameworks to provide an intuitive experience for administrators and staff. Upon startup, users are authenticated through a secure login mechanism before accessing the main dashboard. The system employs deep face embedding models to extract and compare facial features, enabling reliable student identification even under varying lighting and angle conditions. When a student's face is recognized, their attendance is automatically recorded with a timestamp in the database.

The platform includes comprehensive administrative features such as student enrollment with facial registration, attendance record management, and data analytics capabilities. The system maintains persistent records of all attendance events, allowing administrators to generate reports, track attendance trends over time, and monitor student presence patterns. The attendance statistics dashboard displays real-time metrics including present and absent counts, with graphical visualizations of historical attendance data.

## Features

### 1. User Roles
- **Admin**: Full system access, can manage students, teachers, and all attendance
- **Teacher**: Department-specific access, can mark attendance and view department students
- **Student**: Can view their own attendance records

### 2. Student Management
- Add new students with details (Student ID, Name, Roll No, Department, Year, Email, Phone)
- Delete students
- Register/Update face recognition for students

### 3. Teacher Management
- Add teachers with assigned department
- Update teacher details
- Delete teachers

### 4. Face Recognition
- Capture face during student registration
- Mark attendance by face recognition in real-time
- Duplicate face detection to prevent fraud

### 5. Attendance Marking
- Automatic face-based attendance marking
- Manual attendance marking by teachers/admin
- Mark attendance for any date (past or present)

### 6. Attendance Reports & Dashboard
- Filter by date, department, or status
- Export to Excel (.xlsx format)
- Overall attendance statistics, today's summary, and trend chart (last 7 days)
- Department-wise and Student-wise statistics

### 7. Security Features
- Password hashing (SHA256)
- Session management & Role-based access control

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