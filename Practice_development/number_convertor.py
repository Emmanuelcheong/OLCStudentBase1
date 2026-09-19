conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "GB": 1000 ** 3,
    "TB": 1000 ** 4,
    "PB": 1000 ** 5,
    "KiB": 1024,
    "MiB": 1024**2,
    "GiB": 1024**3,
    "TiB": 1024**4,
    "PiB": 1024**5,

}
def is_valid_unit(unit):
    if unit in conversion_factors:
        return True
    else:
        return False

def convert_storage(value, from_unit, to_unit):
    true_value = value * conversion_factors[from_unit]
    new_value = float(true_value / conversion_factors[to_unit])
    return new_value

while True:
    while True:
        num_value = input("Please enter the numerical value to be entered: ")
        if num_value.isdigit():
            break
        else:
            print("Value must be a positive integer")
            continue
    while True:
        source_val = input("Please enter your source unit: ")
        if is_valid_unit(source_val):
            break
        else:
            print("Your source unit must be in the dictionary")