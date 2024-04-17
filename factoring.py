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

    def calculate_private_exponent(p, q, e):
        """Calculate the private exponent d."""
        Euler_totient = (p - 1) * (q - 1)#essential for deriving the private exponent
        d = pow(e, -1, Euler_totient)# pow() function calculates modular exponentiation efficiently.
        return d
    
    
    for p in range(2, N):
        if N % p == 0 and is_prime(p):#checks if p factor of N and p is prime factor.
            q = N // p
            d = calculate_private_exponent(p, q, e)
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
runtime="""p, q, d = factor_modulus(N, e)"""
execution_time = timeit.timeit(runtime, globals=globals(), number=1)#number=1 ensure that the code is only timed once
print("Prime factor p is:", p)
print("Prime factor q is:", q)
print("Private exponent d:", d)
print("Runtime:", execution_time, "seconds")
print("Is private exponent correct:", is_private_exponent_correct)
