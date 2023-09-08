# You are given a string s. You need to reverse the string

def reverse(str):
    str2 = ''
    for i in range(len(str)-1, -1, -1):
        str2 = str2 + str[i]
    return str2

str = input('Enter the String you want to reverse: ')
print('The Reversed String is: ', reverse(str))