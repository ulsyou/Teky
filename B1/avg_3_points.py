ten = input("Nhập tên học sinh: ")
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))

tong_diem = toan + van + anh
diem_trung_binh = tong_diem / 3

print("Tổng điểm của " + ten + " là", tong_diem)
print("Điểm trung bình của " + ten + f" là: {diem_trung_binh:.2f}")

