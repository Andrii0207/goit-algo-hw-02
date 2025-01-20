

def check_symmetric(expession):

    brackets = {"{": "}", "(": ")", "[": "]"}

    stack = []

    for symbol in expession:
        if symbol in brackets.keys():
            stack.append(symbol)
        elif symbol in brackets.values():
            if stack and symbol == brackets[stack[-1]]:
                stack.pop()
            else:
                return print(f"{expession} - вираз не симетричний")
    return f"{expession} - вираз симетричний" if not stack else f"{expession} - вираз не симетричний"


print(check_symmetric("(){[1](1 + 3)(){}}"))  # True
print(check_symmetric("( 23 ( 2 - 3)"))  # False
print(check_symmetric("(({  })"))  # False
