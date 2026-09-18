class Palindrome:
    def is_palindrome(self, value):
        pass
 
class StringPalindrome(Palindrome):
    def is_palindrome(self, value):
        cleaned = value.lower().replace(" ", "")
        return cleaned == cleaned[::-1]
 
class IntegerPalindrome(Palindrome):
    def is_palindrome(self, value):
        s = str(value)
        return s == s[::-1]
 
 
def check_palindrome(checker: Palindrome, value):
    result = checker.is_palindrome(value)
    print(f"{value} -> {'Palindrome' if result else 'Not a Palindrome'}")
 
 
string_checker = StringPalindrome()
int_checker = IntegerPalindrome()
 
# Polymorphism: same method name is_palindrome() behaves differently
check_palindrome(string_checker, "Afifa")
check_palindrome(string_checker, "Rafia")
check_palindrome(int_checker, 123321)
check_palindrome(int_checker, 0000)

