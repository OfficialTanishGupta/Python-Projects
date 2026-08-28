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

print("\n--- Game Over ---")
print(f"Score: {s} / 4")
pct = (s / 4) * 100
print(f"Percentage: {pct}%")
