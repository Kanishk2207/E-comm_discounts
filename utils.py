from decimal import Decimal


def apply_discount(price, discount_prcent) -> Decimal:
    return (price * (Decimal("1.0") - discount_prcent))