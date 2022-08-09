def isPalindrome(word):
    revWord = word[::-1]
    if word==revWord:
        print('Palindrome')
    else:
        print('Not a palindrome')

word = input()
isPalindrome(word)