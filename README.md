# RSA Encryption Task

This project demonstrates the implementation of RSA encryption algorithm with the following functionalities:

- Factorizing a modulus \( N \) to obtain prime factors \( p \) and \( q \).
- Calculating the private exponent \( d \) using the obtained prime factors and a public exponent \( e \).
- Brute-forcing the private exponent \( d \).

## Background

The RSA algorithm is an asymmetric cryptographic algorithm widely used for secure communication. It relies on the difficulty of factoring large composite numbers into their prime factors.

## Task Description

The task involves implementing the following functionalities:

1. **Factorizing the Modulus**: Given a modulus \( N \), the goal is to factorize it into its prime factors \( p \) and \( q \). This is crucial for calculating the private exponent \( d \).

2. **Calculating the Private Exponent**: Using the obtained prime factors \( p \) and \( q \), along with a public exponent \( e \), calculate the private exponent \( d \). The private exponent \( d \) satisfies the equation \( e \cdot d \equiv 1 \mod{\phi(N)} \), where \( \phi(N) = (p - 1) \cdot (q - 1) \).

3. **Brute-Force Approach**: Implement a brute-force approach to find the private exponent \( d \). This involves trying different values of \( d \) until the correct one is found.

## Implementation Details

- The code for factorizing the modulus and calculating the private exponent is implemented in Python.
- It includes functions for checking primality, calculating Euler's totient function, and performing modular exponentiation.
- The implementation demonstrates both efficient and brute-force methods for calculating the private exponent.

## Usage

1. Clone the repository to your local machine.
2. Run the Python script `factoring.py`and `bruteforce.py`.
3. Input the modulus \( N \) and the public exponent \( e \).
4. The program will factorize the modulus, calculate the private exponent, and output the results.

## Contributors

- [Mohamed Moheb](link-to-your-github-profile) - Creator and main contributor.
