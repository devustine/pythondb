import sqlite3

conn = sqlite3.connect("miva_university.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    date_of_birth TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Instructor (
    instructor_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    phone_number TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    course_code TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    credit_hours INTEGER NOT NULL,
    department TEXT NOT NULL,
    instructor_id TEXT NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES Instructor(instructor_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    student_id TEXT NOT NULL,
    course_code TEXT NOT NULL,
    PRIMARY KEY (student_id, course_code),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_code) REFERENCES Course(course_code)
)
""")

# --- Insert Instructors (20) ---
instructors = [
    ("I001", "Dr. Smith", "Computer Science", "08010000001"),
    ("I002", "Dr. White", "Computer Science", "08010000002"),
    ("I003", "Prof. Green", "Information Technology", "08010000003"),
    ("I004", "Dr. Black", "Information Technology", "08010000004"),
    ("I005", "Dr. Adams", "Mathematics", "08010000005"),
    ("I006", "Prof. Brown", "Mathematics", "08010000006"),
    ("I007", "Dr. Clark", "Business", "08010000007"),
    ("I008", "Dr. Davis", "Business", "08010000008"),
    ("I009", "Prof. Evans", "Education", "08010000009"),
    ("I010", "Dr. Foster", "Education", "08010000010"),
    ("I011", "Dr. Grant", "Engineering", "08010000011"),
    ("I012", "Prof. Harris", "Engineering", "08010000012"),
    ("I013", "Dr. Irving", "Law", "08010000013"),
    ("I014", "Dr. Jones", "Law", "08010000014"),
    ("I015", "Prof. King", "Health Sciences", "08010000015"),
    ("I016", "Dr. Lewis", "Health Sciences", "08010000016"),
    ("I017", "Dr. Moore", "Arts", "08010000017"),
    ("I018", "Prof. Nelson", "Arts", "08010000018"),
    ("I019", "Dr. Owen", "Economics", "08010000019"),
    ("I020", "Dr. Parker", "Economics", "08010000020"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO Instructor VALUES (?, ?, ?, ?)",
    instructors
)

# --- Insert Students (20) ---
students = [
    ("S001", "Alice Brown", "alice@miva.edu", "2002-01-10"),
    ("S002", "Bob Miller", "bob@miva.edu", "2001-03-22"),
    ("S003", "Charlie Reed", "charlie@miva.edu", "2000-07-15"),
    ("S004", "Diana Cole", "diana@miva.edu", "2003-05-09"),
    ("S005", "Ethan Ward", "ethan@miva.edu", "2002-11-30"),
    ("S006", "Fiona Lane", "fiona@miva.edu", "2001-09-18"),
    ("S007", "George Hill", "george@miva.edu", "2000-12-01"),
    ("S008", "Hannah Scott", "hannah@miva.edu", "2003-02-14"),
    ("S009", "Ian Brooks", "ian@miva.edu", "2002-06-25"),
    ("S010", "Julia West", "julia@miva.edu", "2001-08-08"),
    ("S011", "Kevin Young", "kevin@miva.edu", "2000-04-19"),
    ("S012", "Laura Price", "laura@miva.edu", "2003-10-03"),
    ("S013", "Michael Stone", "michael@miva.edu", "2002-07-27"),
    ("S014", "Nina Ford", "nina@miva.edu", "2001-01-16"),
    ("S015", "Oscar Bell", "oscar@miva.edu", "2000-09-05"),
    ("S016", "Paula Grey", "paula@miva.edu", "2003-03-11"),
    ("S017", "Quinn Hayes", "quinn@miva.edu", "2002-12-20"),
    ("S018", "Ryan Cooper", "ryan@miva.edu", "2001-05-28"),
    ("S019", "Sara Mitchell", "sara@miva.edu", "2000-08-13"),
    ("S020", "Tom Rivera", "tom@miva.edu", "2003-06-07"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO Student VALUES (?, ?, ?, ?)",
    students
)

# --- Insert Courses (20) ---
courses = [
    ("CSC301", "Database Systems", 3, "Computer Science", "I001"),
    ("CSC302", "Data Structures", 3, "Computer Science", "I002"),
    ("CSC303", "Operating Systems", 3, "Computer Science", "I001"),
    ("CSC304", "Computer Networks", 3, "Computer Science", "I002"),
    ("IT201", "Python Programming", 3, "Information Technology", "I003"),
    ("IT202", "Data Security", 3, "Information Technology", "I004"),
    ("IT203", "Web Development", 3, "Information Technology", "I003"),
    ("MTH101", "Calculus I", 3, "Mathematics", "I005"),
    ("MTH102", "Linear Algebra", 3, "Mathematics", "I006"),
    ("BUS201", "Business Management", 2, "Business", "I007"),
    ("BUS202", "Accounting Basics", 2, "Business", "I008"),
    ("EDU101", "Teaching Methods", 2, "Education", "I009"),
    ("EDU102", "Curriculum Design", 2, "Education", "I010"),
    ("ENG201", "Engineering Drawing", 3, "Engineering", "I011"),
    ("ENG202", "Mechanics", 3, "Engineering", "I012"),
    ("LAW101", "Introduction to Law", 2, "Law", "I013"),
    ("LAW102", "Constitutional Law", 3, "Law", "I014"),
    ("HSC201", "Public Health", 2, "Health Sciences", "I015"),
    ("ART101", "Fine Arts", 2, "Arts", "I017"),
    ("ECO201", "Microeconomics", 3, "Economics", "I019"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO Course VALUES (?, ?, ?, ?, ?)",
    courses
)

# --- Insert Enrollments (20+) ---
enrollments = [
    ("S001", "CSC301"), ("S001", "CSC302"), ("S001", "IT201"),
    ("S002", "CSC301"), ("S002", "IT202"), ("S002", "MTH101"),
    ("S003", "CSC301"), ("S003", "BUS201"), ("S003", "ECO201"),
    ("S004", "CSC302"), ("S004", "IT203"), ("S004", "ART101"),
    ("S005", "CSC303"), ("S005", "CSC304"), ("S005", "ENG201"),
    ("S006", "IT201"), ("S006", "IT202"), ("S006", "MTH102"),
    ("S007", "BUS201"), ("S007", "BUS202"), ("S007", "ECO201"),
    ("S008", "EDU101"), ("S008", "EDU102"), ("S008", "ART101"),
    ("S009", "CSC301"), ("S009", "LAW101"),
    ("S010", "HSC201"), ("S010", "CSC302"),
    ("S011", "ENG202"), ("S011", "MTH101"),
    ("S012", "LAW102"), ("S012", "BUS201"),
    ("S013", "CSC304"), ("S013", "IT203"),
    ("S014", "CSC301"), ("S014", "EDU101"),
    ("S015", "ECO201"), ("S015", "MTH102"),
    ("S016", "ART101"), ("S016", "HSC201"),
    ("S017", "CSC303"), ("S017", "IT201"),
    ("S018", "BUS202"), ("S018", "LAW101"),
    ("S019", "ENG201"), ("S019", "CSC302"),
    ("S020", "CSC301"), ("S020", "IT202"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO Enrollment VALUES (?, ?)",
    enrollments
)

conn.commit()
print("Tables created and data inserted successfully.")

print("\n--- a) Students and their enrolled courses ---")
cursor.execute("""
SELECT Student.name, Course.title
FROM Student
JOIN Enrollment ON Student.student_id = Enrollment.student_id
JOIN Course ON Enrollment.course_code = Course.course_code
ORDER BY Student.name
""")
for row in cursor.fetchall():
    print(row)

print("\n--- b) Instructor teaching Database Systems ---")
cursor.execute("""
SELECT Instructor.name, Instructor.department, Instructor.phone_number
FROM Course
JOIN Instructor ON Course.instructor_id = Instructor.instructor_id
WHERE Course.title = 'Database Systems'
""")
for row in cursor.fetchall():
    print(row)

print("\n--- c) Number of students in each course ---")
cursor.execute("""
SELECT Course.title, COUNT(Enrollment.student_id) AS student_count
FROM Course
LEFT JOIN Enrollment ON Course.course_code = Enrollment.course_code
GROUP BY Course.course_code, Course.title
ORDER BY student_count DESC
""")
for row in cursor.fetchall():
    print(row)
conn.close()