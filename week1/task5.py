name = input("Enter your name: ")
product = input("Enter a product: ")
price = float(input("Enter the price of the product: "))
Qty = int(input("Enter the quantity: "))
total = price * Qty

print("=" * 30)
print("    RECEIPT    ")
print("=" * 30)

print(f"Customer: {name}")
print(f"\nProduct      Price      Qty")
print("-" * 27)
print(f"{product}         {price:.2f}ETB    {Qty}")
print(f"\ntotal: {total:.2f}ETB")
print(f"\n Thank you for shopping ")
print("=" * 30)