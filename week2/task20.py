
a = []
even = 0
odd = 0
for i in range(5):
    num = int(input("Enter a number: "))
    a.append(num)
for i in range(len(a)):
    if a[i]%2 == 0:
        even += 1
    else:
        odd += 1      
Smallest = min(a)
largest = max(a)
total = sum(a)
average = total / len(a)


print("Smallest:", Smallest)
print("Largest:", largest)
print("Total:", total)
print("Average:", average)
print("Even numbers:", even)
print("Odd numbers:", odd)