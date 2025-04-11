s = "abcabcabcddd"

def lengthOfLongestSubstring(x):
    s_seen = set() #empty set for storing elements which we have checked
    output = 0 #will be the length of the substring
    prev = 0 #the beginning of the substring
    for i in range(len(x)): #limits the length of the operation
        while x[i] in s_seen: #while the element we are on is in fact in the set we created
            s_seen.remove(x[prev]) # we need to remove that because we want a NON Repeating set
            prev += 1 #because we cant have that anymore, we get to one at the right
        s_seen.add(x[i]) # while it is NOT in seen we add the element to the set

        if i - prev + 1 > output: # if the length of the output lower than the new substring, we renew it
            output = i - prev + 1 #+1 here really helps us especially when we got just a repeating string

    print(output)

lengthOfLongestSubstring(s)
