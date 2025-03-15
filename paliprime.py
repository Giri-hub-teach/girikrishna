def is_palindrome(n):
    return str(n) == str(n)[::-1]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n + 1):
        if n % i == 0:
            return False
    return True
def is_palindrome_prime(n):
    return is_palindrome(n) and is_prime(n)

def check_number(num):
    if is_palindrome_prime(num):
        return f"{num} is a palindrome prime."
    else:
        return f"{num} is not a palindrome prime."
result = check_number(11)
print(result)
