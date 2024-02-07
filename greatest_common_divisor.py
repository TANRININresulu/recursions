print("\n" + "IN THE NAME OF ALLAH RAHMAN AND RAHIM" + "\n")

def gcd(a, b):
    if(a == 0): # double base condition provides freedom of
        return b
    if(b == 0): # calling gcd function in any argument order by Grace of Our Compassionate and Merciful Owner ALLAH
        return a
    
    if(a > b):
        return gcd(a % b, b) # modular arithmetic improves performance 
    else:
        return gcd(a, b % a) # dramatically between very large and small numbers by Grace of Our Compassionate and Merciful Owner ALLAH

print("greatest common divisor of 8 and 4 is : " + str(gcd(8, 4)))
print("greatest common divisor of 18 and 26 is : " + str(gcd(18, 26)) + "\n")