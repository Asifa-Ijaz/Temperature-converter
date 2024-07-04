print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1/2): ")

if choice == "1":
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = 59 * celsius + 32
    print(f"{celsius} celsius is equal to {fahrenheit} fahrenheit")

elif choice == "2":
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = 95 *(Fahrenheit - 32 )
    print(f"{Fahrenheit} Fahrenheit is equal to {Celsius} celsius")

else:
    print("Invalid choice. Please enter 1 or 2")








