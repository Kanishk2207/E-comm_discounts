from database.gloabl_data import all_discounts
from database.data_models import DiscountType
from database.gloabl_data import all_cart_items
from utils import apply_discount

def validate_discount_voucher(voucher_code: str):
    """Validate discount Voucher

    Args:
        voucher_code (str): _description_

    Returns:
        _type_: _description_
    """
    for discount in all_discounts:
        if discount.discount_type == DiscountType.VOUCHER and discount.voucher_code == voucher_code:
            return True
    
    return False

def apply_discount_voucher(voucher_code: str):
    for discount in all_discounts:
        if discount.discount_type == DiscountType.VOUCHER and discount.voucher_code == voucher_code:
            discounted_cart_price = all_cart_items.get("discounted_cart_value")
            discount = apply_discount(discounted_cart_price, discount.value)
            all_cart_items["discounted_cart_value"] = discount
            if "discounts" not in all_cart_items:
                all_cart_items["discounts"] = []
            all_cart_items["discounts"].append({DiscountType.VOUCHER.value:(discounted_cart_price - discount)})

def validate_payment_method_discount(bank_name: str):
    if "payment_info" not in all_cart_items:
        print("Please add payment method to access discount.")
    
    bank_name = all_cart_items.get("payment_info").bank_name

    for discount in all_discounts:
        if discount.discount_type == DiscountType.BANK and discount.bank_name.lower() == bank_name.lower():
            discounted_cart_price = all_cart_items.get("discounted_cart_value")
            discount = apply_discount(discounted_cart_price, discount.value)
            all_cart_items["discounted_cart_value"] = discount
            if "discounts" not in all_cart_items:
                all_cart_items["discounts"] = []
            all_cart_items["discounts"].append({DiscountType.BANK.value:(discounted_cart_price - discount)})