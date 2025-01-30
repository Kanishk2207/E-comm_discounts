from database.gloabl_data import all_products, all_cart_items
from database.crud import add_cart_item
from database.data_models import CartItem

def add_product_to_cart(product_id: str, quantity: int ,size: str):
    """
    Adds a product to the cart if the product ID exists in the product list.

    Parameters:
        product_id (str): The unique identifier of the product to be added.
        quantity (int): The quantity of the product to add to the cart.
        size (str): The size variant of the product (if applicable).

    Updates:
        - Adds the product to the cart if it exists.
        - Displays an error message if the product ID is not found.
        - Handles exceptions gracefully and prints an error message in case of failure.
    """
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
    """
    Retrieves and displays all items in the cart, including product details and cart totals.

    Outputs:
        - Prints details of each product in the cart.
        - Prints the total cart value and discounted cart value.
    """
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