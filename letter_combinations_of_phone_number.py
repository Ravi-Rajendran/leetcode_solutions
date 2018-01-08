'''
Letter combinations of a phone number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
'''

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == '' or digits is None:
        return []

    phone = [' ', '', 'abc', 'def',
            'ghi', 'jkl', 'mno',
            'pqrs', 'tuv', 'wxyz']

    def print_words(digits, cur_digit, result, output):
        if cur_digit == len(digits):
            output.append(''.join(result))
            return
        for i in range(len(phone[int(digits[cur_digit])])):
            result[cur_digit] = phone[int(digits[cur_digit])][i]
            print_words(digits, cur_digit+1, result, output)
            if digits[cur_digit] in ['0', '1']:
                return

    result = [None] * len(digits)
    output = []
    print_words(digits, 0, result, output)
    return output

print(letterCombinations('23'))
