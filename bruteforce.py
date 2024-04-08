import timeit
def brute_force_private_exponent(p, q, e):
    """Brute force the private exponent d."""
    Euler_totient = (p - 1) * (q - 1)
    d = 2  # Start with a candidate value of 2
    while True: # loop continues until correct value of d is found
        if (e * d) % Euler_totient == 1:
            return d
        d += 1  # Try the next value of d


p,q,e = 
private_exponent = brute_force_private_exponent(p, q, e)
code_to_measure = """d = brute_force_private_exponent(p, q, e)"""
execution_time = timeit.timeit(code_to_measure, globals=globals(), number=1)
print("Private exponent d:", private_exponent)
print("Runtime:", execution_time, "seconds")
