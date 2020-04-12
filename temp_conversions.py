def celsius_to_fahrenheit(temp):
    new_temp = (9/5) * temp + 32
    return f"{new_temp:.2f}\N{DEGREE SIGN}F"


def fahrenheit_to_celsius(temp):
    new_temp = 5/9 * (temp - 32)
    return f"{new_temp:.2f}\N{DEGREE SIGN}C"


def kelvin_to_fahrenheit(temp):
    new_temp = 9/5 * (temp - 273) + 32
    return f"{new_temp:.2f}\N{DEGREE SIGN}F"


def fahrenheit_to_kelvin(temp):
    new_temp = 5/9 * (temp - 32) + 273
    return f"{new_temp:.2f} K"


def celsius_to_kelvin(temp):
    new_temp = temp + 273
    return f"{new_temp:.2f} K"


def kelvin_to_celsius(temp):
    new_temp = temp - 273
    return f"{new_temp:.2f}\N{DEGREE SIGN}C"


def convert():
    temp = float(input("Please enter your current temperature as a number only: "))
    user_input = input(
        'Which function do you want to use?\n(a) F to C\n(b) C to F\n(c) K to F\n(d) F to K\n(e) K to C\n(f) C to K\n\n')
    if user_input == "a":
        func = fahrenheit_to_celsius
    elif user_input == "b":
        func = celsius_to_fahrenheit
    elif user_input == "c":
        func = kelvin_to_fahrenheit
    elif user_input == "d":
        func = fahrenheit_to_kelvin
    elif user_input == "e":
        func = kelvin_to_celsius
    elif user_input == "f":
        func = celsius_to_kelvin
    else:
        return "No correct entry made."
    return func(temp)