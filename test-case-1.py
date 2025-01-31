import unittest
from decimal import Decimal

from database.data_models import Product, Discount, DiscountType, BrandTier, PaymentInfo
from database.gloabl_data import all_discounts, all_discounts_applied, all_cart_items

from database.crud import get_all_product
from database.fake_data import add_all_dummy_data
from service.cart_service import add_product_to_cart, get_cart_items
from service.payment_service import post_payment_info, get_payment_info
from service.discount_service import validate_discount_voucher, apply_discount_voucher, validate_payment_method_discount
from database.gloabl_data import all_discounts_applied

def setUpModule():
    """Setup test data before running tests"""
    add_all_dummy_data()

    print("Setup module completed")

class TestProductDiscount(unittest.TestCase):
    def test_discount_application(self):
        """Test if brand and category discounts apply correctly."""

        product = Product(
            id="p1",
            brand="PUMA",
            brand_tier=BrandTier.PREMIUM,
            category="T-shirts",
            base_price=Decimal("1000.00"),
            current_price=Decimal("1000.00")
        )
        
        # Check if discount is applied correctly
        expected_final_price = Decimal("1000.00") * (Decimal("1.0") - (Decimal("0.40") + Decimal("0.10")))
        self.assertEqual(product.current_price, expected_final_price)
        
        # Check if discounts are recorded in global tracking
        self.assertIn("p1", all_discounts_applied)
        self.assertTrue(len(all_discounts_applied["p1"]) > 0)

        
        # Check if discounts are recorded in global tracking
        self.assertIn("p1", all_discounts_applied)
        self.assertTrue(len(all_discounts_applied["p1"]) > 0)

    def test_multiple_discount_application(self):
        """Test if multiple discounts are applied correctly."""

        add_product_to_cart(product_id="752b11c1-7656-4044-b27b-1d9a75ba0c52", size="M", quantity=3)
        # Please refer to database/fake_data.py for dummy discounts and product implimentation
        
        # # Check if discount is applied correctly
        expected_final_price_after_brand_and_category_discount = (Decimal("1000.00") * (Decimal("1.0") - Decimal("0.40") - Decimal("0.10"))) * 3

        # self.assertEqual(discounted_cart_value, expected_final_price)
        
        payment_info = PaymentInfo(
            method="CARD",
            bank_name="ICICI",
            card_type="CREDIT"
        )

        post_payment_info(payment_info.method, payment_info.bank_name, payment_info.card_type)
        validate_payment_method_discount(bank_name=payment_info.bank_name)

        current_final_price = all_cart_items.get("discounted_cart_value")

        # Calculate expected final price
        bank_discount = Decimal("0.10")
        expected_final_price = expected_final_price_after_brand_and_category_discount * (Decimal("1.0") - bank_discount)
        
        self.assertEqual(current_final_price, expected_final_price)
        
        # Check if discounts are recorded in global tracking
        self.assertIn("752b11c1-7656-4044-b27b-1d9a75ba0c52", all_discounts_applied)
        self.assertTrue(len(all_discounts_applied["752b11c1-7656-4044-b27b-1d9a75ba0c52"]) > 0)

if __name__ == "__main__":
    unittest.main()
