'''
Implement atoi to convert a string to an integer.
https://leetcode.com/problems/string-to-integer-atoi/description/
'''

def atoi(str):
    str = str.strip()
    if str == '':
        return 0

    index = 0
    result = 0
    sign = False

    if str[0] in '-+':
        if len(str) == 1 or (len(str) > 1 and not str[1].isdigit()):
            return 0
        if str[0] == '-':
            sign = True
        index += 1
    print(sign)

    while index < len(str):
        print(str[index])
        if str[index].isdigit():
            result = result * 10 + int(str[index])
            index += 1
        else:
            break

    if sign:
        result = -result

    print(str, result)
    return result


# f = open("atoi_test_cases.txt", 'r')
# for x in f:
# 	x = x.strip()
# 	print('%10s : %10s' % (x, str(atoi(x))))

cases = ["", "123", "-123", "1-23", "bc-123",
		 "123b", "123 45b", "123ab12", "abc",
		 "+1",  "+", "    010"]

for case in cases:
	print('%10s : %10d' %(case, atoi(case)))
