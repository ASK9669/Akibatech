
inventory = {}


def add_product():
    name = input("Enter product name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    if name.lower() in (product.lower() for product in inventory):
        print("Product already exists.")
        return

    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    if price < 0:
        print("Price cannot be negative.")
        return

    if stock < 0:
        print("Stock cannot be negative.")
        return

    inventory[name] = {"price": price, "stock": stock}
    print("Product added successfully.")


def search_product():
    name = input("Enter product name to search: ").strip()

    for product in inventory:
        if product.lower() == name.lower():
            print("Name:", product)
            print("Price:", inventory[product]["price"])
            print("Stock:", inventory[product]["stock"])
            return

    print("Product not found.")


def update_price():
    name = input("Enter product name: ").strip()

    for product in inventory:
        if product.lower() == name.lower():
            price = float(input("Enter new price: "))

            if price < 0:
                print("Price cannot be negative.")
                return

            inventory[product]["price"] = price
            print("Price updated successfully.")
            return

    print("Product not found.")


def increase_stock():
    name = input("Enter product name: ").strip()

    for product in inventory:
        if product.lower() == name.lower():
            quantity = int(input("Enter quantity to add: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                return

            inventory[product]["stock"] += quantity
            print("Stock increased successfully.")
            return

    print("Product not found.")


def sell_product():
    name = input("Enter product name: ").strip()

    for product in inventory:
        if product.lower() == name.lower():
            quantity = int(input("Enter quantity to sell: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                return

            if quantity > inventory[product]["stock"]:
                print("Not enough stock available.")
                return

            inventory[product]["stock"] -= quantity
            total = quantity * inventory[product]["price"]

            print("Sale successful.")
            print("Total sale amount:", total)
            print("Remaining stock:", inventory[product]["stock"])
            return

    print("Product not found.")


def total_inventory_value():
    total = 0

    for product in inventory:
        price = inventory[product]["price"]
        stock = inventory[product]["stock"]
        total += price * stock

    print("Total inventory value:", total)
    return total


def low_stock_report(threshold=5):
    print("Low-stock products:")

    found = False

    for name, details in inventory.items():
        if details["stock"] < threshold:
            print(name, "- Stock:", details["stock"])
            found = True

    if not found:
        print("No low-stock products.")


def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    for name, details in inventory.items():
        print(
            name,
            "| Price:", details["price"],
            "| Stock:", details["stock"]
        )


def main():
    while True:
        print("\n--- INVENTORY MANAGEMENT SYSTEM ---")
        print("1. Add product")
        print("2. Search product")
        print("3. Update price")
        print("4. Increase stock")
        print("5. Sell product")
        print("6. Total inventory value")
        print("7. Low-stock report")
        print("8. Display all products")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            search_product()
        elif choice == "3":
            update_price()
        elif choice == "4":
            increase_stock()
        elif choice == "5":
            sell_product()
        elif choice == "6":
            total_inventory_value()
        elif choice == "7":
            threshold = int(input("Enter low-stock threshold: "))
            if threshold < 0:
                print("Threshold cannot be negative.")
            else:
                low_stock_report(threshold)
        elif choice == "8":
            display_inventory()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
