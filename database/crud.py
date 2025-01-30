import json
from decimal import Decimal
from database.data_models import Discount, Product, CartItem, PaymentInfo
from database.gloabl_data import all_discounts, all_products, all_cart_items, all_payment_info, all_discounts_applied


def add_discount(discount: Discount):
    """
    Adds a single discount to the global discount list.

    Parameters:
        discount (Discount): The discount object to be added.
    
    Updates:
        - Appends the discount to the global discount list.
    """
    global all_discounts
    all_discounts.append(discount)

def add_multiple_discounts(disounts: list[Discount]):
    """
    Adds multiple discounts to the global discount list.

    Parameters:
        discounts (list[Discount]): A list of discount objects to be added.

    Updates:
        - Extends the global discount list with the given discounts.
    """
    global all_discounts
    all_discounts.extend(disounts)

def add_product(product: Product):
    """
    Adds a single product to the global product list.

    Parameters:
        product (Product): The product object to be added.

    Updates:
        - Appends the product to the global product list.
    """
    global all_products
    all_products.append(product)

def get_all_product():
    """
    Retrieves and displays all stored products.

    Outputs:
        - Prints product details including ID, brand, category, base price, and current price.
    """
    global all_products
    for product in all_products:
        product_dict = product.dict()
        for key, value in product_dict.items():
            print(f"{key}: {value}")
        print() 

def add_multiple_products(products: list[Product]):
    """
    Adds multiple products to the global product list.

    Parameters:
        products (list[Product]): A list of product objects to be added.

    Updates:
        - Extends the global product list with the given products.
    """
    global all_products
    all_products.extend(products)

def add_cart_item(cart_item: CartItem):
    """
    Adds an item to the cart and recalculates total and discounted cart values.

    Parameters:
        cart_item (CartItem): The cart item object containing product, quantity, and size.

    Updates:
        - Appends the cart item to the global cart.
        - Recalculates total cart value and discounted cart value.
        - Applies any available discounts to the item.
    """
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
    """
    Adds multiple cart items to the global cart.

    Parameters:
        cart_items (list[CartItem]): A list of cart item objects to be added.

    Updates:
        - Extends the global cart list with the given cart items.
    """
    global all_cart_items
    all_cart_items.extend(cart_items)

def add_payment_info(payment_info: PaymentInfo):
    """
    Adds payment information and links it to the cart.

    Parameters:
        payment_info (PaymentInfo): The payment information object to be added.

    Updates:
        - Appends the payment info to the global payment list.
        - Stores the payment info in the cart for discount validation.
    """
    global all_payment_info
    all_payment_info.append(payment_info)
    all_cart_items["payment_info"] = payment_info
    