def product_of_digits(x):
    x = abs(x)
    if x < 10:
        return x
    return (x%10)*product_of_digits(x//10)
print(product_of_digits(234))

def array_to_sting(a, index = 0):
    if index == len(a):
        return ""
    number = str(a[index])
    if index == len(a)-1:
        return number
    else:
        return number + "," + array_to_sting(a, index + 1)
print(array_to_sting([1, 2, 3, 4]))

def log(base,value):
    if value <= 0 or base <= 1:
        raise ValueError("Value must be greater than 0 and base must be greater than 1")
    if value < base:
        return 0
    return 1 + log(base, value//base)
print(log(10, 123456))