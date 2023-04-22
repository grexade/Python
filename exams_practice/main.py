# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def simple_function():
    return 0, 1, 2


def quiz():
    num1 = int(input("Enter a Number: "))
    num2 = int(input("Enter another Number: "))

    if num1 > num2:
        num1, num2 = num2, num1
    else:
        num1, num2 = num1, num2

    gcd = num1 % num2

    print(gcd)
    print(num1)
    print(num2)
    #while


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Grexade')
    #quiz()
    print()

    big = max("Hello world")
    print(big + " yes")


    print()

    groups = {"cmpe242": [15, 24,17, 22], "cmpe112": [34, 23, 43, 78, 15]}

    for course in groups.keys():
        print(course + "-" + str(len(groups[course])))

    x, y, z = simple_function()
    print(x)
    print(y)
    print(z)

    print()
    alist = list(simple_function())
    print(alist)

    print()
    a, b = [10, 20]
    print(a)
    print(b)

    print()
    colors = ['red', 'blue', 'green']
    print(colors[0])    ## red
    print (colors[2] )   ## green
    print (len(colors))  ## 3

    b = colors
    print(colors)
    print(b)

    print()
    lists = ['larry', 'curly', 'moe']
    if 'curly' in lists:
        print('yay')

    print()
    quiz()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
