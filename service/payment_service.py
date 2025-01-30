from database.data_models import PaymentInfo
from database.gloabl_data import all_payment_info
from database.crud import add_payment_info

def post_payment_info(method: str, bank_name: str = "", card_type: str = ""):
    """
    Stores payment information in the system.

    Parameters:
        method (str): The payment method (e.g., Credit Card, Debit Card, UPI, etc.).
        bank_name (str, optional): The name of the bank (default is an empty string).
        card_type (str, optional): The type of card (e.g., Visa, Mastercard, default is an empty string).

    Updates:
        - Creates a new PaymentInfo object.
        - Adds the payment information to the global storage.

    Exceptions:
        - Catches and prints an error message if adding payment info fails.
    """
    try:
        global all_payment_info
        payment_info = PaymentInfo(
            method=method,
            bank_name=bank_name,
            card_type=card_type
        )

        add_payment_info(payment_info=payment_info)

    except Exception as ex:
        print(f"error in adding payment info, please try again later {ex}")

def get_payment_info():
    """
    Retrieves and displays all stored payment information.

    Outputs:
        - Prints the details of each stored payment method, including method, bank name, and card type.
    """
    global all_payment_info
    for payment_info in all_payment_info:
            payment_info_dict = payment_info.dict()
            for key, value in payment_info_dict.items():
                print(f"{key}: {value}")
            print() 