# function will be given numbers only and will only return true or false
# integers but can be positive or negative
# determine whether the integer is a palindrome
# all negative numbers will be false
# range 0-9 will all be true
# middle number of odd lengthed numbers will not need to be checked

def is_a_palindrome(number):
    x = 0
    if number < 0:
        print("false")
        return False
    elif number in range(0, 10):
        print("true")
        return True
    else:
        digit_list = [int(digit) for digit in str(number)]
        print(digit_list)
        computation = len(digit_list) / 2
        if len(digit_list) / 2 != 0:
            del digit_list[(int(len(digit_list) / 2))]
            while x <= len(digit_list) / 2:
                if digit_list[x] != digit_list[-(x+1)]:
                    print("false")
                    return False
                else:
                    x += 1
                    if x == int(computation):
                        print("true")
                        return True
        elif len(digit_list) / 2 == 0:
            while x <= len(digit_list) / 2:
                if digit_list[x] != digit_list[-(x+1)]:
                    print("false")
                    return False
                else:
                    x += 1
                    if x == computation:
                        print("true")
                        return True

is_a_palindrome(number)

# number % 2
# if number not % 2
