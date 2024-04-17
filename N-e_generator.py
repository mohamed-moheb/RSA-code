import random

def generate_values(bit):
    """Generate valid values of N and e for RSA."""
    # Generate a random prime number for p and q
    p = random.randint(2**(bit-1), 2**bit - 1)
    while not is_prime(p):
        p = random.randint(2**(bit-1), 2**bit - 1)
    
    q = random.randint(2**(bit-1), 2**bit - 1)
    while not is_prime(q) or q == p:
        q = random.randint(2**(bit -1), 2**bit  - 1)

    # Calculate N and Euler's totient function
    N = p * q

    # Choose a prime number e
    e = random.choice([3, 5, 17, 257, 65537])  # Common choices for e

    return N, e

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

N, e = generate_values(8)
print("Generated N:", N)
print("Generated e:", e)
