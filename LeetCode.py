s = "abcabcbb"

def lengthOfLongestSubstring(x):
    output = 0
    s_list = []
    s_dict = {}
    for i in range(len(x)):
        s_dict.update(x[i])
        if x[i] != x[i-1]:
            output += 1
    print(output)
    print(s_dict)

