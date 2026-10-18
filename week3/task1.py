
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)

    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount, tax_rate)

    final_amount = amount_after_discount + tax

    print("\n========== SHOPPING RECEIPT ==========")

    for item in items:
        total = item["price"] * item["quantity"]
        print(f"{item['name']}: {item['quantity']} x "
              f"{item['price']} = {total:.2f} Birr")

    print("--------------------------------------")
    print(f"Subtotal:       {subtotal:.2f} Birr")
    print(f"Discount:      -{discount:.2f} Birr")
    print(f"Tax:            {tax:.2f} Birr")
    print("--------------------------------------")
    print(f"Final Amount:   {final_amount:.2f} Birr")
    print("======================================")

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
    }


receipt = generate_receipt(items, 15)
