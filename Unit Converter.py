def kilometers_to_miles(kilometers):
    """Convert Kilometers to Miles"""
    return kilometers * 0.621371

def inches_to_centimeters(inches):
    """Convert Inches to Centimeters"""
    return inches * 2.54

def fahrenheit_to_celsius(fafrenheit):
    """Convert Celsius to Fahrenheit"""
    return (fahrenheit - 32) * 5 / 9

def main():
    while True:
        print("\nUnit Converter")
        print("1. Enter Kilometers")
        print("2. Enter Temperature")
        print("3. Enter Inches")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ").strip()

        if choice == "1":
            try:
               kilometers = float(input("Enter kilometers: "))
               miles = kilometers_to_miles(kilometers)
               print(f"{kilometers} is equal to {miles:.2f} miles.")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}F is equal to {celsius:.2f}C.")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            try:
                inches = float(input("Enter Inches: "))
                centimeters = inches_to_centimeters(inches)
                print(f"{inches} is equal to {centimeters:.2f} centimeters.")
            except ValueError:
                print("Please enter valid number!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

if __name__=="__main__":
    main()

































