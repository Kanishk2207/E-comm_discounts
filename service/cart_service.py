from database.gloabl_data import all_products, all_cart_items
from database.crud import add_cart_item
from database.data_models import CartItem

def add_product_to_cart(product_id: str, quantity: int ,size: str):
    global all_products
    found_product = True
    try:
        for product in all_products:
            if product.id == product_id:
                found_product = False
                cart_item = CartItem(
                    product=product,
                    size=size,
                    quantity=quantity
                )

                add_cart_item(cart_item=cart_item)

        if found_product:
            print("Could not find the product with the entered ID, please enter correct product ID")

    except Exception as ex:
        print(f"error in adding product to cart, please try again later {ex}")
        # Normally we send a HTTP exeption to the response json

def get_cart_items():
        for key, value in all_cart_items.items():
            if key == "products":
                for product in value:
                    cart_item_dict = product.dict()
                    for key, value in cart_item_dict.items():
                        print(f"{key}: {value}")
                    print() 
                continue
            print(f"{key}: {value}")
        print()