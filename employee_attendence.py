--Case Study: Employee Attendance Management System


def mark_attendance(attendance_records, employee_id, date, status):
    attendance_records.append((employee_id, date, status))
    print(f"Attendance marked for Employee {employee_id}: {status}")

def search_attendance(attendance_records, employee_id):
    print(f"\nSearching Attendance for Employee ID {employee_id}:")
    for record in attendance_records:
        if record[0] == employee_id:
            print(f"Date: {record[1]}, Status: {record[2]}")

def attendance_summary(attendance_records, employees):
    attendance_count = {emp[0]: {'Present': 0, 'Total': 0} for emp in employees}
    
    for record in attendance_records:
        emp_id, _, status = record
        attendance_count[emp_id]['Total'] += 1
        if status == "Present":
            attendance_count[emp_id]['Present'] += 1
    
    print("\nAttendance Summary:")
    for emp_id, emp_name, _ in employees:
        total_days = attendance_count[emp_id]['Total']
        present_days = attendance_count[emp_id]['Present']
        percentage = (present_days / total_days) * 100 if total_days > 0 else 0
        print(f"{emp_name}: {percentage:.2f}% Present")


attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Present"),
    (105, "2025-03-01", "Absent"),
]

employees = [
    (101, "Alice Johnson", "HR"),
    (102, "Bob Smith", "IT"),
    (103, "Charlie Brown", "Finance"),
    (104, "David White", "IT"),
    (105, "Eve Black", "Marketing")
]

mark_attendance(attendance_records, 102, "2025-03-02", "Present")
mark_attendance(attendance_records, 103, "2025-03-02", "Absent")

search_attendance(attendance_records, 102)

attendance_summary(attendance_records, employees)
-------------------------------------------------------------------------------

Output-
Attendance marked for Employee 102: Present
Attendance marked for Employee 103: Absent

Searching Attendance for Employee ID 102:
Date: 2025-03-01, Status: Absent
Date: 2025-03-02, Status: Present

Attendance Summary:
Alice Johnson: 100.00% Present
Bob Smith: 50.00% Present
Charlie Brown: 50.00% Present
David White: 100.00% Present
Eve Black: 0.00% Present
