def is_prime(n):
        """Check if a number is prime using trial division."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n**0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True 
