import os

class Student:
    def __init__(self, name, student_id, math_grade, literature_grade, english_grade):
        self.name = name
        self.student_id = student_id
        self.math_grade = math_grade
        self.literature_grade = literature_grade
        self.english_grade = english_grade

    def calculate_weighted_average(self, math_weight, literature_weight, english_weight):
        total_weight = math_weight + literature_weight + english_weight
        weighted_average = (
            (self.math_grade * math_weight) +
            (self.literature_grade * literature_weight) +
            (self.english_grade * english_weight)
        ) / total_weight
        return weighted_average

class ClassRoom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Học sinh {student.name} đã được xóa khỏi lớp {self.class_name}.")
                return
        print(f"Không tìm thấy học sinh có mã số {student_id} trong lớp {self.class_name}.")

    def update_student_grades(self, student_id, math_grade, literature_grade, english_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.math_grade = math_grade
                student.literature_grade = literature_grade
                student.english_grade = english_grade
                print(f"Điểm của học sinh {student.name} đã được cập nhật.")
                return
        print(f"Không tìm thấy học sinh có mã số {student_id} trong lớp {self.class_name}.")

    def print_students(self):
        print(f"Danh sách học sinh lớp {self.class_name}:")
        for student in self.students:
            print(f"Tên: {student.name}, Mã số: {student.student_id}, Toán: {student.math_grade}, Văn: {student.literature_grade}, Anh: {student.english_grade}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for student in self.students:
                file.write(f"{student.name},{student.student_id},{student.math_grade},{student.literature_grade},{student.english_grade}\n")
        print(f"Dữ liệu đã được lưu vào file {filename}.")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.students = []
                for line in file:
                    name, student_id, math_grade, literature_grade, english_grade = line.strip().split(',')
                    student = Student(name, student_id, float(math_grade), float(literature_grade), float(english_grade))
                    self.students.append(student)
            print(f"Dữ liệu đã được đọc từ file {filename}.")
        else:
            print(f"Không tìm thấy file {filename}.")

def print_menu():
    print("=============== Menu ===============")
    print("1. Thêm học sinh")
    print("2. Xóa học sinh")
    print("3. Cập nhật điểm học sinh")
    print("4. In danh sách học sinh")
    print("5. Lưu dữ liệu vào file")
    print("6. Đọc dữ liệu từ file")
    print("7. Tính điểm trung bình theo trọng số cho từng học sinh")
    print("0. Thoát")
    print("====================================")

def main():
    classroom = ClassRoom("Lớp A")

    while True:
        print_menu()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            name = input("Nhập tên học sinh: ")
            student_id = input("Nhập mã số học sinh: ")
            math_grade = float(input("Nhập điểm Toán: "))
            literature_grade = float(input("Nhập điểm Văn: "))
            english_grade = float(input("Nhập điểm Anh: "))
            student = Student(name, student_id, math_grade, literature_grade, english_grade)
            classroom.add_student(student)
            print("Học sinh đã được thêm vào lớp.")

        elif choice == '2':
            student_id = input("Nhập mã số học sinh cần xóa: ")
            classroom.remove_student(student_id)

        elif choice == '3':
            student_id = input("Nhập mã số học sinh cần cập nhật điểm: ")
            math_grade = float(input("Nhập điểm Toán mới: "))
            literature_grade = float(input("Nhập điểm Văn mới: "))
            english_grade = float(input("Nhập điểm Anh mới: "))
            classroom.update_student_grades(student_id, math_grade, literature_grade, english_grade)

        elif choice == '4':
            classroom.print_students()

        elif choice == '5':
            filename = input("Nhập tên file để lưu dữ liệu: ")
            classroom.save_to_file(filename)

        elif choice == '6':
            filename = input("Nhập tên file để đọc dữ liệu: ")
            classroom.load_from_file(filename)

        elif choice == '7':
            math_weight = float(input("Nhập trọng số cho môn Toán: "))
            literature_weight = float(input("Nhập trọng số cho môn Văn: "))
            english_weight = float(input("Nhập trọng số cho môn Anh: "))
            print("Điểm trung bình theo trọng số của các học sinh:")
            for student in classroom.students:
                weighted_average = student.calculate_weighted_average(math_weight, literature_weight, english_weight)
                print(f"{student.name}: {weighted_average}")

        elif choice == '0':
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()