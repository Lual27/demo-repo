def is_palindrome(word):
    return word == word[::-1]

result =  is_palindrome("racecar")
print(result)

result = is_palindrome("hello")
print(result)