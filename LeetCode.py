s = "abcabcbb"

def lengthOfLongestSubstring(x):
    output = 0
    s_list = []
    s_dict = {}
    for i in range(len(x)):
        if x[i] != x[i-1]:
            s_list.append(x[i])
            output += 1
    print(output)
    print(s_list)
    print(s_list.count("a"))

lengthOfLongestSubstring(s)
