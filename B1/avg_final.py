print("="*40)
print("Chương trình tính điểm trung bình học kỳ".center(40))
print("="*40)

# Nhập tên học sinh
ten = input("Nhập tên học sinh: ")
mon_hoc = input("Nhập tên môn học: ")
print("-"*40)

# Hệ số các loại kiểm tra
he_so_kiem_tra_mieng = 1
he_so_kiem_tra_15_phut = 1
he_so_kiem_tra_1_tiet = 2
he_so_diem_cuoi_ki = 3

# Nhập điểm cho từng loại kiểm tra
kiem_tra_mieng = float(input("Nhập điểm kiểm tra miệng: "))
kiem_tra_15_phut = float(input("Nhập điểm kiểm tra 15 phút: "))
kiem_tra_1_tiet = float(input("Nhập điểm kiểm tra 1 tiết: "))
diem_cuoi_ki = float(input("Nhập điểm cuối kỳ: "))
print("-"*40)

# Tính tổng điểm và điểm trung bình
tong_diem = (kiem_tra_mieng * he_so_kiem_tra_mieng +
             kiem_tra_15_phut * he_so_kiem_tra_15_phut +
             kiem_tra_1_tiet * he_so_kiem_tra_1_tiet +
             diem_cuoi_ki * he_so_diem_cuoi_ki)

tong_he_so = (he_so_kiem_tra_mieng + he_so_kiem_tra_15_phut +
              he_so_kiem_tra_1_tiet + he_so_diem_cuoi_ki)

diem_trung_binh = tong_diem / tong_he_so

# In kết quả
print("="*40)
print(f"Kết quả học tập của {ten} cho môn {mon_hoc}".center(40))
print("="*40)
print(f"Tổng điểm của {ten} là: {tong_diem:.2f}")
print(f"Điểm trung bình của {ten} là: {diem_trung_binh:.2f}")
print("="*40)
print("Kết thúc chương trình".center(40))
print("="*40)
