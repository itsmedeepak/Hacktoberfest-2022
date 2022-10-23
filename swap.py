def swap_case(s):
    new_s = ""
    for char in s:
        if(char.islower()):
          new_s += char.upper()
        else:
          new_s +=  char.lower()
    return new_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
