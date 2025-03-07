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
