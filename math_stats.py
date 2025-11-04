"""
math_stats.py - A collection of basic algebraic and statistical functions
for software testing exercises using unittest.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
        """Return the power of """
        return base ** exponent

def square_root(n):
    """Return the square root of n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return n ** 0.5

def absolute_value(n):
    """Return the absolute value of n."""
    return abs(n)

def mean(numbers):
    """Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers: A list or tuple of numeric values.
        
    Returns:
        The mean as a float.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers.
    
    Args:
        numbers: A list or tuple of numeric values.
        
    Returns:
        The median value.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    """Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers: A list or tuple of numeric values.
        
    Returns:
        The mode value, or None if all values appear with equal frequency.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    if len(modes) == len(frequency):
        return None
    return modes[0] if len(modes) == 1 else modes

def variance(numbers):
    """Calculate the population variance of a list of numbers.
    
    Args:
        numbers: A list or tuple of numeric values.
        
    Returns:
        The variance as a float.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of empty list")
    
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    """Calculate the population standard deviation of a list of numbers.
    
    Args:
        numbers: A list or tuple of numeric values.
        
    Returns:
        The standard deviation as a float.
        
    Raises:
        ValueError: If the list is empty.
    """
    return variance(numbers) ** 0.5

def is_even(n):
    """Check if a number is even.
    
    Args:
        n: An integer.
        
    Returns:
        True if n is even, False otherwise.
    """
    return n % 2 == 0

def is_prime(n):
    """Check if a number is prime.
    
    Args:
        n: An integer.
        
    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate the factorial of n.
    
    Args:
        n: A non-negative integer.
        
    Returns:
        The factorial of n.
        
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a, b):
    """Calculate the greatest common divisor of a and b using Euclidean algorithm.
    
    Args:
        a: An integer.
        b: An integer.
        
    Returns:
        The GCD of a and b.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a