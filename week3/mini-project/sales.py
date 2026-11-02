
def generate_receipt(sale):
    print("\n========== SALES RECEIPT ==========")
    print("Product Name:", sale["product_name"])
    print("Quantity:", sale["quantity"])
    print("Unit Price:", f"{sale['unit_price']:.2f}")
    print("-----------------------------------")
    print("Total Cost:", f"{sale['total']:.2f}")
    print("===================================")


def record_sale(products):
    print("\n===== RECORD SALE =====")

    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return None

    except ValueError:
        print("Invalid input!")
        return None

    for product in products:
        if product["id"] == product_id:

            if quantity > product["quantity"]:
                print("Insufficient stock!")
                print("Available stock:", product["quantity"])
                return None

            total = quantity * product["price"]

            # Reduce available stock
            product["quantity"] -= quantity

            sale = {
                "product_id": product["id"],
                "product_name": product["name"],
                "quantity": quantity,
                "unit_price": product["price"],
                "total": total
            }

            print("\nSale recorded successfully!")
            generate_receipt(sale)

            return sale

    print("Product not found!")
    return None
