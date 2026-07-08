"""
1.Khi gọi GET /products/1 API trả về 404 Not Found vì :
    @app.get("/products/product_id")
        FastAPI hiểu "product_id" là chuỗi cố định, nên chỉ tồn tại endpoint:
            GET /products/product_id
2.Dòng code đang khai báo sai Path Parameter là :@app.get("/products/product_id")
3./products/product_id không phải là Path Parameter vì :Path Parameter trong FastAPI phải được đặt trong dấu ngoặc nhọn {}
4. Endpoint đúng cần sửa thành :@app.get("/products/{product_id}")
"""

from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop Dell", "price": 15000000},
    {"id": 2, "name": "Chuột Logitech", "price": 350000},
    {"id": 3, "name": "Bàn phím cơ", "price": 1200000}
]


@app.get("/products/{product_id}")
def get_product_detail(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": "Không tìm thấy sản phẩm"
    }
  
