
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

# def validate_number(s):
#     if not s:
#         return "Invalid"

#     # handle negative
#     if s[0] == '-':
#         s = s[1:]

#     if not s:
#         return "Invalid"

#     dot_count = s.count('.')

#     if dot_count == 0:
#         # Integer check
#         for ch in s:
#             if ch < '0' or ch > '9':
#                 return "Invalid"
#         return "Integer"

#     elif dot_count == 1:
#         # Float check
#         left, right = s.split('.')

#         if left == "" or right == "":
#             return "Invalid"

#         if not left.isdigit() or not right.isdigit():
#             return "Invalid"

#         return "Float"

#     else:
#         return "Invalid"

#validate email address
# def validEmail(s):
#     if '@' not in s:
#         return False
#     if s.count('@')!=1:
#         return False
#     at_pos = s.index('@')

#     if at_pos ==0 or at_pos == len(s)-1:
#         return False
    
#     if'.' not in s[at_pos:]:
#         return False
#     if s.endswith('.'):
#         return False
#     return True

# s =[
#     "abc@gmail.com",
#     "abc@gmail",
#     "@gmail.com",
#     "abc@gmail.",
#     "abc@@gmail.com"
#  ]

# for e in s :
#     print(e,"->", validEmail(e))


# def extractNo(s):
#     curr = ""
#     new_list = []
#     for i in s:
#         if i.isdigit():
#             curr = curr + i
#         else:
#             if curr != "":
#                 new_list.append(int(curr))
#             curr = ""
#     if curr != "":
#         new_list.append(int(curr))
#     return new_list

# stri = "a12b34c5"
# print(extractNo(stri))

#convert string to camel Case
# def camel_case(s):
#     new_s=""
#     cap_next = False
#     for i in s:
#         if i== " " or i=="_" or i=="-":
#             cap_next=True
#         else:
#             if cap_next:
#                 new_s += i.upper()
#                 cap_next = False
#             else:
#                 new_s += i.lower()
#     return new_s

# print(camel_case("hello world program"))
# print(camel_case("convert_to_camel case"))


# count frequency of each character in a string
# def countFreq(s):
#     new_dict = {}
#     for i in s:
#         if i in new_dict:
#             new_dict[i]+=1
#         else:
#             new_dict[i]=1
#     return new_dict

# print(countFreq("aabbbdee"))

#count first non repeating character in a string
# def countNonR(s):
#     new_dict={}
#     for i in s:
#         if i in new_dict:
#             new_dict[i] +=1
#         else:
#             new_dict[i]=1
#     for i in new_dict:
#         if new_dict[i]==1:
#             return i
#     return None
    
# print(countNonR("aabbccde"))
            

# check if an string is an isogram
#isogram wo hote jinme repeating character ni hota

# def isogram(s):
#     return len(set(s))==len(s)

# print(isogram('Machine'))
# print(isogram('Hello'))
# print("\n-----------\n")
# def is_iso(s):
#     new_set = set()
#     for i in s:
#         if i in new_set:
#             return False
#         new_set.add(i)
#     return True

# print(is_iso('Machine'))
# print(is_iso('Hello'))


#Longest substring without non repeating characters
# def longSubstr(s):
#     left=0, max_length=0
#     newSet= set()
#     for i in range(len(s)):
#         while s[i] in newSet:
#             newSet.remove(s[left])
#             left=left+1
#         newSet.add(s[i])
#         max_length=max(max_length, i-left+1)
#     return max_length

# print(longSubstr("abcabcbb"))  # 3
# print(longSubstr("bbbbb"))     # 1
# print(longSubstr("pwwkew"))    # 3

#check if one string is a subsequence of another
# def subseq(s1,s2):
#     i=0
#     j=0
#     while i<len(s1) and j<len(s2):
#         if s1[i]==s2[j]:
#             i+=1
#         j+=1
#     return i == len(s1)

# print(subseq("abc","aXwbfYc"))

# Phase 4 - String Compression

# def comp_str (s):
#     if not s:
#         return ""
    
#     result = ""
#     count = 1

#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             count+=1
#         else:
#             result += s[i-1] + str (count)
#             count = 1

#     result += s[-1]+str(count)

#     return result


# print(comp_str("aaabbc"))
# print(comp_str("abcd"))
# print(comp_str("aaaaaavvv"))

# def substr(s, sub):
#     i=0
#     count=0
#     while i <= len(s) - len(sub):
#         if s[i:i+len(sub)] == sub:
#             i = i+len(sub)
#             count = count+1
#         else:
#             i=i+1
#     return count

