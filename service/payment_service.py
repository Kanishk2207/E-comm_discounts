from database.data_models import PaymentInfo
from database.gloabl_data import all_payment_info
from database.crud import add_payment_info

def post_payment_info(method: str, bank_name: str = "", card_type: str = ""):
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
    global all_payment_info
    for payment_info in all_payment_info:
            payment_info_dict = payment_info.dict()
            for key, value in payment_info_dict.items():
                print(f"{key}: {value}")
            print() 