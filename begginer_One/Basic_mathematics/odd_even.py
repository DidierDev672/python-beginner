def odd_even(n):
    if (n < 0):
        print("Numbers less than zero and negative are not allowed")
        return

    if n % 2 != 0:
        print(f"El numero {n} es impar.")
        return True
    else:
        print(f"El numero {n} es par.")
        return False


odd_even(4)
odd_even(5)
odd_even(6)
odd_even(9)
