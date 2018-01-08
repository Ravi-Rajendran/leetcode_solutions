'''
Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/description/
'''

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if s is None or len(s) <= 1:
        return s

    s2 = '|'.join(map(str, s))
    s2 = '|' + s2 + '|'
    p = [0] * len(s2)
    c = r = m = n = 0

    for i in range(1, len(s2)):
        if i > r:
            p[i], m, n = 0, i-1, i+1
        else:
            i2 = c*2-i
            if p[i2] < r-i-1:
                p[i], m = p[i2], -1
            else:
                p[i], n, m = r-i, r+1, i*2-n
        while m >= 0 and n < len(s2) and s2[m] == s2[n]:
            p[i], m, n = p[i]+1, m-1, n+1
        if (i+p[i]) > r:
            c, r = i, i+p[i]
    length = c = 0
    for i in range(1, len(s2)):
        if length < p[i]:
            length, c = p[i], i
    ss = s2[c-length: c+length+1]
    return ''.join([ss[x] for x in range(1, len(ss), 2)])


test_cases = ['babad', 'cbbd', 'cat', 'canac', 'abba']
for s in test_cases:
    print(longestPalindrome(s))
