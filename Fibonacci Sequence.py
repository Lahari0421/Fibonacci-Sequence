def generate_fibonacci(n):
    fibonacci_sequence = []
    a,b = 0,1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a,b=b,a+b
    return fibonacci_sequence
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if num_terms <=0:
        print("Please enter a positive integer.")
    else:
        sequence = generate_fibonacci(num_terms)
        print("Fibonacci sequence:")
        print(sequence)
except ValueError:
    print("Invalid input. Please enter an integer.")
