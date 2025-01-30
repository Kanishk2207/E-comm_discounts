import json
from decimal import Decimal
from database.data_models import Discount, Product, CartItem, PaymentInfo
from database.gloabl_data import all_discounts, all_products, all_cart_items, all_payment_info, all_discounts_applied


def add_discount(discount: Discount):
    global all_discounts
    all_discounts.append(discount)

def add_multiple_discounts(disounts: list[Discount]):
    global all_discounts
    all_discounts.extend(disounts)

def add_product(product: Product):
    global all_products
    all_products.append(product)

def get_all_product():
    global all_products
    for product in all_products:
        product_dict = product.dict()
        for key, value in product_dict.items():
            print(f"{key}: {value}")
        print() 

def add_multiple_products(products: list[Product]):
    global all_products
    all_products.extend(products)

def add_cart_item(cart_item: CartItem):
    global all_cart_items

    # Add item to cart
    all_cart_items["products"].append(cart_item)

    # Recalculate total cart values
    base_total = Decimal("0.0")
    discounted_total = Decimal("0.0")

    for item in all_cart_items["products"]:
        base_total += item.product.base_price * item.quantity
        discounted_total += item.product.current_price * item.quantity

    all_cart_items["total_cart_value"] = base_total
    all_cart_items["discounted_cart_value"] = discounted_total

    if "discounts" not in all_cart_items:
        all_cart_items["discounts"] = []

    product_id = cart_item.product.id

    if product_id in all_discounts_applied:
        for discount in all_discounts_applied[product_id]:
            adjusted_discount = {key: value * item.quantity for key, value in discount.applied_discounts.items()}
            all_cart_items["discounts"].append(adjusted_discount)



def add_multiple_cart_items(cart_items: list[CartItem]):
    global all_cart_items
    all_cart_items.extend(cart_items)

def add_payment_info(payment_info: PaymentInfo):
    global all_payment_info
    all_payment_info.append(payment_info)
    all_cart_items["payment_info"] = payment_info
    