s = "abcabcbbdddd"

def lengthOfLongestSubstring(x):
    s_seen = set()
    output = 0
    prev = 0
    for i in range(len(x)):
        while x[i] in s_seen:
            s_seen.remove(x[prev])
            prev += 1
        s_seen.add(x[i])

        if i - prev + 1 > output:
            output = i - prev + 1

    print(output)

lengthOfLongestSubstring(s)
