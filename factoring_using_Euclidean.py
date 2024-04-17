import timeit

def factor_modulus(N, e):
    """Factor the modulus to obtain prime factors and calculate the private exponent."""
    
    def is_prime(n):
        """Check if a number is prime using trial division."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n**0.5) + 1 #square root of n.
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False #in case not prime.
        return True #in case prime.
    
    def extended_gcd(a, b):
        """Extended Euclidean Algorithm."""
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = extended_gcd(b, a % b)
            return d, y, x - (a // b) * y

    def calculate_private_exponent_using_euclidean(e, Euler_totient):
        """Calculate the private exponent d using the extended Euclidean algorithm."""
        d = extended_gcd(e, Euler_totient)[1]
        # Ensure d is positive
        d = d % Euler_totient
        return d
    
    for p in range(2, N):
        if N % p == 0 and is_prime(p):
            q = N // p
            Euler_totient = (p - 1) * (q - 1)
            d = calculate_private_exponent_using_euclidean(e, Euler_totient)
            return p, q, d

def rsa_encrypt(message, e, N):
    """Encrypt a message using RSA."""
    encrypted_message = pow(message, e, N)
    return encrypted_message

def rsa_decrypt(encrypted_message, d, N):
    """Decrypt an encrypted message using RSA."""
    decrypted_message = pow(encrypted_message, d, N)
    return decrypted_message

def check_private_exponent(d, N, e, test_message):
    """Check if the private exponent is correct by encrypting and decrypting a test message."""
    encrypted_message = rsa_encrypt(test_message, e, N)
    decrypted_message = rsa_decrypt(encrypted_message, d, N)
    return decrypted_message == test_message

N = 21509
e = 65537
test_message = 12345
p, q, d = factor_modulus(N, e)
is_private_exponent_correct = check_private_exponent(d, N, e, test_message)
runtime = """p, q, d = factor_modulus(N, e)"""
execution_time = timeit.timeit(runtime, globals=globals(), number=1)
print("Prime factor p is:", p)
print("Prime factor q is:", q)
print("Private exponent d:", d)
print("Runtime:", execution_time, "seconds")
print("Is private exponent correct:", is_private_exponent_correct)