# print(substr("abababa","aba"))

#replcce a substring with a new substring in a string
# def newsub(s,o,n):
#     i=0
#     result=""
#     while i <= len(s)-len(o):
#         if s[i:i+len(o)] == o:
#             result += n
#             i+= len(o)
#         else:
#             result += s[i]
#             i+=1

#     result += s[i:]
#     return result

# print(newsub("hello world","world","python"))

#extract substring between the characters

# def substrbw(s,start,end):
#     cs=-1
#     ce=-1
#     for i in range(len(s)):
#         if s[i] == start and cs==-1:
#             cs=i
#         elif s[i] == end and ce==-1: 
#             ce=i
#             break
#     if cs==-1 or ce==-1 or ce<cs:
#         return ""
#     res= s[cs:ce+1]
#     return res

# print(substrbw("abc[d]e","[","]"))

# check whether a string is a rotation of another string or not
# def is_rotation(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     return s2 in (s1+s1)

# print(is_rotation("abcd","cdab"))

#compare two string without using .equals()
# def compstr(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             return False
#     return True

# print(compstr("hi","hil"))

# find position of a substring in a string
# def poss(s1,s2):
#     i=0
#     while i <= len(s1)-len(s2):
#         if s1[i:i+len(s2)]==s2:
#             return i
#         i+=1
#     return -1

# print(poss("hello world","world"))

# find all unique character in a string

# def unichar(s1):
#     i=0
#     freq={}
#     for i in s1:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     result =""
#     for i in s1:
#         if freq[i]==1:
#             result = result+i
#     return result

# print(unichar("aabbccdef"))

#rotate a string left by k characters
# def rotatestr(s1,k):
#     k=k%len(s1)
#     left=s1[0:k]
#     right=s1[k:]
#     return right+left


# print(rotatestr("abcd",6))

#Merge two strings alternately

# def mergeStr(s1,s2):
#     res=""
#     i=0
#     j=0
#     while i< len(s1) and j<len(s2):
#         res=res+s1[i]+s2[j]
#         i+=1
#         j+=1

#     while i<len(s1):
#         res=res+s1[i]
#         i+=1

#     while j<len(s2):
#         res=res+s2[j]
#         j+=1

#     return res

# print(mergeStr("abc","pqrst"))

# permutations of stirng
# def perm(s1):
#     if len(s1)==1:
#         return [s1]

#     res = []
#     for i in range(len(s1)):
#         fixed = s1[i]
#         remaining = s1[:i]+s1[i+1:]
#         for j in perm(remaining):
#             res.append(fixed+j)
        
#     return res


# print(perm("ac"))

# edit distance
# def edit_dist(s1,s2):

#     if len(s1) ==0:
#         return len(s2)
#     if len(s2)==0:
#         return len(s1)
#     if s1[-1] == s2[-1]:
#         return edit_dist(s1[:-1], s2[:-1])
#     return 1 + min(
#         edit_dist(s1, s2[:-1]),    # insert
#         edit_dist(s1[:-1], s2),    # delete
#         edit_dist(s1[:-1], s2[:-1])# replace
#     )

# print(edit_dist("cat", "cut"))   # 1
# print(edit_dist("kitten", "sitting"))  # 3


# New Question as per the pattern of DSA
# a. ARRAY
#  TWO SUMS
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# # test cases
# print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
# print(twoSum([3, 2, 4], 6))        # [1, 2]
# print(twoSum([3, 3], 6))           # [0, 1]

#best time to buy & sell stock
# def bass(a1):
#     # buy=a1[0]
#     # store = 0
#     # for i in a1:
#     #     if i<buy:
#     #         buy=i
#     #     else:
#     #         profit = i - buy
#     #         if profit > store:
#     #             store = profit
#     # return store
#     min_price = float('inf')
#     max_profit = 0

#     for i in a1:
#         min_price = min(min_price, i)
#         max_profit = max(max_profit, i-min_price)
#     return max_profit
    

# print(bass([7,1,5,3,6,4]))

#maximum subarray
# def maxSubArray(nums):
#     current_sum = nums[0]
#     max_sum = nums[0]

#     for i in range(1, len(nums)):
#         current_sum = max(nums[i], current_sum + nums[i])
#         max_sum = max(max_sum, current_sum)

#     return max_sum


# # test cases
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
# print(maxSubArray([1]))                      # 1
# print(maxSubArray([5,4,-1,7,8]))              # 23
# print(maxSubArray([-1,-2,-3,-4]))             # -1

# n = 5
# sum = 0

# for i in range(1, n + 1):
#     res += i ** 3

# print(res)

