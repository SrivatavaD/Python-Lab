# # print("This is the basic calculator");
# # a = int(input("Enter the number"));
# # b = int(input("Enter the second number"));
# # print("The calc is " ,  a + b , a - b , a * b , a / b);

# # Some basic questions and answers to practice input, output, and basic operations in Python.
# list = [2,4,5,1,2,5,10,8,6,9]
# l = []
# count = 0

# for i in list:
#     if i == 2:
#         l.append(i)
#         count +=1
#     else:
#         pass  

# print(l)
# print(count)


# # Palindrome check
# # If a string is the same after reversing, it is called a palindrome.
# name1 = input("Enter name: ")
# reverse_name1 = name1[::-1]

# print("Original string:", name1)
# print("Reversed string:", reverse_name1)

# if name1 == reverse_name1:
#     print(name1, "is a palindrome.")
# else:
#     print(name1, "is not a palindrome.")


# name2 = "devansh"
# reverse_name2 = name2[::-1]

# print("Original string:", name2)
# print("Reversed string:", reverse_name2)

# if name2 == reverse_name2:
#     print(name2, "is a palindrome.")
# else:
#     print(name2, "is not a palindrome.")


# # Separate letters and numbers from a string
# text = "a1b2c3d4"

# letters = ""
# numbers = ""

# for character in text:
#     if character >= "a" and character <= "z":
#         letters = letters + character
#     elif character >= "0" and character <= "9":
#         numbers = numbers + character

# print("Original text:", text)
# print("Letters:", letters)
# print("Numbers:", numbers)


# # Reverse every word, but keep word positions same
sentence = input("Enter a sentence: ")

words = sentence.split()
new_words = []

for word in words:
    reverse_word = word[::-1]
    new_words.append(reverse_word)

final_sentence = " ".join(new_words)

print("Original sentence:", sentence)
print("Final sentence:", final_sentence)

# Use of slicing in python
# Slicing is a powerful feature in Python that allows you to extract a portion of a sequence (like a string, list, or tuple) by specifying a start index, an end index, and an optional step. The syntax for slicing is: sequence[start:end:step].
# name = input("enter your name: ")
# print(name[::-1])

# num = [1,2,3,4,5,1,2,4,2,3,8,6]
# print(num [::1])

# some basic slicing examples
# test = "python"
# print(test[1:5])

# test = "abcdef"
# print(test)