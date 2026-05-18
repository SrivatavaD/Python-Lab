# The provided code stub reads an integer,n, from STDIN. For all non-negative integers ,i<n  print i^2 .
# Example
# The list of non-negative integers that are less than   n = 3 is [0,1,2] . Print the square of each number on a separate line.

# n = int(input("Enter the number: "))
# for i in range(n):
#     print(i**2)

    # Without using any string methods, try to print the following:
    #  123...n

# n = int(input())
# for n in range(1,n+1): print(n,end="")

# for i in range(5):
#     print(i)

n = "devansh"
print(n[-4:-2])

# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.

def count_substring(string, sub_string):

    rep = 0
    
    f = string.find(sub_string)
    while (f != -1):
        rep = rep + 1
        string = string[f+1:]
        f = string.find(sub_string)

    return rep
    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

