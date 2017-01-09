

def add_strings(number1, number2):

    if not number1.isdigit() or not number2.isdigit():
        return "Fail!"

    # pad the strings with 0's 
    number1 = number1.zfill(max(len(number1), len(number2)))
    number2 = number2.zfill(max(len(number1), len(number2)))
    result = ""
    carry = 0

    for i in range(len(number1)-1, -1, -1):
        resultNum = int(number1[i]) + int(number2[i]) + carry

        if resultNum > 9:
            carry = 1
        else:
            carry = 0
        result = str(resultNum % 10) + result

    if carry:
        result = str(1) + result

    return result


def multiply_recursive(number1, number2):

    # check that the string contain actual numbers
    if (not number1.isdigit() or not number2.isdigit()):
        return "Fail!"

    # we are good if its 1 by 1 digit
    if len(number1) == 1 and len(number2) == 1:
        return str(int(number1) * int(number2))

    # if one of the numbers is all zeros, then we need to return 0
    if (number1 == '0'*len(number1) or number2 == '0'*len(number2)):
        return '0'*max(len(number1),len(number2))
    
    max_len = max(len(number1), len(number2))
    if (max_len % 2):
        max_len = max_len + 1

    # pad the strings with 0's 
    number1 = number1.zfill(max_len)
    number2 = number2.zfill(max_len)

    # now compute the recursion
    # 10^n.ac + 10^n/2.(ad+bc) + bd

    num1Half1 = number1[:int(len(number1)/2)]
    num1Half2 = number1[int(len(number1)/2):]
    num2Half1 = number2[:int(len(number2)/2)]
    num2Half2 = number2[int(len(number2)/2):]

    ac = multiply_recursive(num1Half1, num2Half1)
    ad = multiply_recursive(num1Half1, num2Half2)
    bc = multiply_recursive(num1Half2, num2Half1)
    bd = multiply_recursive(num1Half2, num2Half2)

    
    ac = ac + '0'*max_len
    ad_bc = add_strings(ad,bc) + '0'*(int((max_len)/2))



    return add_strings(add_strings(ac, ad_bc), bd).lstrip('0')



output = multiply_recursive("3141592653589793238462643383279502884197169399375105820974944592", "2718281828459045235360287471352662497757247093699959574966967627")

print(output)












     




    







