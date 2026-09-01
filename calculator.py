a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))
if op == "+":
    res = a + b
elif op == "-":
    res = a - b
elif op == "*":
    res = a * b
elif op == "/":
    if b == 0:
        res = "Error: Cannot divide by zero"
    else:
        res = a / b
else:
    res = "Invalid operator"
print("Result:", res)
