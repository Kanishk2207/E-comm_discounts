# E-commerce Discount System

## Overview
This is an implementation of a dummy e-commerce discount system. The project mimics database interactions using lists and dictionaries instead of a real database.

## Project Structure
- **database/**: Contains data-related files with `.py` extensions. No actual database is used; data is stored in lists and dictionaries.
- **global_variables.py**: Holds data structures mimicking database tables.
- **data_models.py**: Defines data models used throughout the project.
- **crud.py**: Implements CRUD operations for the in-memory data structures.
- **fake_data.py**: Preloads some dummy data for testing.
- **service/**: Contains all service functions related to payment processing, discount validation, and cart operations.
- **main.py**: The entry point that implements a CLI for users to interact with the system.

## Getting Started
### Step 1: Run the CLI
Execute the following command:
```sh
python3 main.py
```
You will see the following menu:
```
Hello, Welcome to E-com CLI, Please choose one of the above options:
    1. List all products
    2. Add item in the cart
    3. Show your cart details
    4. Add discount vouchers
    5. Add Payment Method
    9. Exit
```

### Step 2: List All Products
Enter `1` to list all available products.

### Step 3: Add Item to Cart
Enter `2` to add an item to the cart. You will be prompted for:
- **Product ID**
- **Size of the product**
- **Quantity**

After providing these details, the item will be successfully added to the cart.

### Step 4: Show Cart Details
Enter `3` to display the current cart details, including all added products and their pricing.

### Step 5: Apply Discount Voucher
Enter `4` to apply a discount voucher.
- You will be prompted to enter a voucher code.
- Currently, only the `SUPER69` voucher is available (as defined in `fake_data.py`).
- After applying the voucher, discounts will be reflected in the cart.
- Verify the applied discount by entering `3` again to check cart details.

### Step 6: Add Payment Method
Enter `5` to add a payment method.
- You will be prompted to choose a payment method (e.g., `UPI`, `Card`).
- If selecting `Card`, you will need to specify:
  - **Bank Name**
  - **Card Type**
- Only **ICICI Bank** offers an additional discount.
  - To apply the bank offer, enter `card` as the payment method, `icici` as the bank name, and `credit` as the card type.

After adding the payment method, enter `3` to verify all applied discounts, payment info, and the final cart total including base and discounted prices.

## Exit the Program
Enter `9` to exit the CLI.

---

This project provides a simple and interactive way to explore e-commerce discount logic, voucher validation, and payment processing in a CLI environment.

