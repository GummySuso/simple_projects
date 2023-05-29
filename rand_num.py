"""
Random Number Generator
Author: Lukka Wolff
"""
import random

def r_gen(low, high, parity):
    """Returns an even or odd number random number between the low and high bounds
    Paramaters: low, high, even (int);
        parity: 0 (even), 1 (odd), 2 (no preference)
    """
    num = random.randint(low,high)
    val = num%2
    if (parity!=2):
        if (val != parity):
            if (num==high):
                num -= 1
            else:
                num -= 1
    return num

print(r_gen(-100,0,2))
