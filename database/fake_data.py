from database.data_models import Discount, DiscountType, Product, BrandTier, CartItem
from decimal import Decimal
from database.gloabl_data import all_discounts, all_products
from database.crud import add_multiple_discounts, add_multiple_products

discounts = [
    Discount(
        id="d1f518ff-41e7-4297-8155-fd3bc12c4f54",
        discount_type=DiscountType.BRAND,
        value=Decimal("0.40"),  
        brand="PUMA"
    ),
    
    Discount(
        id="05c4f544-429f-4767-925e-1279064a8306",
        discount_type=DiscountType.CATEGORY,
        value=Decimal("0.10"),  
        category="T-shirts"
    ),
    
    Discount(
        id="e73d055c-e822-43e9-acf0-3d219644365f",
        discount_type=DiscountType.BANK,
        value=Decimal("0.10"),  
        bank_name="ICICI"
    ),

    Discount(
        id="046f53d4-05d6-4646-a5e0-be1a54b4ef18",
        discount_type=DiscountType.VOUCHER,
        value=Decimal("0.69"),  
        voucher_code="SUPER69"
    )

]

add_multiple_discounts(disounts=discounts)

products = [
    Product(
        id="752b11c1-7656-4044-b27b-1d9a75ba0c52",
        brand="PUMA",
        brand_tier=BrandTier.REGULAR,
        category="T-shirts",
        base_price=1000,
        current_price=1000
    )
]

def add_all_dummy_data():
    add_multiple_products(products=products)

