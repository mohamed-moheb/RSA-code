def brute_force_private_exponent(p, q, e):
    """Brute force the private exponent d."""
    Euler_totient = (p - 1) * (q - 1)
    d = 1  # Start with a candidate value of 1
    while True:
        if (e * d) % Euler_totient == 1:
            return d
        d += 1  # Try the next value of d
