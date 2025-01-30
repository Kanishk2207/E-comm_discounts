from database.crud import get_all_product
from database.fake_data import add_all_dummy_data
from service.cart_service import add_product_to_cart, get_cart_items
from service.payment_service import post_payment_info, get_payment_info
from service.discount_service import validate_discount_voucher, apply_discount_voucher, validate_payment_method_discount
from database.gloabl_data import all_discounts_applied

if __name__ == "__main__":

    add_all_dummy_data()

    while True:
        print("""Hello, Welcome to E-com CLI, Please choose one of the above options:
            1. List all products
            2. Add item in the cart
            3. Show your cart details
            4. Add discount vouchers
            5. Add Payment Method
            9. Exit
              """)
        input_value = input("Please enter your choice: ").strip()

        match input_value:
            case "1":
                get_all_product()
                # print("These are discounts: \n \n",all_discounts_applied)

            case "2":

                    print(f"""
                    Please enter the details of the product you want to add to cart
                    """)

                    product_id = input("Please enter ID: ").strip()
                    quantity = int(input("Please enter quantity of the product: ").strip())
                    size = input("Please enter size of the product: ").strip()

                    add_product_to_cart(product_id=product_id, quantity=quantity, size=size)

                    print("Product added to cart successfully")

            case "3":
                print("cart items: \n")
                get_cart_items()
            
            case "4":
                print("""
                    Please enter the voucher code:
                    """)
                voucher_code = input("Enter code here: ").strip()

                if validate_discount_voucher(voucher_code=voucher_code):
                    apply_discount_voucher(voucher_code=voucher_code)

            case "5":

                print(f"""
                    Please enter the details of the payment method you want to add to cart, leave blank for not appliable fields
                    """)

                method = input("Please enter payment method: ").strip()
                bank_name=""
                bank_name=""
                if method.lower != "upi":
                    bank_name = input("Please enter bank name: ").strip()
                    card_type = input("Please enter card type: ").strip()

                post_payment_info(method=method, bank_name=bank_name.lower(), card_type=card_type.lower())
                validate_payment_method_discount(bank_name=bank_name)
            
            case "9":
                print("Closing app gracefully")
                break
            
            case _:
                print("Please enter valid input")
        