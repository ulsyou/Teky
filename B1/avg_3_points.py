print("="*40)
print("Chương trình tính điểm trung bình".center(40))
print("="*40)

ten = input("Nhập tên học sinh: ")
print("-"*40)
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))
print("-"*40)

tong_diem = toan + van + anh
diem_trung_binh = tong_diem / 3

print(f"Tổng điểm của {ten} là: {tong_diem}")
print(f"Điểm trung bình của {ten} là: {diem_trung_binh:.2f}")

print("="*40)
print("Kết thúc chương trình".center(40))
print("="*40)
