# This is a sample Python script.
import csv


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# reading CSV file
# read the first file
with open('readtask.csv') as rt:
    reader = csv.reader(rt)
    # selecting the first line of each line at a time and put into interestingrows
    interestingrows = [row for ids, row in enumerate(reader) if ids % 3 == 1]
    updated = []

    # selecting the required rows[135] and columns[42]
    for i in range(134):
        updated = (interestingrows[i][0:45])
        # print(updated)

# reading the second file
with open('demo.csv') as dd:
    #next(dd)
    reader = csv.reader(dd)
    success_score = []
    for row in reader:
        # extracting the success score row and inserting into a new list
        success_score.append(row[7])

    # inserting the list element into the first file's second column
    for i in range(134):
        interestingrows[i].insert(2, success_score[i])
    # create a new file, set in a write mode
    with open('student_performance.csv', 'w') as nw:
        writer = csv.writer(nw)

        for i in range(134):
            print(interestingrows[i][0:45])
            # while iterating the updated rows for display, write into the new csv file
            writer.writerow(interestingrows[i][0:45])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
