def simple_calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("Enter the operation (1/2/3/4 or +, -, *, /): ").strip()
        
        if operation in ["1", "+"]:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation in ["2", "-"]:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation in ["3", "*"]:
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation in ["4", "/"]:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation choice. Please try again.")
            continue
        
        play_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for using the Simple Calculator. Goodbye!")
            break

if __name__ == "__main__":
    simple_calculator()
