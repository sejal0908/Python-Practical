# Practical 4 - Conditions and Branching

# Question 1

player_name = "Lionel Messi"
sport = "Soccer"
achievements = 7

if achievements > 10:
    print(player_name, sport, achievements)
else:
    print(player_name, "does not have more than 10 achievements")


# Question 2

player_name = "Roger Federer"
sport = "Tennis"
achievements = 20

if sport == "Tennis" or achievements == 20:
    print("Success")


# Question 3

player_name = "Usain Bolt"
sport = "Athletics"
achievements = 8

if achievements < 10 and sport != "Soccer":
    print(player_name, sport, achievements)


# Question 4

num = int(input("Enter a number between 1 and 9999: "))

if num < 1 or num > 9999:
    print("Invalid input")
else:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if str(num) == str(num)[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

    digit_sum = sum(int(digit) for digit in str(num))

    if num % digit_sum == 0:
        print("Divisible by the sum of its digits")
    else:
        print("Not divisible by the sum of its digits")


# Question 5

for i in range(-5, 6):
    print(i)


# Question 6

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for colour in squares:
    print(colour)


# Question 7

squares = ['orange', 'orange', 'orange', 'blue', 'orange']
new_squares = []

i = 0

while i < len(squares):
    if squares[i] != 'orange':
        break
    new_squares.append(squares[i])
    i += 1

print(new_squares)


# Question 8

animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]

seven_letter_animals = []

i = 0

while i < len(animals):
    if len(animals[i]) == 7:
        seven_letter_animals.append(animals[i])
    i += 1

print(seven_letter_animals)