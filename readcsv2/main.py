import csv

# Open the second .csv file in read mode
with open('demo.csv', 'r') as second_file:
    # Create a CSV reader object
    reader = csv.reader(second_file)

    # Initialize an empty list to store the values from the 7th column
    seventh_column = []

    # Iterate over the rows in the CSV reader object
    for row in reader:
        # Append the value in the 7th column to the list
        seventh_column.append(row[7])

# Open the first .csv file in read mode
with open('readtask.csv', 'r') as first_file:
    # Create a CSV reader object
    reader = csv.reader(first_file)
    #interestingrows = []
    #interestingrows += row[0]
    interestingrows = [row for ids, row in enumerate(reader) if ids % 3 == 1]
    # Open the first .csv file in write mode
    with open('first_file.csv', 'w') as first_file_updated:
        # Create a CSV writer object
        writer = csv.writer(first_file_updated)

        # Initialize a counter to keep track of the current row
        counter = 0

        # Iterate over the rows in the CSV reader object
        for row in interestingrows:
            # If this is the first row (header), write it as is to the updated file
            # if counter == 0:
            #     writer.writerow(row)
            # else:
                # Otherwise, insert the value from the 7th column of the second file
                # in the 3rd column of the current row and write it to the updated file

            row.insert(2, seventh_column[counter ])
            writer.writerow(row)
            print(row)
            #interestingrows = [row for ids, row in enumerate(reader) if ids % 3 == 1]
            # Increment the counter
            counter += 1
