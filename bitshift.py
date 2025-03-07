#I was able to multiply two positive integers using only bit-shifting and addition by implementing a method based on the binary representation of numbers. Basically the algorithm iterates through each bit of the multiplier, shifting the multiplicand accordingly, and adding the results when the corresponding bit is set.


def multiply(a, b):
    result = 0
    shift_count= 0
    while b > 0:
        if b & 1:  
            result += a << shift_count  
        a <<= 1 
        b >>= 1 
        shift_count += 1
    return result


