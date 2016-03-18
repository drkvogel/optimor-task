"""
20 + (10 - 4) * 3

20 10 4 - 3 * + == 38
20 6 3 * +
20 18 +
38
"""

def postfix_calc(in_list):
    stack = []
    valid = ['-', '+', '*']
    try:
        for item in in_list:
            print "got: " + str(item)
            if isinstance(item, int):
                stack.append(item)
            elif item in valid:
                # pop preceding two operands and apply operator to them
                operator = item
                operand2 = stack.pop()
                operand1 = stack.pop()
                if operator == '-':
                    result = operand1 - operand2
                elif operator == '+':
                    result = operand1 + operand2
                elif operator == '*':
                    result = operand1 * operand2
                else:
                    raise Exception("oops")
                print "result: " + str(result)
                stack.append(result)
            else:
            	raise Exception("invalid symbol: " + str(item) + " encountered")
    except Exception as e:
        print("Error: " + e.message)

if __name__ == '__main__':
    in_list = [20, 10, 4, '-', 3, '*', '+']
    postfix_calc(in_list)

    # bad_list = [20, 10, 4, 'abc', 3, '*', '+']
    # postfix_calc(bad_list)