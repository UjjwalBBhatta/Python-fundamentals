def add():
    """This function returns the sum of the input"""
    while(True):
        try:
            num1 = float(input("Enter a number to add: "))
            num2 = float(input("Enter another number to add: "))
            return num1 + num2
        except ValueError:
            print("Input valid numbers")
        except Exception as e:
            print(f"an error occured: {e}")

