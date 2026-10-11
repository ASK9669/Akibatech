N = int(input("Enter a positive integer: "))
even = 0
odd = 0
for i in range(1,N+1):
    if i%2 == 0:
        even += 1
    else:
        odd += 1
total = N*(N+1)//2
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Sum of numbers from 1 to", N, "is:", total)