# n = 11
# if n <= 1:
#     print(False)
# else:
#     is_prime = True  # Flag variable
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     print(is_prime)

# function to check if a substring 
# s[low..high] is a palindrome
# def checkPal(str, low, high):
#     while low < high:
#         if str[low] != str[high]:
#             return False
#         low += 1
#         high -= 1
#     return True

# # function to find the longest palindrome substring
# def getLongestPal(s):
    
#     n = len(s)

#     # all substrings of length 1 are palindromes
#     maxLen = 1
#     start = 0

#     # nested loop to mark start and end index
#     for i in range(n):
#         for j in range(i, n):

#             # check if the current substring is 
#             # a palindrome
#             if checkPal(s, i, j) and (j - i + 1) > maxLen:
#                 start = i
#                 maxLen = j - i + 1

#     return s[start:start + maxLen]

# if __name__ == "__main__":
#     s = "forgeeksskeegfor"
#     print(getLongestPal(s))

    #DP

# def getLongestPal(s):
#     n = len(s)
#     dp = [[False] * n for _ in range(n)]
    
#     # dp[i][j] if the substring from [i to j] is a palindrome or not
#     start = 0
#     maxLen = 1
    
#     # all substrings of length 1 are palindromes
#     for i in range(n):
#         dp[i][i] = True
    
#     # check for substrings of length 2
#     for i in range(n - 1):
#         if s[i] == s[i + 1]:
#             dp[i][i + 1] = True
#             if maxLen == 1:
#                 start = i
#                 maxLen = 2
    
#     # check for substrings of length 3 and more
#     for length in range(3, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1
    
#             # if s[i] == s[j] then check for [i+1 .. j-1]
#             if s[i] == s[j] and dp[i + 1][j - 1]:
#                 dp[i][j] = True
#                 if length > maxLen:
#                     start = i
#                     maxLen = length
    
#     return s[start:start + maxLen]
        
# if __name__ == "__main__":
#     s = "forgeeksskeegfor"
#     print(getLongestPal(s))


# time complexity questions
# a = 0
# b = 0
# for i in range(N):
#   a = a + random()

# for i in range(M):
#   b= b + random()

# def fun(n,m):
#     for i in range(n):
#         print(i)
#     for i in range(m):
#         print(i)


# print(fun(1,2))

# def fun(N,M):
#     arr=[]
#     counter=0
#     for i in range(N):
#         arr.append(i)
#     for i in range(M):
#         counter+=1
#     print(counter)

# def function(N,M):
#   counter=0
#   for i in range(N):
#     for j in range(M):
#         counter+=1
#     print(counter)

#     def fun(n,m):
#     arr=[[0]*m for i in range(n)]
#     for i in range(n):
#         for j in range(m):
#             k=1
#             while k<n*m:
#                 k*=2

# LOGIC BUILDING PROBLEMS

# 1. check even or odd
# def evenOdd (num):
#     if num==0:
#         return True
#     if num%2==0:
#         return "It is even"
#     else:
#         return "It is odd"
# print(evenOdd(int(input())))

# 2.) Multiplication Table
# def multiTable(num):
#     if num==0:
#         return "Enter some other number"
#     for i in range(1,11):
#         print(num ,"*", i, "= ", num * i)

# multiTable(int(input()))

# 3.) Program for sum of n natural number
# def natural(num):
#     if num == 0:
#         return 0
#     res=0
#     for i in range(1,num+1):
#         res=res+i

#     return res
# print(natural(int(input())))

# 4.) Program for sum of square of first n natural number
# def sqNat(num):
#     if num==0:
#         return 0
#     res = 0
#     for i in range(1,num+1):
#         res = res + i*i
#     return res
# print(sqNat(int(input())))

# 5.) Swap Two Numbers
# def swap(a,b):
#     # c=a
#     # a=b
#     # b=c
#     # return (a,b)

#     # a= (a*b)
#     # b= a//b
#     # a=a//b

#     # a = a+b
#     # b = a-b
#     # a=a-b

#     a= a ^ b
#     b= a^b
#     a=a^b

#     return a,b
# print(swap(int(input()), int(input())))

#6.) find closest to n divisible by m
def closestn(n,m):
    if m==0:
        raise ValueError("Divisor can't be equal to 0")
    lower = round(n/m)*m
    upper = lower + m if n>=0 else lower - m
    if abs(n-lower)<abs(n-upper):
        return lower
    elif abs(n-lower) > abs(n-upper):
        return upper
    else:
        return lower if abs(lower)>abs(upper) else upper

print(closestn(int(input()), int(input())))