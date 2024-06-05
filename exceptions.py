#zero division

#value error

input

try:
    print(1/"S")
except ZeroDivisionError as e:
    print("Error Code: integer division or modulo by zero")
except TypeError as n:
    print(f"Error Code: invalid literal for int() with base 10: {divis}")
