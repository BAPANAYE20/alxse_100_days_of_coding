# a Python Functtion to add two nummbers
def add_numbers(num1, num2):
    return num1 + num2

#main code
if __name__ == "__main__":
#so we input the two numbers
    num1 = float(input("Enter the first digit: "))
    num2 = float(input("Enter the second digit: "))

    #At this stage we will the two numbers
    results = add_numbers(num1, num2)

    #Here we will print the results
    print("The results pf adding", num1, "and", num2, "is", results)