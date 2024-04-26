# Asking the user for input and converting kg into joules using E=mc²

def joules():
    E = int(input("Input the mass in kg which you want to convert to Joules: "))
    return E * 300000000 ** 2

# Printing the answer as an integer

print("The equivalent number of Joules is:", int(joules()))

