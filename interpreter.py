# Ask user to input expression
expression = (input("Expression: "))

# If expression is a str like 1 + 1, then this assign 1 to x, + to y, and 1 to z.
x, y, z = expression.split(" ")

# Matches expression to correct case
match expression:
    case _ if "+" in expression: #Tells what to do if + is in function
        result = float(x) + float(z) #If it has "+", turns the result into float.
        print(f"{result:.1f}") #Prints the result to the tenths place.
    case _ if "-" in expression:
        result = float(x) - float(z)
        print(f"{result:.1f}")
    case _ if "/" in expression:
        result = float(x) / float(z)
        print(f"{result:.1f}")
    case _ if "*" in expression:
        result = float(x) * float(z)
        print(f"{result:.1f}")