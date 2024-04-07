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

N = 204713
e = 65537
p, q, d = factor_modulus(N, e)
runtime="""p, q, d = factor_modulus(N, e)"""
execution_time = timeit.timeit(runtime, globals=globals(), number=1)#number=1 ensure that the code is only timed once
print("Prime factor p is:", p)
print("Prime factor q is:", q)
print("Private exponent d:", d)
print("Runtime:", execution_time, "seconds")
