
def add_product(products):
    print("\n===== ADD PRODUCT =====")

    name = input("Enter product name: ").strip()

    if not name:
        print("Product name cannot be empty!")
        return None

    for product in products:
        if product["name"].lower() == name.lower():
            print("Product already exists!")
            return None

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        if price <= 0 or quantity < 0:
            print("Invalid price or quantity!")
            return None

    except ValueError:
        print("Please enter valid numbers!")
        return None

    product_id = max(
        [p["id"] for p in products], default=0
    ) + 1

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    print(f"{name} added successfully!")
    return product


def view_products(products):
    print("\n===== ALL PRODUCTS =====")

    if not products:
        print("No products available.")
        return

    print("-" * 65)
    print(f"{'ID':<8}{'NAME':<20}{'PRICE':<17}{'STOCK':<10}")
    print("-" * 65)

    for product in products:
        print(
            f"{product['id']:<8}"
            f"{product['name']:<20}"
            f"{product['price']:<17.2f}"
            f"{product['quantity']:<10}"
        )

    print("-" * 65)


def search_product(products):
    print("\n===== SEARCH PRODUCT =====")

    name = input("Enter product name: ").strip().lower()

    for product in products:
        if name in product["name"].lower():
            print("\nProduct found!")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Stock:", product["quantity"])
            return product

    print("Product not found.")
    return None


def update_product(products):
    print("\n===== UPDATE PRODUCT =====")

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Invalid product ID!")
        return

    for product in products:
        if product["id"] == product_id:

            print("\n1. Update Name")
            print("2. Update Price")
            print("3. Update Quantity")

            choice = input("Choose an option: ")

            if choice == "1":
                new_name = input("Enter new name: ").strip()

                if not new_name:
                    print("Name cannot be empty!")
                    return

                if any(
                    p["name"].lower() == new_name.lower()
                    and p["id"] != product_id
                    for p in products
                ):
                    print("Product name already exists!")
                    return

                product["name"] = new_name

            elif choice == "2":
                try:
                    new_price = float(input("Enter new price: "))

                    if new_price <= 0:
                        print("Price must be positive!")
                        return

                    product["price"] = new_price

                except ValueError:
                    print("Invalid price!")
                    return

            elif choice == "3":
                try:
                    new_quantity = int(input("Enter new quantity: "))

                    if new_quantity < 0:
                        print("Quantity cannot be negative!")
                        return

                    product["quantity"] = new_quantity

                except ValueError:
                    print("Invalid quantity!")
                    return

            else:
                print("Invalid choice!")
                return

            print("Product updated successfully!")
            return

    print("Product not found.")
