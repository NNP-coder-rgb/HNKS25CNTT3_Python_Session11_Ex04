# 1. Phân tích Input / Output
# Dữ liệu đầu vào (Input):
# Danh sách sản phẩm mặc định product_list chứa các dictionary gồm các key: product_id, product_name, price, quantity, sold.
# Lựa chọn tính năng từ bàn phím (option).
# Mã sản phẩm cần tương tác và số lượng mua/nhập kho do người dùng nhập vào.
# Dữ liệu đầu ra (Output):
# Danh sách sản phẩm hiển thị kèm Trạng thái (Còn hàng / Sắp hết hàng / Hết hàng) dựa theo số lượng tồn kho.
# Báo cáo tổng doanh thu và sản phẩm có số lượng bán ra cao nhất.
# Các câu thông báo lỗi hoặc thông báo thành công cho từng trường hợp nghiệp vụ.
# Khởi tạo danh sách sản phẩm ban đầu của cửa hàng thời trang Yody

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

option = 0
found = False

while option != 5:
    print()
    print('===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====')
    print('1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho')
    print('2. Bán sản phẩm cho khách hàng')
    print('3. Nhập thêm hàng vào kho')
    print('4. Xem báo cáo doanh thu')
    print('5. Thoát chương trình')
    
    option = int(input('Nhập lựa chọn của bạn (1-5): '))
        
    match option:
        case 1:
            print()
            if product_list == []:
                print('Danh sách sản phẩm hiện đang trống.')
            else:
                print('Danh sách sản phẩm hiện tại: ')
                for i, item in enumerate(product_list, start = 1):
                    if item["quantity"] == 0:
                        status = "Hết hàng"
                    elif item["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"

                    print(f'{i}. Mã SP: {item["product_id"]} | Tên: {item["product_name"]} | '
                          f'Giá: {item["price"]} | Tồn kho: {item["quantity"]} | '
                          f'Đã bán: {item["sold"]} | Trạng thái: {status}')
            print()
            
        case 2:
            print()
            found = False 
            input_id_search = input('Nhập mã sản phẩm khách muốn mua: ').strip().upper()
            
            for item in product_list:
                if input_id_search == item['product_id']:
                    found = True 
                    
                    input_quantity = input('Nhập số lượng khách mua: ').strip()
                    if not input_quantity.isdigit() or int(input_quantity) <= 0:
                        print('Số lượng mua không hợp lệ')
                    else:
                        input_quantity = int(input_quantity)
                        if input_quantity > item['quantity']:
                            print('Số lượng trong kho không đủ để bán')
                        else:
                            item['quantity'] -= sell_qty
                            item['sold'] += sell_qty
                            total_pay = item['price'] * sell_qty
                            print(f'Bán hàng thành công! Số tiền khách cần thanh toán: {total_pay} VND')
                    break 

            if found == False:
                print('Không tìm thấy sản phẩm cần bán')
            print()
            
        case 3:
            print()
            found = False 
            input_id_search = input('Nhập mã sản phẩm cần nhập thêm: ').strip().upper()
            
            for item in product_list:
                if input_id_search == item['product_id']:
                    found = True
                    
                    input_qty_str = input('Nhập số lượng nhập thêm: ').strip()
                    if not input_qty_str.isdigit() or int(input_qty_str) <= 0:
                        print('Số lượng Nhập kho không hợp lệ')
                    else:
                        import_qty = int(input_qty_str)
                        item['quantity'] += import_qty
                        print(f'Nhập thêm hàng thành công! Tồn kho mới của {item["product_name"]} là: {item["quantity"]}')
                    break 
                    
            if found == False:
                print('Không tìm thấy sản phẩm cần Nhập kho')
            print()
            
        case 4:
            print()
            total_sold_units = sum(item['sold'] for item in product_list)
        
            if total_sold_units == 0:
                print('Chưa có doanh thu phát sinh.')
            else:
                print('===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====')
                total_revenue = 0 
                max_sold = -1     
                best_seller_name = "" 
                
                for i, item in enumerate(product_list, start = 1):
                    total_revenue += item_revenue 
                    
                    print(f'{i}. {item["product_name"]} | Đã bán: {item["sold"]} | Doanh thu: {item_revenue}')
                    
                    if item['sold'] > max_sold:
                        max_sold = item['sold'] 
                        best_seller_name = item['product_name'] 
                        
                print(f'\nTổng doanh thu: {total_revenue}')
                print(f'Sản phẩm bán chạy nhất: {best_seller_name}')
            print()
            
        case 5:
            print('Thoát chương trình.')
            
        case _:
            print('"Lựa chọn không hợp lệ", vui lòng nhập lại!')
