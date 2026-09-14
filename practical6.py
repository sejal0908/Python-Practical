# Practical 6
# Problem 1 - Fixing Buggy Code using super()
class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print("Name:", self.name)
        print("ID:", self.id)


class Emp(Person):

    def __init__(self, name, id):
    
        super().__init__(name, id)

    
    def Print(self):
        print("Emp class called")


Emp_details = Emp("Mayank", 103)

Emp_details.Display()
Emp_details.Print()

# Problem 2 - Anagram Check

def anagram_check(word1, word2):

    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


word1 = input("\nEnter first word: ")
word2 = input("Enter second word: ")

if anagram_check(word1, word2):
    print("The words are Anagrams.")
else:
    print("The words are not Anagrams.")


# armstrong number check

def armstrong_check(number):

    original_number = number

    number_of_digits = len(str(number))

    total = 0
    for digit in str(number):
        total = total + int(digit) ** number_of_digits

    if total == original_number:
        return True
    else:
        return False


number = int(input("\nEnter a number: "))

if armstrong_check(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")


# Problem 4 - Classes and Objects


class Vehicle:

    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = 0


    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Maximum Speed:", self.max_speed, "kmph")
        print("Mileage:", self.mileage, "kmpl")
        print("Color:", self.color)
        print("Seating Capacity:", self.seating_capacity)

vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)


vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)

print("\nFirst Vehicle")
vehicle1.display_properties()

print("\nSecond Vehicle")
vehicle2.display_properties()