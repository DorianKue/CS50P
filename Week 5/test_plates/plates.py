def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[:2].isalpha():
        has_number = False
        if s.isalpha():
            return True
        for c in s:
            if c.isnumeric():
                has_number = True
                if s[s.index(c) :].isnumeric() and c != "0":
                    return True
                else:
                    return False
    else:
        return False


if __name__ == "__main__":
    main()
