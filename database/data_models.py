from pydantic import BaseModel, model_validator, field_validator
from typing import List, Optional, Dict
from decimal import Decimal
from enum import Enum
from datetime import datetime
from database.gloabl_data import all_discounts, all_discounts_applied
from utils import apply_discount

class BrandTier(Enum):
   PREMIUM = "premium"
   REGULAR = "regular"
   BUDGET = "budget"

class DiscountType(Enum):
    BRAND = "brand"
    CATEGORY = "category"
    VOUCHER = "voucher"
    BANK = "bank"

class Discount(BaseModel):
    id: str
    discount_type: DiscountType 
    value: Decimal 
    brand: Optional[str] = None
    category: Optional[str] = None
    voucher_code: Optional[str] = None
    bank_name: Optional[str] = None

class Product(BaseModel):
    id: str
    brand: str
    brand_tier: BrandTier
    category: str
    base_price: Decimal
    current_price: Decimal

    @model_validator(mode="before")
    def apply_discounts(cls, values):
        """Automatically apply brand and category discounts to current_price."""
        base_price = values.get("base_price")
        if base_price is None:
            raise ValueError("Base price is required.")
        
        brand = values.get("brand")
        category = values.get("category")
        id = values.get("id")

        discount_percentage = Decimal("0.0")

        global all_discounts_applied

        if id not in all_discounts_applied:
            all_discounts_applied[id] = []
        
        # Apply global all_discounts here
        for discount in all_discounts:
            if discount.discount_type == DiscountType.BRAND and discount.brand == brand:
                discount_percentage += discount.value  # Apply brand discount
                discount_price = DiscountedPrice(
                    original_price=base_price,
                    final_price=apply_discount(base_price, discount.value),
                    applied_discounts={DiscountType.BRAND:(base_price-(base_price * (Decimal("1.0") - discount.value)))},
                    message="this is message"
                )

                all_discounts_applied[id].append(discount_price)

            if discount.discount_type == DiscountType.CATEGORY and discount.category == category:
                discount_percentage += discount.value  # Apply category discount
                discount_price = DiscountedPrice(
                    original_price=base_price,
                    final_price=apply_discount(base_price, discount.value),
                    applied_discounts={DiscountType.CATEGORY:(base_price-apply_discount(base_price, discount.value))},
                    message="this is message"
                )

                all_discounts_applied[id].append(discount_price)

        # Ensure discount does not exceed 100%
        discount_percentage = min(discount_percentage, Decimal("1.0"))

        # Calculate the final price
        values["current_price"] = apply_discount(base_price, discount_percentage)

        return values

class CartItem(BaseModel):
   product: Product
   quantity: int
   size: str


class PaymentInfo(BaseModel):
   method: str  # CARD, UPI, etc
   bank_name: Optional[str]
   card_type: Optional[str]  # CREDIT, DEBIT

class DiscountedPrice(BaseModel):
   original_price: Decimal
   final_price: Decimal
   applied_discounts: Dict[str, Decimal]  # discount_name -> amount
   message: Optional[str]
