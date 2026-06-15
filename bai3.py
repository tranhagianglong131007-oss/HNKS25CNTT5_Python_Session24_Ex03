class MemberCard:
    # Class Attribute
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    # Getter cho points
    @property
    def points(self):
        return self.__points

    # Getter cho tier
    @property
    def tier(self):
        return self.__tier

    # Instance Method: Tích điểm
    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned
        print(f"Khách hàng: {self.name}")
        print(f"Hóa đơn: {bill_amount:,} VNĐ")
        print(f"Số điểm được tích: {earned}")
        print(f"Tổng điểm hiện tại: {self.__points}")
        if self.__points >= 100 and self.__tier == "Standard":
            self.__tier = "VIP"
            print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    # Instance Method: Đổi điểm
    def redeem_points(self, points_to_use):
        if points_to_use <= 0 or points_to_use > self.__points:
            print("\nKhông thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {self.__points}")
            print("Điểm cũ được giữ nguyên:")
            print(f"Số điểm sau giao dịch: {self.__points}")
        else:
            self.__points -= points_to_use
            discount = points_to_use * MemberCard.point_value_vnd
            print(f"\nĐã trừ {points_to_use} điểm.")
            print(f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!")
            print(f"Số điểm còn lại: {self.__points}")
            print(f"Hạng thẻ hiện tại: {self.__tier}")

    # Class Method: Cập nhật tỷ giá
    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value
        print("\nCập nhật tỷ giá thành công!")
        print(f"Tỷ giá mới: 1 điểm = {cls.point_value_vnd:,} VNĐ")

    # Static Method: Kiểm tra mã thẻ
    @staticmethod
    def is_valid_card_id(card_id):
        return (len(card_id) == 4 and
                card_id.startswith("RC") and
                card_id[2:].isdigit())


# ================= MAIN FLOW =================
cards_database = [
    MemberCard("RC01", "Nguyen Van A"),
    MemberCard("RC02", "Tran Thi B")
]
cards_database[0]._MemberCard__points = 150
cards_database[0]._MemberCard__tier = "VIP"
cards_database[1]._MemberCard__points = 20

while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
    print("6. Thoát chương trình")
    print("======================================================")

    choice = input("Chọn chức năng (1-6): ")

    match choice:
        case "1":
            print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
            for i, card in enumerate(cards_database, 1):
                print(f"{i}. Mã: {card.card_id} | Tên: {card.name:<15} | Điểm: {card.points} | Hạng: {card.tier}")

        case "2":
            print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
            card_id = input("Nhập mã thẻ: ").strip()
            if not MemberCard.is_valid_card_id(card_id):
                print("Mã thẻ không hợp lệ! Phải có dạng RCxx (xx là 2 chữ số).")
                continue

            # KHÔNG DÙNG any() NỮA
            duplicate = False
            for c in cards_database:
                if c.card_id == card_id:
                    duplicate = True
                    break

            if duplicate:
                print("Mã thẻ đã tồn tại trong hệ thống! Vui lòng kiểm tra lại.")
                continue

            name = input("Nhập tên khách hàng: ").strip()
            
            new_card = MemberCard(card_id, name)
            
            cards_database.append(new_card)
            
            print("Đăng ký thẻ thành viên thành công!")
            
            print(f"Mã thẻ: {new_card.card_id}")
            print(f"Tên khách hàng: {new_card.name}")
            print(f"Điểm ban đầu: {new_card.points}")
            print(f"Hạng thẻ: {new_card.tier}")

        case "3":
            print("--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
            
            card_id = input("Nhập mã thẻ: ").strip()
            card = None
            
            for c in cards_database:
                if c.card_id == card_id:
                    card = c
                    break
            if not card:
                
                print("Không tìm thấy mã thẻ trong hệ thống!")
                continue
            
            bill = int(input("Nhập tổng tiền hóa đơn: "))
            card.earn_points(bill)

        case "4":
            print("--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
            card_id = input("Nhập mã thẻ: ").strip()
            card = None
            
            for c in cards_database:
                if c.card_id == card_id:
                    card = c
                    break
                
            if not card:
                print("Không tìm thấy mã thẻ trong hệ thống!")
                continue
            
            points_to_use = int(input("Nhập số điểm muốn sử dụng: "))
            card.redeem_points(points_to_use)

        case "5":
            print("--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))
            MemberCard.update_point_value(new_value)

        case "6":
            print("Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-6.")
