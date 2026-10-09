digit = int(input("Enter a digit: "))
s = len(str(digit))
lst = []
for i in range(s):
    lst.append(digit % 10)
    digit //= 10
print(sum(lst))
