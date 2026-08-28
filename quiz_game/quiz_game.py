print("Welcome to computer quiz")

p = input("Do you want to play? (yes/no): ").lower().strip()

if p != "yes":
    print("Goodbye!")
    quit()

print("\nLet's start!\n")
s = 0

a = input("1. What does CPU stand for? ").lower().strip()
if a == "central processing unit":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("2. What does GPU stand for? ").lower().strip()
if a == "graphics processing unit":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("3. What does RAM stand for? ").lower().strip()
if a == "random access memory":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("4. What does PSU stand for? ").lower().strip()
if a == "power supply unit":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("5. What does ROM stand for? ").lower().strip()
if a == "read only memory":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("6. What does SSD stand for? ").lower().strip()
if a == "solid state drive":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("7. What does HDD stand for? ").lower().strip()
if a == "hard disk drive":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("8. What does IP stand for in IP address? ").lower().strip()
if a == "internet protocol":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("9. What does URL stand for? ").lower().strip()
if a == "uniform resource locator":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

a = input("10. What does USB stand for? ").lower().strip()
if a == "universal serial bus":
    print("Correct!")
    s += 1
else:
    print("Incorrect!")

print("\n--- Game Over ---")
print(f"Score: {s} / 10")
pct = (s / 10) * 100
print(f"Percentage: {pct}%")
