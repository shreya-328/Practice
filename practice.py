# # Factorial using recursion
# def fact(no):
#     if no==0 or no==1: 
#         return 1
#     return no * fact (no-1)
# no = 4
# print(fact(no))

# # from a list find the second largest number
# def secondHigh(no):
#     if len(no) == 1:
#         return no[0]
#     num = list(set(no))
#     num.sort()
#     return num[-2]

# no = [1,2,3,4,1,2,3,2,4,5,6]
# print(secondHigh(no))

# from a list of strings find the strings which are palindrom

# def palin(p):
#     new_list=[]
#     for i in p:
#         new_s=i
#         if i==new_s[-1::-1]:
#             new_list.append(i)

#     return new_list

# p = ['madam','hello', 'noon','python','level','1221']
# print(palin(p))
# palindromes = [word for word in p if word == word[::-1]]
# print(palindromes)  


#Anagram
# def ana(w1,w2):
#     w1 = w1.lower().replace(" ","")
#     w2 = w2.lower().replace(" ","")
#     if sorted(w1) == sorted(w2):
#         return ' Anagram'
#     else:
#         return 'Not Anagram'
# w1 = 'Dormitoryw'
# w2 = 'Dirty Room'
# print(ana(w1,w2))
# def has_anagram(word_list):
#     seen = set()   # store sorted versions

#     for word in word_list:
#         clean = word.lower().replace(" ", "")
#         sorted_word = "".join(sorted(clean))

#         if sorted_word in seen:
#             return True   # anagram mil gaya

#         seen.add(sorted_word)

#     return False  # koi anagram nahi mila


# # Example
# words = ['listen', 'hello', 'race', 'care', 'world']
# print(has_anagram(words))


# 30questions
##reverse a string

# def reverse_str(s):
#     new_s = ""
#     for i in s[::-1]:
#         new_s = new_s+i
#     return new_s
# s="qwerty"
# print(reverse_str(s))


# s='qwerty'
# print(s[::-1])

# check whether a string is palindorme or not
# s='madam'
# palin = s[::-1]
# if(s==palin):
#     print("YES")
# else:
#     print("NO")

## using two pointers
# def check_palin(s):
#     left = 0 
#     right = len(s)-1
#     while(left<right):
#         if s[left]!=s[right]:
#             return False
#         left = left+1
#         right = right-1

#     return True
# s="madam"
# print(check_palin(s))

# count vowels and consonants + if a str contains any character
# def countV(s):
#     for ch in s:
#         if ch< '0' or ch >'9':
#             return False
#     return True

# s='123r'
# print(countV(s))
    

#     vowel=0 
#     c=0
#     for i in s:
#         if i.isalpha():
#             if i.lower() in ['a','e','i','o','u']:
#                 vowel+=1
#             else:
#                 c +=1
#     print("Vowel = ", vowel, "Consonant = ",c)
# s="Hello World"
# countV(s)

# Swap cases of a character in a string
# def swapC(s):
#     new_s=''
#     for i in s:
#         if i.islower():
#             new_s=new_s+i.upper()
#         elif i.isupper():
#             new_s=new_s+i.lower()
#         else:
#             new_s=new_s+i
        
#     print(new_s)

# s="Hello World"
# swapC(s)

# def str_to_charA(s):
#     char_arr = []
#     for ch in s:
#         char_arr.append(ch)
#     print("char array: ",char_arr)
#     result =""
#     for ch in char_arr:
#         result+=ch
#     print("back to str " , result)

# s="hello"
# str_to_charA(s)

##remove punctuations from a string
# def remp(s):
#     new_s=''
#     for i in s:
#         if i.isalpha() or i.isdigit() or i==' ':
#             new_s=new_s+i
#     return new_s    
# s="Hello, World! how are you?"
# print(remp(s))

# count no of words in a string
# def countWord(s) -> int:
#     count = 0
#     in_word = False

#     for ch in s:
#         if ch != ' ':
#             if not in_word:
#                 count += 1
#                 in_word = True
#         else:
#             in_word = False

#     return count


# s = "Hello World, How are you? are you doing well? i can't believe it's been that long."
# print(countWord(s))


def validate_number(s):
    if not s:
        return "Invalid"

    # handle negative
    if s[0] == '-':
        s = s[1:]

    if not s:
        return "Invalid"

    dot_count = s.count('.')

    if dot_count == 0:
        # Integer check
        for ch in s:
            if ch < '0' or ch > '9':
                return "Invalid"
        return "Integer"

    elif dot_count == 1:
        # Float check
        left, right = s.split('.')

        if left == "" or right == "":
            return "Invalid"

        if not left.isdigit() or not right.isdigit():
            return "Invalid"

        return "Float"

    else:
        return "Invalid"
