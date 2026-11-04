import sqlite3

conn = sqlite3.connect("employee_training.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    Employee_ID INTEGER PRIMARY KEY,
    Employee_Name TEXT NOT NULL,
    Department TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Instructor (
    Instructor TEXT PRIMARY KEY,
    Training_Location TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    Course_Title TEXT PRIMARY KEY,
    Course_Date TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Teaches (
    Instructor TEXT PRIMARY KEY,
    Course_Title TEXT NOT NULL,
    FOREIGN KEY (Instructor) REFERENCES Instructor(Instructor),
    FOREIGN KEY (Course_Title) REFERENCES Course(Course_Title)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    Employee_ID INTEGER NOT NULL,
    Course_Title TEXT NOT NULL,
    PRIMARY KEY (Employee_ID, Course_Title),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID),
    FOREIGN KEY (Course_Title) REFERENCES Course(Course_Title)
)
""")

conn.commit()
print("Final normalized tables created successfully.")
conn.close()