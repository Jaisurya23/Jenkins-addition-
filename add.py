def add(a,b):
    result = a + b
    return f"The sum of {a} and {b} is {result}."
if __name__ == "__main__":   
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    print(add(a,b))                   