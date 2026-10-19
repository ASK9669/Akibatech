
def validate_units(units):
    if units < 0:
        return False
    return True


def calculate_tier_charges(units):
    if not validate_units(units):
        raise ValueError("Units consumed cannot be negative.")

    first_tier = min(units, 50)
    second_tier = min(max(units - 50, 0), 100)
    third_tier = max(units - 150, 0)

    charge1 = first_tier * 0.50
    charge2 = second_tier * 0.75
    charge3 = third_tier * 1.20

    return {
        "first_tier_units": first_tier,
        "first_tier_charge": charge1,
        "second_tier_units": second_tier,
        "second_tier_charge": charge2,
        "third_tier_units": third_tier,
        "third_tier_charge": charge3
    }


def calculate_total_bill(units, service_fee=0):
    if not validate_units(units):
        raise ValueError("Units consumed cannot be negative.")

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    charges = calculate_tier_charges(units)

    energy_charge = (
        charges["first_tier_charge"]
        + charges["second_tier_charge"]
        + charges["third_tier_charge"]
    )

    total = energy_charge + service_fee

    return round(total, 2)


def generate_billing_summary(units, service_fee=0):
    if not validate_units(units):
        raise ValueError("Units consumed cannot be negative.")

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    charges = calculate_tier_charges(units)
    energy_charge = (
        charges["first_tier_charge"]
        + charges["second_tier_charge"]
        + charges["third_tier_charge"]
    )

    total_bill = calculate_total_bill(units, service_fee)

    return {
        "units_consumed": units,
        "tier_charges": charges,
        "energy_charge": round(energy_charge, 2),
        "service_fee": service_fee,
        "total_bill": total_bill
    }


def display_billing_summary(summary):
    print("\n--- ELECTRICITY BILL ---")
    print("Units consumed:", summary["units_consumed"])

    charges = summary["tier_charges"]

    print(
        "First 50 units:",
        f'{charges["first_tier_charge"]:.2f} Birr'
    )
    print(
        "Next 100 units:",
        f'{charges["second_tier_charge"]:.2f} Birr'
    )
    print(
        "Above 150 units:",
        f'{charges["third_tier_charge"]:.2f} Birr'
    )

    print(f'Energy charge: {summary["energy_charge"]:.2f} Birr')
    print(f'Service fee: {summary["service_fee"]:.2f} Birr')
    print(f'Total bill: {summary["total_bill"]:.2f} Birr')


# Main program
try:
    units = float(input("Enter units consumed: "))
    service_fee = float(input("Enter service fee (0 if none): "))

    if not validate_units(units):
        print("Error: Units cannot be negative.")
    elif service_fee < 0:
        print("Error: Service fee cannot be negative.")
    else:
        summary = generate_billing_summary(units, service_fee)
        display_billing_summary(summary)

except ValueError:
    print("Error: Please enter valid numbers.")
