# s = "abcdabcdabcdeee"
#
# def lengthOfLongestSubstring(x):
#     s_seen = set() #empty set for storing elements which we have checked
#     output = 0 #will be the length of the substring
#     prev = 0 #the beginning of the substring
#     for i in range(len(x)): #limits the length of the operation
#         while x[i] in s_seen: #while the element we are on is in fact in the set we created
#             s_seen.remove(x[prev]) # we need to remove that because we want a NON Repeating set
#             prev += 1 #because we cant have that anymore, we get to one at the right
#         s_seen.add(x[i]) # while it is NOT in seen we add the element to the set
#
#         if i - prev + 1 > output: # if the length of the output lower than the new substring, we renew it
#             output = i - prev + 1 #+1 here really helps us especially when we got just a repeating string
#
#     print(output)
#     print(s_seen)
#
# lengthOfLongestSubstring(s)

# def validate_user(name, email, password):
#     def validate_name(name):
#         if type(name) == "str" and len(name) > 2:
#             return True
#         else:
#             raise ValueError
#
#     def validate_email(email):
#         if type(email) != "str":
#             raise ValueError
#         elif len(email) <= 1:
#             raise ValueError
#         elif string.count('@') != 1:
#             raise ValueError
#         elif email[email.find("@"):] not in top_level_domains:
#             raise ValueError
#         else:
#             return True
#
#     def validate_password(password):
#         if len(password) > 8:
#             raise ValueError
#         elif sum(1 for i in password if i.isupper()) == 0:
#             raise ValueError
#         elif sum(1 for i in password if i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0:
#             raise ValueError
#         else:
#             return True
#
#
# def register_user(name, email, password):
#     dict = {}
#     if validate_user() == ValueError:
#         return False
#     else:
#         dict.update({"name": name, "email": email, "password": password})
#         print(dict)
#
# validate_user('John', 'john@example.com', 'securePassword123')


# def reverse(x: int) -> int:
#     sign = -1 if x < 0 else 1
#     x_abs = abs(x)
#     reversed_num = str(x)[::-1]
#     if int(reversed_num) < (-2**31) or int(reversed_num) > (2**31) - 1:
#         return 0
#     return sign * int(reversed_num)

def myAtoi(s: str) -> int:
    if len(s) == 0:
        return 0

    cleaner_s = s.strip()
    if len(cleaner_s) == 0:
        return 0

    a = []
    sign = 1
    index = 0

    if cleaner_s[0] == '-':
        sign = -1
        index = 1

    elif cleaner_s[0] == '+':
        sign = +1
        index = 1

    for i in cleaner_s[index:]:
        if not i.isdigit():
            break

        a.append(i)
    if not a:
        return 0

    if sign * int("".join(a)) < (-2 ** 31):
        print(-2 ** 31)

    if sign * int("".join(a)) > (2 ** 31 - 1):
        print(2 ** 31 - 1)

    print(sign * int("".join(a)))





