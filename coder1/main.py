# This is a sample Python script.
import random


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


#dry= don't repeat yourself

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("It's Grexade")

with open('words.txt', 'r') as hand:
    di = dict()
    for line in hand:
        line = line.rstrip()
        words = line.split()
        for w in words:
            di[w] = di.get(w, 0) + 1

print(di)
print()

temp = list()
for k,v in di.items():
    newtemp = (v,k)
    temp.append(newtemp)

temp = sorted(temp, reverse=True)

for v,k in temp[:5]:
    print(k,v)

print()
print(sorted([(v,k) for k,v in di.items()], reverse=True))


class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()


class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()
print()


is_hot = True
is_cold = True

if is_hot:
    print("Drink water")
elif is_cold:
    print("wear warm clothes")
else:
    print("enjoy your day!")


print()

house_price = 1000000

buyer_credit = False

if buyer_credit:
    down_payment = 1000000 * 0.1

else:
     down_payment = 1000000 * 0.2
print(f"Down Payment: ${down_payment}")
print("{:,}".format(down_payment))

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible")

print()

name ="John Smith"

print(len(name))

if len(name) <3:
    print("Name must be atleast 3 character!")
elif len(name) > 50:
    print("Name is too short!")
else:
    print("Name looks good")

print()

# print("Welcome to the weight conversion!")
# num = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
#
# if unit.upper() == "L":
#     conv = 0.453592* num
#     print(f"You are {conv} kilos")
# else:
#     conv = num // 0.453592
#     print(f"You are {conv} pounds")

i = 1
while i<=5:
    print("*" * i)
    i= i+1
print("Done")

print()
sum = 0
prices = [10, 20, 30, 40, 50]
for item in prices:
    sum += item
print(f"Total: {sum}")

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

print()
numbers = [5, 2, 10, 2, 2, 8, 9, 6]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)
print()

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😀",
#         ":(": "😌"
#     }
#
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output

#
# message = input(">")
# print(emoji_converter(message))

x="33"
print(x*3)


#object is an instance of a class
#constructor is called at the time of creating an object
#dry = don't repeat yourself
class Person:
    def __init__(self, namez):
        self.namez = namez

    def talk(self):
        print(f"Hi, I am {self.namez}")


john = Person("John Smith")
bob = Person("Bob Jones")
john.talk()
bob.talk()
print()

for i in range(3):
    print(random.randint(10, 20))


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

print()
try:
    age = int(input("Enter age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be Zero")
except ValueError:
    print("Invalid Value")


# sec_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == sec_number:
#         print("You won!")
#         break
# else:
#     print("sorrt!")

# print()
# print("Welcome!")
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped...")
#     elif command == "help":
#         print("""
#     Start - to start the car
#     Stop - to stop the car
#     quit - to quit
#              """)
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that!")

#word frequency on data page

# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://www.url.com')
# with open fhand as urllib.request.urlopen('http://www.google.com')
#
# fhand = open(r"fhand", "www.google.com")
#
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[words] = counts.get(word, 0) + 1
# print(counts)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
