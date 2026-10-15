def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_odd_or_not(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def reverse_string(s):
    return s[::-1]

def analyze_number(n):
    prime_status = is_prime(n)
    divisors = get_divisors(n)
    digit_sum = sum_of_digits(n)
    reversed_str = reverse_string(str(n))
    odd_or_even = is_odd_or_not(n)

    
    return {
        "is_prime": prime_status,
        "is_odd_or_not": odd_or_even,
        "divisors": divisors,
        "sum_of_digits": digit_sum,
        "reversed_string": reversed_str
    }

print(analyze_number(123))  
