def main():
    x, y, z = input("Expression: ").split(" ")
    x = int(x)
    y = str(y)
    z = int(z)
    print("Answer:", calc(x, y, z))

def calc(x, y, z):
    if y == "+":
        return float(round(x + z, 1))
    elif y == "-":
        return float(round(x - z, 1))
    elif y == "*":
        return float(round(x * z, 1))
    elif y == "/":
        return float(round(x / z, 1))

main()
