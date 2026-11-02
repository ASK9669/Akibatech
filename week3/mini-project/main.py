
def calculate_revenue(sales):
    revenue = 0

    for sale in sales:
        revenue += sale["total"]

    return revenue


def inventory_value(products):
    total_value = 0

    for product in products:
        total_value += product["price"] * product["quantity"]

    return total_value


def low_stock(products, threshold=5):
    print("\n===== LOW STOCK PRODUCTS =====")

    found = False

    for product in products:
        if product["quantity"] <= threshold:
            print(
                f"{product['name']} - "
                f"Remaining stock: {product['quantity']}"
            )
            found = True

    if not found:
        print("No low-stock products.")


def sales_summary(sales):
    print("\n===== SALES SUMMARY =====")

    if not sales:
        print("No sales recorded.")
        return

    print("-" * 65)
    print(
        f"{'PRODUCT':<20}"
        f"{'QUANTITY':<12}"
        f"{'UNIT PRICE':<15}"
        f"{'TOTAL':<15}"
    )
    print("-" * 65)

    for sale in sales:
        print(
            f"{sale['product_name']:<20}"
            f"{sale['quantity']:<12}"
            f"{sale['unit_price']:<15.2f}"
            f"{sale['total']:<15.2f}"
        )

    print("-" * 65)


def view_reports(products, sales):
    while True:
        print("\n===== BUSINESS REPORTS =====")
        print("1. Total Revenue")
        print("2. Inventory Value")
        print("3. Low Stock Products")
        print("4. Sales Summary")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            revenue = calculate_revenue(sales)
            print(f"Total Revenue: {revenue:.2f}")

        elif choice == "2":
            value = inventory_value(products)
            print(f"Inventory Value: {value:.2f}")

        elif choice == "3":
            low_stock(products)

        elif choice == "4":
            sales_summary(sales)

        elif choice == "5":
            break

        else:
            print("Invalid option!")
