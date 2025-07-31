
import sqlite3

class StudentDB:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_student(self, name, age, email):
        try:
            self.conn.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", (name, age, email))
            self.conn.commit()
            print("✅ Student added successfully.")
        except Exception as e:
            print("❌ Error:", e)

    def view_students(self):
        cursor = self.conn.execute("SELECT * FROM students")
        for row in cursor:
            print(row)

    def search_student(self, student_id):
        cursor = self.conn.execute("SELECT * FROM students WHERE id=?", (student_id,))
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            print("❌ Student not found.")

    def update_student(self, student_id, name, age, email):
        self.conn.execute("UPDATE students SET name=?, age=?, email=? WHERE id=?", (name, age, email, student_id))
        self.conn.commit()
        print("✅ Student updated.")

    def delete_student(self, student_id):
        self.conn.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()
        print("✅ Student deleted.")

def main():
    db = StudentDB()
    while True:
        print("\n1. Add\n2. View All\n3. Search\n4. Update\n5. Delete\n6. Exit")
        choice = input("Choose: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            email = input("Email: ")
            db.add_student(name, age, email)

        elif choice == '2':
            db.view_students()

        elif choice == '3':
            sid = int(input("Enter ID: "))
            db.search_student(sid)

        elif choice == '4':
            sid = int(input("Enter ID: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            email = input("New Email: ")
            db.update_student(sid, name, age, email)

        elif choice == '5':
            sid = int(input("Enter ID to delete: "))
            db.delete_student(sid)

        elif choice == '6':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == '__main__':
    main()
