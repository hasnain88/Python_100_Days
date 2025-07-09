word = input("Enter a String: ")


# Version 01
# palindrom_flag = True
# for i in range(len(word)):
#     if word[i] != word[len(word)-i-1]:
#         palindrom_flag = False
#         break
#     else:
#         palindrom_flag=True



# Version 02
def check_palindrome(word):
    l = len(word)
    for i in range(l):
        if word[i]!=word[l-i-1]:
            return False
    return True

if check_palindrome(word):
    print("The String is a Palindrome")
else:
    print("The String is not a Palindrome")