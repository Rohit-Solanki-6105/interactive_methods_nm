import math

def evaluate_function(func_str, x):
    """
    Evaluate the function string at given x value
    Supports basic mathematical operations and functions
    """
    # Replace 'x' with the actual value
    func_str = func_str.replace('x', str(x))
    
    # Replace common mathematical notations
    func_str = func_str.replace('^', '**')  # Replace ^ with ** for exponentiation
    func_str = func_str.replace('ln', 'math.log')  # Natural logarithm
    func_str = func_str.replace('log', 'math.log10')  # Base 10 logarithm
    func_str = func_str.replace('sin', 'math.sin')
    func_str = func_str.replace('cos', 'math.cos')
    func_str = func_str.replace('tan', 'math.tan')
    func_str = func_str.replace('sqrt', 'math.sqrt')
    func_str = func_str.replace('exp', 'math.exp')
    
    try:
        return eval(func_str)
    except:
        raise ValueError("Invalid function expression")

def bisection_method(func_str, a, b, epsilon, max_iterations=100):
    """
    Implement bisection method for root finding
    
    Parameters:
    func_str: Function as string (e.g., "x^3 - x - 1")
    a, b: Initial interval [a, b]
    epsilon: Tolerance for convergence
    max_iterations: Maximum number of iterations
    
    Returns:
    List of iteration data for table display
    """
    
    # Check if root exists in the interval
    fa = evaluate_function(func_str, a)
    fb = evaluate_function(func_str, b)
    
    if fa * fb > 0:
        raise ValueError("Function has the same sign at both endpoints. Root may not exist in the given interval.")
    
    iterations = []
    previous_c = None  # To store the previous midpoint
    
    print(f"Bisection Method for f(x) = {func_str}")
    print(f"Initial interval: [{a}, {b}]")
    print(f"Tolerance (ε): {epsilon}")
    print("-" * 100)
    
    # Table header
    print(f"{'Iteration':<10} |{'a':<12} |{'f(a)':<12} |{'b':<12} |{'f(b)':<12} |{'c':<12} |{'f(c)':<12} |{'|ck-ck-1|':<12}")
    print("-" * 100)
    
    for i in range(max_iterations):
        # Calculate midpoint
        c = (a + b) / 2
        
        # Evaluate function at endpoints and midpoint
        fa = evaluate_function(func_str, a)
        fb = evaluate_function(func_str, b)
        fc = evaluate_function(func_str, c)
        
        # Calculate |c_k - c_(k-1)|
        if previous_c is None:
            c_difference = 0.0  # For the first iteration, there's no previous c
        else:
            c_difference = abs(c - previous_c)
        
        # Store iteration data
        iteration_data = {
            'iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'fa': fa,
            'fb': fb,
            'fc': fc,
            'c_difference': c_difference
        }
        iterations.append(iteration_data)
        
        # Print iteration data
        if i == 0:
            print(f"{i+1:<10} |{a:<12.6f} |{fa:<12.6f} |{b:<12.6f} |{fb:<12.6f} |{c:<12.6f} |{fc:<12.6f} |{'---':<12}")
        else:
            print(f"{i+1:<10} |{a:<12.6f} |{fa:<12.6f} |{b:<12.6f} |{fb:<12.6f} |{c:<12.6f} |{fc:<12.6f} |{c_difference:<12.6f}")
        
        # Check for convergence
        if i > 0 and c_difference < epsilon or abs(fc) < epsilon:
            print("-" * 100)
            print(f"Root found: x = {c:.6f}")
            print(f"f({c:.6f}) = {fc:.6f}")
            print(f"Converged in {i+1} iterations")
            break
        
        # Store current c as previous for next iteration
        previous_c = c
        
        # Update interval based on sign of f(c)
        if fa * fc < 0:
            b = c  # Root is in [a, c]
        else:
            a = c  # Root is in [c, b]
    
    else:
        print(f"Maximum iterations ({max_iterations}) reached without convergence")
        print(f"Current approximation: x = {c:.6f}")
    
    return iterations

def main():
    """
    Main function to get user input and run bisection method
    """
    print("=" * 50)
    print("BISECTION METHOD FOR ROOT FINDING")
    print("=" * 50)
    
    try:
        # Get function input
        func_str = input("Enter the function f(x) (e.g., 'x^3 - x - 1'): ").strip()
        
        # Get interval endpoints
        a = float(input("Enter the left endpoint (a): "))
        b = float(input("Enter the right endpoint (b): "))
        
        # Get tolerance
        epsilon = float(input("Enter the tolerance (ε): "))
        
        print("\n")
        
        # Run bisection method
        iterations = bisection_method(func_str, a, b, epsilon)
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()