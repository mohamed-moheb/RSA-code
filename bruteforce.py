import timeit

def brute_force_private_exponent(p, q, e):
    """Brute force the private exponent d."""
    Euler_totient = (p - 1) * (q - 1)
    d = 2  # Start with a candidate value of 2
    while True: # loop continues until correct value of d is found
        if (e * d) % Euler_totient == 1:
            return d
        d += 1  # Try the next value of d
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


p,q,e = 137,157,65537
N=p*q
private_exponent = brute_force_private_exponent(p, q, e)
test_message = 12345
is_private_exponent_correct = check_private_exponent(private_exponent, N, e, test_message)
code_to_measure = """d = brute_force_private_exponent(p, q, e)"""
execution_time = timeit.timeit(code_to_measure, globals=globals(), number=1)
print("Private exponent d:", private_exponent)
print("Runtime:", execution_time, "seconds")
print("Is private exponent correct:", is_private_exponent_correct)
