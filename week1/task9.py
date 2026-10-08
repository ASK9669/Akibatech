Amount = int(input("Enter the amount in USD: "))
usd = 150 
rate = Amount * usd

print("=" * 30)
print(f"CURRENCY EXCHANGE")
print("=" * 30)
print()
print(f"USD Amount: {Amount} USD")
print(f"Exchange Rate: {usd} ETB/USD")
print(f"ETB Amount: {rate} ETB")
print("=" * 30)