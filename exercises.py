'''1 Write a function to check if a number is even.
(input 2: output True, input 3: output False)'''

def check_number(number: int):
    if number % 2 != 0:
        return False
    else:
        return True


print(check_number(14))

'''2 Write a function to check if a number is palindrome.
(121 is palindrome, 321 is not)'''
def check_is_palindrome(number):
    number = str(number)
    if len(number) <= 1:
        return True
    if number[0] == number[-1]:
        return number[0] == number[-1] and check_is_palindrome(number[1:-1])
    else:
        return False


print(check_is_palindrome(80508))

'''3 Write a function to check if a number is power of 2.
(1, 2, 4 power of 2, 3 is not'''

def is_power_of_two(number: int):
    while number > 1:
        number = number/2
    if number == 1:
        return True
    else:
        return False


print (is_power_of_two(125))

'''4 Write a function to convert a given string to all uppercase if it contains at least 2 
uppercase characters in the first 4 characters.'''


def convert_uppercase(sentence: str):
    check_sentence = sentence[0:4]
    count_upper_letter = 0
    for letter in check_sentence:
        if letter.isupper() is True:
            count_upper_letter += 1
    if count_upper_letter >= 2:
        return sentence.upper()
    else:
        return sentence


print(convert_uppercase('MirNa ime'))


'''5 Given a list iterate it and display numbers which are divisible by 5 and if you 
find number greater than 150 stop the loop iteration
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
'''
def divisible_by_five (list1: list):
    list2 = []
    for element in list1:
        if element > 150:
            break
        if element % 5 == 0:
            list2.append(element)
    return list2


print(divisible_by_five([12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]))

'''6 Write a function that takes a list of words and groups the words by their length 
using a dictionary
Input: [‘Lorem, ‘ele’, ‘sit’, ‘incididunt’, ‘a’, ‘su’, ‘dom’, ‘ouch’, ‘ipsum’]
Output: 
{
1: [‘a’],
2: [‘su’],
3: [‘ele’, ‘sit’, ‘dom’]
5: [‘Lorem’, ‘ipsum’]
10: [‘incididunt’]
}'''
#Zgjidhur pjeserisht

def count_letters(strings: list):
    count_dict = {}
    count_letters = 0

    for index, element in enumerate(strings):
        count_letters = len(element)
        count_dict[count_letters] = strings[index]

    return count_dict


print(count_letters(['Lorem', 'ele', 'sit', 'incididunt', 'a', 'su', 'dom', 'ouch', 'ipsum']))


'''7 Create a class Person with first_name and last_name as constructor 
parameters. The class should have a function get_fullname which returns the 
person’s full name (first_name + last_name). Create another class Student, 
inheriting from Person. Student’s get_fullname function should return students 
full name followed by ‘-st.’'''


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __get_fullname__(self):
        self.fullname = (f'{self.first_name} {self.last_name}')
        return self.fullname


person1 = Person('Neta', 'Shehu')
print(person1.__get_fullname__())


class Student(Person):

    def __get_fullname__(self):
        self.fullname = (f'{self.first_name} {self.last_name} -st.')
        return self.fullname


person2 = Student('Mirna', 'Shehu')
print(person2.__get_fullname__())




