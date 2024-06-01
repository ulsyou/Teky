danh_ba = []

while True:
    print("\n--- Quản lý danh bạ điện thoại ---")
    print("1. Hiển thị danh bạ")
    print("2. Thêm liên hệ mới")
    print("3. Sửa liên hệ")
    print("4. Xóa liên hệ")
    print("5. Thoát")

    lua_chon = input("Nhập lựa chọn (1-5): ")

    if lua_chon == "1":
        print("Danh bạ điện thoại:")
        if not danh_ba:
            print("Danh bạ trống.")
        else:
            for ten, sdt in danh_ba:
                print(f"{ten}: {sdt}")

    elif lua_chon == "2":
        ten = input("Nhập tên: ")
        ten_xu_ly = ""
        dau_cach = True
        for char in ten:
            if char == " ":
                ten_xu_ly += char
                dau_cach = True
            else:
                if dau_cach:
                    ten_xu_ly += char.upper()
                    dau_cach = False
                else:
                    ten_xu_ly += char.lower()
        sdt = input("Nhập số điện thoại: ")
        danh_ba.append((ten_xu_ly, sdt))
        print("Đã thêm liên hệ mới.")

    elif lua_chon == "3":
        # Sửa liên hệ
        ten = input("Nhập tên liên hệ cần sửa: ")
        sua_thanh_cong = False
        for i, (t, sdt) in enumerate(danh_ba):
            if t.lower() == ten.lower():
                sdt_moi = input("Nhập số điện thoại mới: ")
                danh_ba[i] = (t, sdt_moi)
                sua_thanh_cong = True
                print("Đã sửa liên hệ.")
                break
        if not sua_thanh_cong:
            print("Không tìm thấy liên hệ.")

    elif lua_chon == "4":
        ten = input("Nhập tên liên hệ cần xóa: ")
        xoa_thanh_cong = False
        for i, (t, sdt) in enumerate(danh_ba):
            if t.lower() == ten.lower():
                del danh_ba[i]
                xoa_thanh_cong = True
                print("Đã xóa liên hệ.")
                break
        if not xoa_thanh_cong:
            print("Không tìm thấy liên hệ.")

    elif lua_chon == "5":
        print("Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
