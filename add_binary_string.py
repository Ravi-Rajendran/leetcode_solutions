"""
Given two binary strings, return their sum
https://leetcode.com/problems/add-binary/description/
"""


def sum_of_binary(a, b):
    if a == '' or a == '0':
        return b
    if b == '' or b == '0':
        return a

    sum_value = ''
    last_a, last_b = len(a)-1, len(b)-1
    carry = 0

    while last_a >= 0 or last_b >= 0 or carry != 0:
        if last_a >= 0:
            carry += eval(a[last_a] + '-0')        # or int(a[last_a])
        if last_b >= 0:
            carry += eval(b[last_b] + '-0')         # or int(b[last_b])

        sum_value = str(carry % 2) + sum_value
        carry //= 2
        last_a -= 1
        last_b -= 1

    return sum_value


if __name__ == "__main__":
    a = '111'
    b = '1011'
    print(sum_of_binary(a, b))
